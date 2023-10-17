#importamos la libreria math para utilizar algunas operaciones matematicas
import math

class circulo:
    def __init__(self, radio):
        self.radio = radio

    def area_circulo(self):
        area = math.pi * self.radio**2
        return area
#Le asignamos un radio inicializador de 8
circ = circulo(8)


total_area = circ.area_circulo()

print(f"El área del círculo es {total_area}")
