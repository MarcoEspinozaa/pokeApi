from get_module import get_info

def tipoEspecial(lista, listaespecies):
    if len(lista) == 1:
        #Se obtiene el tipo de pokemon normal, Ej: Volador
        tipo = [lista[0]['type']['name']]
        #En caso de cumplir con la condición particular se agrega el tipo particular
        if listaespecies['is_baby'] == True:
            tipo.append('baby')
        elif listaespecies['is_legendary'] == True:
            tipo.append('legendary')
        elif listaespecies['is_mythical'] == True:
            tipo.append('mythical')
    else:
        #Se obtiene el tipo de pokemon normal, Ej: Volador, Hielo
        tipo = [lista[0]['type']['name'], lista[1]['type']['name']]
        #En caso de cumplir con la condición particular se agrega el tipo particular
        if listaespecies['is_baby'] == True:
            tipo.append('baby')
        elif listaespecies['is_legendary'] == True:
            tipo.append('legendary')
        elif listaespecies['is_mythical'] == True:
            tipo.append('mythical')

    return tipo


if __name__ == '__main__':
    nombrePokemon = 'articuno'
    types = get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types']
    especiePokemon = get_info(f'https://pokeapi.co/api/v2/pokemon-species/{nombrePokemon}')
    print(tipoEspecial(types,especiePokemon))
    nombrePokemon = 'charizard'
    types = get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types']
    especiePokemon = get_info(f'https://pokeapi.co/api/v2/pokemon-species/{nombrePokemon}')
    print(tipoEspecial(types,especiePokemon))