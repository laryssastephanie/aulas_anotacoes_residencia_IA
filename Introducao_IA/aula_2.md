## Inteligência Artificial - Aula 2
### Aprendizado de Máquina
- Definições:
    - Ciência (ou arte) da programação de computadores para que eles possam aprender com os dados;
    - "Campo de estudo que oferece aos computadores a capacidade de aprender sem serem explicitamente programados". Arthur Samuel, 1959;
    - Um algoritmo determinístico possui regras claras para retornar resultados de acordo com a entrada fornecida;
    Se a entrada pode variar muito, esse conjunto de regras será muito grande, podendo tornar o tempo de execução inviável;
- Programação 'tradicional' (Sistema baseados em regras):
    - Natureza dinâmica dos problemas exige redefinição constante das regras;
    - Sistema de detecção de SPAM de e-mail:
        - Ex: um filtro de spam baseado em Aprendizado de Máquina é capaz de utilizar critérios diversos para fazer tal classificação;
            - Caracterização de um SPAM pode ser adaptada dinamicamente de acordo com marcações atribuídas pelos usuários;
            - Spammers identificam que as regras não detectam números e trocam 'Dois' por 2.

                    Data + Program ==> Computation ==> Results
- Machine Learning:
    - Fundamentalmente, envolve a construção de modelos matemáticos para ajudar entender dados;
        - Funções arbitrariamente complexas
    - Ajustes de parâmetros:
        - Permite que os modelos sejam adaptados aos dados observados;
    - Desta forma, tais modelos podem ser usados apra prever e entender aspectos de dados desconhecidos

            Data + Results ==> Computation ==> Program

- Ciclo de desenvolvimento
![ciclo de desenvolvimento](imagens/ciclo_desenv.png)

#### Aprendizagem Estatística
- Até a década de 90, era um problema de estimativa de função a partir de uma determinada coleção de dados;
- Com desenvolvimento de novas técnicas de análisena década de 90 (Ex: Support Vector Machines);
    - Não apenas uma ferramenta para a análise teórica;
    - Ferramenta para a criação de algoritmos práticos para estimar funções com entradas em N-Dimensões
- Como estimar a função f?
    -  processo estatístico é iniciado a partir de um conjunto de eventos conhecidos;
        -Conjunto de treinamento, base de treino;
    - Cada evento possui um ou mais valores de variáveis preditoras X: X1, X2, ..., Xn e um valor de saída Y;
    - Avaliação de desempenho da função f;
    - Distância entre o valor predito e o valor observado E;
    - utilizar aprendizado estatístico no conjunto de treinamento para estimar a função f;
        - Encontrar uma função f' t.q. y = f'(X) p/ qualquer observação (X,Y);
- Por que estimar a função f?
    -Predição: estimar o valor de uma variável de saída Y a partir de uma ou mais valores de variáveis de entrada X;
        - Levando em conta dados futuros (não vistos pelo modelo - para os quais não conhecemos o valor Y);
    - Inferência: entender a relação entre cada variável X e variável Y - como a mudança em X1, ..., Xn afeta o valor de Y;
        - Quais preditores estão associados à resposta?
        - Qual é a relação entre a resposta e cada preditor?

#### Categorias elementares de Algoritmos de Aprendizado de Máquina
- Supervisionado;
    - Classificação;
    - Regressão;
- Não- Supervisionado;
    - Agrupamento;
    - Redução de Dimensionalidade;
- Semi-Supervisionado;
    - Modelos Generativos;

### Aprendizado Supervisionado
- Envolve modelar a relação entre medidas características dos dados e algum rótulo associado aos dados;
- O modelo determinado pode ser usado para aplicar rótulos a novos dados;
- Tipos de algoritmos supervisionados;
    - Classificação: rótulos são categorias discretas;
    - Exemplo filtro de spam: E-mails são marcados como spam ou não-spam. Modelo classifica novos e-mails;
    - Regressão: rótulos são quantidades contínuas;
    - Exemplo: previsão do preço de um carro considerando um conjunto de variáveis preditoras(quilometragem, idade, marca);
- Dado conjunto de treinamento com N exemplos de pares de entrada e saída;
    - Cada Yi é gerado por uma função y = f(x) desconhecida;
