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
    res = []
    while len(res) != n: #bucle hasta que llegemos a los n números
        res.append(random.randint(minimo, maximo)) #añadimos número aleatorio
        if len(res) > 1: #si hay más de 1 elemento en res, comprobamos
            for a, b in zip(res, res[1:]): #recorremos los elementos consecutivos
                if a == b: #si son iguales
                    iguales = True
                    while iguales:
                        res.pop() #quito el último
                        nuevo = random.randint(minimo, maximo)
                        res.append(nuevo) #pongo otro aleatorio
                        if a != nuevo:
                            iguales = False
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
    for i in range(min(len(lista1), len(lista2))):
        res.append(lista1[i])
        res.append(lista2[i])
    if len(lista1) > len(lista2):
        n = len(lista1) - len(lista2)
        res.extend(lista1[-n:])
    elif len(lista2) > len(lista1):
        n = len(lista2) - len(lista1)
        res.extend(lista2[-n:])
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

    #res = []
    #res.extend(lista1)
    #res.extend(lista2)
    #res.sort()
    #return res        --> Solución óptima

    res = []
    for a,b in zip(lista1, lista2):
        if a <= b:
            res.append(a)
            res.append(b)
        elif b < a:
            res.append(b)
            res.append(a)
    dif = abs(len(lista1)-len(lista2))
    if len(lista1) > len(lista2):
        res.extend(lista1[-dif:])
    elif len(lista2) > len(lista1):
        res.extend(lista2[-dif:])
    return res


def ordena_bubble_sort(lista: list) -> None:
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento bubble sort. 

    Parámetros:
    lista (list[int]): Lista de números enteros a ordenar.
    """    
    cambios = 1
    while cambios != 0:
        cambios = 0
        for a,b in zip(lista, lista[1:]):
            if a > b:
                pongo = lista.index(b) 
                quito = lista.index(a)
                lista.pop(quito)
                lista.insert(pongo, a)
                cambios += 1
    return lista
            
