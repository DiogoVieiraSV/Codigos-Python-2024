#Faça um programa uq eimprima os 10 primeiros números da sequencia de fibonacci

#sei os dois primeiros números da sequencia
a = 0
b = 1

for i in range (10):
    print(a)
    a, b = b, a + b
    # Atualizo os valores de a e b
