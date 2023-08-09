# funciones.py
import random
from tkinter import messagebox
import tkinter as tk
from Preguntas_Preguntados import preguntas_cat

CATEGORIAS = [
    'Deporte',
    'Ciencia',
    'Geografía',
    'Entretenimiento',
    'Historia',
    'Arte'
]

OPCIONES = ['Preguntas Aleatorias', 'Elección de Categoría', 'Salir']

def menu_principal():
    for num, opcion in enumerate(OPCIONES, start=1):
        print(f'{num}. {opcion}')
    return input(f'Elija un modo (1-{len(OPCIONES)}): ')

def preguntas(categoria):
    preguntas_categoria = preguntas_cat[categoria]
    if not preguntas_categoria:
        return True
    pregunta = random.choice(preguntas_categoria)
    print(pregunta["nombre"])
    respuesta = int(input("\n".join(f"{i+1}- {opcion}" for i, opcion in enumerate(pregunta["opciones"])) + "\n>>> "))
    print("Correcto" if respuesta == pregunta["respuesta"] else "Incorrecto")
    return respuesta == pregunta["respuesta"]

def Salir():
    print('Gracias por jugar')
    exit()

def seleccionar_categoria():
    ventana_categorias = tk.Tk()
    ventana_categorias.title("Selección de Categoría")

    etiqueta_categoria = tk.Label(ventana_categorias, text="Elija una categoría:")
    etiqueta_categoria.pack(pady=10)

    categoria_actual = tk.StringVar()
    for i, categoria in enumerate(CATEGORIAS):
        tk.Radiobutton(ventana_categorias, text=categoria, variable=categoria_actual, value=categoria).pack()

    boton_confirmar = tk.Button(ventana_categorias, text="Confirmar", command=ventana_categorias.destroy)
    boton_confirmar.pack(pady=5)

    ventana_categorias.mainloop()
    return categoria_actual.get()
