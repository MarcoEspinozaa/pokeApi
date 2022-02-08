
def tipoEspañol(argumento):
    español = ['normal', 'lucha', 'volador', 'veneno', 'tierra', 'roca', 'bicho', 'fantasma',
                'acero', 'fuego', 'agua', 'planta', 'eléctrico', 'psíquico', 'hielo',
                'dragón', 'oscuro', 'hada', 'bebé', 'legendario', 'mítico']

    #inglesEspañol = {'normal':'normal', 'fighting':'lucha', 'flying':'volador', 'poison':'veneno',
     #               'ground':'tierra', 'rock':'roca', 'bug':'bicho', 'ghost':'fantasma',
      #              'steel':'acero', 'fire':'fuego', 'water':'agua', 'grass':'planta', 
       #             'electric':'eléctrico', 'psychic':'psíquico', 'ice':'hielo', 'dragon':'dragón',
        #            'dark':'oscuro', 'fairy':'hada', 'baby':'bebé', 'legendary':'legendario',
         #           'mythical':'mítico'}

    if type(argumento) == list:
        listaEspañol = []
        for item in argumento:
            if item == 'normal':
                listaEspañol.append(español[0])
            elif item == 'fighting':
                listaEspañol.append(español[1])
            elif item == 'flying':
                listaEspañol.append(español[2])
            elif item == 'poison':
                listaEspañol.append(español[3])
            elif item == 'ground':
                listaEspañol.append(español[4])
            elif item == 'rock':
                listaEspañol.append(español[5])
            elif item == 'bug':
                listaEspañol.append(español[6])
            elif item == 'ghost':
                listaEspañol.append(español[7])
            elif item == 'steel':
                listaEspañol.append(español[8])
            elif item == 'fire':
                listaEspañol.append(español[9])
            elif item == 'water':
                listaEspañol.append(español[10])
            elif item == 'grass':
                listaEspañol.append(español[11])
            elif item == 'electric':
                listaEspañol.append(español[12])
            elif item == 'psychic':
                listaEspañol.append(español[13])
            elif item == 'ice':
                listaEspañol.append(español[14])
            elif item == 'dragon':
                listaEspañol.append(español[15])
            elif item == 'dark':
                listaEspañol.append(español[16])
            elif item == 'fairy':
                listaEspañol.append(español[17])
            elif item == 'baby':
                listaEspañol.append(español[18])
            elif item == 'legendary':
                listaEspañol.append(español[19])
            elif item == 'mythical':
                listaEspañol.append(español[20])

        return listaEspañol
    
    else:
        if argumento == 'normal':
            argumento = (español[0])
        elif argumento == 'fighting':
            argumento = (español[1])
        elif argumento == 'flying':
            argumento = (español[2])
        elif argumento == 'poison':
            argumento = (español[3])
        elif argumento == 'ground':
            argumento = (español[4])
        elif argumento == 'rock':
            argumento = (español[5])
        elif argumento == 'bug':
            argumento = (español[6])
        elif argumento == 'ghost':
            argumento = (español[7])
        elif argumento == 'steel':
            argumento = (español[8])
        elif argumento == 'fire':
            argumento = (español[9])
        elif argumento == 'water':
            argumento = (español[10])
        elif argumento == 'grass':
            argumento = (español[11])
        elif argumento == 'electric':
            argumento = (español[12])
        elif argumento == 'psychic':
            argumento = (español[13])
        elif argumento == 'ice':
            argumento = (español[14])
        elif argumento == 'dragon':
            argumento = (español[15])
        elif argumento == 'dark':
            argumento = (español[16])
        elif argumento == 'fairy':
            argumento = (español[17])
        elif argumento == 'baby':
            argumento = (español[18])
        elif argumento == 'legendary':
            argumento = (español[19])
        elif argumento == 'mythical':
            argumento = (español[20])
        
        return argumento


if __name__ == '__main__':
    lista = ['poison', 'fire','mythical']
    español = tipoEspañol(lista)
    print(español)
    prueba2 = tipoEspañol('ghost')
    print(prueba2)