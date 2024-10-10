#Faça um programa que some infinitamente numeros que o usuario colocar e só pare de somar caso ele escreva "parar"
x = True
soma = 0
while (x==True):
    numero = float(input("digite um numero:"))
    continuar = input("Continuar ou parar?").lower()
    if (continuar == "parar"):
        soma += numero
        x=False
        print(f"a soma deu {soma}")
    else:
        soma += numero