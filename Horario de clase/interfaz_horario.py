import tkinter as tk
import sys
import os

# Agregamos la carpeta horario al path para importar app.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'horario')))
from Horario import Horario_clases

if __name__ == "__main__":
    root = tk.Tk()
    app = Horario_clases(root)
    root.mainloop()