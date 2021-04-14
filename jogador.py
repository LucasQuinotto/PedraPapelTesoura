class Jogador:

    def apresentar_cartas(self, cartas_jogador):
        print("\n  SUAS CARTAS: \n")
        for i in range(len(cartas_jogador)):
            print(f"{i+1} - {cartas_jogador[i]}")

    def escolher_carta_jogador(self, cartas_jogador):
        while True:
            if len(cartas_jogador) == 0:
                print("Vish, acabaram as cartas ... a Rodada empata !!")
                return "nada"
            else:
                carta_escolhida = input("\nESCOLHA UMA CARTA PARA JOGAR: ")
                if carta_escolhida not in cartas_jogador:
                    print("Esta carta não existe !!  Você esta maluco ?!")
                else:
                    cartas_jogador.remove(carta_escolhida)
                    return carta_escolhida
