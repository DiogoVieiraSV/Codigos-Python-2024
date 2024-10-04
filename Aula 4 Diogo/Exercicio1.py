#faça um programa que valide se um aluno pode fazer o curso de python, onde o único critério é ele ter idade maior ou igual a 16 anos

print("Soube que você se interessou no curso de python, mas precisa ter maior que 16 anos para pdoer começar")

idade = int(input("Qual é a sua idade?"))
if (idade>=16):
     print("Sim, você pode fazer o curso!")

else:
    print("Não, você ainda não pode fazer o curso!")