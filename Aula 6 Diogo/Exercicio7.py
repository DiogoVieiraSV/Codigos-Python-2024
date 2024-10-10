#faça um programa que peça 2 numeros e faça uma operação com base mo seguinte menu: 1- soma dis numeros; 2- subtrai; 3- multiplica; 4-dividir

def calcular():
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    operacao = int(input("Digite o número da operação desejada: "))
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if operacao == 1:
        resultado = num1 + num2
        print(f"O resultado da soma é: {resultado}")
    elif operacao == 2:
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    elif operacao == 3:
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    elif operacao == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida.")

calcular()
