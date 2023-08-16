import random
from Preguntas_Preguntados import preguntas_cat
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter as messagebox

OPCIONES_MODOS= ['Preguntas Aleatorias',
    "Eleccion de Categoria",
    'De a 2 jugadores',
    ]


CATEGORIAS = ['Deporte',
    'Ciencia',
    'Geografia',
    'Entretenimiento',
    'Historia',
    'Arte']


#     Modo 1 Jugador
#Hace la pregunta y respuesta

preguntas_hechas = {categoria: set() for categoria in CATEGORIAS}

def preguntas(categoria, preguntas_hechas):
    preguntas_categoria = preguntas_cat[categoria]
    preguntas_disponibles = [pregunta for pregunta in preguntas_categoria if pregunta not in preguntas_hechas[categoria]]
    if len(preguntas_disponibles) == 0:
        return False
    numero_random = random.randint(0, len(preguntas_disponibles)-1)

    pregunta = preguntas_disponibles[numero_random]
    print(pregunta["nombre"])
    
    texto_opciones = ""
    for i, opcion in enumerate(pregunta["opciones"]):
        texto_opciones += f"{i+1}- {opcion}\n"

    respuesta_usuario = int(input(texto_opciones + "\n>>>"))
    respuesta_correcta = respuesta_usuario == pregunta["respuesta"]

    print("Correcto" if respuesta_correcta else "Incorrecto")
    preguntas_hechas[categoria].append(pregunta)  # Agrega la pregunta a las preguntas hechas
    return respuesta_correcta



###     Modo 2 Jugadores  ###

#Muestra las coronas ganadas
def mostrar_info_jugador(jugador, num_jugador):
    print(f"datos del jugador {num_jugador}")
    for categoria, valor in jugador.items():
        print(f"{categoria}: {'Ganado' if valor else 'No ganado'}")


#Crea una lista de las categorias que le falta ganar
def categorias_faltan(info_jugador):
    lista = []
    for cat, valor in info_jugador.items():
        if not valor:
            lista.append(cat)
    return lista

#Al tener 3 respuestas correctas, te permite elegir una categoria y si acertas la pregunta te da la corona de esa catgeoria
def elegir_categoria(correctos, info_jugador):
    global preguntas_hechas
    if correctos == 3:
        print('Elegí la categoria')
        lista_categorias = categorias_faltan(info_jugador)
        print(lista_categorias)

        eleccion = input('>>>').capitalize()
        if eleccion in lista_categorias:
            
            respuesta = preguntas(eleccion)
            if respuesta:
                info_jugador[eleccion] = True
        return info_jugador
    return False


#Modo eleccion de categoria
def eleccion_cat(correctos,incorrectos, info_jugador,preguntas_hechas):
    
    print('Elegí la categoria')
    lista_categorias = categorias_faltan(info_jugador)
    print(lista_categorias)
    print(f"")

    eleccion = input('>>>').capitalize()
    
    
    while correctos < 10 and incorrectos < 3:
        if eleccion in lista_categorias:
            
            respuesta = preguntas(eleccion, preguntas_hechas)
        if respuesta:
            info_jugador[eleccion] = True
            correctos += 1
            
        else:
                incorrectos += 1

        print(f'Respuestas correctas: {correctos}/10')
        print(f'Respuestas incorrectas: {incorrectos}/3')
        print(f'')
        
    return False
