# main_2.py
import tkinter as tk
import random
from tkinter import messagebox
from funciones_2 import preguntas, CATEGORIAS, OPCIONES, menu_principal, seleccionar_categoria

# Variables para controlar el juego
correctos = 0
incorrectos = 0
categoria_actual = None

def iniciar_juego():
    global correctos, incorrectos, categoria_actual

    opcion = modo_var.get()

    if opcion == 'Salir':
        messagebox.showinfo("Fin del juego", "Gracias por jugar.")
        ventana_principal.destroy()
        return

    if opcion == 'Elección de Categoria':
        categoria_actual = seleccionar_categoria()
    else:
        categoria_actual = CATEGORIAS[random.randint(0, len(CATEGORIAS) - 1)]

    correctos = 0
    incorrectos = 0
    mostrar_pregunta()

def mostrar_pregunta():
    global correctos, incorrectos
    respuesta = preguntas(categoria_actual)

    if respuesta:
        correctos += 1
        messagebox.showinfo("Correcto", "¡Respuesta correcta!")
    else:
        incorrectos += 1
        messagebox.showerror("Incorrecto", "Respuesta incorrecta. ¡Inténtalo de nuevo!")

    if correctos == 10:
        messagebox.showinfo("Fin del juego", "¡Ganaste!")
    elif incorrectos == 3:
        messagebox.showinfo("Fin del juego", "¡Perdiste! Inténtalo de nuevo.")
    else:
        mostrar_pregunta()

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Preguntados")
ventana_principal.geometry("800x600")
ventana_principal.iconbitmap("interrogacion.ico")
ventana_principal.config(bg="gray")
ventana_principal.config(bd=25)
ventana_principal.config(relief="groove")

# Frame principal para centrar los elementos
frame_principal = tk.Frame(ventana_principal, bg="gray")
frame_principal.config(width=800, height=600)
frame_principal.pack(expand=True)

# Crear la etiqueta para el título
etiqueta_titulo = tk.Label(frame_principal, text="Elige un modo:", font=("Arial", 24), bg="gray")
etiqueta_titulo.pack(pady=20)


# Opciones para el menú desplegable
opciones_modos = ['Preguntas Aleatorias',
            'Elección de Categoria',
            'Salir']

# Variable para almacenar la opción seleccionada
modo_var = tk.StringVar()
modo_var.set(opciones_modos[0])  # Establecer el valor predeterminado en la primera opción

# Crear el menú desplegable con las opciones
menu_desplegable = tk.OptionMenu(frame_principal, modo_var, *opciones_modos)
menu_desplegable.config(font=("Arial", 20), width=20)
menu_desplegable.pack(pady=10)

# Botón para iniciar el juego
boton_iniciar = tk.Button(frame_principal, text="Iniciar juego", command=iniciar_juego, font=("Arial", 20), padx=20, pady=10)
boton_iniciar.pack(pady=20)

# Centrar el frame principal
frame_principal.update_idletasks()
width = frame_principal.winfo_width()
height = frame_principal.winfo_height()
x = (ventana_principal.winfo_screenwidth() // 2) - (width // 2)
y = (ventana_principal.winfo_screenheight() // 2) - (height // 2)


ventana_principal.mainloop()
