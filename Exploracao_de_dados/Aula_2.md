## Regressão Linear Simples
#### Definição
- Tenta prever valores numéricos diretamente a partir de atributos de um novo exemplo;
    - Ex: prever a temperatura de amanhã a partir das condições atmosféricas
- Definição:
    - Prever uma variável quantitativa Y e R (alvo);
    - Utilizar as variáveis preditoras (X1, ..., Xn);
    - Objetivo: encontrar o modelo h

            Y = h(x1,...,Xn)

- Estratégia: Utilizar um conjunto de exemplor (dataset) onde a resposta correta é conhecida para "aprender" um modelo.

#### O caso Univariado
- Variável de resposta tem uma relação linear com os atributos;
- O nosso modelo h é então represetando como uma reta;
- Objetivo: encontrar o melhor conjunto de parâmetros de acordo com os dados de treinamento;
- Equação da reta: 
            
        y = mx + n

        onde:
        m é o coeficiente angular (inclinação);
        n é o coeficiente linear.

- Critério para seleção de melhor reta h:
        - Passe o mais próximo possível de todos os pontos.

#### Na prática:
- Utilizando o scikit-lear
            
        linear_model = LinearRegression()
        linear_model.fit(X, y)
        linear_model.predict(X)

- Fazer a separação entre dados de treino e teste;
- Lidar com situações de Under/Over fitting
    - Calculo do erro de generalização (out-of-sample error);

            from sklearn.model_selection import train_test_split
            x_train, x_test, y_train, y_test = train_test_split(x, y)

- Evitar over fitting sempre!

## Agrupamento
- Separa os dados de treinamento em K grupos;
- Algoritmo amplamente utilizado na prática;
    - Simples;
    - Fácil de se interpretar;
    - Eficiente computacionalmente;
- Partindo de um número conhecido de grupos K:
    - Selecione K centróides (instancias que representarão cada grupo);
    - Atribua cada isntancia ao cluster que tiver o centróide mais próximo;
    - Recomputa o centróide de acordo com a nova separação;
    - ...

- No scikit-learn:
            
        from sklearn.cluster import KMeans
        kmeans = KMeans(n_clusters = 4)
        lmeans.fit(X)
        y_kmeans = kmeans.predict(X)





