class Rectangulo:
    def __init__(self, largo, ancho):
        self.la = largo
        self.an = ancho

    def calcular_area_rectangulo(self):
        area_rectangulo = self.la * self.an
        return area_rectangulo