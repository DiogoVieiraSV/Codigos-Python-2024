# função: calcula o quadrado de um número
def quadrado (numero):
    return numero **2

numero = float(input("digite um número: "))
resultado = quadrado(numero)  #recebe o retorno da função
print(f"O quadrado de {numero} é {resultado}")