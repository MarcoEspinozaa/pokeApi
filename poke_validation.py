
with open("pokemon_list.txt", "r") as f:
    pokemon_lista = f.readlines()
    
pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista]

#import data as d --> No justiciaba crear un módulo exclusivamente para un par de párrafos

def validate(name, p_l = pokemon_lista): #mensaje = d.validacion_pokemon):
    while name not in p_l:
        if name =='codigo-cero':
            name = 'type-null'
        else:
            name = input(('''
            El nombre del pokémon no existe o no es inválido.
            \033[1mNota:\033[0m Si el nombre del pokémon tiene espacios reemplace por "-". 
            No coloque ningún tipo de signo de puntuación adicional.
            \033[1mEjemplo:\033[0m Mr. Mime, se debe ingresar como mr-mime o Mr-Mime.
                                    
            Vuelve a escribir el nombre del pokémon deseado: ''')).lower()

    return name

if __name__ == '__main__':
    name = input('nombre: ')
    print(validate(name))
