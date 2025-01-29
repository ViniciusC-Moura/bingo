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
    