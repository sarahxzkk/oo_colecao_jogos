from modelos.jogo import Jogo

jogo_zelda = Jogo('Zelda', 'RPG')
jogo_sonic = Jogo('Sonic', 'Plataforma')

jogo_zelda.alterar_status()

jogo_zelda.recebe_nota('Gomes', 10)

def main():
    Jogo.listar_jogos()

if __name__ == '__main__':
    main()