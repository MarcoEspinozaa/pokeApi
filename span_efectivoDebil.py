from pipes import Template
from damage_relations import relacionDaño
from tipo_español import tipoEspañol
from get_module import get_info
from string import Template

def efectivoHtml(efectivoDebil):

    divSuperEfectivo = ''
    divDebil = ''
    divResistente = ''
    divPocoEficaz = ''
    divInmune = ''
    divIneficaz = ''

    divTemplate = Template('<span class="label $tipo">$esp</span>')  
    
    for item in efectivoDebil[0]:
        divSuperEfectivo += divTemplate.substitute(tipo = item, esp = tipoEspañol(item).capitalize())+'\n'

    for item in efectivoDebil[1]:
        divDebil += divTemplate.substitute(tipo = item, esp = tipoEspañol(item).capitalize())+'\n'

    for item in efectivoDebil[2]:
        divResistente += divTemplate.substitute(tipo = item, esp = tipoEspañol(item).capitalize())+'\n'

    for item in efectivoDebil[3]:
        divPocoEficaz += divTemplate.substitute(tipo = item, esp = tipoEspañol(item).capitalize())+'\n'

    for item in efectivoDebil[4]:
        divInmune += divTemplate.substitute(tipo = item, esp = tipoEspañol(item).capitalize())+'\n'

    for item in efectivoDebil[5]:
        divIneficaz += divTemplate.substitute(tipo = item, esp = tipoEspañol(item).capitalize())+'\n'
        
    return divSuperEfectivo, divDebil, divResistente, divPocoEficaz, divInmune, divIneficaz


if __name__ == '__main__':
    nombrePokemon = 'charmander'
    efectivoDebil = relacionDaño(get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types'])
    print(efectivoHtml(efectivoDebil))
    nombrePokemon = 'pichu'
    efectivoDebil = relacionDaño(get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types'])
    print(efectivoHtml(efectivoDebil))
