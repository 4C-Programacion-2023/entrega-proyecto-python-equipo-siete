import tkinter as tk
from  Funciones import Ventana_Inicio,InterfazPreguntasAleatorias, InterfazPreguntasCategoria, InterfazPreguntasVF


if __name__ == "__main__":
    while True:
        
        ventana_inicio = Ventana_Inicio()
        
        
        modo_seleccionado = ventana_inicio.modo_var.get()
        if modo_seleccionado == "Preguntas Aleatorias":
            
            jugar=InterfazPreguntasAleatorias()
            jugar.iniciar()
        elif modo_seleccionado == "Eleccion de Categoria":
            jugar_eleccion=InterfazPreguntasCategoria()
            jugar_eleccion=tk.mainloop()
        elif modo_seleccionado == "Verdadero o Falso":
             interfaz = InterfazPreguntasVF()
             interfaz.iniciar()

        