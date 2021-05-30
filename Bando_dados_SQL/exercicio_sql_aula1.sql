--Criação da tabela Person e inserção dos dados teste
create table Person (id unique, person varchar(30), family varchar(30));
insert into Person (id, personal, family) values (1, "Laryssa", "Costa");
insert into Person (id, personal, family) values (2, "Vinicius", "Borges");

--Criação da tabela Site e inserção dos dados teste
create table Site (name varchar(30), lat real, long real);
insert into Site (name, lat, long) values ("DR-1", -49.85, -128.57);
insert into Site (name, lat, long) values ("DR-3", -47.15, -126.72);
insert into Site (name, lat, long) values ("DR-2", -17.25, -196.09);


--Criação da tabela Visited e inserção dos dados teste
create table Visited (id unique, site varchar(30), dated varchar(30), foreign key(site) references Site(name));
insert into Visited (id, site, dated) values (619, "DR-1", "1927-02-08");
insert into Visited (id, site, dated) values (622, "DR-1", "1927-02-10");
insert into Visited (id, site, dated) values (620, "DR-3", "1930-01-09");

--Criação da tabela Survey e inserção dos dados teste
create table Survey (taken integer, person integer, quant varchar(30), reading real, foreign key(taken) references Visited(id), foreign key(person) references Person(id));
insert into Survey (taken, person, quant, reading) values (619, 1, "rad", 9.82),(619, 1, "sal", 0.13),(622, 1, "rad", 7.8);

--Exercícios:
--Listar quantidade de visitas que cada site recebeu
select count (site) as qntd, site from visited group by site;

--Listar sites que nao receberam visitas (utilizando subquery)
select * from site s where s.name not in (select site from visited);

--Listar métricas que foram observadas na tabela survey
select distinct quant from Survey;

--Listar pessoas que fizeram mais de dois levantamentos
select s.person as id_person, p.personal as name, count(s.person) as qtd_survey from survey s 
inner join person p on s.person = p.id 
group by s.person having count(s.person) > 2;

--Listar pessoas que o sobrenome possua DYR no meio da palvra // Não tem DYR, então procurei por Bor para aparecer Borges;
select family from Person where family like '%DYR%';
select family from Person where family like '%BOR%';

--Listar visitacoes a uma lista de sites passados como parâmetro
select * from visited where site in ("DR-1", "DR-3");

--verifique quantas linhas possuem valor nulo na coluna quant na tabela survey
select count(quant) from Survey where quant is NULL;

--retorne a medida de lat lon utilizando como parametro de busca um intervalo de datas
select s.name, s.lat, s.long,v.dated from site s 
inner join visited v on s.name = v.site 
where date(dated) < date ('1927-12-31') and date(dated) > date('1927-01-01');

--Retorne a quantidade de medições realizadas por cada pessoa na tabela person
select p.personal, count(s.person) as qntd_medicao from survey s 
inner join person p on s.person = p.id 
group by s.person;

--retorne a pessoa que tem a maior quantidade de medições de temperatura entre 10 e 30
select p.personal, count(s.person) as qtd from Survey s 
inner join Person p on p.id = s.person 
where quant = 'temp' and reading > 10 and reading < 30 
group by person order by qtd desc limit 1;
