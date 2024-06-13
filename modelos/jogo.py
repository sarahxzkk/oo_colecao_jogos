#metodo especial construtor __ini__
#metodo especial __srt__ para mostar um objeto em forma de texto

class Jogo:
    jogos = []
    
    def __init__(self, nome, categoria):        
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Jogo.jogos.append(self)
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    @classmethod
    def listar_jogos(cls):
        print(f"{'Nome do jogo'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}")
        for jogo in cls.jogos:
            print(f'{jogo._nome.ljust(20)} | {jogo._categoria.ljust(20)} | {jogo.ativo}')    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    def alterar_status(self):
        self._ativo = not self._ativo    
     
    
    
jogo_zelda = Jogo('zelda', 'RPG')
jogo_zelda.alterar_status()
jogo_metroid = Jogo('Metroid', 'Plataforma')

Jogo.listar_jogos()