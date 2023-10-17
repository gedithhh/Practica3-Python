class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None  
        self.notas = {}  

    def Display(self):
    
        print(f"Nombre: {self.nombre} ")
        print(f"Número de Registro: {self.numero_registro}")
        print(f"Edad: {self.edad} años" )
        print(f"Notas: {self.notas}")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, curso, nota):
        self.notas[curso] = nota

alumno_mostrar = Alumno("Luciana Rojas Palacios", "00231")

alumno_mostrar.setAge(17)
alumno_mostrar.setNota("Contabilidad I", 12)
alumno_mostrar.setNota("Matematica Discreta", 15)
alumno_mostrar.setNota("Tesis II", 13)

alumno_mostrar.Display()
