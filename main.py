import random

# ...==================================== Funçôes Auxiliares =====================================...

def gerar_cartela(modo):
    if modo == 'rápido':
        return [[random.sample(range(1, 11), 2),
                 random.sample(range(11, 21), 2),   
                 random.sample(range(21, 31), 2)]]
    else:  # modo demorado
        return [[random.sample(range(1, 11), 3),
                 random.sample(range(11, 21), 3),
                 random.sample(range(21, 31), 3),
                 random.sample(range(31, 41), 3)]]

def imprimir_cartela(cartela, numeros_sorteados, modo):
    if modo == 'rápido':
        qtd = 10
    else:
        qtd = 18
    print("-" * qtd)
    for linha in zip(*cartela):
        print(" | ".join(f"({num:02})" if num in numeros_sorteados else f" {num:02} " for num in sum(linha, [])))
    print("-" * qtd)
