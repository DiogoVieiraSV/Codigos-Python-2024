#Faça um programa que diga quais dos 20 primeiros numero multiplos de 5 são pares
somaimpar = 0
for i in range (5,101, 5):
    if (i % 2==0):
        print(i)
    else:
        somaimpar += i
print(somaimpar)
    

 