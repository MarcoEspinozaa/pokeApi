from validador import validateOpcion 
from poke_validation import validate
import time
import sys
import os

def inputMenu():
    op_sys = 'cls' if sys.platform == 'win32' else 'clear'

    print('\033[1m' + 'POKÉDEX \n' '\033[0m'.center(50, " "))
    opcion = input('''Ingrese una opción para comenzar!
        1. Ingresar a la base de datos pokémon
        0. Salir del pokédex
    > ''')
    # 1. validar opcion
    opcion = validateOpcion(['0','1'], opcion)

    # 2. Definir el comportamiento de Salir
    if opcion == '0':
        print("Nos vemos pronto!")
        time.sleep(2)
        os.system(op_sys)
        # finalizar programa
        exit()

    #Limpiar pantalla
    os.system(op_sys)
    print('\033[1m' + 'POKÉDEX \n' '\033[0m'.center(50, " "))
    print('''Bienvenido a la pokedex, aquí puedes consultar por tu pokémon favorito ..''')
    nombrePokemon = input('Ingresa el nombre del pokémon: ')
    #Valida nombre pokémon
    nombrePokemon = validate(nombrePokemon) #--> Nombre en minúscula, el api es sensible a mayúscula

    return nombrePokemon