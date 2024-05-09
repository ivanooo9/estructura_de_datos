def bubble_sort(arr):
    # Obtenemos la longitud del arreglo

    n = len(arr)

    # Bucle externo que representa cada "pase" completo a través del arreglo
    for i in range(n):

        # Bucle interno que compara cada par de elementos adyacentes
        # Solo necesitamos comparar hasta n-i-1, ya que los elementos

        for j in range(0, n-i-1):
            # Si el elemento en la posición j es mayor que el elemento
            # en j+1, los intercambiamos
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


array = [64, 34, 25, 12, 22, 11, 90]
# Llamamos a la función bubble_sort para ordenar el arreglo
bubble_sort(array)
# Imprimimos el arreglo
print("Arreglo ordenado:", array)
