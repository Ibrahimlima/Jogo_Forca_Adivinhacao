
def jogar():
    import random
    print("****************************")
    print("Ola, bem vindo ao jogo de adivinhação!!")
    print("****************************")
    numero_secreto = int(random.randint(0,100))
    tentativas = 0
    chance = 1


    print("Qual o nível de dificuldade desejada?")
    print("Nível 1 : Fácil / Nível 2 : médio / Nivel 3 : Difícil")
    nivel = int(input("digite aqui a dificuldade desejada: "))

    if(nivel == 1):
        tentativas = 15
        pontos = 100
    if(nivel == 2):
        tentativas = 10
        pontos = 200
    if(nivel == 3):
        tentativas = 5
        pontos = 300


    while (chance <= tentativas):
        print("Tentativa {} de {}".format(chance, tentativas))
        chute = int(input("Digite seu palpite entre 1 e 100: "))
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print("você digitou ", chute)

        if(chute < 1 or chute > 100):
            print("você deve digitar um número entre 1 e 100")
            continue


        if(acertou):
            print("Você Acertou!!")
            pontos = pontos + chute
            break
        else:
            if(maior):
                print("você errou, Seu numero foi Maior que o número secreto")
                chance = chance + 1
            elif(menor):
                print("você errou, Seu numero foi Menor que o número secreto")
                chance = chance + 1
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


    print("")
    print("FIM DO JOGO, o número secreto era", numero_secreto)
    print("Sua Pontuação é {}".format(pontos))


if(__name__ == "__main__"):
    jogar()