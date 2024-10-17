#programa que gera 1 numero aleatório entre 1 e 200, o usuario tem 10 palpites para tentar acertar.o istema sempre da um feedback dizendo se o "numero secreto" é maior ou menor que o palpite do usuario
import random

numero_secreto = random.randint(1, 200)
tentativas = 10
acertou = False

print("Adivinhe o número entre 1 e 200. Você tem 10 palpites.")

for tentativa in range(tentativas):
    palpite = int(input(f"Tentativa {tentativa + 1}: "))
    
    if palpite < 1 or palpite > 200:
        print("Escolha um número entre 1 e 200.")
    else:
        if palpite < numero_secreto:
            print("O número secreto é maior.")
        elif palpite > numero_secreto:
            print("O número secreto é menor.")
        else:
            print(f"Parabéns! Você acertou: {numero_secreto}!")
            acertou = True

if not acertou:
    print(f"Você não acertou. O número era: {numero_secreto}.")
    
       