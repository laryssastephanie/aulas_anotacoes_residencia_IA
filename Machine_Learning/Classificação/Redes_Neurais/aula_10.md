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
