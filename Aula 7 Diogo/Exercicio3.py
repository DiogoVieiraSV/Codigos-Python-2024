#faça um programa que receba 1 numero e diga se ele é primerio ou não


#peço um numero ao usúario
numero = int(input("Entre com um numero: "))
#vejo se o numero é primo ou não
primo = True
#faço um loop que vai do numero 2 até o numero antecessor a ele
for i in range (2, numero):
#Se um numero for divisivel pr qualquer numero sem ser 1 ou ele mesmo, primo será falso
    if (numero % i == 0):
        primo = False
#se primo for falso, é porque ele é divisivel por mais algum numero sem ser 1 e ele mesmo
if (primo == False):
    print("esse numero não é primo")
else:
    print("Esse é um numero primo")
    

