def suma_matrices(m1: list[list[int | float]], m2: list[list[int | float]]) -> list[list[int | float]]:
    """
    Suma dos matrices y devuelve el resultado.

    Parámetros:
    m1 (list[list[int | float]]): Primera matriz.
    m2 (list[list[int | float]]): Segunda matriz.

    Devuelve:
    list[list[int | float]]: Matriz resultante de la suma.
    """
    filas = len(m1)
    columnas = len(m1[0])

    if len(m2) != filas: #si m2 no tiene el mismo nº de listas (filas) que m1
        return
    
    for a, b in zip(m1, m2): #para cada elemento de la fila 
        if len(a) != columnas or len(b) != columnas: #comprobar que tengan mismo nº de columnas
            return 
    res = []
    for a, b in zip(m1, m2): #vamos lista a lista en paralelo
        fila_nueva = []         
        for uno, otro in zip(a, b):    #a la lista res le vamos a añadir cada iteración del bucle una lista
            suma = uno + otro           # nueva lista_nueva con la suma de cada índice de dicha fila
            fila_nueva.append(suma)
        res.append(fila_nueva)
    return res





   
    

        


   

def multiplica_matrices(m1: list[list[int | float]], m2: list[list[int | float]]) -> list[list[int | float]]:
    """
    Multiplica dos matrices y devuelve el resultado.

    Parámetros:
    m1 (list[list[int | float]]): Primera matriz.
    m2 (list[list[int | float]]): Segunda matriz.

    Devuelve:
    list[list[int | float]]: Matriz resultante de la multiplicación.
    """
    elementos, columnasm1 = len(m1[0]) #elementos = columnas
    filasm1 = len(m1)
    filasm2 = len(m2)
    columnasm2 = len(m2[0])
    for fila1, fila2 in zip(m1, m2):
        if len(fila1) != elementos or len(fila2) != elementos:
            return 
    if columnasm1 != filasm2:
        return  #comprobaciones requeridas ya implementadas 
    
    filas = filasm1
    columnas = columnasm2

    #implementar el cálculo


