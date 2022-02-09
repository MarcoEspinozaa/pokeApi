from pipes import Template
from damage_relations import relacionDaño
from get_module import get_info
from string import Template

def efectivoHtml(efectivoDebil):
    inglesEspañol = {'normal':'Normal', 'fighting':'Lucha', 'flying':'Volador', 'poison':'Veneno',
                    'ground':'Tierra', 'rock':'Roca', 'bug':'Bicho', 'ghost':'Fantasma',
                    'steel':'Acero', 'fire':'Fuego', 'water':'Agua', 'grass':'Planta', 
                    'electric':'Eléctrico', 'psychic':'Psíquico', 'ice':'Hielo', 'dragon':'Dragón',
                    'dark':'Siniestro', 'fairy':'Hada', 'baby':'Bebé', 'legendary':'Legendario',
                    'mythical':'Mítico'}

    divSuperEfectivo = ''
    for item in efectivoDebil[0]:
        itemEsp = inglesEspañol[item]
        divSuperEfectivo = divSuperEfectivo + f'<span class="label {item}">{itemEsp}</span>\n'

    divDebil = ''
    for item in efectivoDebil[1]:
        itemEsp = inglesEspañol[item]
        divDebil = divDebil + f'<span class="label {item}">{itemEsp}</span>\n'

    divResistente = ''
    for item in efectivoDebil[2]:
        itemEsp = inglesEspañol[item]
        divResistente = divResistente + f'<span class="label {item}">{itemEsp}</span>\n'

    divPocoEficaz = ''
    for item in efectivoDebil[3]:
        itemEsp = inglesEspañol[item]
        divPocoEficaz = divPocoEficaz + f'<span class="label {item}">{itemEsp}</span>\n'

    divInmune = ''
    for item in efectivoDebil[4]:
        itemEsp = inglesEspañol[item]
        divInmune = divInmune + f'<span class="label {item}">{itemEsp}</span>\n'

    divIneficaz = ''
    for item in efectivoDebil[5]:
        itemEsp = inglesEspañol[item]
        divIneficaz = divIneficaz + f'<span class="label {item}">{itemEsp}</span>\n'
        
    return divSuperEfectivo, divDebil, divResistente, divPocoEficaz, divInmune, divIneficaz


if __name__ == '__main__':
    nombrePokemon = 'charmander'
    efectivoDebil = relacionDaño(get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types'])
    print(efectivoHtml(efectivoDebil))
    nombrePokemon = 'pichu'
    efectivoDebil = relacionDaño(get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types'])
    print(efectivoHtml(efectivoDebil))
