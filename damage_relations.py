from get_module import get_info

def relacionDaño(type):
    if len(type) == 1:
        tipo = [type[0]['type']['name']]
        damage_relations = get_info(f'https://pokeapi.co/api/v2/type/{tipo[0]}')['damage_relations']

        #Super Efectivo
        superEfectivo = damage_relations['double_damage_to']
        efectivo = []
        for item in superEfectivo:
            efectivo.append(item['name'])
        #Debil Contra
        debil = []
        debilContra = damage_relations['double_damage_from']
        for item in debilContra:
            debil.append(item['name'])
        #Resistente contra
        resistente = []
        resistenteContra = damage_relations['half_damage_from']
        for item in resistenteContra:
            resistente.append(item['name'])
        #Poco Eficaz
        pocoEficaz = []
        pocoEficazContra = damage_relations['half_damage_to']
        for item in pocoEficazContra:
            pocoEficaz.append(item['name'])
        #Inmune
        inmune = []
        inmuneContra = damage_relations['no_damage_from']
        for item in inmuneContra:
            inmune.append(item['name'])
        #Ineficaz
        ineficaz = []
        inefizasContra = damage_relations['no_damage_to']
        for item in inefizasContra:
            ineficaz.append(item['name'])

        return efectivo, debil, resistente, pocoEficaz, inmune, ineficaz

    else:
    ##### --> Relacion daño primer de los dos tipos  ####    
        tipo = [type[0]['type']['name'], type[1]['type']['name']]
        damage_relations1 = get_info(f'https://pokeapi.co/api/v2/type/{tipo[0]}')['damage_relations']
        damage_relations2 = get_info(f'https://pokeapi.co/api/v2/type/{tipo[1]}')['damage_relations']

        #Super Efectivo
        efectivo = []
        superEfectivo = damage_relations1['double_damage_to']
        for item in superEfectivo:
            efectivo.append(item['name'])
        superEfectivo = damage_relations2['double_damage_to']
        for item in superEfectivo:
            efectivo.append(item['name'])
        if len(efectivo) > 0:
            efectivo = set(efectivo)
        #Debil Contra
        debil = []
        debilContra = damage_relations1['double_damage_from']
        for item in debilContra:
            debil.append(item['name'])
        debilContra = damage_relations2['double_damage_from']
        for item in debilContra:
            debil.append(item['name'])
        if len(debil) > 0:
            debil = set(debil)
        #Resistente contra
        resistente = []
        resistenteContra = damage_relations1['half_damage_from']
        for item in resistenteContra:
            resistente.append(item['name'])
        resistenteContra = damage_relations2['half_damage_from']
        for item in resistenteContra:
            resistente.append(item['name'])
        if len(resistente) > 0:
            resistente = set(resistente)
        #Poco Eficaz
        pocoEficaz = []
        pocoEficazContra = damage_relations1['half_damage_to']
        for item in pocoEficazContra:
            pocoEficaz.append(item['name'])
        pocoEficazContra = damage_relations2['half_damage_to']
        for item in pocoEficazContra:
            pocoEficaz.append(item['name'])
        if len(pocoEficaz) > 0:
            pocoEficaz = set(pocoEficaz)
        #Inmune
        inmune = []
        inmuneContra = damage_relations1['no_damage_from']
        for item in inmuneContra:
            inmune.append(item['name'])
        inmuneContra = damage_relations2['no_damage_from']
        for item in inmuneContra:
            inmune.append(item['name'])
        if len(inmune) > 0:
            inmune = set(inmune)
        #Ineficaz
        ineficaz = []
        inefizasContra = damage_relations1['no_damage_to']
        for item in inefizasContra:
            ineficaz.append(item['name'])
        inefizasContra = damage_relations2['no_damage_to']
        for item in inefizasContra:
            ineficaz.append(item['name'])
        if len(ineficaz) > 0:
            ineficaz = set(ineficaz)

    return efectivo, debil, resistente, pocoEficaz, inmune, ineficaz

if __name__ == '__main__':
    nombrePokemon = 'charmander'
    tipo = get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types']
    print(nombrePokemon)
    print(relacionDaño(tipo))
    nombrePokemon = 'articuno'
    tipo = get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')['types']
    print(nombrePokemon)
    print(relacionDaño(tipo))