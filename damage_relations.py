from get_module import get_info
from special_type import tipoEspecial

#Se crea una función para una operación repetitiva
def rellenaLista(listaDamage):
    listaSalida = []
    for item in listaDamage:
            listaSalida.append(item['name'])

    return listaSalida


def relacionDaño(tipo):
    if len(tipo) == 1:
        damage_relations = get_info(f'https://pokeapi.co/api/v2/type/{tipo[0]}')['damage_relations']

        #Super Efectivo
        efectivo = rellenaLista(damage_relations['double_damage_to'])
        #Debil Contra
        debil = rellenaLista(damage_relations['double_damage_from'])
        #Resistente contra
        resistente = rellenaLista(damage_relations['half_damage_from'])
        #Poco Eficaz
        pocoEficaz = rellenaLista(damage_relations['half_damage_to'])
        #Inmune
        inmune = rellenaLista(damage_relations['no_damage_from'])
        #Ineficaz
        ineficaz = rellenaLista(damage_relations['no_damage_to'])

        return efectivo, debil, resistente, pocoEficaz, inmune, ineficaz

    else:
    ##### --> Relacion daño dos tipos  ####    
        damage_relations1 = get_info(f'https://pokeapi.co/api/v2/type/{tipo[0]}')['damage_relations']
        damage_relations2 = get_info(f'https://pokeapi.co/api/v2/type/{tipo[1]}')['damage_relations']

        #Super Efectivo
        efectivo = set(rellenaLista(damage_relations1['double_damage_to'])+
                        rellenaLista(damage_relations2['double_damage_to']))
        #Debil Contra
        debil = set(rellenaLista(damage_relations1['double_damage_from'])+
                    rellenaLista(damage_relations2['double_damage_from']))
        #Resistente contra
        resistente = set(rellenaLista(damage_relations1['half_damage_from'])+
                        rellenaLista(damage_relations2['half_damage_from']))
        #Poco Eficaz
        pocoEficaz = set(rellenaLista(damage_relations1['half_damage_to'])+
                        rellenaLista(damage_relations2['half_damage_to']))
        #Inmune: Es una de las dos listas que pueden venir vacías, es por eso la condición
        if len(rellenaLista(damage_relations1['no_damage_from'])) > 0 or len(rellenaLista(damage_relations2['no_damage_from'])) > 0:
            inmune = set(rellenaLista(damage_relations1['no_damage_from'])+
                         rellenaLista(damage_relations2['no_damage_from']))
        else:
            inmune = []
        #Ineficaz: Es una de las dos listas que pueden venir vacías, es por eso la condición
        if len(rellenaLista(damage_relations1['no_damage_to'])) > 0 or len(rellenaLista(damage_relations2['no_damage_to'])) > 0:
            ineficaz = set(rellenaLista(damage_relations1['no_damage_to'])+
                            rellenaLista(damage_relations2['no_damage_to']))
        else:
            ineficaz = []
        
        

    return efectivo, debil, resistente, pocoEficaz, inmune, ineficaz


if __name__ == '__main__':
    #### Prueba 1 ####
    #Probar cambiando el nombre del pokémon
    nombrePokemon = 'charmander'
    pokemonType = get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types']
    especiePokemon = get_info(f'https://pokeapi.co/api/v2/pokemon-species/{nombrePokemon}')
    #Obteniendo la lista de tipos de este pokémon en particular
    tipo = tipoEspecial(pokemonType, especiePokemon)
    print(nombrePokemon)
    print(relacionDaño(tipo))

    #### Prueba 2 ####
    #Probar cambiando el nombre del pokémon
    nombrePokemon = 'articuno'
    pokemonType = get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types']
    especiePokemon = get_info(f'https://pokeapi.co/api/v2/pokemon-species/{nombrePokemon}')
    #Obteniendo la lista de tipos de este pokémon en particular
    tipo = tipoEspecial(pokemonType, especiePokemon)
    print(nombrePokemon)
    print(relacionDaño(tipo))