# teste-tecnico-Bloxs-gestao-de-investimentos

## A Ideia deste projeto e uma API que realize operações bancárias e uma aplicação web que possibilite realizar as operações via API

## Rota "/cria_conta"
Método: POST
Descrição: Cria uma nova conta para um cliente.
    
    Parâmetros:
    nome (string): Nome completo do cliente.
    cpf (string): CPF do cliente.
    data_nascimento (string): Data de nascimento do cliente (formato: YYYY-MM-DD).
    saldo (float): Saldo inicial da conta.
    limite_saque_diario (float): Limite de saque diário da conta.
    tipo_conta (string): Tipo da conta (ex: "corrente", "poupança", etc.).

    Retorno:
    mensagem (string): Mensagem indicando se a conta foi criada com sucesso.
    id_conta (int): ID da conta criada.
    Código:



## Rota "/conta/int:id_conta/depositos"
Método: POST
Descrição: Realiza um depósito em uma determinada conta.
    
    Parâmetros:
    id_conta (int): ID da conta em que será realizado o depósito.
    valor (float): Valor a ser depositado na conta.

    Retorno:
    mensagem (string): Mensagem indicando se o depósito foi realizado com sucesso.
    saldo_atual (float): Saldo atual da conta após o depósito.

## Rota "/conta/int:id_conta/saldo"
Método: GET
Descrição: Retorna o saldo atual de uma determinada conta.

    Parâmetros:
    id_conta (int): ID da conta que se deseja obter o saldo.

    Retorno:
    saldo_atual (float): Saldo atual da conta.


## Rota "/contas/<int:id_conta>/saques" 
Descrição: Permite que um usuário faça um saque em uma determinada conta.
Método: POST

    Parâmetros: 
    id_conta (inteiro) : O id da conta na qual o usuário deseja fazer o saque. 
    No corpo da requisição,o usuário deve enviar o valor do saque em JSON, no formato: {"valor": float}.

    Retorno : "mensagem": "Saque realizado com sucesso"





## Rota "/contas/int:id_conta/desbloqueio"

Método: PUT
Descrição: Desbloquear conta 

    Parâmetros:
    id_conta (int): ID da conta a ser desbloqueada
    Corpo da requisição: Nenhum

    Resposta:

    Status code: 200 OK
    Corpo da resposta: {"mensagem": "Conta desbloqueada com sucesso"}



## "/conta/int:id_conta/transacoes"

Método: GET
Descrição: Rota Listar transações de uma conta 

    Parâmetros:

    id_conta (int): ID da conta
    Corpo da requisição: Nenhum

    Resposta :

    Status code: 200 OK
    Corpo da resposta: [{"idTransacao": 1, "valor": 100.0, "dataHora": "2023-03-10 10:00:00", "idConta": 1}, {"idTransacao": 2, "valor": -50.0, "dataHora": "2023-03-10 11:00:00", "idConta": 1}]