def selection_sort(arr):
    # Longitud del arreglo

    n = len(arr)

    # Iteramos sobre todo el arreglo
    for i in range(n):

        # Encontramos el índice del mínimo elemento en el subarreglo no ordenado
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Intercambiamos el mínimo elemento encontrado con el primer elemento del subarreglo no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Ejemplo de uso
array = [64, 34, 25, 12, 22, 11, 90]

# Llamamos a la función selection_sort para ordenar el arreglo
selection_sort(array)

# Imprimimos el arreglo ordenado
print("Arreglo ordenado:", array)
