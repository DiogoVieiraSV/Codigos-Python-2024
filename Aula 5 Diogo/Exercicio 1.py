numero = int(input("digite um numero de 1 a 3:"))

if numero == 1:
    print ("Parabens sua Classe é BÁRBARO!")
    classe = "Bárbaro"
elif numero ==2:
    print("Parabens sua Classe é MAGO")
    classe = "Mago"
elif numero == 3:
    print("parabens sua classe ARQUEIRO ")
    classe = "Arqueiro"

else:
    print("os numeros que digitou não corresponde ao que pedi, tente novamente!")

numero2= int(input( "se voce quer o equipamento curto digite 1 se quer o longo digite 2:"))
if numero2== 1:
    print("voce escolheu arma curta")
    arma= "curta"
elif numero2==2:
    print("voce escolheu a arma de longa alcance")
    arma="longo"
else:
    print("caso nao digitou o numero certo, tente novamente")

print(f"parabens voce escolheu a classe {classe} e se equipamento e uma arma {arma}!")

