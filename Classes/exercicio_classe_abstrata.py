import math
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self, x, y):
        self.x, self.y = x, y

    @abstractmethod
    def calculaArea(self):
        pass

    @abstractmethod
    def desenhe(self):
        pass


class Forma2D(FormaGeometrica):
    def __init__(self, x, y):
        super().__init__(x, y)


class Forma3D(FormaGeometrica):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


class Poligono(Forma2D):
    def __init__(self, x, y, quantidade_lados, tamanho_lados, apotema):
        super().__init__(x, y)
        self.quantidade_lados = quantidade_lados
        self.tamanho_lados = tamanho_lados
        self.apotema = apotema

    def calculaArea(self):
        perimetro = self.quantidade_lados * self.tamanho_lados
        area = (perimetro * self.apotema) / 2
        print("O perímetro do Polígono é " + str(perimetro))
        print("A área do Polígono é " + str(area))

    def desenhe(self):
        print(f"{type(self).__name__} centrada(o) em ({self.x}, {self.y}) \n")

    def compara_poligono(self, outro_poligono):
        return self.x == outro_poligono.x and self.y == outro_poligono.y and self.quantidade_lados == outro_poligono.quantidade_lados and self.tamanho_lados == outro_poligono.tamanho_lados and self.apotema == outro_poligono.apotema
    
    def compara_retangulo(self, retangulo):
        return False

    def compara_quadrado(self, quadrado):
        return False

    def compara_esfera(self, esfera):
        return False

    def compara_cubo(self, cubo):
        return False

    def compara_cilindro(self, cilindro):
        return False

    def __eq__(self, outro):
        return outro.compara_poligono(self)

pol_2D = Poligono(0, 0, 5, 2, 1)
pol_2D.calculaArea()
pol_2D.desenhe()

class Retangulo(Forma2D):
    def __init__(self, x, y, altura, largura):
        super().__init__(x, y)
        self.altura = altura
        self.largura = largura

    def calculaArea(self):
        area = self.altura * self.largura
        perimetro = 2 * (self.altura + self.largura)
        print(f"O perímetro do {type(self).__name__} é " + str(perimetro))
        print(f"A área do {type(self).__name__} é " + str(area))

    def desenhe(self):
        print(f"{type(self).__name__} centrada(o) em ({self.x}, {self.y}) \n")

    def compara_retangulo(self, outro_retangulo):
        return self.x == outro_retangulo.x and self.y == outro_retangulo.y and self.altura == outro_retangulo.altura and self.largura == outro_retangulo.largura

    def compara_poligono(self, poligono):
        return False

    def compara_quadrado(self, quadrado):
        return False

    def compara_esfera(self, esfera):
        return False

    def compara_cubo(self, cubo):
        return False

    def compara_cilindro(self, cilindro):
        return False

    def __eq__(self, outro):
        return outro.compara_retangulo(self)


ret_2D = Retangulo(0, 0, 2, 5)
ret_2D.calculaArea()
ret_2D.desenhe()

class Quadrado(Retangulo):
    def __init__(self, x, y, altura, largura):
        super().__init__(x, y, altura, largura)

    def compara_quadrado(self, outro_quadrado):
        return self.x == outro_quadrado.x and self.y == outro_quadrado.y and self.altura == outro_quadrado.altura and self.largura == outro_quadrado.largura

    def compara_poligono(self, poligono):
        return False

    def compara_retangulo(self, retangulo):
        return False

    def compara_esfera(self, esfera):
        return False

    def compara_cubo(self, cubo):
        return False

    def compara_cilindro(self, cilindro):
        return False

    def __eq__(self, outro):
        return outro.compara_quadrado(self)
    

qd_2D = Quadrado(0, 0, 4, 4)
qd_2D.calculaArea()
qd_2D.desenhe()


