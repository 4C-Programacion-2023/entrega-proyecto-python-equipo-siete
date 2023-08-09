import tkinter as tk
import random
from tkinter import messagebox
from Funciones import categorias

class PreguntadosApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Preguntados")
        self.geometry("400x300")
        self.current_category = None
        self.questions = []
        self.question_index = 0

        self.create_widgets()

    def create_widgets(self):
        self.start_frame = StartFrame(self, self.on_category_selected)
        self.start_frame.pack(fill=tk.BOTH, expand=True)

    def on_category_selected(self, category):
        self.current_category = category
        self.questions = categorias[category]
        self.question_index = 0

        if self.questions:
            self.show_question_frame()
        else:
            messagebox.showinfo("Sin preguntas", "No hay preguntas para esta categoría.")
            self.start_frame.reset()

    def show_question_frame(self):
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            question_frame = QuestionFrame(self, question_data, self.on_answer_submitted)
            question_frame.pack(fill=tk.BOTH, expand=True)
        else:
            self.show_result_frame()

    def on_answer_submitted(self, is_correct):
        if is_correct:
            messagebox.showinfo("¡Respuesta correcta!", "¡Respuesta correcta!")
        else:
            correct_answer = self.questions[self.question_index]["respuesta"]
            messagebox.showinfo("Respuesta incorrecta", f"La respuesta correcta es: {correct_answer}")

        self.question_index += 1
        self.show_question_frame()

    def show_result_frame(self):
        result_frame = ResultFrame(self, self.current_category, self.question_index)
        result_frame.pack(fill=tk.BOTH, expand=True)


class StartFrame(tk.Frame):
    def __init__(self, master, on_category_selected):
        super().__init__(master)
        self.on_category_selected = on_category_selected
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="¡Bienvenido a Preguntados!", font=("Arial", 14)).pack(pady=20)

        self.categories_listbox = tk.Listbox(self, selectmode=tk.SINGLE, font=("Arial", 12))
        for category in categorias.keys():
            self.categories_listbox.insert(tk.END, category)
        self.categories_listbox.pack(pady=10)

        tk.Button(self, text="Jugar", command=self.select_category).pack()

    def select_category(self):
        selected_index = self.categories_listbox.curselection()
        if selected_index:
            category = self.categories_listbox.get(selected_index[0])
            self.on_category_selected(category)

    def reset(self):
        self.categories_listbox.selection_clear(0, tk.END)


class QuestionFrame(tk.Frame):
    def __init__(self, master, question_data, on_answer_submitted):
        super().__init__(master)
        self.question_data = question_data
        self.on_answer_submitted = on_answer_submitted
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text=self.question_data["pregunta"], font=("Arial", 14)).pack(pady=20)

        self.entry_answer = tk.Entry(self, font=("Arial", 12))
        self.entry_answer.pack(pady=10)

        tk.Button(self, text="Verificar", command=self.submit_answer).pack()

    def submit_answer(self):
        user_answer = self.entry_answer.get()
        correct_answer = self.question_data["respuesta"]
        is_correct = user_answer.lower() == correct_answer.lower()
        self.on_answer_submitted(is_correct)


class ResultFrame(tk.Frame):
    def __init__(self, master, category, correct_answers):
        super().__init__(master)
        self.category = category
        self.correct_answers = correct_answers
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="¡Juego completado!", font=("Arial", 14)).pack(pady=20)

        tk.Label(self, text=f"Categoría: {self.category}", font=("Arial", 12)).pack()
        tk.Label(self, text=f"Respuestas correctas: {self.correct_answers}", font=("Arial", 12)).pack()

        tk.Button(self, text="Volver a jugar", command=self.restart_game).pack()

    def restart_game(self):
        self.destroy()
        self.master.start_frame.reset()
        self.master.start_frame.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = PreguntadosApp()
    app.mainloop()