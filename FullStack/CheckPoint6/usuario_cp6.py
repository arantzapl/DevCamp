class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"Usuario: '{self.username}'\nContraseña = '{self.password}'"

# Crear un objeto de la clase Usuario
usuarioCP6 = Usuario("ArantzaPL", "Pass1234")

# Imprimir el objeto para verificar su creación
print(usuarioCP6)

