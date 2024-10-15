#faça um programa usando for que peça 4 números e some apenas 2 numeros impares
soma_impares = 0
contator_impares = 0

for i in range (4):
    numero =int(input("Digite 1 numero: "))
    if numero % 2 != 0:
        soma_impares += numero
        contator_impares += 1
    if contator_impares == 2:
        break
    
print("A soma dos dois primeiros números ímpares é:", soma_impares)
