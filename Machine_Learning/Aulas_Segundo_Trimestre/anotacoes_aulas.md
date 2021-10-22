## Regressão Logística
- Existem problemas para os quais desejamos estimar a classe (rótulo) de uma determinada amostra com base no seu conjunto de dados de entrada, isto é, as características do seu problema;
- Problemas de classificação são similares aos de regressão pois desejamos aprender uma função que, dada uma entrada, estime um valor de saída. A diferença é que nossa saída será mapeada para uma probabilidade (soft classification) ou  rótulo (hard classification) da amostra;
- A técnica de regressão logística é uma das mais utilizadas na literatura, principalmente por serem simples e dar bons resultados em diversas situações. Ela tem esse nome pelo fato de estimar a probabilidade de uma dada amostra pertencer à uma classe em específico. Portanto, é uma técnica de classificação do tipo soft.
- Possui função sigmóide;
- Temos dois problemas principais com MSE quando usamos a técnica de Regressão Logística:
    - A MSE não penaliza muito fortemente erros de classificação e pode levar a um aprendizado insuficiente;
        - Se não penalizar muito os erros, o aprendizado pode não ser tão bom;
    - A função de custo MSE não é convexa para o Regressor Logístico (provado matematicamente).

## Redes Neurais com Percepton Multicamadas

- Redes neurais foram amplamente utilizadas nos anos 80 e 90 e visam imitar o funcionamento do cérebro humano;
- Sua popularidade caiu no final dos anos 90, mas voltaram à cena com novas abordagens baseadas em aprendizado em profundidade;
- Como funcionam?
    - Neurônio: axônio, núcleo, dendritos;
    - Recebem impulsos elétricos pelos axônios e é propagado até os dendritos;
- Matematicamente falando, o neurônio pode ser representado por:
    - Entrada/Bias (Axônio), Função de ativação (núcleo) e saída (dendritos);
- Alguns exemplos de função de ativação (que vai disparar uma saída):
    - Função logística (sigmoide);
    - Função limiar (degrau);
    - Função tangente hiperbólica;
- É desejável que a função de ativação seja derivável;
- Para redes com muitas camadas, o gradiente tende a desaparecer durante o treinamento;

### Perceptron
- Tem o intuito de modelar matematicamente o neurônio humano. Muito embora ele tenha sido a base para muitos algoritmos, seu poder discriminativo é limitado, pois consegue aprender apenas hiperplanos como função de decisão;
- Recebe uma amostra e diz se é +1 ou -1;
- O w é um plano ortogonal ao wTx, portanto ao mudar o w, o wTx muda junto.
- Como aprender o conjunto de pesos w? A ideia intuitiva é mover o vetor de pesos de tal forma que as amostras fiquem posicionadas corretamente no espaço de características;
    - Encontrar um hiperplano de tal forma que amostras da classe +1 fique 'acima' e da classe -1 fique 'abaixo';
- alpha = taxa de aprendizado (ver equação - slide 12);
- bias = deslocamento do hiperplano;
- classes +1 e -1 = quando utilizamos a saída `limiar`;
- se houver acerto, a parte de aprendizado da equação será anulada, sobrará o w + x, que irá mover o hiperplano juntamente com o wTx, até encontrar a posição final;
- Algoritmo:
    - Atribua pesos aleatórios para w;
    - Inicialize alpha;
    - t <- 0;
    - Para cada amostra xi E X¹, faça:
        - w^(t+1) = w^(t) + alpha(yi - hw(t)(xi))xi (atualização do hiperplano);
    - Repita passo 4 até algum critério de convergência for estabelecido;

### Perceptron Multicamadas (Multilayer Perceptron - MLP)
- Basicamente, é um grupo de neurônios que, combinados, permitem o aprendizado de um número maior de funções de decisão;
- w21^1 = peso 2, do neuronio 1, na camada 1;
- Para um problema com c classes, nossa camada de saída necessita de c neurônios;
- Existem diversos algoritmos de treinamento para RN MLP, em que o mais conhecido é chamado de retropropagação, do inglês backpropagation;
- Ele possui dois passos: (i) propagação para frente (forward propagation) e (ii) propagação para trás (backpropagation);
- Backward - Calcula o erro na camada de saída e propaga para trás, depois volta, para ir ajustando até aprender;

### Regularização
- Com o intuito de evitar com que nossos modelos tornem-se muito 'especializados', podemos fazer uso de técnicas de regularização;
- Três casos que podem ocorrer:
    - Subtreinamento (underfitting);
    - Bom treinamento;
    - Sobretreinamento (overfitting);
- Como podemos minimizar o efeito dos pesos associados aos graus maiores? Uma solução para penalizá-los seria multiplicá-los por valores altos;
- Como o objetivo é minimizar a função de custo, a tendência é que o gradiente descendente atribua valores muito pequenos para w3 e w4 no intuito de diminuir a sua influência no valor final;
- Assim, a regularização visa atribuir valores pequenos para os elementos em w de tal forma a termos funções 'mais simples'.

### Máquinas de Vetores de Suporte (SVM)
- São baseadas em conceitos da teoria do aprendizado estatístico, desenvolvida por Vapnik e colegas;
- Basicamente, a ideia seria estudar garantias teóricas sobre condições necessárias para o processo de aprendizado;
- Como dito anteriormente, temos duas principais limitações durante um processo de aprendizagem;
    - overfitting: baixa capacidade de generalização no conjunto de teste;
    - underfitting: baixa capacidade de aprendizado no conjunto de treinamento.
- Qual seria a situação ideal?
    - Um compromisso entre as duas situações, ou seja, uma relação custo-benefício entre supertreinamento e subtreinamento;
