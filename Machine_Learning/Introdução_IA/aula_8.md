## Inteligência Artificial X Aprendizado de Máquina
- Detecção: detectar algum objeto;
- Reconhecimento: dizer o que é aquele objeto;

### Regressão Linear - Relembrando
- Univariada:
    - Em aprendizado de máquina, existem diversos problemas para os quais conhecemos um conjunto de valores de entrada e desejamos estimar o valor de saída. Um exemplo bastante comum é a precificação de imóveis, cujo valor de entrada corresponde ao tamanho de uma casa e a saída desejada é o seu preço;
    - Uma única variável como entrada - univariada;
    - Linear - uma reta;
    - Equação da reta:
        - y = b + ax (b = intercepto, onde a reta cruza o eixo y / a = inclinação da reta);
    - Por que utilizar o MSE ao invés do MAE?
        - O quadrático minimiza a 'energia' total. O L1 tende a minimizar eixos;
        - O formato da função de custo nos remete à uma função quadrática;
    - Gradiente descendente:
        - Faz busca pelos valores de w baseando-se na derivada da função de custo. Como funciona?
            - Atribua valores aleatórios para w = [w0 w1];
            - Avalie a função de custo J(w);
            - Caso o critério de parada tenha sido atingido, vá para o passo 5;
            - Atualize o vetor w e retorne ao passo 2;
            - Fim do algoritmo.
        - Função convexa: um ótimo global;
        - Função não convexa: ótimo local, ótimo global;
        - GD busca a 'melhoe' solução a partir de um ponto inicial. Com base em informações dadas pela derivada da função, ele tende a encontrar um ótimo local ou global. Caso a função seja convexa, ele encontrará o ótimo global.
### Regressão multivariada - Revisão
- Suponha que tenhamos mais variáveis pare representar o problema, visto que utilizar apenas o tamanho da casa não é suficiente para estimarmos o seu valor (números de quartos, capacidade da garagem, piscina, etc.);
- Como podemos melhorar a convergência durante o aprendizado?
     - Gradiente desc. em lotes (mini-batches) ou online;
     - Converge mais rápido do que o gradiente desc. (pode não avaliar todo o espaço de busca);
     - Parecido com o gradiente desc. online, porém é aplicado sobre amostragens aleatórias do conjunto de treinamento;