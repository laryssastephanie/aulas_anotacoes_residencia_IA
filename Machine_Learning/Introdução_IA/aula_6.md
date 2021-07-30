## Regularização para Regressão
### Regressão: Onde estamos
- Mesmo com modelos relativamente simples, conseguimos fazer um fit bom no conjunto de treinamento;

### Seria mesmo?
- Modelos complexos tem tendência a se especializarem demais no conjunto de treinamento;
- Modelos que aderem perfeita e completamente aos exemplos mostrados correm risco de oferfitting;
- Lembre-se: O conjunto de treinamento não é uma representação perfeita do mundo real;
- O objetivo principal é modeloar um fenômeno através de exemplos, saber classificar apenas o conjunto de treinamento não vale de nada.

### Como saber se o modelo tem overfitting?
- Sempre avaliar modelos em amostras que o modelo nunca viu;
- Fazer divisões em bases de treinamento e teste, possivelmente utilizando validação cruzada;
    - Quebrar a partição de treino em n partições e faço várias inicializações;
    - Construo vários modelos;
    - Seleciono o que tem a melhor performance.

### Métrica perfeita na base de teste significa que o modelo é perfeito?
- Não necessariamente: Em nenhum problema não-trivial você terá acesso à uma base de dados completamente representativa do problema;
- Avaliar com uma base de teste alivia, não resolve o problema;
- Nunca haverá exemplos suficientes para modelar perfeitamente o fenômeno.

### Análise do erro do modelo
- Tipos de erro:
    - O erro de predição pode ser dividido em três partes:
        - `Erro irredutível`: não pode ser eliminado, independente do algoritmo usado;
            - Introduzido a partir do enquadramento escolhido do problema;
            - Causado por fatores desconhecidos;
            - Vai exsistir e TEM que existir sempre;
        - `Erro De viés`: suposições feitas por um modelo para tornar a função de destino mais fácil de aprender;
        - `Erro de Variância`: quantidade que a estimativa da função alvo mudará se deferentes dados de treinamento forem usados;

#### Erro de viés
- Diferença entre a previsão esperada (ou média) do nosso modelo e o valor correto que estamos tentando prever;
- Imagine repetir todo processo de construção do modelo mais de uma vez;
    - A cada vez que você reúne novos dados e executa uma nova análise, cria um novo modelo;
    - Devido à aleatoriedade nos conjuntos de dados subjacentes, os modelos resultantes terão uma variedade de previsões;
    - Mede o quão longe, em média, as previsões desses modelos estão do valor correto;
- Nosso modelo possui viés se ele prevê sistematicamente abaixo ou acima da variável alvo;

#### Erro de variância
- Em certo sentido, captura a capacidade de generalização do modelo;
- Quanto nossa previsão mudaria se a treinássemos com dados diferentes;
- Idealmente, não deve mudar muito de um conjunto de dados de treinamento para o próximo;
- Algoritmos que tem uma alta variância são fortemente influenciados pelas especificações dos dados de treinamento;
- Geralmente, algoritmos de aprendizado de máquina não lineares que tem muita flexibilidade tem uma alta variância;
    - Ex: Regressão polinomial com polinômios de alto grau!

#### Dilema: Variância x Viés
- Baixo Viés: sugere menos suposições sobre a forma da função de destino;
    - Árvores de Regressão, Regressão KNN;
- Alto viés: sugere mais suposições sobre a forma da função de destino;
    - Regressão Linear, Regressão Logística;
- Baixa variância: sugere pequenas alterações na estimativa da função de destino com alterações no conjunto de dados de treinamento;
    - Regressão Linear, Regressão Logística;
- Alta variância: sugere alterações na estimatica da função de destino com alterações no conjunto de dados de treinamento;
    - Árvores de Regressão, Regressão KNN.
- Aumentar o viés, diminuirá a var;
- Aumentar a var, diminuirá o viés;
- Modelos muito simples com poucos parametreos tem bias alto e baixa variação;
- Modelos muito complexos - contrário;
- Deve-se buscar o equilibrio;
- Os modelos devem tentar generalizar além do que é observado no conjunto de treinamento;
- A regularização tem o papel de controlar o overfitting dos classificadores;

---
### Regularização
#### Regressão Linear
- Regressão Lasso: mínimos quadrados são modificados para também minimizar a soma absoluta dos coeficientes (regularização L1);
- Regressão Ridge: Mínimos Quadrados são modificados para também minimizar a soma absoluta ao quadrado dos coeficientes (chamada regularização L2);
- Ao utilização de um modelo de regularização leva a uma normalização do modelo;
- Regressão Ridge é útil quando todas as variáveis são relevantes;
- Regressão Lasso da mais prioridade as variáveis que impactam mais no modelo...

#### KNN
- De certa forma, o parametro K já funciona como um regularizador;

#### Árvore de Regressão
- A ideia principal é podar algumas partes da arvore que estão atrapalhando a generalização;
- A poda pode ser feita:
    - Limitando a altura da arvore;
    - Interrompendo o crescimento após um numero de nós;
    - Eliminando (juntando com outros) nós que nao representam um certo número de exemplos.

<br>

- A regularização limita a complexidade dos modelos;
- Seu objetivo é dar um peso à generalização, em contraponto à otimizar a métrica de desempenho;
- Essencial para que os modelos sejam capazes de generalizar para exemplos não vistos.