class Esfera(Forma3D):
    def __init__(self, x, y, z, raio):
        super().__init__(x, y, z)
        self.raio = raio

    def calculaArea(self):
        area = 4 * math.pi * (self.raio ** 2)
        perimetro = 2 * math.pi * self.raio
        volume = (4 * math.pi * (self.raio ** 3)) / 3
        print(f"O perímetro do {type(self).__name__} é " + str(perimetro))
        print(f"A área do {type(self).__name__} é " + str(area))
        print(f"O volume do {type(self).__name__} é " + str(volume))

    def desenhe(self):
        print(f"{type(self).__name__} centrada(o) em ({self.x}, {self.y}) \n")

    def compara_esfera(self, outro_esfera):
        return self.x == outro_esfera.x and self.y == outro_esfera.y and self.z == outro_esfera.z and self.raio == outro_esfera.raio

    def compara_poligono(self, poligono):
        return False

    def compara_retangulo(self, retangulo):
        return False

    def compara_quadrado(self, quadrado):
        return False

    def compara_cubo(self, cubo):
        return False

    def compara_cilindro(self, cilindro):
        return False

    def __eq__(self, outro):
        return outro.compara_esfera(self)

esf = Esfera(0, 0, 0, 5)
esf.calculaArea()
esf.desenhe()

class Cubo(Forma3D):
    def __init__(self, x, y, z, aresta):
        super().__init__(x, y, z)
        self.aresta = aresta

    def calculaArea(self):
        area = 6 * self.aresta ** 2
        perimetro = 12 * self.aresta
        volume = self.aresta ** 3
        print(f"O perímetro do {type(self).__name__} é " + str(perimetro))
        print(f"A área do {type(self).__name__} é " + str(area))
        print(f"O volume do {type(self).__name__} é " + str(volume))

    def desenhe(self):
        print(f"{type(self).__name__} centrada(o) em ({self.x}, {self.y}) \n")

    def compara_cubo(self, outro_cubo):
        return self.x == outro_cubo.x and self.y == outro_cubo.y and self.z == outro_cubo.z and self.aresta == outro_cubo.aresta

    def compara_poligono(self, poligono):
        return False

    def compara_retangulo(self, retangulo):
        return False

    def compara_quadrado(self, quadrado):
        return False

    def compara_esfera(self, esfera):
        return False

    def compara_cilindro(self, cilindro):
        return False

    def __eq__(self, outro):
        return outro.compara_cubo(self)

cb = Cubo(0, 0, 0, 2)
cb.calculaArea()
cb.desenhe()

class Cilindro(Forma3D):
    def __init__(self, x, y, z, raio, altura):
        super().__init__(x, y, z)
        self.raio = raio
        self.altura = altura

    def calculaArea(self):
        areaBase = math.pi * (self.raio ** 2)
        areaLateral = 2 * math.pi * self.altura * self.raio
        areaTotal = (2 * areaBase) + areaLateral
        volume = areaBase * self.altura
        print(f"A área do {type(self).__name__} é " + str(areaTotal))
        print(f"O volume do {type(self).__name__} é " + str(volume))

    def desenhe(self):
        print(f"{type(self).__name__} centrada(o) em ({self.x}, {self.y}) \n")

    def compara_cilindro(self, outro_cilindro):
        return self.x == outro_cilindro.x and self.y == outro_cilindro.y and self.z == outro_cilindro.z and self.raio == outro_cilindro.raio and self.altura == outro_cilindro.altura

    def compara_poligono(self, poligono):
        return False

    def compara_retangulo(self, retangulo):
        return False

    def compara_quadrado(self, quadrado):
        return False

    def compara_esfera(self, esfera):
        return False

    def compara_cubo(self, cubo):
        return False

    def __eq__(self, outro):
        return outro.compara_cilindro(self)

cl = Cilindro(0, 0, 0, 3, 5)
cl.calculaArea()
cl.desenhe()

class limiteMax(Exception):
    pass

def raiseLimiteMax():
    raise limiteMax()

