import random

def inserta_ordenado(lista_nombres: list[str], nombre: str) -> None:
    """
    Inserta un nombre en una lista de nombres manteniendo el orden (de menor a mayor longitud).
    Si la lista recibida no estuviera ordenada por longitud, la función no hace nada.

    Parámetros:
    lista_nombres (list[str]): Lista de nombres ordenada por longitud.
    nombre (str): Nombre a insertar.
    """
    if lista_nombres == []:
            lista_nombres.append(nombre)
            return lista_nombres
    for a, b in zip(lista_nombres, lista_nombres[1:]): 
        if len(a) > len(b):
            return lista_nombres
        elif len(a) <= len(nombre) <= len(b):
            lista_nombres.insert(lista_nombres.index(b), nombre)
            return lista_nombres
        elif len(nombre) < len(a):
            lista_nombres.insert(0,nombre)
            return lista_nombres
        elif len(nombre) > len(b):
            lista_nombres.append(nombre)
            return lista_nombres

    
  



def busca_duplicados(lista: list) -> list:
    """
    Busca y devuelve una lista con los elementos duplicados en la lista recibida.

    Parámetros:
    lista (list): Lista en la que buscar duplicados.

    Devuelve:
    list: Lista con los elementos duplicados.
    """
    # - usando count
    '''duplicados = []
    for n in lista:
        cuenta = lista.count(n)
        if cuenta > 1 and n not in duplicados:
            
            duplicados.append(n)
    return duplicados
    ''' 
    # - usando slicing y sin usar count
    duplicados = []
    for i in lista:
        if i in lista[lista.index(i)+1:] and i not in duplicados:
            duplicados.append(i)
    return duplicados




def genera_aleatorios(n: int, minimo: int, maximo: int) -> list[int]:
    """
    Genera una lista con n números enteros aleatorios en un rango dado,
    asegurando que no haya dos elementos consecutivos iguales.

    Parámetros:
    n (int): Número de elementos en la lista.
    minimo (int): Valor mínimo del rango (inclusive).
    maximo (int): Valor máximo del rango (inclusive).

    Devuelve:
    list[int]: Lista con n números enteros aleatorios.
    """
    lista = []
    for a in range(n):
        lista.append(random.randint(minimo,maximo))
    for i in range(len(lista)-1):
        while i == :
            lista.remove(i)
            lista.insert(i, random.randint(minimo, maximo))
    return lista
         #mal   






def intercala_listas(lista1: list, lista2: list) -> list:
    """
    Intercala dos listas. Si una lista es mayor que la otra, los elementos sobrantes se añaden al final.

    Parámetros:
    lista1 (list): Primera lista.
    lista2 (list): Segunda lista.

    Devuelve:
    list: Lista resultante de intercalar las dos listas.
    """
    # TODO: Implementa esta función
    pass

def mezcla_ordenadas(lista1: list, lista2: list) -> list:
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.

    Parámetros:
    lista1 (list): Primera lista ordenada.
    lista2 (list): Segunda lista ordenada.

    Devuelve:
    list: Lista resultante de mezclar las dos listas ordenadas.
    """
    # TODO: Implementa esta función
    pass

def ordena_bubble_sort(lista: list) -> None:
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento bubble sort. 

    Parámetros:
    lista (list[int]): Lista de números enteros a ordenar.
    """    
# TODO: Implementa esta función
    pass