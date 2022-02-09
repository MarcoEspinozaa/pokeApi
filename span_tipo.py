from string import Template
from special_type import tipoEspecial
from get_module import get_info

def new_spanTipo(tipos):
    inglesEspañol = {'normal':'Normal', 'fighting':'Lucha', 'flying':'Volador', 'poison':'Veneno',
                    'ground':'Tierra', 'rock':'Roca', 'bug':'Bicho', 'ghost':'Fantasma',
                    'steel':'Acero', 'fire':'Fuego', 'water':'Agua', 'grass':'Planta', 
                    'electric':'Eléctrico', 'psychic':'Psíquico', 'ice':'Hielo', 'dragon':'Dragón',
                    'dark':'Siniestro', 'fairy':'Hada', 'baby':'Bebé', 'legendary':'Legendario',
                    'mythical':'Mítico'}

    span_str = ''
    for item in tipos:
        itemEsp = inglesEspañol[item]
        span_str = span_str + f'<span class="label {item}">{itemEsp}</span>\n'

    return span_str


if __name__ == '__main__':
    nombrePokemon = 'mew'
    tipos = tipoEspecial(get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types'],
                        get_info(f'https://pokeapi.co/api/v2/pokemon-species/{nombrePokemon}') )
    print(new_spanTipo(tipos))
    nombrePokemon = 'pichu'
    tipos = tipoEspecial(get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types'],
                        get_info(f'https://pokeapi.co/api/v2/pokemon-species/{nombrePokemon}') )
    print(new_spanTipo(tipos))