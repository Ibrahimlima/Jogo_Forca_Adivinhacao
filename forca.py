import random

def jogar():

    introduçao()
    palavra_secreta = seleçao_da_palavra()

    letras_acertadas = ["_" for letras in palavra_secreta]

    print("Adivinhe a palavra secreta antes que seja enforcado!!")
    print("")


    acertou = False
    enforcou = False
    tentativas = 7
    letra_faltando = str(letras_acertadas.count("_"))

    print("É uma fruta!! e tem {} letras".format(letra_faltando))

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = chute_jogador()
        if(chute in palavra_secreta):
            letra_descoberta(palavra_secreta, chute, letras_acertadas)
        else:
            tentativas -= 1
            print("puts!! Você errou!! Você tem mais {} tentativas, boa sorte".format(tentativas))
            desenha_forca(tentativas)


        #enforcou = tentativas == 0
        #acertou = "_" not in letras_acertadas
        print(" ")
        print(letras_acertadas)
        #print(letra_faltando)

        #"""
        if ("_" not in letras_acertadas ):
            print(" ")
            print("Parabéns você acertou a Palavra Secreta!!!")
            mensagem_vencedor()
            break
        if(tentativas == 0):
            print(" ")
            print("Que pena, Você foi enforcado (y.y), a palavra secreta era {}".format(palavra_secreta))
            break 
        #"""


    print("")
    print("FIM DO JOGO")


def introduçao():
    print("****************************")
    print("Ola, bem vindo ao Jogo da Forca!!")
    print("****************************")
    print("")

def seleçao_da_palavra():
    arquivo = open("palavra.txt", "r")

    lista_de_palavras = []
    for linha in arquivo:
        linha = linha.strip()
        lista_de_palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(lista_de_palavras))
    palavra_secreta = lista_de_palavras[numero].upper()
    return palavra_secreta

def chute_jogador():
    chute = input("Qual letra deseja?  ")
    chute = chute.strip().upper()
    return chute


def letra_descoberta(palavra_secreta, chute, letras_acertadas):
    posicao = 0
    for letra in palavra_secreta:
        if (chute.lower() == letra.lower()):
            letras_acertadas[posicao] = letra
            letra_faltando = str(letras_acertadas.count("_"))
        posicao += 1
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


if(__name__ == "__main__"):
    jogar()