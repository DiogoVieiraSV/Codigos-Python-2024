#faça um programa que peça 1 número ao cliente e faça sua tabiada (até o 10)

Tabuada = int(input("Digite um numero inteiro pra ser multiplicado: "))

contador = 1

while contador <= 10:
    print(contador, "X",Tabuada,"=",contador*Tabuada)
    contador += 1