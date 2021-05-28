# Introdução à Estatística

- A estatística provê meios para classificar, resumir, organizar, analisar e interpretar dados;
- Envolve: descrever Conjuntos de Dados e tirar conclusões (fazer estimativas, decisões, previsões, etc. a cerca de conjuntos de dados);
- Estatística descritiva vs inferencial:
    - A descritiva se concentra na descrição das características visíveis de um conjunto de dados;
    - A inferencial se concentra em fazer previsões ou generalizações sobre um conjunto de dados maior, com base em uma amostra desses dados;

### Variáveis
- Podem ser categóricas (qualitativas) ou numéricas (quantitavitas);
    - Qualitativas:
        - Não mede com números;
        - As observações caem dentro de um número finito de grupos;
        - Ordinais: Grau de gravidade de uma doença;
        - Nominais: Presença de um sintoma;
        - Em alguns casos podemos realizar o mapeamento para valores discretos e depois proceder análise como quantitativa;
    - Quantitativas:
        - Informações são registradas como números e representam uma medição objetiva ou uma contagem;
        - Discretas: número de cirurgias;
        - Contínuas: Idade, Pressão Arterial;

### Medidas Resumo - Tabela de Frequências
- Forma de representação da frequência de cada valor distinto da ariável em estudo;
- Frequências relativas: percentagem relativa à frequência;
Frequências acumuladas: número de vezes que uma variável assume um valor inferior ou igual a esse valor;
- Frequências relativas acumuladas: percentagem relativa à frequência acumulada.

### Medidas Resumo - Medidas de Posição
- Valores representativos de uma série completa;
- Redução drástica dos dados;
- Moda: valor de maior frequência no conjunto de valores observados (podem existir mais que uma moda);
- Mediana: Valor que ocupa a posição central numa série de observações ordenada em ordem crescente;
    - Quando quantidade de observações for par, utilizar média aritmética entre valores centrais;
- Média aritmética: Soma de todos os valores dividido pelo número de observações.

### Medidas de Dispersão
- Uma única medida representativa de posição central esconde a informação sobre a variabilidade do conjunto de observações;
- Vários grupos de dados podem ter a mesma média, mas um pode ser mais uniforme que o outro;
- Necessidade de serem criadas medidaas que sumarizem a variabilidade de um conjunto de observações;
    - Permite comparar conjuntos diferentes de valores segundo algum critério estabelecido;
- Alternativas ao Desvio da Média:
    - Considerar o total dos desvios em valor absoluto;
    - Considerar o total dos quadrados dos desvios;
    - Utilizar a média para poder comparar conjuntos com escalas diferentes
    - desvio médio e variância...
- Variância é uma medida de unidade igual ao quadrado da dimensão do dados (se os dados são expressos em cm, a variancia será expressa em cm²) - problemas de interpretação;
- Desvio Padrão: raiz quadrada positiva da varância;
- Ambas as medidas de dispersão (dm e dp) indicam:
    - Em média qual será o 'erro'(desvio) ao tentar substituir cada observação pela medida resumo do conjunto de dados (no caso, a média).
    - exercício...

### Quantis empíricos
- Tanto a média como o desvio padrão podem não ser madidas adequadas para representar um conjunto de dados pois:
    - São afetados, de forma exagerada, por valores extremos;
    - Apenas com estes dois valores não temos ideia da simetria ou assimetria da distribuição dos dados;
- A madiana é um valor que deixa metade dos dados abaixo dela e metade acima;
- Quantil de Ordem p (q(p)), onde p é uma proporção qualquer, 0 < p < 1, tal que 100p% das observações sejam menores do que q(p);
- Os valores, x(1), q1, q2, q3 e x(n) são importantes para se ter uma ideia da assimetria da distribuição dos dados;

### Histogramas
- Gráfico de barras contíguas, com as bases proporcionais aos intervalos das classes e a área de cada retângulo proporcional à respectiva frequência;
- Quanto mais dados tivermos em cada classe, mais alto deve ser o retângulo;

### Análise Bidimensional
- Frequentemente estamos interessados em analisar o comportamento conjunto de duas ou mais variáveis aleatórias;
Encontrar as possíves relações ou associações entre as duas variáveis:
    - Detectadas por meio de métodos gráficos e medidas numéricas.
    - Ex: Existe relação entre a altura de pessoas e a região onde ela nasceu?
    - Qual a frequência esperada de uma pessoa dessa população ter, digamos, mais de 170cm?
        - ex: 500 a cada 1000 pessoas possuem mais que 170cm.
- Incorporar conhecimento para melhorar o entendimento sobre os comportamentos das variáveis;
- Conhecer o grau de dependência entre duas variáveis:
    - prever melhor o resultado de uma delas ao conhecer a outra;
    Exemplo de dependencia: renda familiar e classe social.
- Quando consideramos duas variáveis (ou dois conjunto de dados), podemos ter três situações:
    - Duas variáveis qualitativas;
    - Duas variáveis quantitativas;
    - Uma de cada.
- Gráfico de dispersão de dados - uma maneira simples de verificar a relação entre duas variáveis.
- Tipos de associações:
    - Assoc. linear direta (ou positiva)
    - Dependência linear inversa (ou negativa)

### Medidas de Dependência
- Indica que conforme uma variável muda de valor, a outra variável tende a mudar em uma direção específica;
    - Possível usar o valor de uma variável para prever o valor da outra;
- Covariância: uma medida da tendência de duas variáveis variarem juntas;
    - Possui unidade;
    - Difícil de interpretar;
Correlação: quantificar a força da relaçao entre duas variáveis;
    - Normalização pelo desvio padrão;
    - Sem unidade associada.
    - Cálculo do Z-score - variação entre -1 e 1;
    - Correlação de Pearson:
        - Dependência Linear (!!!)
    
### Probabilidades
- Distribuição de frequências é importante para avaliarmos a variabilidade das observações de um fenômeno;
    - Medidas de posição e variabilidade;
- Espaço amostral - enumeração de todos os resultador possíveis do experimento em questão;
- Probabilidade para cada ponto amostral. A probabilidade do que chamaremos de um evento aleatório ou simplesmente evento;

### Função Probabilidade
...
### Função Densidade de Probabilidade
- Para o caso de variáveis contínuas;
- Cálculo de probabilidade para um dado intervalo;
- Valor = 0 em um ponto arbitrariamente pequeno;
- Teoricamente, qualquer função f, que seja não negativa e cuja área total sob a curva seja igual à unidade, caracterizará uma v.a. contínua.
