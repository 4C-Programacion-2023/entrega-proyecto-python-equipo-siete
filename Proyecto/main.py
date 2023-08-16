import tkinter as tk
from tkinter import ttk
from Funciones import OPCIONES_MODOS

modo_var = None
def Ventana_Inicio():
    global modo_var
    ventana = tk.Tk()
    ventana.title("Preguntados")
    ventana.geometry("1000x800")  
    ventana.config(bg="gray")
    ventana.config(bd=25)
    ventana.config(relief="groove")

    frame_principal = tk.Frame(ventana, bg="gray") 
    frame_principal.pack(expand=True)

    etiqueta_titulo = tk.Label(frame_principal, text="Elige un modo:", font=("Arial", 24), bg="gray")
    etiqueta_titulo.pack(pady=20)



    modo_var = tk.StringVar()
    modo_var.set(OPCIONES_MODOS[0])  
    menu_desplegable = ttk.Combobox(frame_principal, values=OPCIONES_MODOS, textvariable=modo_var, state="readonly", font=("Arial", 18), width=17)
    menu_desplegable.pack(pady=10)

    def iniciar_juego():
        modo_seleccionado = modo_var.get()
        print("Modo seleccionado:", modo_seleccionado)
        ventana.destroy()
        
    boton_iniciar = tk.Button(frame_principal, text="Iniciar juego", command=iniciar_juego, font=("Arial", 20), padx=20, pady=10, bg="pink")
    boton_iniciar.pack(pady=20)

    def Salir():
        print("Saliendo del juego...")
        ventana.destroy()
        return exit()

    boton_salir = tk.Button(frame_principal, text="Salir", command=Salir, font=("Arial", 15), padx=10, pady=10, bg="red")
    boton_salir.pack(pady=10)

    frame_principal.update_idletasks()
    width = frame_principal.winfo_width()
    height = frame_principal.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana.winfo_screenheight() // 2) - (height // 2)
    return ventana.mainloop()


import random
from Funciones import  preguntas, CATEGORIAS, mostrar_info_jugador, categorias_faltan, elegir_categoria, eleccion_cat
from tkinter import messagebox


if __name__ == "__main__":
    incorrectos = 0
    correctos = 0
    Ventana_Inicio()
    modo_seleccionado = modo_var.get()
    preguntas_hechas = {categoria: [] for categoria in CATEGORIAS}
    
    if modo_seleccionado == 'Preguntas Aleatorias':
        print(f"")
        print(f"")
        while correctos < 10 and incorrectos < 3:
            cat_elegida = random.randint(0, len(CATEGORIAS) - 1)
            
            respuesta = preguntas(CATEGORIAS[cat_elegida], preguntas_hechas)

            if respuesta:
                messagebox.showinfo( "Correcto", "Respuesta Correcta ")
                correctos += 1
            
            else:
                incorrectos += 1
                messagebox.showerror("Incorrecto","Respuesta Incorrecta")
            
            print(f'Respuestas correctas: {correctos}/10. Respuestas incorrectas: {incorrectos}/3')
            print(f'')
            print(f'')
            if incorrectos == 3:
                print('Perdiste')
                messagebox.showerror( "Perdiste", "      Perdiste                                                Intentalo de nuevo", icon='warning')
                break
        if correctos == 10:
            messagebox.showinfo( "Ganaste", " ¡Ganaste!       ", )
            print('Ganaste!')
    elif modo_seleccionado == 'De a 2 jugadores':
        print(f"")
        print(f"")
        cant_de_jugadores = 2
        rango = cant_de_jugadores + 1
        info_jugador = [{x: False for x in CATEGORIAS} for i in range(rango)]
        i = 1
        CORONITA = len(CATEGORIAS)
        
        while i != 0: 
            if i == rango:
                i = 1  
            else:
                correctos = 0
                incorrectos = 0
                mostrar_info_jugador(info_jugador[i-1], i)  
                turno_actual = i
                
                while i == turno_actual: 
                    print(f'\nTurno del jugador {i}')  
                    
                    cat_elegida = random.randint(0, CORONITA)  
                    
                    if cat_elegida != CORONITA:  
                        respuesta = preguntas(CATEGORIAS[cat_elegida]) 
                        
                        if respuesta:  
                            correctos += 1 
                            corrio = elegir_categoria(correctos, info_jugador[i-1])
                            if corrio: 
                                i += 1  
                        else:  
                            incorrectos += 1 
                            i += 1  
                    else:  
                        print('Coronita\nElegí la categoria')
                        correctos = 3  
                        elegir_categoria(correctos, info_jugador[i-1])
                        i += 1 
                    

                    if not categorias_faltan(info_jugador[i-1]):
                        print(f'Jugador {i} es el ganador')
                        break 


    elif modo_seleccionado == "Eleccion de Categoria":
        print(f"")
        print(f"")
        info_jugador = {x: False for x in CATEGORIAS}
        eleccion_cat(correctos,incorrectos, info_jugador, preguntas_hechas)
        
        
            
