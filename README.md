# Back-end do e-commerce principal

API de cadastro e login de usuario, com criptografia de senha e JWT, juntamente com busca de produtos em banco de dados para consumo dinamico do Front-end

## Api desenvolvida com Python e Flask

- Funcionalidades:
- registro de usuário (temporário, pois estou desenvolvendo uma cadastro mais moderno e seguro em segundo plano usando JWT)
- Busca de Produtos no banco de dados e retorno para o front-end

## Banco de dados
O banco de dados utilizado nesse projeto foi o PostreSQL, sendo utilizado o ORM SQLAlchemy para a conectividade e manipulaçao de tabelas

## Intruções para uso!

Após clonar o repositório, executo os seguintes comandos:
``` 
pip install -r requirements.txt
```
Após isso, precisará criar um arquivo ".env" com os seguintes conteudos dentro dele:
```
DB_HOST=
DB_NAME=
DB_USER=
DB_PASS=
```
Aí é só adicionar seus dados e usar tranquilamente!