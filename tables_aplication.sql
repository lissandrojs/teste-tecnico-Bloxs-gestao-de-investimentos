CREATE TABLE pessoa (
  idPessoa INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  cpf VARCHAR(128) NOT NULL,
  dataNascimento DATETIME NOT NULL,
  PRIMARY KEY (idPessoa)
);

CREATE TABLE conta (
  idConta INT NOT NULL AUTO_INCREMENT,
  idPessoa INT NOT NULL,
  saldo DECIMAL NOT NULL,
  limiteSaqueDiario DECIMAL NOT NULL,
  flagAtivo TINYINT(1) NOT NULL DEFAULT 1,
  tipoConta INT NOT NULL,
  dataCriacao DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (idConta),
  FOREIGN KEY (idPessoa) REFERENCES pessoa(idPessoa)
);

CREATE TABLE transacoes (
  idTransacao INT NOT NULL AUTO_INCREMENT,
  idConta INT NOT NULL,
  valor DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (idTransacao),
  FOREIGN KEY (idConta) REFERENCES conta(idConta),
  dataCriacao DATETIME NOT NULL DEFAULT NOW()
);

