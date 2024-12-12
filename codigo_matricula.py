import random

def gerar_codigo_matricula(tamanho=8):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(tamanho))

codigo_matricula = gerar_codigo_matricula()