class Quadro:
    def __init__(self, qntd_max = 11):
        self.qntd_max = qntd_max
        self.figuras_geometricas = []

    def incluir_na_lista(self, figura):

        def contem(self, figura): # verificar se a figura já está contida na lista (se for identica em relação aos atributos, não será adicionada)
            for i, f in enumerate(self.figuras_geometricas): #percorrer com um for contendo o índice (i) e figura(f)
                if (f == figura):
                    return True
            return False
        if (not contem(self, figura)):
            if(len(self.figuras_geometricas) >= self.qntd_max):
                raise limiteMax(f"\nLimite atingido. Máximo: {self.qntd_max}\n") # a quantidade máxima atribuida foi de 11. Ao tentar adicionar o 12º elemento (len da lista será maior que a qntd_max), retornará a exceção
            else:
              self.figuras_geometricas.append(figura)
        else:
            print(f"\nFigura {figura} já existe na lista.\n")

    def remover(self, idx): # remove pela posição da figura
        if not isinstance(idx, int):
            raise TypeError("Somente tipo inteiro") # só recebe tipo inteiro. Se digitar outro tipo, retornará exceção.
        if (idx > len(self.figuras_geometricas)):
            raise ValueError("Posição Inválida") # Se pedir para remover algum índice maior do que o tamanho da lista, retornará exceção.
        self.figuras_geometricas.pop(idx)

    def calculaArea(self):
        for figura in self.figuras_geometricas:
            figura.calculaArea()

    def desenhe(self):
        for figura in self.figuras_geometricas:
            figura.desenhe()

    def contador(self):
        for idx, f in enumerate(self.figuras_geometricas):
            print("==========", idx, "==========")
            print(self.figuras_geometricas[idx])

    def remover_forma(self, figura): # remove pela forma, não pelo índice
        for i, f in enumerate(self.figuras_geometricas):
            if (f == figura):
                self.remover(i)
                break

ret1 = Retangulo(0, 0, 2, 4)
ret2 = Retangulo(0, 0, 4, 8)
ret4 = Retangulo(0, 0, 4, 8)
q1 = Quadrado(0, 0, 2, 2)
q2 = Quadrado(0, 0, 4, 4)
pol1 = Poligono(0, 0, 5, 5, 2)
pol2 = Poligono(0, 0, 8, 8, 5)
es1 = Esfera(0, 0, 0, 5)
es2 = Esfera(0, 0, 0, 10)
cb1 = Cubo(0, 0, 0, 6)
cb2 = Cubo(0, 0, 0, 10)
cl1 = Cilindro(0, 0, 0, 5, 10)
cl2 = Cilindro(0, 0, 0, 10, 20)

qd = Quadro(11)
try:
    qd.incluir_na_lista(ret1)
    qd.incluir_na_lista(ret2)
    qd.incluir_na_lista(ret4)
    qd.incluir_na_lista(q1)
    qd.incluir_na_lista(q2)
    qd.incluir_na_lista(pol1)
    qd.incluir_na_lista(pol2)
    qd.incluir_na_lista(es1)
    qd.incluir_na_lista(es2)
    qd.incluir_na_lista(cb1)
    qd.incluir_na_lista(cb2)
    qd.incluir_na_lista(cl1)
    qd.incluir_na_lista(cl2)
except limiteMax as e:
   print(e)
except NameError:
    print(f"\n Forma inválida\n")

qd.contador()

try:
    qd.remover(4.4)
except ValueError:
    print("\nOcorreu um erro de valor")
except TypeError:
    print("\nOcorreu um erro de tipo")

print("\n********* Removendo figura *********\n")

qd.contador()

print("\n********** Removendo Outra Figura **********\n")

rt3 = Retangulo(0, 0, 2, 4) # mesmo rt3 não tendo sido adicionado na lista, ele é idêntico ao rt1, portanto rt1 será removido por comparação.
qd.remover_forma(rt3)
qd.calculaArea()
qd.desenhe()
qd.contador()