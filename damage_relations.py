from get_module import get_info
from normal_type import tipos

#Se crea una función para una operación repetitiva
def tipoDamage(listaTipos, damageBuscado):
    listaTotal = []
    for tipo in listaTipos:
        damage_relations = get_info(f'https://pokeapi.co/api/v2/type/{tipo}') 
        listaDamage = damage_relations['damage_relations'][damageBuscado]

        for item in listaDamage:
            listaTotal.append(item['name'])

    listaTotal_filtrado = set(listaTotal)
    listaTotal = list(listaTotal_filtrado)
    return listaTotal

def relacionDaño(listaTipos):
    #Super Efectivo
    efectivo = tipoDamage(listaTipos,'double_damage_to')
    #Debil Contra
    debil = tipoDamage(listaTipos,'double_damage_from')
    #Resistente contra
    resistente = tipoDamage(listaTipos, 'half_damage_from')
    #Poco Eficaz
    pocoEficaz = tipoDamage(listaTipos, 'half_damage_to')
    #Inmune
    inmune = tipoDamage(listaTipos, 'no_damage_from')
    #Ineficaz
    ineficaz = tipoDamage(listaTipos, 'no_damage_to')

    return efectivo, debil, resistente, pocoEficaz, inmune, ineficaz



if __name__ == '__main__':
    #### Prueba 1 ####
    #Probar cambiando el nombre del pokémon
    nombrePokemon = 'charmander'
    pokemonType = get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types']
    #Obteniendo la lista de tipos de este pokémon en particular
    tipo = tipos(pokemonType)
    print(nombrePokemon)
    print(relacionDaño(tipo))

    #### Prueba 2 ####
    #Probar cambiando el nombre del pokémon
    nombrePokemon = 'articuno'
    pokemonType = get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types']
    #Obteniendo la lista de tipos de este pokémon en particular
    tipo = tipos(pokemonType)
    print(nombrePokemon)
    print(relacionDaño(tipo))