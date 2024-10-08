#faça um programa para lavar rapido 

tipolavagem = int(input("-------------------Bem Vindo ao LavaRapido, qual opção você gostaria?---------------------\n Digite 1 para Lavagem Completa - R$50,00 \n Digite 2 Lavagem Basica  - R$35,00 \n qual o senhor(a) gostaria?"))
if(tipolavagem == 1):
    print("Você selecionou a lavagem completa")
    valortotal = 50
    categorialavagem = "completa"
elif(tipolavagem == 2):
    print("Você selecionou a lavagem basica")
    valortotal = 35
    categorialavagem = "Basica"
else:
    print("numero invalido, tente novamente")
pretinho = input("Gostaria de adicionar o pretinho na roda por mais R$5,00? (sim ou não)") . lower()
if(pretinho == "sim"):
    valortotal + 5
    print(f"o serviço de {categorialavagem} será no total de R${valortotal}  com pretinho")
else:
    print(f"o serviço de {categorialavagem} será no total de {valortotal}")