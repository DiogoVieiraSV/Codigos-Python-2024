#faça um programa que diga se um numero é impar ou par
#dica: para pegar o resto de uma divisão utilize "%"

numero = int(input("digite um numero:"))

if numero % 2 == 0:
    print(f"seu {numero} é par")
else:
    print(f"seu {numero} é impar")