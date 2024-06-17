#metodo especial construtor __ini__
#metodo especial __srt__ para mostar um objeto em forma de texto
from modelos.nota import Avaliacao

class Jogo:
    jogos = []
    
    def __init__(self, nome, categoria):        
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        #criando uma lista de notas
        self._avaliacao = []
        Jogo.jogos.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    
    def listar_jogos(cls):
        print(f"{'Nome do jogo'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}")
        for jogo in cls.jogos:
            print(f'{jogo._nome.ljust(20)} | {jogo._categoria.ljust(20)} | {str(jogo.media_avaliacao).ljust(20)} | {jogo.ativo}')  
              
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'  
      
    def alterar_status(self):
        self._ativo = not self._ativo
        
    def recebe_nota(self, usuario, nota):
        avaliacao = Avaliacao(usuario, nota)
        self._avaliacao.append(avaliacao)
  
    @property   
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_de_notas, 1)
        return media