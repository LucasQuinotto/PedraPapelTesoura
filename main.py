import jogo
import jogador

jogo_atual = jogo.Jogo()
jogador = jogador.Jogador()

numero_rodadas = 5
placar_jogador = 0
placar_oponente = 0

baralho = ["pistola", "pistola", "pistola"]

for i in range(9):
    baralho.append("pedra")
    baralho.append("papel")
    baralho.append("tesoura")


jogo_atual.comecar_rodadas(baralho, numero_rodadas, jogador.apresentar_cartas,
                           jogador.escolher_carta_jogador, placar_jogador, placar_oponente)
