from get_module import get_info
from poke_validation import validate
from etapa_previa import preview
from get_stats import estadisticas
from special_type import tipoEspecial
from get_description import descEspañol
from damage_relations import relacionDaño
from string import Template
from show import show_pics
from input import inputMenu
from span_tipo import new_spanTipo
from span_efectivoDebil import efectivoHtml

import time
import os
import sys
import random

# Valores iniciales
op_sys = 'cls' if sys.platform == 'win32' else 'clear'
#Limpiar pantalla
os.system(op_sys)

while True:
    #Crea menú
    nombrePokemon = inputMenu()
    nombre = nombrePokemon.capitalize() #--> Variable $nombre a modificar html base
    #Obteniendo datos del pokémon
    pokemon = get_info(f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}')
    #Obteniendo datos especie pokémon
    especiePokemon = get_info(f'https://pokeapi.co/api/v2/pokemon-species/{nombrePokemon}')
    #Obtener ID
    id = pokemon['id'] #--> Variable $id a modificar html base
    #Obtener Peso
    peso = pokemon['weight']/10 #--> Variable $peso a modificar html base
    #Etapa previa en caso de tener
    htmlPreview = preview(especiePokemon) #--> Variable $htmlPreview a modificar html base
    #Obtener estadíasticas y traducirlas al español
    estadistics = estadisticas(pokemon['stats'])
    hp , atk, defen, spAtk, spDef, vel = estadistics #--> Variables $hp, $atk, etc.. a modificar html base 
    #Obetener tipo y tipos especiales(baby, legendary o mythical)
    tipos = tipoEspecial(pokemon['types'],especiePokemon) #--> Agrega tipo baby, legandary o mythical de ser necesario
    spanTipo = new_spanTipo(tipos) #--> Variable $spanTipo a modificar html base
    #Obtener descripcion aleatorea
    descripcionesEspañol = descEspañol(especiePokemon['flavor_text_entries'])
    descripcion = descripcionesEspañol #--> Variable $descripcion a modificar html base
    #Relaciones de daño --> efectivo, debil, resistente, poco eficaz, inmune, ineficaz
    efectivoDebil = relacionDaño(pokemon['types'])
    spanSupEfec, spanDebil, spanResistente, spanEficaz, spanInmune, spanIneficaz = efectivoHtml(efectivoDebil)
    #Foto frontal del pokémon
    imagen = pokemon['sprites']['front_default']
    img_url = imagen #--> Variable $img_url a modificar html base

    ######## Editando archivo html ########
    with open('base.html','r') as infile:
        entrada = infile.read()
    document_template = Template(entrada)
    ######## Sustituyendo variables ########
    html = document_template.substitute(
        id = id, nombre = nombre, img_url = img_url, htmlPreview = htmlPreview,
        peso = peso,hp = hp , atk = atk, defen = defen, spAtk = spAtk, spDef = spDef, 
        vel = vel, spanTipo = spanTipo, descripcion = descripcion, spanSupEfec = spanSupEfec,
        spanDebil = spanDebil, spanResistente = spanResistente, spanEficaz = spanEficaz,
        spanInmune = spanInmune, spanIneficaz = spanIneficaz)
    ######## Mostrando el html ########
    show_pics(html,'output')
    #Limpia pantalla para empezar de nuevo
    os.system(op_sys)



