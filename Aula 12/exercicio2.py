#Faça um programa que simule o armário de uma escola e permita colocar o nome do aluno responsavel/pagante da gaveta. O armario tem a dimensão 5x5
print("valores dos armarios: \n armario comum: 30$ \n armario vip:50$")



matriz_comum = [
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""]
    
    ]

matriz_vip= [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

armario = input("qual armario voce gostaria de adquirir vip ou normal?").lower()
nome = input("qual é o seu nome?")


if armario == "vip":
    linha = int(input("Em qual linha do armário será sua gaveta? (0 a 2)"))
    coluna = int(input("Em qual coluna do armário será sua gaveta? (0 a 2)"))
    matriz_vip[linha][coluna] = nome
    for linha in matriz_vip:
        print(linha)
elif armario == "normal":
    linha = int(input("Em qual linha do armário será sua gaveta? (0 a 2)"))
    coluna = int(input("Em qual coluna do armário será sua gaveta? (0 a 2)"))
    matriz_comum[linha][coluna] = nome
    for linha in matriz_comum:
        print(linha)
        
else:
    print("armario não identifcado")

