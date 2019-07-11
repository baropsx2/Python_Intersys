'''
Crear una función que se llame cadenas, la función va a recibir una lista y debe devolver una lista con las cadenas
que contenga la lista original.
Ejemplo:
cadenas([1, 2, 3, “hola”, 0, “mundo”]) ---> [“hola”, “mundo”]
cadenas([1, 2]) ---> []
cadenas([“hola”, 23, 56, “frfr”]) ---> [“hola”, “frfr”]
'''



def cadenas(lista):
    lista_almacen = []
    for x in lista:
        if x == type([]):
            lista_almacen.insert(lista_almacen)
        return lista_almacen



# cadenas([1, 2, 3, “hola”, 0, “mundo”])