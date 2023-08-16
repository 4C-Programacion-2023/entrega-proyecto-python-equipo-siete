import random
from Preguntas_Preguntados import preguntas_cat
from tkinter import *
import tkinter as messagebox
OPCIONES = ['reguntAleatoria',
            'Elección de Categoria',
            ]


CATEGORIAS = ['Deporte',
    'Ciencia',
    'Geografia',
    'Entretenimiento',
    'Historia',
    'Arte']



def menu_principal():
    for num, opciones in enumerate(OPCIONES):
        print(f'{num + 1}. {opciones}')
    decision = input(f'Elija un modo (1-{len(OPCIONES)}): ')
    return decision

#Hace la pregunta y respuesta
def preguntas(categoria):
    preguntas_categoria = preguntas_cat[categoria]
    if len(preguntas_categoria) == 0:
        return True
    numero_random_2 = random.randint(0, len(preguntas_categoria)-1)

    pregunta = preguntas_categoria[numero_random_2]
    print(pregunta["nombre"])
    
    texto_opciones = ""
    for i, opcion in enumerate(pregunta["opciones"]):
        texto_opciones += f"{i+1}- {opcion}\n"

    respuesta_usuario= int(input(texto_opciones + "\n>>>"))
    respuesta_correcta = respuesta_usuario == pregunta["respuesta"]

    print("Correcto" if respuesta_correcta else "Incorrecto")
    return respuesta_correcta


#     Modo 2 Jugadores  

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
def eleccion_cat(correctos,incorrectos, info_jugador):
    
    print('Elegí la categoria')
    lista_categorias = categorias_faltan(info_jugador)
    print(lista_categorias)
    print(f"")

    eleccion = input('>>>').capitalize()
    
    
    while correctos < 10 and incorrectos < 3:
        if eleccion in lista_categorias:
        
            respuesta = preguntas(eleccion)
        if respuesta:
            info_jugador[eleccion] = True
            correctos += 1
            
        else:
                incorrectos += 1

        print(f'Respuestas correctas: {correctos}/10')
        print(f'Respuestas incorrectas: {incorrectos}/3')
        print(f'')
        
    return False
