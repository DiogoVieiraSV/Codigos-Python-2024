#faça um programa que pergunte quantas rodas tem um veiculo, se tiver 4 diga que é um carro ou van, se tiver 2 diga que é um bicicleta ou van.

rodas = int(input("quantas rodas tem um veiculo?"))

if (rodas == 4):
    print("acho que é um carro ou uma van")
elif (rodas == 2):
    print("acho que é uma moto ou biclicleta")
elif (rodas==6):
    print("acho que é um onibus")
elif(rodas>=8 and rodas<=20):
    print("acho que é um caminhão")
else:
    print("não foi possivel encontra um veiculo correspondente ao numero de rodas")
