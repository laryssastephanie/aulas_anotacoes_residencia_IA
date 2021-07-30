## Regressão Polinomial - Além da Linearidade
### Motivação para o uso
- Os modelos polinomiais podem ser usados naquelas situações em que a relação entre estudo e explicação variáveis é curvilínea;
- Caso especial de regressão linear:
    - Ajustamos a equação polinomial nos dados com uma relação curvilínea entre as variáveis dependentes e independentes;
- Verificar equação - slide 4
- Utilizamos o método dos mínimos quadrados para encontrar os parâmetros θi:
    - Descida do gradiente também aplicável;
- Escolha do grau do polinômio;
    - Manter o grau mais baixo possível;
    - Forward Selection vs Backward Elimination

### Definições
- Hierarquia
    - Um modelo é considerado hierárquico se contiver os termos x, x², x³, ... e não hierárquico caso alguns termos estejam faltando;
- Extrapolação: As curvaturas na região dos dados e a região de extrapolação podem ser diferentes;
- Pode ter curvas inesperadas em direções inadequadas;
- Por que são considerados casos especiais de regressão linear?

- `Técnica Splines` - quebra a 'curva' em varios segmentos, podendo analisar uma parte de forma quadrática e outra parte de forma linear, por exemplo.
    - Utilizado também para fazer Smoothing;

### Regressão KNN (K-Nearest Neighbours)
- Se k = 3, então devemos encontrar os 3 exemplos mais próximos do valor desejado;
- Média dos vizinhos -> Determinação de um novo ponto;
- K -> número de vizinhos;
- Uma métrica de distância para encontrar os vizinhos 'mais próximos';
- Uma forma de definir o peso para cada exemplo;
- Vantagens:
    - O modelo aprendido não precisa ser linear;
    - Não há fase de treinamento;
    - Poucos parâmetros a serem definidos.
- Desvantagens:
    - Processo de inferência muito custoso;
    - Sensitividade a ruído e escala.

---

## Outras formas de regressão - Árvore de Regressão
- Aprende uma estrutura de árvore binária, que divide o conjunto de treinamento de acordo com os valores dos atributos;
- Resulta em um modelo fácil de visualizar e interpretar, muito utilizado em domínios em que a solução 'caixa-preta' é aceitável;
### Como aprender a árvore?
- Repetir iterativamente até que um critério de parada seja atingido:
    - Encontrar o melhor valor para particionar cada atributo;
    - Selecionar a melhor partição entre as definidas no passo anterior;
    - Particionar os dados de treinamento conforme escolhido no passo anterior;

- A predição para uma amostra é definida como uma média do valor y de todos os exemplos no conjunto de treinamento que caem naquela mesma partição.
- Vantagens:
    - Pouco afetada pela escala dos atributos;
    - Intuitiva e fácil de compreender;
- Desvantagens:
    - Pequenas alterações nos dados podem resultar em grandes alterações nas árvores;
    - Valores preditos na regressão não são muito precisos;
    - Processo de treinamento relativamente custoso.