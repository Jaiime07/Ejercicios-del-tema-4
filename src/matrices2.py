def multiplica_matrices(m1: list[list[int | float]], m2: list[list[int | float]]) -> list[list[int | float]]:
    """
    Multiplica dos matrices y devuelve el resultado.

    Parámetros:
    m1 (list[list[int | float]]): Primera matriz.
    m2 (list[list[int | float]]): Segunda matriz.

    Devuelve:
    list[list[int | float]]: Matriz resultante de la multiplicación.
    """
    



    
    
    


def suma_matrices(m1: list[list[int | float]], m2: list[list[int | float]]) -> list[list[int | float]]:
    """
    Suma dos matrices y devuelve el resultado.

    Parámetros:
    m1 (list[list[int | float]]): Primera matriz.
    m2 (list[list[int | float]]): Segunda matriz.

    Devuelve:
    list[list[int | float]]: Matriz resultante de la suma.
    """
    filas1, col1 = len(m1), len(m1[0])
    filas2, col2  = len(m2), len(m2[0])
    res = []
   
    #comprobar que tengan las mismas filas
    if filas1 != filas2:
        return 
    #comprobar que cada fila tenga el mismo num de elementos
    for f1, f2 in zip(m1, m2):
        if len(f1) != col1 or len(f2) != col1:
            return

    for f1, f2 in zip(m1, m2):
        fila_nueva = []

        for elem1, elem2 in zip(f1, f2):
            fila_nueva.append(elem1 + elem2) 
        res.append(fila_nueva)
            
    return res