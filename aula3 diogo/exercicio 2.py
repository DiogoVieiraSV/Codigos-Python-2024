#peça para o usuario o seu peso em Quilos e sua altura em metros, Com base nisso, retorne para o seu IMC
#IMC = peso / (altura x altura)
print("boa noite! adicionamos uma inteligenia que mete seu peso a partir da sua altura!!!")
valorpeso = float(input("para começarmos, informe seu peso?"))
valoraltura = int(float(input("Agora, qual é a sua altura?")))
print("sabendo disso, vamos agora calcular seu IMC!")
IMC = valorpeso / (valoraltura *2)
print(f"Pronto!! calculamos seu IMC e seu IMC é {IMC}")