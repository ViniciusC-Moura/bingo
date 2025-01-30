import random

# ...==================================== Funçôes Auxiliares =====================================...

def gerar_cartela(modo):
    if modo == 'rápido':
        return [[random.sample(range(1, 21), 3),
                 random.sample(range(21, 31), 3)]]
    else:  # modo demorado
        return [[random.sample(range(1, 21), 4),
                 random.sample(range(21, 31), 4),
                 random.sample(range(31, 41), 4)]]

def imprimir_cartela(cartela, numeros_sorteados, modo):
    if modo == 'rápido':
        qtd = 10
    else:
        qtd = 18
    print("-" * qtd)
    for linha in zip(*cartela):
        print(" | ".join(f"({num:02})" if num in numeros_sorteados else f" {num:02} " for num in sum(linha, [])))
    print("-" * qtd)

def sortear_numeros(modo):
    if modo == 'demorado':
        intervalo = 40
    else:
        intervalo = 30
    return random.sample(range(1, intervalo + 1), intervalo)

def verificar_ganhadores(cartelas, numeros_sorteados):
    vencedores = []
    for i, cartela in enumerate(cartelas):
        numeros_cartela = set(sum(sum(cartela, []), []))
        if numeros_cartela.issubset(numeros_sorteados):
            vencedores.append(i + 1)
    return vencedores if vencedores else None