- Quando o aprendizado é consistente, ou seja, quando f* consegue aprender dos dados?
    - Primeiramente precisamos definir o espaço de funções F que o nosso classificador fará parte. 
    - Fall: espaço de todas as funções possíveis;
    - F: espaço das funções que o classificador pode aprender;
    - fbayes: classificador de mínimo risco possível;
    - fmin: classificador de mínimo risco em F.
- Fazemos uma analogia com o algoritmo do Perceptron no sentido que ambos utilizam uma função de decisão linear, ou seja, um hiperplano. A diferença é que o hiperplano do Perceptron não possui propriedades ótimas que o hiperplano encontrado no SVM possui;
- Quando temos um problema de otimização sujeito à restrições de desigualdade, utilizamos duas principais ferramentas matemáticas: condições `KKT (Karush-Kuhn-Tucker)` e os chamados `Multiplicadores de Lagrange`;

- Um outro desafio é: como tornar SVM válido para problems de classificação com múltiplas classes? Basicamente, para um problema com c classes temos duas abordagens:
    - OVA (One versus all): treinamos c SVM's e removemos a função sgn da Equação 26 (slide) para que a mesma retorne uma pontuação (score). A classe da amostra corresponde àquela SVM que retornou a maior pontuação. Essa pontuação geralmente é calculada como sendo a distância da amostra a ser classificada até o hiperplano de separação (maior a distância, maior a pontuação);
    - OVO (one versus one): treinamos c(c-1)/2 classificadores SVM, isto é, todos os pares de combinações entre classes. Para cada combinação, o classificador vencedor recebe um voto, e a classe escolhidaa é a do classificador que recebeu a maior quantidade de votos. Uma desvantagem dessa abordagem é que, quando o número de classes é alto, ela é muito custosa.

### Floresta de Caminhos ótimos
- Existe um conjunto de abordagens que tratam o problema de classificção de padrões como sendo uma tarefa de particionamento em grafos. No entanto, o que seriam esses chamados grafos?
- Grafos podem ser entendidos como estruturas de dados que são compostas por vértices e arestas e que, dependendo de suas propriedades, podem modelar diferentes problemas.
- A OPF visa modelar o problema de classificação das amostras como sendo uma tareda de particionamento de um grafo em grupos de amostras com o mesmo rótulo;
- Neste sentido, as amostras do conjunto de dados correspondem aos nós do grafo e as arestas são definidas por alguma relação de adjacência escolhida previamente;
- Possui, atualmente, versões supervisionadas, não supervisionadas e semi-supervisionadas.

### k-Vizinhos mais Próximos (KNN)
- Uma das técnicas mais tradicionais em aprendizado de máquina;
- Dada uma amostra x qualquer do conjunto de teste, o seu rótulo y será o mesmo da amostra mais próxima do conjunto de treinamento;
- É interessante para problemas de recomendação e recuperação, dado que faz uso das amostras mais próximas para tomada de decisão;
- Outro ponto importante diz respeito à regressão por k-NN, que também é bastante simples;
    - Neste caso, ao conectar à amostra de teste aos seus k cizinhos mais próximos, basta utilizar, por exemplo, o valor médio de suas saídas como sendo  o valor a ser estimado;
- Uma variante do kNN é a sua versão ponderada, conhecida por wwighted kNN;
    - A ideia consiste em associar pesos à cada um dos k vizinhos mais próximos, que podem ser o inverso de sua distência para a amostra em questão, por exemplo;

### Classificador Bayesiano
- A teoria de Decisão Bayesiana é um ferramental matemático que nos prmite construir classificadores paramétricos, ou seja, técnicas que assimem a hipótese de que os dados seguem alguma distribuição (hipótese Gaussiana na grande maioria dos casos);
- p(x|wi): Probabilidade condicional da classe wi (verossimilhança) - Ela descreve a função de densidade de probabilidade, ou seja, qual o comportamento de x dentro da classe wi;
    - Ex: Se x corresponde à altura do jogador em metros, p(x|wi) descreve a distribuição das alturas dos jogadores de futebol e p(x|w2) descreve a distribuição das alturas dos jogadores de basquete.
- p(wi|x): Probabilidade a posteriori da classe wi, isto é, a probabilidade de decidirmos pela classe wi dada que observamos a amostra x;

### k-Médias
- Existem problemas para os quais não temos acesso aos rótulos da classe, ou seja, temos um problema de aprendizado não supervisionado (agrupamento);
- O k-Means objetiva agrupar dados com base nas distancias entre as amostras. Geralmente, a distancia euclidiana é uma das mais utilizadas;
- O objetivo da técnica é particionar as amostras em k < m grupos;

### Modelo de Mistura de Gaussianas
- É uma técnica de aprendizado não supervisionado que pode ser entendida como uma generalização do k-médias. Ao invés de estimarmos os centroides de cada agrupamento, tentamos estimar também a forma e proporção de cada Gaussiana que compõe a mistura;

### Análise de Componentes Principais
- Técnicas de redução de dimensionalidade/transformação do espaço de características visam obter versões mais compactas/representativas de nossos dados;
- Usualmente, em problemas de classificação, temos a impressão de, quanto mais características temos, melhor será a taxa de acerto de nossa técnica;
- Maldição da dimensionalidade = quando temos número limitado de amostras;
- Fenômeno de Hughes: para um número finito de amostras, existe uma dimensionalidade d* que, após este valor, o desempenho da taxa de classificação diminui;
- Número de amostras como função das características: em classificadores não paramétricos, o número de amostras deve ser uma função exponencial do numero de características;
- Gaussianas multivariadas: a densidade das amostras tende a se concentrar na cauda da distribuição, ou seja, longe da média amostral, dificultando a classificação.
- Autovalores e Autovetores...