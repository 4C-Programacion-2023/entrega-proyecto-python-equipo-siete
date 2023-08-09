import tkinter as tk
from tkinter import messagebox
from Preguntas_Preguntados import preguntas_cat as preguntas
from Funciones import CATEGORIAS
import random
indice_pregunta_actual = random.randint(0, len(CATEGORIAS) - 1)

# Función para manejar el botón "Responder".
def responder(opcion):
    pregunta_actual = preguntas[indice_pregunta_actual]
    respuesta_correcta = pregunta_actual["respuesta_correcta"]

    if opcion == respuesta_correcta:
        messagebox.showinfo("Correcto", "¡Respuesta correcta!")
    else:
        messagebox.showerror("Incorrecto", "Respuesta incorrecta. ¡Inténtalo de nuevo!")

    # Pasar a la siguiente pregunta
    siguiente_pregunta()

def siguiente_pregunta():
    global indice_pregunta_actual

    indice_pregunta_actual += 1

    if indice_pregunta_actual < len(preguntas):
        # Actualizar la etiqueta de la pregunta y los botones de opciones.
        pregunta_actual = preguntas[indice_pregunta_actual]
        label_pregunta.config(text=pregunta_actual["pregunta"])
        for i, opcion in enumerate(pregunta_actual["opciones"]):
            botones_opcion[i].config(text=opcion)
    else:
        # Mostrar mensaje cuando se respondieron todas las preguntas.
        messagebox.showinfo("Fin del juego", "Has respondido todas las preguntas.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Preguntados")

# Etiqueta para la pregunta
label_pregunta = tk.Label(ventana, text=preguntas[indice_pregunta_actual]["pregunta"])
label_pregunta.pack(pady=10)

# Crear botones de opciones
botones_opcion = []
pregunta_actual = preguntas[indice_pregunta_actual]
for i, opcion in enumerate(pregunta_actual["opciones"]):
    boton = tk.Button(ventana, text=opcion, command=lambda opc=opcion: responder(opc))
    boton.pack(pady=5)
    botones_opcion.append(boton)

# Iniciar la interfaz gráfica
ventana.mainloop()