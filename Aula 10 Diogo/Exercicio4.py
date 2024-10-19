poderes_pikachu = ["choque do trovão", "calda de ferro", "ataque rapido", "esquiva"]

print ("poderes do Pikachu: ", poderes_pikachu)

print("seu pokemon evoluiu e agora pode receber o poder 'bola de eletricidade'")
resposta = input("mas para ter essa habilidade, precisa tirar uma habilidade que seu pokemon ja tem.\n deseja tirar alguma habilidade? s/n") 
habilidade = input("qual habilidade?").lower()
if habilidade == "choque do trovão":
    print("Pikachu esqueceu o 'choque do trovão' \n Pikachu aprendeu 'bola de eletricidade' ")
    poderes_pikachu.remove ("choque do trovão")
    poderes_pikachu.append ("bola de eletricidade")
elif habilidade == "calda de ferro":
    print("Pikachu esqueceu o 'calda de ferro' \n Pikachu aprendeu 'bola de eletricidade' ")
    poderes_pikachu.remove ("calda de ferro")
    poderes_pikachu.append ("bola de eletricidade")
elif habilidade == "ataque rapido":
    print("Pikachu esqueceu o 'ataque rapido' \n Pikachu aprendeu 'bola de eletricidade' ")
    poderes_pikachu.remove ("ataque rapido")
    poderes_pikachu.append ("bola de eletricidade")
elif habilidade == "esquiva":
    print("Pikachu esqueceu o 'esquiva' \n Pikachu aprendeu 'bola de eletricidade' ")
    poderes_pikachu.remove ("esquiva")
    poderes_pikachu.append ("bola de eletricidade")

else:
    print("Pikachu não aprendeu 'bola de eletricidade' ")

print(poderes_pikachu)

