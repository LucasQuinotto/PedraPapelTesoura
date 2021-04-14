import colorama
from colorama import Fore, Back, Style

class Jogador:

    def apresentar_cartas(self, cartas_jogador):
        print(Fore.LIGHTBLUE_EX + "\n  SUAS CARTAS:\n")
        for i in range(len(cartas_jogador)):
            print(f"{i+1} - "  + Fore.LIGHTCYAN_EX + f"{cartas_jogador[i]}" + Fore.LIGHTBLUE_EX)


    def escolher_carta_jogador(self, cartas_jogador):
        while True:
            if len(cartas_jogador) == 0:
                print("Vish, acabaram as cartas ... a Rodada empata !!")
                return "nada"
            else:
                carta_escolhida = input(Fore.LIGHTBLUE_EX + "\n ESCOLHA UMA CARTA PARA JOGAR: ")
                if carta_escolhida not in cartas_jogador:
                    print("Esta carta não existe !!  Você esta maluco ?!")
                else:
                    cartas_jogador.remove(carta_escolhida)
                    return carta_escolhida
