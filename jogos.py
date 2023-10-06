import forca
import adivinhação

def escolha_jogo():
    print("****************************")
    print("*****ESCOLHA SEU JOGO!!*****")
    print("****************************")

    print("1 : Forca / 2: Adivinhação")

    jogo = int(input("Qual jogo deseja?  "))

    if(jogo == 1):
        print("Jogo Escolhido foi: Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo Escolhido foi: Adivinhação")
        adivinhação.jogar()


if(__name__ == "__main__"):
    escolha_jogo()