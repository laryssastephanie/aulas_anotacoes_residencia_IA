import numpy as np
from datetime import datetime

# a = np.array([1, 2, 3]) # vetor de 1 dimensão
# print(a.ndim)
# b = np.array([[1, 2, 3], [4, 5, 6]]) # duas dimensões
# print(a.ndim)

# a.shape # retorna (2, 3) = tamanho da matriz

# c = np.ones((2, 3)) # apenas valores de 1

# d = np.eye(3) # 3 x 3 de 1 na diagonal


# list(range(1, 10))
# e = np.arange(1,10)

# f = np.linspace(0, 0.5, 6)

def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c

def python(n):
    a = list(range(n))
    b = list(range(n))
    c = []
    for i in range(len(a)):
        a[i] = i**2
        b[i] = i**3
        c.append(a[i] + b[i])

    return c

a = np.array([[1, 2, 3], [5, 6, 7], [8, 9, 10]])
print(a[1, 2]) # segunda linha, terceira coluna
print(a[0, :]) # primeira linha, todas as colunas
print(a[0, 0:2]) # a partir do zero, me retorne 2 elementos

b = a[1:3, 1:3]
print(b)

a[1, 1] = 0 # vai mudar em a e em b, pois sao compartilhados
print(a)
print(b)

a[0:2, 1] = 0
print(a)

a = np.arange(10)
print(a)

print(a > 4) # retorna booleanos

print (a[a>4]) # retorna as posições que são True
print(a[(a>4) & (a<7)])

a[(a>4) & (a<7)] = 0 # troca os valores correspondentes por 0
print(a)

a.dtype # retorna tipo
a.shape # forma da matriz
a.ndim # dimensão
a.nbytes
a.T # transposta

np.max(a) # maior elemento
np.min(a) # menor elemento
np.sum(a) # soma de todos os elementos
np.std(a) # desvio padrão

