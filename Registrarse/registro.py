import hashlib

usuarios = {}

def encriptar_contrasena(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar_usuario(datos_usuario):
    correo = datos_usuario.get("correo")
    contrasena = datos_usuario.get("contrasena")
    confirmar = datos_usuario.get("confirmar")

    # Validar campos obligatorios
    campos_requeridos = ["nombre", "documento", "edad", "nacimiento", "direccion", "correo", "contrasena", "confirmar"]
    if any(not datos_usuario.get(campo) for campo in campos_requeridos):
        return False, "Por favor, completa todos los campos."

    if contrasena != confirmar:
        return False, "Las contraseñas no coinciden."

    if correo in usuarios:
        return False, "El correo ya está registrado."

    usuarios[correo] = {
        "nombre": datos_usuario.get("nombre"),
        "documento": datos_usuario.get("documento"),
        "edad": datos_usuario.get("edad"),
        "nacimiento": datos_usuario.get("nacimiento"),
        "direccion": datos_usuario.get("direccion"),
        "contrasena": encriptar_contrasena(contrasena)
    }

    return True, f"Usuario {datos_usuario.get('nombre')} registrado exitosamente."
    
