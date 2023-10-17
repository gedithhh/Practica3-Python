#Creamos la clase rectangulo
class rectangulo:
    def __init__(self, largo, ancho):
        self.la = largo
        self.an = ancho

    def calcular_area_rectangulo(self):
        area_rectangulo = self.la * self.an
        return area_rectangulo


#Solicitamos al usuario los datos de largo y ancho

largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

rect = rectangulo(largo, ancho)

area_rect_total = rect.calcular_area_rectangulo()


print(f"El área del rectángulo es {area_rect_total}")


