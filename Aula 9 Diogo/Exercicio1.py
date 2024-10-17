
jogar = True
while jogar == True:
    contador = 0
    print("kahhot iniciando")
    resposta1 = input("Python é uma linguem de programação que é mais simples e facil de entender? \n s/n?").lower()
    if (resposta1 == "s"):
        print("Acertou")
        contador += 1
    else:
        print("errou")

    resposta2 = input("'For' é uma forma de imprimir? \n s/n?").lower()
    if (resposta2 == "s"):
        print("Errou")
    
    else:
        print("Acertou")
        contador += 1

    resposta3 = input("input é uma forma de fazer a impressão fazer loop? \n s/n?").lower()
    if (resposta3 == "s"):
        print("Errou")
    
    else:
        print("Acertou")
        contador += 1
    
    print(f"você acertou: {contador}")

    input("deseja jogar novamente? \n s/n?")
    if (resposta3 == "n"):
        jogar = False