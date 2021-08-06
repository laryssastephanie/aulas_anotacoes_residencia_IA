# Exercicios-SQL

Exercícios referente a SQL

Nessa aula vamos realizar as seguintes atividades:

1 corrigir e discutir os exercícios passados na aula de BD

https://github.com/ai2-education-fiep-turma-3/04-banco-de-dados/tree/main/exercicios/aula1

2 rever procedimentos VPN e uso do gitlab

Conecte na VPN e execute os comandos a seguir:
  * ping no servidor SQL SERVER 192.168.65.141

  * ssh no servidor GPU ssh hub@192.168.64.9 senha hub@2020

3 acessar uma base SQL server pelo python e retornar o resultado para um dataframe 

4 Explorar o problema da sicoob 

4.1 O grupo vai falar rapidamente sobre seus achados até o momento

4.2 vamos dividir a turma em grupos. Cada grupo vai construir uma visão única dos dados, para representar alguma informação relevante a respeito de crédito, inadimplencia ou perfil de cliente
  
  A base sicoob é montada em SQL SERVER e possui uma grande quantidade de tabelas. A simples unificação com joins não resolverá o problema, certamente isso sera investigado ao longo das 4 sprints. Nesse primeiro contato a expectativa é que você consiga explorar a base, encontrar alguma informação relevante com suporte do dicionário de dados e criar uma versão unificada com joins.

obs: Sugiro instalar o microsoft azure para ajudar a navegar pelas tabelas

A entrega dos exercício será feita nesse mesmo respoitório. Por se tratar de dados de clientes podemos carregar código apenas no gitlab do Senai.

4.3 Para Entregar
* Leia os registros da tabela tce.clientefisica
* Retorne quantos clientes sao homens e quantos sao mulheres
* Retorne os tipos de regime de casamento, quantos registros tem para cada tipo
