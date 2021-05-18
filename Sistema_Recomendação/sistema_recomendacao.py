import sys
import numpy as np

class Usuario:
    # definindo atributos
    def __init__(self, id_usuario, idade, genero, ocupacao, cep):
        self.id_usuario = id_usuario
        self.idade = idade
        self.genero = genero
        self.ocupacao = ocupacao
        self.cep = cep
        self.avaliacoes = []

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)
        # para dicionario: self.avaliacoes[avaliacao.filme.id_filme] = avaliacao
    
    def avaliar_filme(self, filme, nota):
        avaliacao = Avaliacao(self, filme, nota) # self aqui é o proprio usuario
        self.adicionar_avaliacao(avaliacao)
        filme.adicionar_avaliacao(avaliacao)
        # filme.avaliacoes.append(avaliacao) # para lista
        # filme.avaliacoes[usuario.id_usuario] = avaliacao # para dicionario
        # mas com a linha 20, não preciso reescrever, pois criou-se um método específico pra isso na linha 13

    def as_numpy_array(self, tamanho):
        vetor_usuario = np.zeros(tamanho)
        for avaliacao in self.avaliacoes:
            vetor_usuario[int(avaliacao.filme.id_filme)-1] = int(avaliacao.nota) # -1 para incluir o 0

        return vetor_usuario
        
    # exercicios serao baseados nessa def:
    def similaridade(self, outro_usuario, tamanho, algoritmo_de_similaridade):
        return algoritmo_de_similaridade.calcula(self.as_numpy_array(tamanho)), outro_usuario.as_numpy_array(tamanho)

class Filme:
    def __init__(self, id_filme, titulo, data_lancamento, url_imdb, generos):
        self.id_filme = id_filme
        self.titulo = titulo
        self.data_lancamento = data_lancamento
        self.url_imdb = url_imdb
        self.generos = generos # Lista de (objetos do tipo) Genero
        self.avaliacoes = []

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

class Genero:
    def __init__(self, id_genero, nome):
        self.id_genero = id_genero
        self.nome = nome

class Avaliacao:
    def __init__(self, usuario, filme, nota):
        self.usuario = usuario
        self.filme = filme
        self.nota = nota

class SistemaDeRecomendacao:
    def __init__(self):
        self.usuarios = dict() # dicionario para ficar como se fosse: self.usuarios['1']
        self.filmes = dict()
        self.generos = dict()

    def carregar_do_diretorio(self, diretorio):
        self.carregar_usuarios_do_arquivo(f"{diretorio}/u.user")
        self.carregar_generos_do_arquivo(f"{diretorio}/u.genre") # carregar generos antes de fazer acesso ao self.generos (linha 64)
        self.carregar_filmes_do_arquivo(f"{diretorio}/u.item")
        self.carregar_avaliacoes_do_arquivo(f"{diretorio}/u.data")

    def carregar_usuarios_do_arquivo(self, localizacao_arquivo):
        try:
            arquivo = open(localizacao_arquivo, 'r')
            for linha in arquivo:
                campos = linha.split("|") # no arquivo u.user, estao separados por | - terei uma lista de 5 posições
                usuario = Usuario(campos[0], campos[1], campos[2], campos[3],
                                campos[4])
                self.usuarios[usuario.id_usuario] = usuario # se utilizar lista, seria: self.usuarios.append(usuario)
        except Exception as e:
            print(e)
            sys.exit(1)

    def carregar_generos_do_arquivo(self, localizacao_arquivo): # antes de filmes, pq quando for criar um filmes, precisa passar uma lista de generos ANTES
        try:
            arquivo = open(localizacao_arquivo, 'r')
            for linha in arquivo:
                campos = linha.split("|")
                # Assume que não existe linha em branco no fim do arquivo
                genero = Genero(id_genero=campos[1].rstrip(), nome=campos[0]) # o id do genero esta na posiçao 1 e o nome na posição 0 # rstrip tira espaços/quebra de linha
                # self.generos.append(genero)
                self.generos[genero.id_genero] = genero # adicionar no dicionario = dict[chave] = valor
        except Exception as e:
            print(e)
            sys.exit(1)

    def carregar_filmes_do_arquivo(self, localizacao_arquivo):
        try:
            arquivo = open(localizacao_arquivo, 'r', encoding='iso-8859-1') 
            for linha in arquivo:
                campos = linha.split("|")
                generos = []
                # pegar um subespaço dessa lista de generos (0, 0, 0, 1, 1, 0, etc) e criar nova lista
                campos_generos = campos[5:-1]
                for i in range(len(campos_generos)): # passar cada um dos elementos que tenho no campo de genero
                    if campos_generos[i] == "1": #verificar se o valor no campo [i] é 1. Se for, aquele filme pertence àquele genero
                        generos.append(self.generos[str(i)]) # se for 1, adicionar na lista generos, no índice [i] - converter em string
                filme = Filme(campos[0], campos[1], campos[2], campos[4], generos)
                self.filmes[filme.id_filme] = filme

        except Exception as e:
            print(e)
            sys.exit(1)

    def carregar_avaliacoes_do_arquivo(self, localizacao_arquivo):
        try:
            arquivo = open(localizacao_arquivo, 'r')
            for linha in arquivo:
                campos = linha.split("\t") # \t significa o TAB
                usuario = self.usuarios[campos[0]]
                filme = self.filmes [campos[1]]
                nota = int(campos[2])
                usuario.avaliar_filme(filme, nota) # método criado anteriormente

        except Exception as e:
            print(e)
            sys.exit(1)

class AlgoritimoSimilaridade(SistemaDeRecomendacao):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcula(self):
        pass

class SimilaridadeCosseno(AlgoritimoSimilaridade):
    def __init__(self):
        super().__init__()

    def calcula(self, usuario_ref, outro_usuario):
        print(usuario_ref.id_usuario)
        print(str(outro_usuario.id_usuario))
        self.vetor_usuario_referencia = self.usuarios[usuario_ref.id_usuario].as_numpy_array(len(self.filmes))
        self.vetor_outro_usuario = sr.usuarios[outro_usuario.id_usuario].as_numpy_array(len(self.filmes))
        similaridade = np.dot(self.vetor_usuario_referencia, self.vetor_outro_usuario)/(np.sqrt(sum
                        (self.vetor_usuario_referencia**2))*np.sqrt(sum(self.vetor_outro_usuario**2)))
        return similaridade

class SimilaridadePearson(AlgoritimoSimilaridade):
    def __init__(self):
        super().__init__()

    def calcula(self, usuario_ref, outro_usuario):
        self.vetor_usuario_referencia  = self.usuarios[self.id_usuario].as_numpy_array(len(self.filmes))
        self.vetor_outro_usuario = sr.usuarios[outro_usuario.id_usuario].as_numpy_array(len(self.filmes))
        self.media_vetor_usuario_referencia = np.average(self.vetor_usuario_referencia)
        self.media_vetor_outro_usuario = np.average(self.vetor_outro_usuario)

        a = np.sum(self.vetor_usuario_referencia - self.media_vetor_usuario_referencia) * np.sum
        b = np.sqrt(sum(self.vetor_usuario_referencia - self.vetor_usuario_referencia)**2) * np.sqrt(
            sum(self.vetor_outro_usuario) - self.media_vetor_outro_usuario)**2
        p = a/b
        return p
        

sr = SistemaDeRecomendacao()
sr.carregar_do_diretorio("/home/laryssacosta/workspace/python-warmup/ml-100k")