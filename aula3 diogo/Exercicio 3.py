#faça um programa que calcule o tamanho do sapato de um cachorro sabendo que sempre será o dobro do tamanho da coleira dele. Calcule também o tamanho da fucinheira sabendo que é o triplo do tamanho da coleira.


coleira = int(input("entre com o tamanho da coleira do seu cachorro:"))
tamanhodosapato = coleira *2
tamanhofuncinheira = coleira *3

print(f"recomenda-se um sapato do tamanho:{tamanhodosapato}")
print(f"recomenda-se uma funcinheira do tamanho: {tamanhofuncinheira}")