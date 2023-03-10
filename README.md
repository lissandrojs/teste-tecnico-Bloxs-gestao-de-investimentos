# teste-tecnico-Bloxs-gestao-de-investimentos

## A Ideia deste projeto e uma API que realize operações bancárias e uma aplicação web que possibilite realizar as operações via API

## Aplicação quebrada em 2 serviço sendo este api o principal , o front-end interface de interação com o usuario https://github.com/lissandrojs/front_my_finances_bloxs

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
## Exemplo
        {
            "nome": "Fulano de Tal",
            "cpf": "123.456.789-00",
            "data_nascimento": "1985-07-15",
            "saldo": 1000.00,
            "limite_saque_diario": 500.00,
            "tipo_conta": "poupanca"
        }

    Retorno:
    mensagem (string): Mensagem indicando se a conta foi criada com sucesso.
    id_conta (int): ID da conta criada.
    Código:
## Exemplo Sucesso
                {
                    "mensagem": "Conta criada com sucesso",
                    "id_conta": 123
                }


## Rota "/conta/int:id_conta/depositos"
Método: POST
Descrição: Realiza um depósito em uma determinada conta.
    
    Parâmetros:
    id_conta (int): ID da conta em que será realizado o depósito.
    valor (float): Valor a ser depositado na conta.
## Exemplo
            {
                "valor": 100.50
            }

    Retorno:
    mensagem (string): Mensagem indicando se o depósito foi realizado com sucesso.
    saldo_atual (float): Saldo atual da conta após o depósito.

## Exemplo Sucesso
                    {
                         "mensagem": "Depósito realizado com sucesso",
                         "saldo_atual": 600.50
                    }

## Rota "/conta/int:id_conta/saldo"
Método: GET
Descrição: Retorna o saldo atual de uma determinada conta.

    Parâmetros:
    id_conta (int): ID da conta que se deseja obter o saldo.
## Exemplo
            Passar somente o id da conta na requisição

    Retorno:
    saldo_atual (float): Saldo atual da conta.
## Exemplo Sucesso
            {
            "saldo_atual": 1500.0
            }


## Rota "/contas/<int:id_conta>/saques" 
Descrição: Permite que um usuário faça um saque em uma determinada conta.
Método: POST

    Parâmetros: 
    id_conta (inteiro) : O id da conta na qual o usuário deseja fazer o saque. 
    No corpo da requisição,o usuário deve enviar o valor do saque em JSON, no formato: {"valor": float}.
## Exemplo 
            {
                "valor": 500
            }
    Retorno :
## Exemplo Sucesso
            {
                "mensagem": "Saque realizado com sucesso",
                "saldo_atual": 1500
            }

## Exemplo Error
            {
                "mensagem": "Conta não encontrada"
            }

            {
                "mensagem": "Saldo insuficiente"
            }

            {
                "mensagem": "Valor de saque excede o limite diário"
            }


## Rota "/contas/int:id_conta/desbloqueio"

Método: PUT
Descrição: Desbloquear conta 

    Parâmetros:
    id_conta (int): ID da conta a ser desbloqueada
    Corpo da requisição: Nenhum
## Exemplo
            {
                "motivo": "Fraude detectada"
            }

    Resposta:

## Exemplo Sucesso
                    {
                        "mensagem": "Conta bloqueada com sucesso"
                    }

## Rota "/conta/int:id_conta/transacoes"

Método: GET
Descrição: Rota Listar transações de uma conta 

    Parâmetros:

    id_conta (int): ID da conta
    Corpo da requisição: Nenhum

    Resposta :

            [
                {
                    "idTransacao": 1,
                    "valor": 100,
                    "dataHoraTransacao": "2022-03-10T17:30:00",
                    "idConta": 1
                },
                {
                    "idTransacao": 2,
                    "valor": -50,
                    "dataHoraTransacao": "2022-03-11T14:25:00",
                    "idConta": 1
                },
                {
                    "idTransacao": 3,
                    "valor": 200,
                    "dataHoraTransacao": "2022-03-12T09:40:00",
                    "idConta": 1
                }
            ]

