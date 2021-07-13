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
![ciclo de desenvolvimento](ciclo_desenv.png)

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

#### Aprendizado Supervisionado
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
    - Ockham
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