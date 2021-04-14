import jogo
import jogador

jogo_atual = jogo.Jogo()
jogador = jogador.Jogador()

numero_rodadas = 10
placar_jogador = 0
placar_oponente = 0

baralho = ["pedra", "pedra", "pedra", "pedra", "pedra", "pedra", "pedra", "pedra", "pedra",
           "papel", "papel", "papel", "papel", "papel", "papel", "papel", "papel", "papel",
           "tesoura", "tesoura", "tesoura", "tesoura", "tesoura", "tesoura", "tesoura", "tesoura", "tesoura",
           "pedra", "pedra", "pedra", "pedra", "pedra", "pedra", "pedra", "pedra", "pedra",
           "papel", "papel", "papel", "papel", "papel", "papel", "papel", "papel", "papel",
           "tesoura", "tesoura", "tesoura", "tesoura", "tesoura", "tesoura", "tesoura", "tesoura", "tesoura",
           "pedra", "papel", "tesoura", "pistola", "pistola", "pistola"]


jogo_atual.comecar_rodadas(baralho, numero_rodadas, jogador.apresentar_cartas,
                           jogador.escolher_carta_jogador, placar_jogador, placar_oponente)
