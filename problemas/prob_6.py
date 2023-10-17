class Producto:
    # Constructor de clase
    def __init__(self, titulo, precio, anio):
        self.titulo = titulo
        self.precio = precio
        self.anio = anio
        print('Se ha añadido el producto:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.anio)
    
class Catalogo:

    productos = []  # Esta lista contendrá objetos de la clase productos

    def __init__(self, productos=[]):
        self.productos = productos

    def agregar_producto(self, p):  # p será un objeto Productos
        self.productos.append(p)

    def mostrar_producto(self):
        for p in self.productos:
            print(p) 
    def filtro_por_año(self, anio):
        productos_filtrados = [p for p in self.productos if p.anio == anio]
        if productos_filtrados:
            print(f"\n\nProductos del año {anio}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No se encontraron productos del año {anio}.")

producto_1 = Producto("Caja de cambios", 124, 2018)
producto_2 = Producto("Radiador", 342, 2021)
producto_3 = Producto("Chasis", 675, 2022)
producto_4 = Producto("Bateria", 231, 2023)
producto_5 = Producto("Motor", 432, 2020)

catalogo= Catalogo()
catalogo.agregar_producto(producto_1)
catalogo.agregar_producto(producto_2)
catalogo.agregar_producto(producto_3)
catalogo.agregar_producto(producto_4)
catalogo.agregar_producto(producto_5)


print("\n\nCatálogo de productos:")
catalogo.mostrar_producto()


catalogo.filtro_por_año(2023)

