#calcule o desconto dos seguintes produtos calça azul R$ 120,00, Jaqueta Verde R$ 150,00
print("qual sua idade") 
#armazeno na variável
idade = int (input())
#colocando os valor do produto
valor_calca_azul = 120
valor_jaqueta_verde= 150
#colocando os descontos no valor do produto
valor_com_desconto_calca_azul = valor_calca_azul- idade
valor_com_desconto_jaqueta_verde = valor_jaqueta_verde- idade
#Explicando para o usuário quais são os produtos e seus valores sem desconto
print(f"na nossa loja temos os seguintes produtos: calça azul com o valor {valor_calca_azul} e uma jaqueta verde com o valor {valor_jaqueta_verde}")
#Explicando para o usuário quais são os produtos e seus valores com desconto
print(f"graças a sua idade, nos daremos um desconto de R${idade} para você nos dois produtos!")
print(f"A calça azul custará {valor_com_desconto_calca_azul} e a jaqueta custará {valor_com_desconto_jaqueta_verde}")