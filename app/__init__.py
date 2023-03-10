from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_apidoc import ApiDoc
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_migrate import Migrate
import os
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

apidoc = ApiDoc(app)
migrate = Migrate(app, db)


class Pessoa(db.Model):
    idPessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(120), nullable=False, unique=True)
    dataNascimento = db.Column(db.DateTime , nullable=False)
    conta = db.relationship('Conta', backref='pessoa', uselist=False)

    def __repr__(self):
        return '<Pessoa %r>' % self.name


class Conta(db.Model):
    idConta = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Float, default=0.0)
    limiteSaqueDiario = db.Column(db.Float, default=0.0)
    flagAtivo = db.Column(db.Boolean, default=True)
    tipoConta = db.Column(db.Integer)
    idPessoa = db.Column(db.Integer, db.ForeignKey('pessoa.idPessoa'), nullable=False)

    transacao = db.relationship('Transacao', backref='conta', lazy=True)

    def __repr__(self):
        return '<Conta %r>' % self.id


class Transacao(db.Model):
    idTransacao = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    dataTransacao = db.Column(db.DateTime, default=datetime.utcnow)

    idConta = db.Column(db.Integer, db.ForeignKey('conta.idConta'), nullable=False)

    def __repr__(self):
        return '<Transacao %r>' % self.id

@app.get('/')
def hello():
    return "Bem vindo Claro investidor" 

@app.post("/cria_conta")
def criar_conta():
    dados = request.json
    pessoa = Pessoa(nome=dados["nome"], cpf=dados["cpf"], dataNascimento=dados["data_nascimento"])
    db.session.add(pessoa)
    db.session.flush()
    conta = Conta(saldo=dados["saldo"], limiteSaqueDiario=dados["limite_saque_diario"], 
                  tipoConta=dados["tipo_conta"], idPessoa=pessoa.idPessoa)
    db.session.add(conta)
    db.session.commit()
    return jsonify({"mensagem": "Conta criada com sucesso", "id_conta": conta.idConta}), 201



@app.post("/conta/<int:id_conta>/depositos")
def depositar(id_conta):
    dados = request.json
    conta = Conta.query.get(id_conta)
    if not conta:
        return jsonify({"mensagem": "Conta não encontrada"}), 404
    valor_deposito = dados["valor"]
    conta.saldo += valor_deposito
    transacao = Transacao(valor=valor_deposito, idConta=id_conta)
    db.session.add(transacao)
    db.session.commit()
    return jsonify({"mensagem": "Depósito realizado com sucesso", "saldo_atual": conta.saldo}), 200


@app.get("/conta/<int:id_conta>/saldo")
def saldo(id_conta):
    conta = Conta.query.get(id_conta)
    if not conta:
        return jsonify({"mensagem": "Conta não encontrada"}), 404
    return jsonify({"saldo_atual": conta.saldo}), 200



@app.post("/contas/<int:id_conta>/saques")
def sacar(id_conta):
    dados = request.json
    conta = Conta.query.get(id_conta)
    if not conta:
        return jsonify({"mensagem": "Conta não encontrada"}), 404
    valor_saque = dados["valor"]
    if valor_saque > conta.saldo:
        return jsonify({"mensagem": "Saldo insuficiente"}), 400
    if valor_saque > conta.limiteSaqueDiario:
        return jsonify({"mensagem": "Valor de saque excede o limite diário"}), 400
    conta.saldo -= valor_saque
    transacao = Transacao(valor=-valor_saque, idConta=id_conta)
    db.session.add(transacao)
    db.session.commit()
    return jsonify({"mensagem": "Saque realizado com sucesso", "saldo_atual": conta.saldo}), 200



@app.put("/contas/<int:id_conta>/bloqueio")
def bloquear_conta(id_conta):
    conta = Conta.query.get(id_conta)
    if not conta:
        return jsonify({"mensagem": "Conta não encontrada"}), 404
    if not conta.flagAtivo:
        return jsonify({"mensagem": "Conta já está bloqueada"}), 400
    conta.flagAtivo = False
    db.session.commit()
    return jsonify({"mensagem": "Conta bloqueada com sucesso"}), 200


@app.get('/conta/<int:id_conta>/transacoes')
def get_transacoes(id_conta):
    conta = Conta.query.get_or_404(id_conta)
    transacoes = Transacao.query.filter_by(idConta=id_conta).all()
    return jsonify([t.__dict__ for t in transacoes]) 