# se ingresan los datos de los alumnos y se registran en un diccionario
usuarios = {
    "juan123@gmail.com": "juan123",
    "pedro456@gmail.com": "pedro456",
    "andrea789@gmail.com": "andrea789",
}

#funciones para registrar un nuevo usuario 
def registrar_usuario(correo, contraseña):
    if correo in usuarios:
        return "El correo ya está registrado."
    usuarios[correo] = contraseña
    return "Registro exitoso."

# Función para iniciar sesión
def login_usuario(correo, contraseña):
    if correo in usuarios and usuarios[correo] == contraseña:
        return "Login exitoso. ¡Bienvenido al Dojo!"
    return "Correo o contraseña incorrectos."