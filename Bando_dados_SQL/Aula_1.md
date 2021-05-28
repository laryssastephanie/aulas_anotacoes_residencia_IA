# Banco de dados e SQL

- Exemplo: Notas em uma disciplina;
- Preciso armazenar dados do aluno (nome, matricula), notas (do aluno, disciplina) e disciplina (nome, código);
- O armazenamento era muito caro, mas hoje em dia é muito barato;

### Banco de dados relacionais
- O que são banco de dados?
    - Qualquer coisa que coleta e organiza dados;
        - Uma planilha contendo as reservas dos clientes;
        - Um arquivo de texto simples contendo dados de horários de voos;
        - Sistema de gerenciamento de banco de dados relacional (Relational Database Management System - RDBMS);
            - Um tipo de banco de dados que contém uma ou mais tabelas que podem ter relacionamentos entre si;
- Chaves primárias = entrada única, não são repetidas
- Chaves estrangeiras = estão em outra tabela

### O que são banco de dados?
- Instancia: União entre RDBMS, tabela e dados;
Esquema: "Forma" de um BD;
    - Projeto de BD: organização e dependência dos dados
- Controle de concorrência: É necessário permitir que vários usuários tenham acesso às informações;
- Recuperação e falhas: Se houver um problema, é necessário dispor novamente os dados com a garantia de que eles estão de acordo com as regras de integridade;
- Linguagens para Definição de dados - Data definition language - DDL e para Modificação e Recuperação de dados - Data Modification Language - DML.

### SGBD (Sistema Gerenciador de Banco de Dados)
- Aplicação que provê suporte ao uso de Banco de Dados;
 - Permite construir e manipular Banco de Dados;
 - Utiliza os recursos do sistema operacional para disponibilizar os bancos de dados;
    -Sistemas de arquivos, Servidores aguardando requisições, Gerência de Memória, Cache de dados, etc.
    - MySQL, SQL Server, PostgreSQL, entre outros
- Alternativas Lightweight: SQLite, Microsoft Access
    - Manipulação direta de arquivos de banco de dados;
    - Não existe a necessidade de conexão a servidor de banco de dados
- SGBD possui um ou mais banco de dados;
- Um banco de dados possui uma ou mais tabelas;
- Uma tabela possui:
    - Uma ou mais colunas;
    - Possui um índice primário:
        - Valor que identifica uma linha de tabela unicamente;
        - Não pode conter entradas repetidas;
        - Pode ser composto até por mais que um campo;
        - CPF, (Nome, Sobrenome, CEP);

### SGBD VS Texto
- Armazena dados e meta dados x Utiliza linguagem procedural;
- Usa ferramentas e linguagens de consulta x Forte acoplamento entre dados e programas;
- Múltiplas visões dos dados (de acordo com o usuário) x Uma única visão dos dados;
- Provê uma interface de acesso aos dados x Interface definível apenas em aplicações;
- Eficiência, compartilhamento, segurança e tolerência a falhas x Difícil padronização.

### Modelando um banco de dados
- Uma forma de criar um BD a partir de um cenário real é utilizar modelos que mapeiam entidades conhecidas para elementos de banco de dados;
    - Modelo Conceitual: Descrição do banco de dados de forma independente de implementação em um SGBD;
        - Modelo de Entidade e Relacionamento (MER): Descrição dos elementos que devem compor o banco de dados: entidades e relacionamentos entre estas;
    - Diagrama de Entidade e Relacionamento (DER): Representação visual dos elementos que devem compor o BD;
        - Entidades, atributos, relacionamentos, chaves primarias, cardinalidade;

### Modelo Conceitual
...

### Principais Elementos
- Atributos
    - Simples: composto por um valor único
        - Ex: nome, sobrenome, nome da mãe, etc.
    - Composto: composição de outros atributos
        - Ex: Endereço (Rua, número, complemento)
    - Multi-valorado: contém diversos valores para um mesmo atributo
        - Ex: telefones para contato
    - Determinante: define unicamente uma entidade
        - Ex: CPF, RG, CNPJ, etc.
- Relacionamento entre Entidades
    - Semântica de pertencimento de uma entidade em relação a outra restrito por meio de um recurso chamado cardinalidade
        - Um para um, Um para muitos, Muitos para muitos;
- Chaves
    - Chave primária: define elementos de forma única na tabela;
        - Pode ser uma ou mais colunas;
    - Chave estrangeira: conjunto de colunas em uma tabela idêntica a chave primária de outra tabela
        - Usado para definir relacionamentos

## Structure Query Language - SQL
### Introdução
- Linguagem padrão para os SGBDs Relacionais;
- Dividida em 4 módulos:
    - Linguagem de Definição de dados;
    - Controle;
    - Transação;
    - Manipulação;

### Seleção de dados
- Filtro por colunas;
- Filtro por registros;
- Classificação de registros;
- Agrupamento de registros em uma tabela;
- Unificação de tabelas;

sqlite3 - para sair ctrl D ou .exit
sqlite3 chinook.db
.mode box - tabela 
.help mode para verificar
nulls last
select distinct - tirar repetidos