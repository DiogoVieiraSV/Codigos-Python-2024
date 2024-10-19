#Criando uma lista simples com 3 pokémons
pokemons = ["pikachu", "Charmander", "Bulbasaur"]

#Exibindo a lista
print("Lista de pokémons", pokemons)

#Acessando o primeiro pokémon da lista
print("Primeiro pokémon:", pokemons[0])

#adicionando um novo pokémon à  lista
pokemons.append("Squirtle")
print("Lista de Pokémons após adicionar Squirtle:", pokemons)

#removendo o pokémon "Charmander" da lista
pokemons.remove("Charmander")
print("lista de pokémons após remover charmander:", pokemons)

#Exibindo o tamanho da lista
print("Número de Pokémons na lista:", len(pokemons))