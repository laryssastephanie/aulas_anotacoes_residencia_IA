## Regressão Logística
- Existem problemas para os quais desejamos estimar a classe (rótulo) de uma determinada amostra com base no seu conjunto de dados de entrada, isto é, as características do seu problema;
- Problemas de classificação são similares aos de regressão pois desejamos aprender uma função que, dada uma entrada, estime um valor de saída. A diferença é que nossa saída será mapeada para uma probabilidade (soft classification) ou  rótulo (hard classification) da amostra;
- A técnica de regressão logística é uma das mais utilizadas na literatura, principalmente por serem simples e dar bons resultados em diversas situações. Ela tem esse nome pelo fato de estimar a probabilidade de uma dada amostra pertencer à uma classe em específico. Portanto, é uma técnica de classificação do tipo soft.
- Possui função sigmóide;
- Temos dois problemas principais com MSE quando usamos a técnica de Regressão Logística:
    - A MSE não penaliza muito fortemente erros de classificação e pode levar a um aprendizado insuficiente;
        - Se não penalizar muito os erros, o aprendizado pode não ser tão bom;
    - A função de custo MSE não é convexa para o Regressor Logístico (provado matematicamente).
