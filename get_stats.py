from get_module import get_info

#stats = {}
#Se necesita solo el valor de las claves, pero para futuros usos se deja el código a disposición
def estadisticas(lista):
    stats= []
    for item in lista:
        stats.append(item['base_stat']) 
    #for item in lista:
    #    stats[item['stat']['name']] = item['base_stat']
    #listaEspañol = ['HP', 'Ataque', 'Defensa', 'Ataque Especial', 'Defensa Especial', 'Velocidad']
    #listaStats = stats.values()
    #español = {k:v for k,v in zip(listaEspañol, listaStats)}

    return stats
    #return español


if __name__ == '__main__':
    nombrePokemon = 'charmander'
    iterador = get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['stats']
    print(nombrePokemon)
    print(estadisticas(iterador))