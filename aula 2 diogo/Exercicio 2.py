#crie um programa que pergunte o nome do cliente, o carro, a cor do carro e imprima uma mensagem agradecendo a preferencia com ao informações citadas ao cliente na mensagem 
print("ola seja bem vindo ao lava jato Experimental!!!!")
nome = input("Qual é o seu nome?")
Nome_do_meio = input("Qual seu nome do meio?")
Sobrenome = input("Qual é o seu sobrenome?")
modelo_do_carro = input("qual é o modelo do seu carro?")
cor_do_carro = input("qual a cor do seu carro?")
print(nome+" "+ Nome_do_meio +" "+ Sobrenome)
print(modelo_do_carro+" "+ cor_do_carro)
print(" Agradeçemos pela Preferencia " + nome + " o seu veiculo: " + modelo_do_carro + " de cor " + cor_do_carro + " será limpo em breve ")
print("gostaria que seu veiculo " + modelo_do_carro + " seja lavado hoje ou amanhã? ")
agendamento = input()
print(f"ok, a limpeza do {modelo_do_carro} agendaremos para {agendamento}")
print("volte sempre!!")