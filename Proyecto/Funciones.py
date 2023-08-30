import tkinter as tk
from tkinter import PhotoImage
from Preguntas_Preguntados import preguntas_cat
import random
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Preguntas_Preguntados2 import preguntas_vof
import sys


imagenes_categorias = {
    "Deporte": "deporte.png",
    "Historia": "historia.png",
    "Ciencia": "ciencia.png",
    "Geografia":"Geografia.png",
    "Entretenimiento":"Entretenimiento.png",
    "Arte":"Arte.png"

}

OPCIONES_MODOS = ["Preguntas Aleatorias", "Eleccion de Categoria", "Verdadero o Falso"]

class Ventana_Inicio:
    def __init__(self):
        color_violeta = "#5e16ea"
        self.ventana = tk.Tk()
        self.ventana.title("Preguntados")
        self.ventana.geometry("1000x750")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.ventana.config(bg=color_violeta, bd=25, relief="groove")
        self.ventana.resizable(False, False)
        self.ventana.iconbitmap("pregunta2.ico")

        background_image = Image.open("Pantalla_Inicio.png")  # Cambia por la ruta de tu imagen de fondo
        self.background_photo = ImageTk.PhotoImage(background_image)
        self.background_label = tk.Label(self.ventana, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.frame_principal = tk.Frame(self.ventana, bg=color_violeta)
        self.frame_principal.pack(expand=True, padx=20, pady=20)
        
        etiqueta_titulo = tk.Label(self.frame_principal, text="Bienvenido a ", font=("Tahoma", 20), bg=color_violeta)
        etiqueta_titulo.pack(pady=0)
        etiqueta_titulo2 = tk.Label(self.frame_principal, text="Preguntados", font=("Impact", 38), bg=color_violeta)
        etiqueta_titulo2.pack(pady=0)

        etiqueta_modo = tk.Label(self.frame_principal, text="Elige un modo ↓↓↓ ", font=("Tahoma", 20), bg=color_violeta)
        etiqueta_modo.pack(pady=20)

        self.modo_var = tk.StringVar()
        self.modo_var.set(OPCIONES_MODOS[0])
        
        menu_desplegable = ttk.Combobox(self.frame_principal, values=OPCIONES_MODOS, textvariable=self.modo_var, state="readonly", font=("Arial", 18), width=25, justify="center")
        menu_desplegable.pack(pady=10, padx=10)

        boton_iniciar = tk.Button(self.frame_principal, text="Iniciar Juego", command=self.ventana.destroy, font=("Arial", 20), padx=15, pady=7, bg="green", fg="white")
        boton_iniciar.config(bd=6,  relief="raised") 
        boton_iniciar.pack(pady=20)

        boton_salir = tk.Button(self.frame_principal, text="Salir", command=self.cerrar_ventana, font=("Arial", 15), padx=10, pady=10, bg="red", fg="white", width=5, height=1)
        boton_salir.config(bd=5,  relief="raised") 
        boton_salir.pack(pady=10)

        self.ventana.mainloop()


    def cerrar_ventana(self):
        print("Saliendo del juego...")
        self.ventana.destroy()
        sys.exit()

class InterfazPreguntasAleatorias:
    def __init__(self):
        self.ventana = tk.Tk()  
        self.ventana.title("Preguntas y Opciones")
        self.ventana.geometry("800x600")
        self.ventana.iconbitmap("pregunta2.ico") 

        self.imagen_label = tk.Label(self.ventana)
        self.imagen_label.pack()
        imagen = PhotoImage(file="ImagPregunta.png")
        self.imagen_label = tk.Label(self.ventana, image=imagen)
        self.imagen_label.image = imagen
        self.imagen_label.pack()

        self.pregunta_label = tk.Label(self.ventana, text="", font=("Arial", 18), wraplength=600)
        self.pregunta_label.pack(pady=10)

        self.botones_frame = tk.Frame(self.ventana)
        self.botones_frame.pack()

        self.botones = []
        for i in range(4):
            boton = tk.Button(self.botones_frame, text="", font=("Arial", 16),width=25, height=1, command=lambda i=i: self.boton_presionado(i))
            boton.config(bd=5, highlightbackground="black", relief="raised") 
            boton.grid(row=i // 2, column=i % 2, padx=20, pady=10, sticky="w")
            self.botones.append(boton)


        self.color_gris = "#b4b5b4"
        self.respuestas_label = tk.Label(self.ventana, bg=self.color_gris, text="Respuestas Correctas: 0/10   Respuestas Incorrectas: 0/3", font=("Arial", 16))
        self.respuestas_label.config(bd=5, highlightbackground="black", relief="sunken") 
        self.respuestas_label.pack(pady=5)

        self.respuestas_correctas = 0
        self.respuestas_incorrectas = 0

        self.boton_salir = tk.Button(self.ventana, text="Atras", font=("Arial", 12), bg="red", fg="white", command=self.reinicio_juego)
        self.boton_salir.pack(side="left", anchor="sw", padx=15, pady=15)
        
        self.siguiente_pregunta()

    def iniciar(self):
        self.siguiente_pregunta()
        self.ventana.mainloop() 

    def reinicio_juego(self):
        self.ventana.destroy()
        
    def boton_presionado(self, opcion):
        if opcion == self.pregunta_actual["respuesta"] - 1:
            self.respuestas_correctas += 1
            resultado = messagebox.showinfo( "Correcto", "Respuesta Correcta ")
            
            self.siguiente_pregunta()
        else:
            self.respuestas_incorrectas += 1
            resultado = messagebox.showerror("Incorrecto","Respuesta Incorrecta")
            
            self.siguiente_pregunta()
        
        self.actualizar_respuestas()

    def siguiente_pregunta(self):
        while self.respuestas_correctas < 10 and self.respuestas_incorrectas < 3:
            categoria_aleatoria = random.choice(list(preguntas_cat.keys()))
            preguntas_categoria = preguntas_cat[categoria_aleatoria]
            self.pregunta_actual = random.choice(preguntas_categoria)

            self.pregunta_label.config(text=self.pregunta_actual["nombre"])

            for i, opcion in enumerate(self.pregunta_actual["opciones"]):
                self.botones[i].config(text=str(i + 1) + ". " + str(opcion))


            self.actualizar_respuestas()
            return
        if self.respuestas_incorrectas == 3:
            print('Perdiste')
            messagebox.showerror("Perdiste", "     Perdiste\n\nInténtalo de nuevo", icon='warning')
            self.ventana.destroy()
            
        if self.respuestas_correctas == 10:
            messagebox.showinfo( "Ganaste", "  ¡Ganaste!       ", )
            print('Ganaste!')
            self.ventana.destroy()
            
    def actualizar_respuestas(self):
        texto_respuestas = f"Respuestas Correctas: {self.respuestas_correctas}   Respuestas Incorrectas: {self.respuestas_incorrectas}"
        self.respuestas_label.config(text=texto_respuestas)

class InterfazPreguntasCategoria:
    def __init__(self):
        self.ventana_seleccion = tk.Tk()
        self.ventana_seleccion.title("Seleccionar Categoría")
        self.ventana_seleccion.geometry("600x400")

        self.categoria_seleccionada = tk.StringVar(value=list(preguntas_cat.keys())[0])  # Inicializar con la primera categoría

        self.label_categoria = tk.Label(self.ventana_seleccion, text="Selecciona una categoría:",font=("Verdana", 30))
        self.label_categoria.pack()

        for categoria in preguntas_cat.keys():
            radio_button = tk.Radiobutton(self.ventana_seleccion, text=categoria, variable=self.categoria_seleccionada, value=categoria,font=23)
            radio_button.pack()

        self.boton_empezar = tk.Button(self.ventana_seleccion, text="Empezar", command=self.abrir_ventana_juego, font=("Arial", 20), padx=15, pady=7, bg="green", fg="white")
        self.boton_empezar.config(bd=6,  relief="raised") 
        self.boton_empezar.pack()

    
    def abrir_ventana_juego(self):
        self.ventana_seleccion.destroy()
        categoria_seleccionada = self.categoria_seleccionada.get()
        VentanaJuego(preguntas_cat[categoria_seleccionada], categoria_seleccionada)

class VentanaJuego:
    def __init__(self, preguntas_categoria,categoria_seleccionada):
        self.ventana_juego = tk.Tk()
        self.ventana_juego.title("Juego")
        self.ventana_juego.geometry("800x600")
        self.ventana_juego.iconbitmap("pregunta2.ico")

        imagen_path = f"{categoria_seleccionada}.png"
        imagen_pil = Image.open(imagen_path)
        nuevo_tamaño = (300, 200)  # Cambia los valores según tus necesidades
        imagen_pil = imagen_pil.resize(nuevo_tamaño, Image.ANTIALIAS)  # Redimensiona con antialiasing
        imagen = ImageTk.PhotoImage(imagen_pil)

        self.imagen_label = tk.Label(self.ventana_juego, image=imagen)
        self.imagen_label.image = imagen
        self.imagen_label.pack()
            
        self.respuestas_correctas = 0
        self.respuestas_incorrectas = 0
        self.preguntas_categoria = preguntas_categoria
        self.pregunta_actual = None

        self.pregunta_label = tk.Label(self.ventana_juego, text="", font=("Arial", 18))
        self.pregunta_label.pack()

        self.botones = []
        
        self.botones = []
        for _ in range(4):
            boton = tk.Button(self.ventana_juego, text="", command=lambda i=_: self.boton_presionado(i), font=("Arial", 16), width=30, height=1)
            boton.config(bd=5, highlightbackground="black", relief="raised") 
            boton.pack(pady=3)
            self.botones.append(boton)

        self.color_gris = "#b4b5b4"
        self.respuestas_label = tk.Label(self.ventana_juego, bg=self.color_gris, text="Respuestas Correctas: 0/10   Respuestas Incorrectas: 0/3", font=("Arial", 16))
        self.respuestas_label.config(bd=5, highlightbackground="black", relief="sunken") 
        self.respuestas_label.pack(pady=5)

        
        self.siguiente_pregunta()

        self.ventana_juego.mainloop()

    def boton_presionado(self, opcion):
        if opcion == self.pregunta_actual["respuesta"] - 1:
            self.respuestas_correctas += 1
            resultado = messagebox.showinfo("Correcto", "Respuesta Correcta")
        else:
            self.respuestas_incorrectas += 1
            resultado = messagebox.showerror("Incorrecto", "Respuesta Incorrecta")
        
        self.siguiente_pregunta()

    def siguiente_pregunta(self):
        if self.respuestas_correctas < 10 and self.respuestas_incorrectas < 3:
            self.pregunta_actual = random.choice(self.preguntas_categoria)

            self.pregunta_label.config(text=self.pregunta_actual["nombre"])

            for i, opcion in enumerate(self.pregunta_actual["opciones"]):
                self.botones[i].config(text=str(i + 1) + ". " + str(opcion))

            self.actualizar_respuestas()
        elif self.respuestas_incorrectas == 3:
            print('Perdiste')
            messagebox.showerror("Perdiste", "     Perdiste\n\nInténtalo de nuevo", icon='warning')
            self.ventana_juego.destroy()
        elif self.respuestas_correctas == 10:
            print('Ganaste!')
            messagebox.showinfo("Ganaste", "  ¡Ganaste!       ")
            self.ventana_juego.destroy()

    def actualizar_respuestas(self):
        texto_respuestas = f"Respuestas Correctas: {self.respuestas_correctas}   Respuestas Incorrectas: {self.respuestas_incorrectas}"
        self.respuestas_label.config(text=texto_respuestas)



class InterfazPreguntasVF:
    def __init__(self):
        self.ventana = tk.Tk()  
        self.ventana.title("Verdadero o Falso")
        self.ventana.geometry("800x600")
        self.ventana.iconbitmap("pregunta2.ico") 
        background_image = Image.open("interfazVoF.jpeg")  
        self.background_photo = ImageTk.PhotoImage(background_image)
        self.background_label = tk.Label(self.ventana, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.imagen_label = tk.Label(self.ventana)
        self.imagen_label.pack()
        imagen = PhotoImage(file="ImagPregunta.png")
        self.imagen_label = tk.Label(self.ventana, image=imagen)
        self.imagen_label.image = imagen
        self.imagen_label.pack()

        self.pregunta_label = tk.Label(self.ventana, text="", font=("Arial", 18), wraplength=600, bg="gray")
        self.pregunta_label.pack(pady=10)

        self.botones_frame = tk.Frame(self.ventana)
        self.botones_frame.pack()

        self.botones = []
        for i in range(2):
            boton = tk.Button(self.botones_frame, text="", font=("Arial", 16),width=25, height=1, command=lambda i=i: self.boton_presionado(i))
            boton.config(bd=5, highlightbackground="black", relief="raised", bg= "purple") 
            boton.grid(row=i // 2, column=i % 2, padx=0, pady=0, sticky="w")
            self.botones.append(boton)


        self.color_gris = "#b4b5b4"
        self.respuestas_label = tk.Label(self.ventana, bg=self.color_gris, text="Respuestas Correctas: 0/10   Respuestas Incorrectas: 0/3", font=("Arial", 16))
        self.respuestas_label.config(bd=5, highlightbackground="black", relief="sunken") 
        self.respuestas_label.pack(pady=5)

        self.respuestas_correctas = 0
        self.respuestas_incorrectas = 0

        self.boton_salir = tk.Button(self.ventana, text="Atras", font=("Arial", 12), bg="red", fg="white", command=self.reinicio_juego)
        self.boton_salir.pack(side="left", anchor="sw", padx=15, pady=15)
        
        self.siguiente_pregunta()

    def iniciar(self):
        self.siguiente_pregunta()
        self.ventana.mainloop() 

    def reinicio_juego(self):
        self.ventana.destroy()
        
    def boton_presionado(self, opcion):
        if opcion == self.pregunta_actual["respuesta"] - 1:
            self.respuestas_correctas += 1
            resultado = messagebox.showinfo( "Correcto", "Respuesta Correcta ")
            
            self.siguiente_pregunta()
        else:
            self.respuestas_incorrectas += 1
            resultado = messagebox.showerror("Incorrecto","Respuesta Incorrecta")
            
            self.siguiente_pregunta()
        
        self.actualizar_respuestas()

    def siguiente_pregunta(self):
        while self.respuestas_correctas < 10 and self.respuestas_incorrectas < 3:
            categoria_aleatoria = random.choice(list(preguntas_vof.keys()))
            preguntas_categoria = preguntas_vof[categoria_aleatoria]
            self.pregunta_actual = random.choice(preguntas_categoria)

            self.pregunta_label.config(text=self.pregunta_actual["nombre"])

            for i, opcion in enumerate(self.pregunta_actual["opciones"]):
                self.botones[i].config(text=str(i + 1) + ". " + str(opcion))


            self.actualizar_respuestas()
            return
        if self.respuestas_incorrectas == 3:
            print('Perdiste')
            messagebox.showerror("Perdiste", "     Perdiste\n\nInténtalo de nuevo", icon='warning')
            self.ventana.destroy()
            
        if self.respuestas_correctas == 10:
            messagebox.showinfo( "Ganaste", "  ¡Ganaste!       ", )
            print('Ganaste!')
            self.ventana.destroy()
            
    def actualizar_respuestas(self):
        texto_respuestas = f"Respuestas Correctas: {self.respuestas_correctas}   Respuestas Incorrectas: {self.respuestas_incorrectas}"
        self.respuestas_label.config(text=texto_respuestas)
