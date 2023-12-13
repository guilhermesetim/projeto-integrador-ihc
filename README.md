# Back-end plataforma de acessibilidade
Repositório destinada ao backend da aplicação do portal de acessibilidade, proposto com projeto integrador da disciplina de Interação Humano-Computador.

## Funcionalidades
A aplicação Flask tem um endpoint /todo/cronograma/ que, ao ser acessado, conecta-se a um banco de dados MySQL para buscar informações de um cronograma. As informações recuperadas são formatadas e retornadas como uma resposta JSON.

## Linguagem e Bibliotecas
A aplicação foi desenvolvida em Python, utilizando o framework Flask para criar a API web. A biblioteca mysql.connector é usada para se conectar ao banco de dados MySQL. Além disso, a biblioteca jsonify do Flask é utilizada para formatar as respostas em JSON.

## Instalação de Dependências
Para instalar as dependências necessárias, você pode utilizar o comando pip no terminal:

```
pip install Flask flask-cors mysql-connector-python
```

Este comando instalará o Flask, a extensão Flask-CORS para lidar com questões de política de mesma origem (CORS), e a biblioteca mysql-connector-python para a comunicação com o banco de dados MySQL.

## Configuração
O arquivo config.json contém as informações de acesso ao banco de dados:
```
{
    "database": {
        "host": "seu_host",
        "user": "seu_usuario",
        "password": "sua_senha",
        "database": "seu_banco_de_dados"
    }
}
```
Substitua os valores de seu_host, seu_usuario, sua_senha e seu_banco_de_dados pelos dados do seu banco de dados.

## Executando a Aplicação
A aplicação estará disponível em http://projetoacessibilidade.mysql.pythonanywhere-services.com/. Acesse http://projetoacessibilidade.mysql.pythonanywhere-services.com/todo/cronograma/ para obter as informações do cronograma.

Esta aplicação é um exemplo simples e inicial do projeto, pode exigir ajustes para atender aos requisitos específicos ao longo do projeto.