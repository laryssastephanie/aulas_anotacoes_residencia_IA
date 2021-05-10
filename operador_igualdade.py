class FormaGeometrica:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

class Quadrado(FormaGeometrica):
    def __init__(self, x, y, lado=1):
        super().__init__(x, y)
        self.lado = lado

# class Circulo(FormaGeomatrica):
#     def __init__(self, x, y, raio=1):
#         super().__init__(x,y)
#         self.raio = raio

# c1 = Circulo(0, 0, 1)
# c2 = Circulo(0, 0, 1)
# print(c1 == c2)

# mesmo tendo os mesmos atributos, retorna FALSE

# fazer operador de igualdade:

class Circulo(FormaGeometrica):
    def __init__(self, x, y, raio=1):
        super().__init__(x,y)
        self.raio = raio
    def __eq__(self, outro):
        if(type(outro) is Circulo):
            return self.x == outro.x and self.y == outro.y and self.raio == outro.raio # comparação de todos os atributos
        return False

c1 = Circulo(0, 0, 1)
c2 = Circulo(0, 0, 1)
c3 = Circulo(1, 1, 1)
print(c1 == c2) # retorna True: mesma forma, atributos identicos
print(c1 == c3) # retorna False: mesma forma, atributos diferentes

q1 = Quadrado(0, 0, 1)
print(c1 == q1) #retorna False: forma diferente, atributos iguais