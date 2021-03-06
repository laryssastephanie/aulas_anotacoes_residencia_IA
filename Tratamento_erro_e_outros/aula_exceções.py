"""Anotações"""

# Exceções - sinalizam erros especiais
# Só precisam ser tratados quando fizer sentido
# Muitas classes de exceções disponíveis

# Sinalizar que algo deu errado: Lançando Exceção
# Utilizar instrução raise seguida da classe que define a exceção

class Triangulo:
    def __init__(self, base, altura):
        if not isinstance(base, float) or not isinstance(altura, float):
            raise TypeError("Somente tipo float") # o que vier após o raise, não será executado!
        self.base, self.altura = base, altura
        
    def calcula_area(self):
        return self.base*self.altura/2


# print(t2 = Triangulo("a", "b")) # retorna o erro 'Somente tipo float'
t3 = Triangulo(1.0, 1.0)
print(t3.calcula_area())

#Tratamento da exceção: try except

try:
    t2 = Triangulo("a", "b")
except:
    print("Ocorreu um erro") # O funcionamento do método não será interrompido.

# Exceções - formato geral:
# vai testando quais os tipos de erro para ver qual irá retornar ao usuário.

try:
    codigo_que_lanca_excecao()
except ValueError:
    print("ValueError")
except TypeError:
    print("Type Error")
except Exception as e:
    print("Outro erro")
else: 
    print("Código executado caso não ocorra Exceção") #caso não tenha ocorrido uma exceção
finally:
    print("Código de limpeza que sempre é executado") 

# Exceções personalizadas
# Subclasse de algum tipo de Buitlin Exception
# Podem ser organizadas em Categorias utilizando o mecanismo de herança

class ErroDeIO(Exception): 
    pass

class ErroDeEscrita(ErroDeIO):
    pass

class ErroDeLeitura(ErroDeIO):
    pass

def raiseErroDeIO(): 
    raise ErroDeIO()

def raiseErroDeEscrita():
    raise ErroDeEscrita()

def raiseErroDeLeitura():
    raise ErroDeLeitura()

# print(raiseErroDeIO())
# print(raiseErroDeEscrita())
# print(raiseErroDeLeitura())

for func in (raiseErroDeIO, raiseErroDeEscrita, raiseErroDeLeitura):
    try:
        func()
    except ErroDeIO as e:
        print(f"Erro de IO: {e.__class__}") # pode ter várias except

# raise = notifica que algo deu errado
# exemplo parecido com os exercicios de formas geometricas:

class ErroDeIndice(Exception):
    pass

class ErroDeIndiceForaDoIntervalo(Exception):
    pass


class Quadro:
    formas_geometricas = []

    def adicionar_forma(self, forma):
        Quadro.formas_geometricas.append(forma)


    def remover_forma_em(self, idx = 0):
        if not isinstance(idx, int):
            raise ErroDeIndice("Valor não inteiro")
        if idx < 0 or idx > len(Quadro.formas_geometricas) -1:
            raise ErroDeIndiceForaDoIntervalo("Valor fora do intervalo")

qd = Quadro()

try:
    qd.remover_forma_em(5)
except ErroDeIndice as e:
    print(e)
except ErroDeIndiceForaDoIntervalo as e: # 'as e' para pegar a msg do raise do erro criado. Se nao tiver o 'as e', pode printar qlqr outra msg aqui.
    print(e)
print(len(qd.formas_geometricas))