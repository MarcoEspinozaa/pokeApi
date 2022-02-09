from get_module import get_info

#Se crea este módulo por la necesidad especial de los pokémon que tienen un solo tipo y son legendarios, bebé o mítico
def tipos(lista):
    if len(lista) == 1:
        #Se obtiene el tipo de pokemon normal, Ej: Volador
        tipo = [lista[0]['type']['name']]
    else:
        #Se obtiene el tipo de pokemon normal, Ej: Volador, Hielo
        tipo = [lista[0]['type']['name'], lista[1]['type']['name']]

    return tipo


if __name__ == '__main__':
    nombrePokemon = 'articuno'
    types = get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types']
    print(tipos(types))
    nombrePokemon = 'entei'
    types = get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types']
    print(tipos(types))