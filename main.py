import random

modo = int(input("Indique o modo de jogo:\n1 - RÁPIDO\n2 - DEMORADO\n"))
num_jogadores = 2*modo
rapido = num_jogadores == 2

# ...==================================== Funçôes Auxiliares =====================================...


def gerar_cartela():
    global rapido

    if rapido:
        cartela = [[], []]
        coluna1 = random.sample(range(1, 11), 2)
        coluna2 = random.sample(range(11,21), 2)
        coluna3 = random.sample(range(21, 31), 2)

        for i in range(2):
            cartela[i].append(coluna1[i])
            cartela[i].append(coluna2[i])
            cartela[i].append(coluna3[i])

        return cartela
    
    else:  # modo demorado
        cartela = [[], [], []]
        coluna1 = random.sample(range(1, 11), 3)
        coluna2 = random.sample(range(11,21), 3)
        coluna3 = random.sample(range(21, 31), 3)
        coluna4 = random.sample(range(31, 41), 3)

        for i in range(3):
            cartela[i].append(coluna1[i])
            cartela[i].append(coluna2[i])
            cartela[i].append(coluna3[i])
            cartela[i].append(coluna4[i])

        return cartela


def imprimir_cartela(cartela):
        global numeros_sorteados
        for i in cartela:
            print(" ".join(f"({j:02})" if j in numeros_sorteados else f" {j:02} " for j in i ))
        print("")

def sortear_numeros():
    global numeros_sorteados
    global rapido

    if not rapido:
        intervalo = 40
    else:
        intervalo = 30
    return random.sample(range(1, intervalo + 1), intervalo)

def verificar_ganhadores(cartelas, numeros_sorteados):
    vencedores = []
    for i, cartela in enumerate(cartelas):
        numeros_cartela = set(sum(cartela, []))
        if numeros_cartela.issubset(numeros_sorteados):
            vencedores.append(i + 1)
    return vencedores if vencedores else None


def bingo():

    global numeros_sorteados
    numeros_sorteados = []

    cartelas = [gerar_cartela() for _ in range(num_jogadores)]

    print(cartelas)


    print("\nCartelas geradas:")
    for i, cartela in enumerate(cartelas):
        print(f"Jogador {i+1}:")
        imprimir_cartela(cartela)
   
    input("\nDigite ENTER para iniciar o bingo ")


    for num in sortear_numeros():
        numeros_sorteados.append(num)
        print(f"\n=> Última dezena sorteada: {num:02}")
        print(f"Dezenas sorteadas até o momento: {' '.join(f'{n:02}' for n in sorted(numeros_sorteados))}")
       
        for i, cartela in enumerate(cartelas):
            print(f"\nJogador {i+1}:")
            imprimir_cartela(cartela)
       
        input("\nDigite ENTER para continuar ")
       
        ganhador = verificar_ganhadores(cartelas, numeros_sorteados)
        if ganhador:
            if len(ganhador) > 1:
                print(f"\nBINGO! Os Jogadores {ganhador} venceram!")
            else:
                print(f"\nBINGO! O Jogador {ganhador} venceu!")
            break

bingo()
