def f5_apendiza_valor(lista,valor):
    lista.append(valor)
    print(lista)
    return lista


def f5_funcion_division(l1,v1,l2,v2):
    division = l1[v1]/l2[v2]
    resto = l1[v1]%l2[v2]
    print(f'la division es {division}')
    print(f'el resto es {resto}')

def ejercicio_2():
    v1 = input ('Introduce el valor a asignar a la varible S ')
    v2 = input ('Introduce el valor a asignar a la varible Y ')
    return (v1,v2)
