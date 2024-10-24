import time
import random

# Definição dos personagens
aventureiro = [
    ["Vida", "Ataque"],
    [1000, 20]
]
assaltante = [
    ["Vida", "Ataque"],
    [600, 20]
]


def lutar(aventureiro, assaltante):
    print("A luta começou!\n")

    while aventureiro[1][0] > 0 and assaltante[1][0] > 0:
        variavelaventureiro = random.randint(1,20)
        variavelassaltante = random.randint(1,20)
        assaltante[1][0] -= 20 * variavelassaltante
        aventureiro[1][0] -= 20 * variavelaventureiro
        # Ataques simultâneos
        dano_aventureiro = aventureiro[1][1]
        dano_assaltante = assaltante[1][1]

        assaltante[1][0] -= dano_aventureiro
        aventureiro[1][0] -= dano_assaltante

        # Exibir status após a rodada
        print(f"Aventureiro - Vida: {aventureiro[1][0]}, Ataque: {aventureiro[1][1]}")
        print(f"Assaltante - Vida: {assaltante[1][0]}, Ataque: {assaltante[1][1]}\n")

        # Verifica se alguém perdeu
        if aventureiro[1][0] <= 0:
            print("Aventureiro foi derrotado!")
            break
        elif assaltante[1][0] <= 0:
            print("Assaltante foi derrotado!")
            break
        time.sleep(4)

    # Exibir valores finais
    print("Luta finalizada!")
    print(f"Aventureiro - Vida final: {aventureiro[1][0]}")
    print(f"Assaltante - Vida final: {assaltante[1][0]}")

# Chama a função de luta
lutar(aventureiro, assaltante)
    


