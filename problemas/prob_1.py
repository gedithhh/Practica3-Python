def calcular_cantidad_combustible():
    while True:
        try:
            #Solicitamos la fraccion con numeros enteros y en el formato X/Y
            entrada = input("Ingrese una fracción en formato X/Y : ")
            if '/' not in entrada:
                print("El formato no es correcto. Ingrese X/Y.")
                continue
             #Toma los numeros en cadena para luego dividirlos y asignarles a X y y por separado
            x, y = map(int, entrada.split('/'))
            if y == 0 or x > y:
                print("El formato es incorrecto.  X debe ser menor a Y y no puede ser 0.")
                continue
            
            #Asignamos la variable porcentaje para almacenar ahi la division lista en porcentaje
            porcentaje = (x / y) * 100

            if porcentaje < 1:
                print("E")
            elif porcentaje > 99:
                print("F")
            else:
                print(f"{round(porcentaje)}%")

            break
        #Asignamos los except solicitados
        except ValueError:
            print("El formato es incorrecto. Porfavor debe ingresar dos números enteros ")
        except ZeroDivisionError:
            print("El formato es incorrecto. El denominador no puede ser cero.")

calcular_cantidad_combustible()
