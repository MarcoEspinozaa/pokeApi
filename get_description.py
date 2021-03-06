from get_module import get_info
import random

def descEspañol(lista):
    descripcionesEspañol = []
    for item in lista:
        if item['language']['name'] == 'es':
            descripcionesEspañol.append(item['flavor_text'].replace("\n"," "))
            descripcion = random.choice(descripcionesEspañol)

    return descripcion


if __name__ == '__main__':
    nombrePokemon = 'charmander'
    especie = get_info(f'https://pokeapi.co/api/v2/pokemon-species/{nombrePokemon}')['flavor_text_entries']
    print(nombrePokemon)
    print(descEspañol(especie))