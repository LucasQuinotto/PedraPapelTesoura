import random
import colorama
from colorama import Fore, Back, Style


class Jogo:

    def comecar_rodadas(self, baralho,numero_rodadas,ver_cartas, escolher_carta,placar_jogador,placar_oponente):

        print(Fore.LIGHTBLUE_EX)
        print("\n -I=O=I-I=O=I-I=O=I-I=O=I-I=O=I-I=O=I-I=O=I-I=O=I-I=O=I-\n" +
              Fore.LIGHTCYAN_EX + "  BEM VINDO AO PEDRA, PAPEL, TESOURA E PISTOLA ROYALE !!\n" +
              Fore.LIGHTBLUE_EX + " -I=O=I-I=O=I-I=O=I-I=O=I-I=O=I-I=O=I-I=O=I-I=O=I-I=O=I-")

        for i in range(numero_rodadas):

            vencedor_rodada = "ninguém"

            print(Fore.LIGHTCYAN_EX)
            print(f"  PLACAR:"
                  f" \t\tJOGADOR: {placar_jogador}\n"
                  f" \t\t\t\tOPONENTE: {placar_oponente}")
            print(Fore.LIGHTBLUE_EX)
            print(" VOCÊ ESTA NO " + Fore.LIGHTCYAN_EX + f"{i+1}°" + Fore.LIGHTBLUE_EX + " ROUND !!")
            cartas_jogador = self.distribuir_cartas_jogador(baralho,[])
            cartas_oponente = self.distribuir_cartas_oponente(baralho,[])

            while vencedor_rodada == "ninguém":
                ver_cartas(cartas_jogador)
                carta_escolhida_jogador = escolher_carta(cartas_jogador)
                if carta_escolhida_jogador == "nada":
                    break
                elif "pistola" in cartas_oponente:
                    carta_escolhida_oponente = "pistola"
                    cartas_oponente.remove("pistola")
                else:
                    carta_escolhida_oponente = cartas_oponente[0]
                    cartas_oponente.pop(0)

                vencedor_rodada = self.definir_ganhador_rodada(carta_escolhida_jogador,carta_escolhida_oponente)
                if vencedor_rodada == "jogador":
                    placar_jogador += 1
                elif vencedor_rodada == "oponente":
                    placar_oponente += 1

        print(Fore.LIGHTCYAN_EX)
        print(f"\n\t  PLACAR FINAL:"
              f"  \tJOGADOR: {placar_jogador}\n"
              f"  \t\t\t\t\t\tOPONENTE: {placar_oponente}")


    def distribuir_cartas_jogador(self, baralho, mao_jogador=None):
        while len(mao_jogador) < 3:
            random.shuffle(baralho)
            mao_jogador.append(baralho[0])
            baralho.pop(0)
        return mao_jogador


    def distribuir_cartas_oponente(self, baralho, mao_oponente=None):
        while len(mao_oponente) < 3:
            random.shuffle(baralho)
            mao_oponente.append(baralho[0])
            baralho.pop(0)
        return mao_oponente


    def definir_ganhador_rodada(self, carta_escolhida_jogador, carta_escolhida_oponente):

       while True:
            if carta_escolhida_jogador == "pedra" and carta_escolhida_oponente == "pedra":
                print("Ambos os jogadores escolheram pedra ...  O round empatou !!")
                return "ninguém"
            elif carta_escolhida_jogador == "pedra" and carta_escolhida_oponente == "papel":
                print("O oponente escolheu papel ...  Você perdeu a rodada ...")
                return "oponente"
            elif carta_escolhida_jogador == "pedra" and carta_escolhida_oponente == "tesoura":
                print("O oponente escolheu tesoura !! Você ganhou a rodada !!")
                return "jogador"
            elif carta_escolhida_jogador == "pedra" and carta_escolhida_oponente == "pistola":
                print("PEW PEW PEW !!  O oponente escolheu pistola ...  Você perdeu a rodada ...")
                return "oponente"

            elif carta_escolhida_jogador == "papel" and carta_escolhida_oponente == "pedra":
                print("O oponente escolheu pedra !!  Você ganhou a rodada !!")
                return "jogador"
            elif carta_escolhida_jogador == "papel" and carta_escolhida_oponente == "papel":
                print("Ambos os jogadores escolheram papel ...  O round empatou !!")
                return "ninguém"
            elif carta_escolhida_jogador == "papel" and carta_escolhida_oponente == "tesoura":
                print("O oponente escolheu tesoura ... Você perdeu a rodada ...")
                return "oponente"
            elif carta_escolhida_jogador == "papel" and carta_escolhida_oponente == "pistola":
                print("PEW PEW PEW !!  O oponente escolheu pistola ...  Você perdeu a rodada ...")
                return "oponente"

            elif carta_escolhida_jogador == "tesoura" and carta_escolhida_oponente == "pedra":
                print("O oponente escolheu pedra ...  Você perdeu a rodada ...")
                return "oponente"
            elif carta_escolhida_jogador == "tesoura" and carta_escolhida_oponente == "papel":
                print("O oponente escolheu papel !!  Você ganhou a rodada !!")
                return "jogador"
            elif carta_escolhida_jogador == "tesoura" and carta_escolhida_oponente == "tesoura":
                print("Ambos os jogadores escolheram tesoura ...  O round empatou !!")
                return "ninguém"
            elif carta_escolhida_jogador == "tesoura" and carta_escolhida_oponente == "pistola":
                print("PEW PEW PEW !!  O oponente escolheu pistola ...  Você perdeu a rodada ...")
                return "oponente"

            elif carta_escolhida_jogador == "pistola" and carta_escolhida_oponente == "pedra":
                print("PEW PEW PEW !! O oponente escolheu pedra !!  Você ganhou o round !!")
                return "jogador"
            elif carta_escolhida_jogador == "pistola" and carta_escolhida_oponente == "papel":
                print("PEW PEW PEW !! O oponente escolheu papel !!  Você ganhou o round !!")
                return "jogador"
            elif carta_escolhida_jogador == "pistola" and carta_escolhida_oponente == "tesoura":
                print("PEW PEW PEW !! O oponente escolheu tesoura !!  Você ganhou o round !!")
                return "jogador"
            elif carta_escolhida_jogador == "pistola" and carta_escolhida_oponente == "pistola":
                print("PEW PEW PEW PEW PEW !! Ambos os jogadores escolheram pistola ... O round empatou !!")
                return "ninguém"
