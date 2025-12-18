import random
from collections import Counter

def inserta_ordenado(lista_nombres: list[str], nombre: str) -> None:
    """
    Inserta un nombre en una lista de nombres manteniendo el orden (de menor a mayor longitud).
    Si la lista recibida no estuviera ordenada por longitud, la función no hace nada.

    Parámetros:
    lista_nombres (list[str]): Lista de nombres ordenada por longitud.
    nombre (str): Nombre a insertar.
    """
    ordenada = sorted(lista_nombres, key = len)
    for a, b in zip(ordenada, lista_nombres):
        if a != b:
            return 
    lista_nombres.append(nombre)
    return lista_nombres.sort(key = len)

def busca_duplicados_count(lista: list) -> list:
    """
    Busca y devuelve una lista con los elementos duplicados en la lista recibida.

    Parámetros:
    lista (list): Lista en la que buscar duplicados.

    Devuelve:
    list: Lista con los elementos duplicados.
    """
    res =[]
    contador = Counter(lista)
    for a in contador:
        if contador[a] > 1:
            res.append(a)
    return res

def busca_duplicados(lista: list) -> list:
    res = []
    for elem in lista:
        pos = lista.index(elem)
        if elem in lista[pos+1 : ] and elem not in res:
            res.append(elem)
    return res

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
    res = []
    while len(res) < n:
        nuevo = random.randint(minimo, maximo)
        if res == [] or nuevo != res[-1]:
            res.append(nuevo)
    return res

def intercala_listas(lista1: list, lista2: list) -> list:
    """
    Intercala dos listas. Si una lista es mayor que la otra, los elementos sobrantes se añaden al final.

    Parámetros:
    lista1 (list): Primera lista.
    lista2 (list): Segunda lista.

    Devuelve:
    list: Lista resultante de intercalar las dos listas.
    """
    res = []
    for a, b in zip(lista1, lista2):
        res.append(a)
        res.append(b)
    if len(lista1) > len(lista2):
        ultima_pos = len(lista2)
        res.extend(lista1[ultima_pos:])
    elif len(lista2) > len(lista1):
        ultima_pos = len(lista1)
        res.extend(lista2[ultima_pos:])
    return res


def mezcla_ordenadas(lista1: list, lista2: list) -> list:
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.

    Parámetros:
    lista1 (list): Primera lista ordenada.
    lista2 (list): Segunda lista ordenada.

    Devuelve:
    list: Lista resultante de mezclar las dos listas ordenadas.
    """
    res = []
    res.extend(lista1)
    res.extend(lista2)
    ordenada = sorted(res)
    return ordenada

def ordena_bubble_sort(lista: list) -> None:
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento bubble sort. 

    Parámetros:
    lista (list[int]): Lista de números enteros a ordenar.
    """    
    intercambios = 1
    while intercambios > 0:
        intercambios = 0
        for a, b in zip(lista, lista[1:]):
            if a > b:
                pos_a_insertar = lista.index(b)
                primero = lista.pop(lista.index(a))
                
                lista.insert(pos_a_insertar, primero)
                intercambios += 1
    return lista