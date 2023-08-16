import tkinter as tk
from Preguntas_Preguntados import preguntas_cat
import random
from Funciones import CATEGORIAS, preguntas

def verificar_respuesta(respuesta_correcta, opcion_seleccionada):
    if opcion_seleccionada == respuesta_correcta:
        resultado_label.config(text="¡Respuesta correcta!", fg="green")
    else:
        resultado_label.config(text="¡Respuesta incorrecta!", fg="red")


bentanajuego = tk.Tk()
bentanajuego.title("Preguntas sobre Python")

categoria_aleatoria = random.choice(CATEGORIAS)
preguntas_deporte = preguntas_cat[categoria_aleatoria]
pregunta_aleatoria = random.choice(preguntas_deporte)
pregunta = pregunta_aleatoria["nombre"]

opciones = ["A", "B", "C", "D"]
opciones_pregunta = pregunta_aleatoria["opciones"]

opciones_aleatorias = random.sample(opciones_pregunta, len(opciones_pregunta))


opciones_dict = dict(zip(opciones, opciones_aleatorias))

pregunta_label = tk.Label(bentanajuego, text=pregunta, padx=10, pady=10)
pregunta_label.pack()

for opcion_letra, opcion_text in opciones_dict.items():
    opcion_button = tk.Button(bentanajuego, text=f"{opcion_letra}: {opcion_text}", padx=10, pady=10, command=lambda opcion_seleccionada=opcion_letra: verificar_respuesta(opciones_pregunta.index(opciones_dict[opcion_seleccionada]) + 1, opcion_seleccionada))
    opcion_button.pack()

resultado_label = tk.Label(bentanajuego, text="", padx=10, pady=10)
resultado_label.pack()

bentanajuego.mainloop()
