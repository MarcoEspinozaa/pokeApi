from get_module import get_info

def preview(diccionario):
    if diccionario['evolves_from_species'] is None:
        htmlPreview = ''
    else:
        etapaPrevia = diccionario['evolves_from_species']['name']
        htmlPreview = f'Etapa previa: {etapaPrevia.capitalize()}'

    return htmlPreview


if __name__ == '__main__':
    nombrePokemon = 'charmander'
    etapaPrevia_1 = preview(get_info(f'https://pokeapi.co/api/v2/pokemon-species/{nombrePokemon}'))
    nombrePokemon = 'pikachu'
    etapaPrevia_2 = preview(get_info(f'https://pokeapi.co/api/v2/pokemon-species/{nombrePokemon}'))

    print(etapaPrevia_1, etapaPrevia_2)
