def ingreso_largo(msg:str = 'Ingrese el largo del rectangulo: ') -> int:
    try:
        x=int(input(msg))
        return x
    except:
        return ingreso_largo(msg)

def ingreso_ancho(msg:str = 'Ingrese el ancho del rectangulo: ') -> int:
    try:
        x=int(input(msg))
        return x
    except:
        return ingreso_ancho(msg)