# Anotações

### Numpy

- Código mais limpo do que o código Python "direto" que tenta realizar a mesma tarefa;
- Menos loops são necessários, porque as operações funcionam diretamente em arrays e matrizes;
- Funções matemáticas tornam a vida mais fácil;
- Algoritmos sujacentes foram projetados com alto desempenho em mente;
- Os arrays do numpy são armazenados de forma mais eficiente;
- Grandes partes do numpy são escritas em C. Isso o torna mais rápido do que o código Python puro;
- Especificar o tamanho;
- Dificuldade de realizar append;
- Soma de vetores (utilizando listas):
    for i in range (len(a)):
        a[ i ] = i ** 2
        b[ i ] = i **3
        c.append(a[ i ] + b[ i ])
- Utilizando Numpy Arrays:
    c = a + b

#### Arrays N-dimensionais
- Arrays de propósito geral e homogêneos;
- Conseguem vetorizar operações;
- O número de dimensões e itens em um array é definido por sua forma (atributo shape);
    - Tupla de N inteiros não negativos que especificam os tamanhos de cada dimensão;
- Tipos especiais associados aos elementos (dtype);
- ndarrays podem compartilhas dados, de modo que as alterações feitas em um podem ser visíveis em outro;
- Segmento unidimensional contíguo de memória de computador;
    - Esquema de indexação que mapeia N inteiros para a localização de um item no bloco;
    - Stride (offset);
- Múltiplas formas de inicialização;

#### Criação de ndarrays
- numpy.array: converte outro objeto (lista, tupla, etc) para ndarray;
- numpy.empty: contrói um ndarray sem inicializar seus elementos;
- numpy.eye: constrói um ndarray com valores 1 na sua diagonal (identidade);
- numpy.ones: cria matriz de tamanho n apenas com valores 1;
- numpy.zeros: cria ndarray de tamanho n apenas com valores 0;
- numpy.full: cria ndarray  preenchido com valor específico;
- Criação a partir de um protótipo: numpy.ones_like, ...

#### Eixos
- No caso de soma:
    - 0 = mantém numero de colunas
    - 1 = mantém número de linhas

#### Aula 9 - 17/05 - 
- código 