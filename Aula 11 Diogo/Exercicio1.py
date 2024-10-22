inventario = ["espada", "poção", "escudo"]

print(inventario)

print("Ao longo da sua jornada de aventuras pelo mundo no RPG, você encontrou um arco muito bom jogado no chão.")
resposta = input("Infelizmente sua mochila está muito cheia. Deseja remover um item do seu inventário para pegar o arco? s/n ").lower()

if resposta == "s":
    item = input("Entendido, qual item deseja tirar? ").lower()
    #parte 2
    if item in inventario:
        inventario.remove(item)
        inventario.append("arco")
        print(f"Você removeu {item} e adicionou o arco.")
        print(inventario)
    else:
        print("Seu item não está no inventário, nada foi removido.")
else:
    print("Nada acontece.")

# Parte 3
print("Enquanto você segue seu caminho, surge um bandido armado e exige a sua poção do inventário.")
resposta2 = input("Você vai enfrentá-lo ou vai entregar a poção? ").lower()

if resposta2 == "enfrentá-lo":
    print("Ótima escolha, aventureiro!")
    resposta3 = input("Agora enfrentará ele com espada ou sem espada? ").lower()

    if resposta3 == "com espada":
        if "espada" in inventario:
            print("A espada está no inventário! Você a pega.")
            print("Você enfrenta o bandido por algumas horas até que consegue intimidá-lo e fazê-lo correr.")
            print("Parabéns, aventureiro! Você pode prosseguir sua jornada!")
        else:
            print("O bandido viu que você está indefeso e te mata. \nGAME OVER!")
    else:
        print("O bandido viu que você está indefeso e te mata. \nGAME OVER!")

else:
    if "poção" in inventario:
        print("Você entregou a poção, mas o bandido disse para você não confiar em bandidos e ele te mata. \nGAME OVER!")
    else:
        print("Você não tem poção no seu inventário. O bandido te mata. \nGAME OVER!")



    
