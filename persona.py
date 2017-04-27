class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido

        self.comprobarEdad(edad)

    def comprobarEdad(self, edad):
        try:
            if edad<0 or edad>150:
                self.edad = "como eres tonto no te la puedo mostrar"
                raise EdadNoValida("Tú eres tonto")
            else:
                self.edad = edad
        except Exception:
            pass


class Currela(Persona):
    def __init__(self, salario, nombre, apellido, edad):
        super(Currela, self).__init__(nombre, apellido, edad)
        self.salario = salario
        print(self.salario)
        print(self.nombre)
        print(self.apellido)
        print(self.edad)


class EdadNoValida(RuntimeError):
    def __init__(self, textoError):
        super(EdadNoValida, self).__init__()
        self.args = textoError
        self.msgError = textoError
        print(self.msgError)


# person = Persona("alvaaro", "Torres", -1)
currito = Currela(99999,"alvaro","Torres",110)
