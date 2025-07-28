import tkinter as tk
from tkinter import messagebox
from Alumno import registrar_usuario, login_usuario

# Funciones que se conectan con alumno.py
def registrar():
    correo = entrada_correo.get()
    contraseña = entrada_contraseña.get()
    resultado = registrar_usuario(correo, contraseña)
    messagebox.showinfo("Registro", resultado)

def login():
    correo = entrada_correo.get()
    contraseña = entrada_contraseña.get()
    resultado = login_usuario(correo, contraseña)
    messagebox.showinfo("Login", resultado)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Escuela del Dojo - Login")
ventana.geometry("300x200")

# Etiquetas y entradas
tk.Label(ventana, text="Correo:").pack(pady=5)
entrada_correo = tk.Entry(ventana)
entrada_correo.pack()

tk.Label(ventana, text="Contraseña:").pack(pady=5)
entrada_contraseña = tk.Entry(ventana, show="*")
entrada_contraseña.pack()

# Botones
tk.Button(ventana, text="Registrar", command=registrar).pack(pady=10)
tk.Button(ventana, text="Iniciar Sesión", command=login).pack()

# Iniciar la aplicación
ventana.mainloop()