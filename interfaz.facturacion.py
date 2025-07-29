import tkinter as tk
from tkinter import messagebox

def procesar_pago():
    monto = entrada_monto.get()
    metodo = metodo_pago.get()
    
    if not monto or not metodo:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        return
    
    try:
        monto = float(monto)
        if monto <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Ingrese un monto válido.")
        return
    
    messagebox.showinfo("Pago Exitoso", f"Se ha procesado un pago de ${monto:.2f} mediante {metodo}.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Pagos")
ventana.geometry("300x200")

# Etiqueta y entrada para el monto
tk.Label(ventana, text="Monto a pagar:").pack(pady=5)
entrada_monto = tk.Entry(ventana)
entrada_monto.pack(pady=5)

# Opciones de método de pago
tk.Label(ventana, text="Método de pago:").pack(pady=5)
metodo_pago = tk.StringVar(value="Efectivo")
tk.Radiobutton(ventana, text="Efectivo", variable=metodo_pago, value="Efectivo").pack()
tk.Radiobutton(ventana, text="Tarjeta", variable=metodo_pago, value="Tarjeta").pack()
tk.Radiobutton(ventana, text="Transferencia", variable=metodo_pago, value="Transferencia").pack()

# Botón para procesar el pago
tk.Button(ventana, text="Pagar", command=procesar_pago).pack(pady=10)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
