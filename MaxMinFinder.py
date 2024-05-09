def encontrar_max_min(arreglo):
    # Manejar el caso de un arreglo vacío
    if len(arreglo) == 0:
        return None, None

    # Inicializar maximo y minimo con el primer elemento del arreglo
    maximo = arreglo[0]
    minimo = arreglo[0]

    # Iterar sobre el resto del arreglo para encontrar el maximo y el minimo
    for num in arreglo[1:]:
        if num > maximo:
            maximo = num
        elif num < minimo:
            minimo = num

    return maximo, minimo


# Ejemplo de uso
entrada = [3, 1, 9, 7, 5, 9]
maximo, minimo = encontrar_max_min(entrada)
print("Max =", maximo, ", Min =", minimo)
