from string import Template
from tipo_español import tipoEspañol
from special_type import tipoEspecial
from get_module import get_info

def new_spanTipo(tipos):
    #Traduce los tipos de pokémon en inglés al español
    enEspañol = tipoEspañol(tipos)

    #Crea líneas html dependiendo del tipo o tipos del pokémon seleccionado
    if len(tipos) == 1:
        tipoHtml = f'<span class="label {tipos[0]}">{enEspañol[0].capitalize()}</span>'
    elif len(tipos) == 2 :
        tipoHtml = (f''' <span class="label {tipos[0]}">{enEspañol[0].capitalize()}</span>
            <span class="label {tipos[1]}">{enEspañol[1].capitalize()}</span> ''')
    else:
        tipoHtml = (f''' <span class="label {tipos[0]}">{enEspañol[0].capitalize()}</span>
            <span class="label {tipos[1]}">{enEspañol[1].capitalize()}</span>
            <span class="label {tipos[2]}">{enEspañol[2].capitalize()}</span> ''')

    return tipoHtml


if __name__ == '__main__':
    nombrePokemon = 'mew'
    tipos = tipoEspecial(get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types'],
                        get_info(f'https://pokeapi.co/api/v2/pokemon-species/{nombrePokemon}') )
    print(new_spanTipo(tipos))
    nombrePokemon = 'pichu'
    tipos = tipoEspecial(get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types'],
                        get_info(f'https://pokeapi.co/api/v2/pokemon-species/{nombrePokemon}') )
    print(new_spanTipo(tipos))