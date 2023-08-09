import tkinter as tk
from tkinter import *
import random
from Preguntas_Preguntados import preguntas_cat
from tkinter import messagebox

class JuegoPreguntas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("800x600")

        self.config(bd=25)
        self.config(relief="groove")
        self.configure(bg="gray")
        self.mostrar_pagina_principal()

    def mostrar_pagina_principal(self):
        etiqueta = tk.Label(self, text="Preguntados", font=("Arial", 24))
        etiqueta.pack(pady=20)
        etiqueta.config(bg="gray")
        

        boton_jugar = tk.Button(self, text="Jugar", command=self.mostrar_pagina_juego)
        boton_jugar.pack()

    def mostrar_pagina_juego(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.pregunta_label = tk.Label(self, text="", font=("Arial", 16), wraplength=400, bg="gray")
        self.pregunta_label.pack(pady=20)

        self.botones = []
        for i in range(4):
            boton = tk.Button(self, text="", font=("Arial", 14), width=30, height=2,
                              command=lambda respuesta=i: self.verificar_respuesta(respuesta+1))
            self.botones.append(boton)
            boton.pack(pady=5)

        self.resultado_label = tk.Label(self, text="", font=("Arial", 16), bg="gray")
        self.resultado_label.pack(pady=20)

        self.pregunta_actual = None
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        categoria = random.choice(list(preguntas_cat.keys()))
        pregunta = random.choice(preguntas_cat[categoria])

        self.pregunta_label.config(text=pregunta["nombre"])
        self.pregunta_actual = pregunta

        for i, opcion in enumerate(pregunta["opciones"]):
            self.botones[i].config(text=opcion)

    def verificar_respuesta(self, respuesta):
        correcto = respuesta == self.pregunta_actual["respuesta"]
        if correcto:
            correctos=+1
            messagebox.showinfo("Correcto", "¡Respuesta correcta!")
        
        else:
            incorrectos=+1
            messagebox.showerror("Incorrecto", "Respuesta incorrecta.")
            
        self.after(100, self.mostrar_pregunta)
        self.resultado_label.config(text=(f'Respuestas correctas:",correctos,"/10. Respuestas incorrectas: {incorrectos}/3'), fg="black", bg="gray")
        

if __name__ == "__main__":
    correctos=0
    incorrectos=0
    juego = JuegoPreguntas()
    juego.mainloop()
    while correctos < 10:
        
        
        if incorrectos == 3:
                messagebox.showerror("Perdiste, INtentalo de nuevo")
                break

    if correctos == 10:
        messagebox.showinfo("Ganaste!!")
