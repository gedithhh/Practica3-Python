from circulo import Circulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado



while True:
    print("\nMenú:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

    opcion = input("\nElija una opción: ")

    if opcion == "1":
        radio = float(input("Ingrese el radio del círculo: "))
        circulo = Circulo(radio)
        area = circulo.calcular_area()
        print(f"El área del círculo es {area:.2f}")
    elif opcion == "2":
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        rectangulo = Rectangulo(largo,ancho)
        area = rectangulo.calcular_area_rectangulo()
        print(f"El área del rectángulo es {area:.2f} ")
    elif opcion == "3":
        lado = float(input("Ingrese el lado del cuadrado: "))
        cuadrado = Cuadrado(lado)
        area = cuadrado.calcular_area()
        print(f"El área del cuadrado es {area:.2f} ")
    elif opcion == "4":
        print("Hasta luego!")
        break
    else:
        print("La opcion es invalidad, porfavor elija una opcion")