- A função f' é chamada de hipótese;
- Aprender é uma busca no espaço de hipóteses possíveis para aquele que terá um bom desempenho, mesmo em novos exemplos além do conjunto de treinamento;
- Para medir a precisão de uma hipótese, fornecemos um conjunto de exemplos de teste que são distintos do conjunto de treinamento;
    - Uma hipótese generaliza bem se prediz corretamente o valor de y para novos exemplos;
- f pode ser estocástica - não é estritamente uma função de X;
    - Aprender a distribuição de probabilidade condicional, P(Y|X);
- Espaço de hipóteses H;
- Uma hipótese consistente concorda com todos os dados;
- Como podemos escolher entre várias hipóteses consistentes?
    - Ockham's razor
    - Escolhendo o espaço de hipóteses;
    - Polinomial em X vs sin(X);

#### Classificação vs Regressão
- In a nutshell
    - A classificação é a tarefa de prever um rótulo de classe discreto;
    - A regressão é a tarefa de prever uma quantidade caontínua;
- Há alguma sobreposição entre os algoritmos de classificação e regressão, por ex.:
    - Um algoritmo de classificação pode prever um valor contínuo, mas o valor contínuo está na forma de uma probabilidade para um rótulo de classe;
    - Um algoritmo de regressão pode prever um valor discreto, mas o valor discreto na forma de uma quantidade inteira;
- Alguns algoritmos podem ser usados para ambos com pequenas modificações;
    - Árvores de decisão e redes neurais artificiais;
- A maneira como avaliamos as previsões de classificação e regressão variam e não se sobrepõe;
    - As previsões de classificação podem ser avaliadas usando acurácia, enquanto as previsões de regressão não;
    - As previsões de regressão podem ser avaliadas usando a raiz do erro médio quadrático, enquanto as previsões de classificação não;

### Aprendizado não Supervisionado
- Dados de treinamento não são rotulados;
- O sistema tenta aprender sem referência ou dados anotados;
    - Ex: com base em dados sobre os visitantes de um site, executar um algoritmo para tentar detectar grupos de visitantes semelhantes;
        - Em nenhum momento você diz ao algoritmo a qual grupo um visitante pertence: ele encontra essas conexões sem ajuda;
- É difícil determinar a validade das inferências tiradas da saída da maioria dos algoritmos de aprendizagem não supervisionados;
    - Eficácia é uma questão de opinião e não pode ser verificada diretamente;
- Redução da dimensionalidade;
    - Tentativa de identificar variedades de baixa dimensão do espaço X que representam alta densidade de dados;
    - Fornece informações sobre as associações entre as variáveis;
        - Se elas podem ou não ser consideradas como funções de um conjunto menor de variáveis 'latentes';
- Agrupamento:
    - Encontrar várias regiões convezas no espaço X que contém modas de P(X);
    - Indica se P(X) pode ser representado por uma mistura de densidades mais simples que representam tipos ou classes distintas de observações;

### Características Fundamentais
- Para qualquer problema a ser investigado como ML temos algumas características comuns:
    - Amostras (Samples): linhas na base de dados;
    - Características (Features): colunas na base de dados;
    - Matriz de Características: combinação de linhas e características;
    - Vetor alvo: coluna que se deseja predizer;
- Algoritmos de ML normalmente necessitam de uma grande quantidade de dados para apresentar uma solução satisfatória;
- Dados precisam ser representativos em relação ao problema que está sendo investigado;
- Considerar a influência das categorias em relação a base completa;
- Qualidade dos dados:
    - Considerar detectar e se possível eliminar Outliers e Ruídos;
    - Descartar dados redundantes;
    - São desnecessários quando colocados no contexto de outro atributo;
    - Ex: Classe social e renda mensal;
    - Descartar dados irrelevantes;
    - Não tem relação com o atributo-alvo;
    - Ex: CPF e doença;

### Projeto iterativo de ML
- Definir o problema que se deseja atacar com um modelo preditivo;
- Organizar os dados de acordo com o problema definido;
- Definir uma métrica de avaliação;
- Separar os dados em treino e teste de acordo com a métrica;
- Inspecionar a solução;
- Propor melhorias no modelo ou organização dos dados;
- O processo de organização de dados de acordo com o modelo definido envolve as seguintes atividades;
    - Trocar dados categóricos ou ordinais por números;
    - Alterar a escala dos dados;
    - Eliminar valores faltantes ou subtituir por outro valor;
    - Separar variáveis preditoras e variáveis alvo;
    - Dividir a base em treino e teste.
