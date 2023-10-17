import random

def generar_enteros_aleatorios(n):
    return [random.randint(0, 100) for _ in range(n)]

def mostrar_lista(lista):
    for numero in lista:
        print(numero, end=" ")
    print()

def ordenar_lista(lista):
    lista.sort()
    mostrar_lista(lista)
