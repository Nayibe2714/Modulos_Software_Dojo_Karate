import tkinter as tk
from tkinter import ttk, messagebox

class Horario_clases:
    def __init__(self, root):  # CORRECCIÓN: __init__ (doble guion bajo)
        self.root = root
        self.root.title("Horario de Clases")

        # Crear la tabla (usando ttk.Treeview)
        self.tree = ttk.Treeview(root, columns=("Hora", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"), show="headings")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Lunes", text="Lunes")
        self.tree.heading("Martes", text="Martes")
        self.tree.heading("Miércoles", text="Miércoles")
        self.tree.heading("Jueves", text="Jueves")
        self.tree.heading("Viernes", text="Viernes")
        self.tree.pack(pady=10)

        # Agregar filas (ejemplo)
        horas = ["8:00-9:00", "9:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-13:00"]
        for hora in horas:
            self.tree.insert("", "end", values=(hora, "", "", "", "", ""))

        # Botón para guardar (ejemplo)
        self.guardar_button = tk.Button(root, text="Guardar Horario", command=self.guardar_horario)
        self.guardar_button.pack(pady=5)

    def guardar_horario(self):
        # Aquí puedes agregar la lógica para guardar el horario
        messagebox.showinfo("Información", "Horario guardado (simulación)")