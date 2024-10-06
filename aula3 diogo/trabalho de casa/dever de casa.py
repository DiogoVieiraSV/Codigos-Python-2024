#Faça um programa que diga se um numero é divisivel por 3 e diga se o numero é divisivel por 5

numero = int(input("Digite um numero:"))

if numero % 3 == 0:
    print(f"seu numero {numero} é divisivel por 3.")
else:
    print(f"seu numero {numero} não é divisivel por 3")

if numero % 5==0:
    print(f"seu numero {numero} é divisivel por 5. ")
else:
    print(f"seu numero {numero} não é divisivel por 5.")