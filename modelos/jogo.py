class Jogo:
    jogos = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = True
        Jogo.jogos.append(self)

    def __str__(self):
        return f'{self.nome} - {self.categoria}'
    
    def listar_jogos():
        for jogo in Jogo.jogos:
            print(f'{jogo.nome} - {jogo.categoria} - {jogo.ativo}')
      

jogo_zelda = Jogo('Zelda', 'RPG')
jogo_metroid = Jogo('Metroid', 'Plataforma')

jogos = [jogo_zelda, jogo_metroid]

Jogo.listar_jogos()