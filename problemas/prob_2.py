def calificaciones():
    while True:
        entrada = input("Ingrese sus calificaciones separadas por comas: ")
        calificaciones = entrada.split(',')
        lista_calif = []

        for calificacion in calificaciones:
            try:
                calificacion_entero = int(calificacion)
                lista_calif.append(calificacion_entero)
            except ValueError:
                print(f"Error: '{calificacion}' Hay un error de tipeo, ingrese solo numeros enteros")
                break
        
        else:
            
            return lista_calif

calif_finales=calificaciones()

print("Las calificaciones ingresadas son:", calif_finales)