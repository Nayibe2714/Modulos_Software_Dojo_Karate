import tkinter as tk
from tkinter import messagebox
import sys
import os

# Para importar el módulo de registro (asumiendo que la estructura está así)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'registro')))
import registro

def registrar():
    datos_usuario = {
        "nombre": entry_nombre.get(),
        "documento": entry_documento.get(),
        "edad": entry_edad.get(),
        "nacimiento": entry_nacimiento.get(),
        "direccion": entry_direccion.get(),
        "correo": entry_correo.get(),
        "contrasena": entry_contrasena.get(),
        "confirmar": entry_confirmar.get()
    }

    exito, mensaje = registro.registrar_usuario(datos_usuario)

    if exito:
        messagebox.showinfo("Éxito", mensaje)
        limpiar_campos()
    else:
        messagebox.showerror("Error", mensaje)

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_documento.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_nacimiento.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_contrasena.delete(0, tk.END)
    entry_confirmar.delete(0, tk.END)

root = tk.Tk()
root.title("Registro de Usuario")

labels = ["Nombre", "Documento de identidad", "Edad", "Fecha de nacimiento", "Dirección", "Correo", "Contraseña", "Confirmar contraseña"]
entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root, width=30)
    if "Contraseña" in text:
        entry.config(show="*")
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

(entry_nombre, entry_documento, entry_edad, entry_nacimiento,
 entry_direccion, entry_correo, entry_contrasena, entry_confirmar) = entries

btn_registrar = tk.Button(root, text="Registrar", command=registrar)
btn_registrar.grid(row=len(labels), column=0, columnspan=2, pady=15)

root.mainloop()