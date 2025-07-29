def procesar_pago():
    
    if not monto or not metodo:
        return
    
    try:
        monto = float(monto)
        if monto <= 0:
            raise ValueError
    except ValueError:
        
        return "Pago Exitoso", f"Se ha procesado un pago de ${monto:.2f} mediante {metodo}."


