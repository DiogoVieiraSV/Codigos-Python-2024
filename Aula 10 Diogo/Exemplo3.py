import random

#Gerando 4 números aleatorios e armazenando em uma lista
numeros = [random.randint(20,50) for i in range (4)]

#Exibindo os números com a função sort
numeros.sort()
numeros.reverse()

print(f"Números ordenados: {numeros}")