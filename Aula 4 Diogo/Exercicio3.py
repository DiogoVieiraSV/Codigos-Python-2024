#Faça um programa que calcule o IMC do usuário e de a classificação confome a tabela
peso = float(input("qual é o seu peso?"))
altura = float(input("qual é a sua altura?"))

imc = int(peso / (altura*2))

if (imc < 18.5):
    classificação = "MAGREZA"
    grau = 0
elif(imc>=18.6 and imc<=24.9):
    classificação = "NORMAL"
    grau = 0
elif(imc>=25 and imc<=29.9):
    classificação = "SOBREPESO"
    grau = 1
elif(imc>=30 and imc<39.9):
     classificação = "OBESIDADE"
     grau = 2

else:
    classificação = "OBESIDADE SEVERA"
    grau = 3


print(f"Seu IMC é: {imc:2f}")
print(f"Classificação: {classificação}")
print(f"Grau de Obesidade: {grau}")