# Luizalabs Employee Manager Application 

Desenvolvimento de uma web app 'fictícia' em Python & Django que simulará uma aplicação que gerenciará as informações do funcionários através de uma API que permita integrá-la a outros sistemas. 
A aplicação irá ter: 

* Um painel Admin feito em Django para que possa gerenciar os dados dos empregados;
* E uma API que permita: listar, adicionar e remover os empregados (somente o Admin);

## Exemplo das URI's de Requisição (Request):

```
curl -H "curl -H "Content-Type: application/javascript" http://localhost:8000/employee/

```

E o resultado do JSon (Response) deverá (exemplo):

```
[
  {
    "name": "Arnaldo Pereira",
    "email": "arnaldo@luizalabs.com",
    "department": "Architecture"
    },
    {
      "name": "Renato Pedigoni",
      "email": "renato@luizalabs.com",
      "department": "E-commerce"
    },
    {
      "name": "Thiago Catoto",
      "email": "catoto@luizalabs.com",
      "department": "Mobile"
    }
]

```

## Recursos Utilizados no Desenvolvimento da Aplicação:

- Python ~ 3.5.0;
- Pip;
- Django ~ 1.9.6;
- Psycopg2; (adaptador do PostgreSql para Python)
- PostgreSQL;
- Django REST Framework;
- Conceito Web & HTTP Protocol;
- Bootstrap Framework 3;
- HTML;
- CSS;
- IDE's: Sublime & Visual Code;

## Acompanhamento do Desenvolvimento dos BackLogs do Projeto:

Caso queira saber o acompanhamento do desenvolvimento de cada backlog do projeto que está sendo
desenvolvido, basta clicar [Aqui](https://trello.com/b/GU7mnbyn/projeto-luizalabs-employee-manager-application)

## Padrão das Rotas Criadas: 

Procurando seguir o padrão e design das API's, segue abaixo as URI's das rotas a serem desenvolvidas:

 ROTA                     |     HTTP(Verbo)   |      Descrição        | 
------------------------- | ----------------- | --------------------- | 
/employee                 |       GET         | Selecionar Todos      | 
/employee                 |       POST        | Atualizar Por Id      | 
/employee/:employee_id    |       GET         | Selecionar Por Id     | 
/employee/:employee_id    |       PUT         | Atualizar Por Id      |    
/employee/:employee_id    |       DELETE      | Excluir Por Id        |


## Padrão da Arquitetura do Projeto:

Como estaremos desenvolvendo usando o framework do Python - **Django** - trabalharemos com a seguinte definição de Arquitetura: MTV

- **M**: Model
- **T**: Template
- **V**: View


## Executando a Aplicação:

Para que o projeto execute de maneira satisfatória, há a necessidade de instalar os programas abaixo:

1) Instalar: Python [AQUI](https://www.python.org/downloads/)
  - Video explicando como instalar Python 3.5 [AQUI](https://www.youtube.com/watch?v=YdNiifNwt_M)

2) Instalar: PostgreSQL [AQUI]()

3) Instalar: Psycopg2 [AQUI]()


(Documentação em desenvolvimento....)
