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
