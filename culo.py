# def elemento_desordenado(arr):


#     merge_sort(arr)
#     return 0



# def division_buscando_desordenado(arr):
#     largo = len(arr)

#     if largo == 2:
#         if arr[0]> arr[1]:
#             return arr[0]
#     elif largo <=1:
#         return
#     split_index = largo//2
#     izq = arr[:split_index]
#     der = arr[split_index:]
#     dividido_izq = division_buscando_desordenado(izq)
#     dividido_der = division_buscando_desordenado(der)
#     if dividido_der != -1:
#         return dividido_der
#     elif dividido_izq != -1:
#         return dividido_izq
#     return -1

# unsortedArr = [1,2,3,4,9,5,6]
# coso = division_buscando_desordenado(unsortedArr)
# print("coso:", coso)


# def busqueda_binaria(lista, item):
#     largo = len(lista)
#     min = 0
#     max =largo
#     posicion = None
    
#     while (min <= max and posicion == None):
#         medio = (min+max)//2
#         if lista[medio] == item:
#             posicion = medio
#         if lista[medio]<item:
#             min = medio +1
#         else:
#             max = medio -1
            
#     return posicion

# Returns index of x in arr if present, else -1
def binarySearch(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = low + (high - low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x)

    # Element is not present in the array
    else:
        return -1


def indice_primer_cero_recursivo(arr, min, max):
    if min > max:
        return -1
    
    if min == max:
        if arr[min] == 0:
            return min
        else:
            return -1

    medio = (min + max) // 2

    if arr[medio] == 0:
        # Buscar en la mitad izquierda
        return indice_primer_cero_recursivo(arr, min, medio - 1)
    else:
        # Buscar en la mitad derecha
        return indice_primer_cero_recursivo(arr, medio + 1, max)

def indice_primer_ceroo(arr):
    return indice_primer_cero_recursivo(arr, 0, len(arr) - 1)

def indice_primer_cero(arr):
    largo = len(arr)
    min = 0
    max =largo-1
    posicion = None
    
    while min <= max:
        medio = (min + max) // 2
        
        if arr[medio] == 0:
            # Verificar si es el primer cero
            if medio == 0 or arr[medio - 1] == 1:
                return medio
            else:
                max = medio - 1
        else:
            min = medio + 1
    return -1

def test_indice_primer_cero():
    # Test cases
    test_cases = [
        ([1, 1, 1, 0, 0, 0, 0, 0, 0], 3),  # Zero starts at index 3
        ([1, 1, 0, 0], 2),                 # Zero starts at index 2
        ([1, 1, 1, 1, 1], -1),             # No zeros
        ([0, 0, 0, 0], 0),                 # All zeros
        ([1, 1, 1, 1], -1),                # No zeros
        ([0, 1, 1, 1], 0),                 # Zero at the beginning
    ]
    
    for arr, expected in test_cases:
        result = indice_primer_cero(arr)
        assert result == expected, f"Failed for arr={arr}. Expected {expected}, but got {result}"
    
    print("All test cases passed!")

# Run the tests
#test_indice_primer_cero()


# def elemento_desordenado(arr):
#     if fuera_de_lugar(arr, 0):
#         return arr[0]
#     return elemento_desordenado_rec(arr, 0, len(arr)-1)

# def fuera_de_lugar(arr, pos):
#     if pos == 0:
#         return arr[0] > arr[1] and (len(arr) < 3 or arr[1] < arr[2]) ## [2 1 3]
#     if pos == len(arr)-1:
#         return arr[pos] < arr[pos-1] and (len(arr) < 3 or arr[pos-2] < arr[pos-1]) # [6 10 7]
#     return arr[pos-1] < arr[pos+1] and (arr[pos] > arr[pos+1] or arr[pos] < arr[pos-1]) #[6 11 10] o # [6 5 10]

# def elemento_desordenado_rec(arr, ini, fin):
#     medio = (ini+fin) // 2

#     if fin < ini:
#         return 0

#     if fuera_de_lugar(arr, medio):
#         return arr[medio]
    
#     izq = elemento_desordenado_rec(arr, ini, medio-1)
#     der = elemento_desordenado_rec(arr, medio+1, fin)

#     return izq + der


def posicion_pico(v, ini, fin):
    actual = (ini+fin) // 2
    if v[actual] > v[actual+1] and v[actual] > v[actual-1]:
        return actual

    if v[actual] > v[actual-1]:
        #lado ascendente
        return posicion_pico(v, actual, fin)
    elif v[actual] > v[actual+1]:
        #lado descendente
        return posicion_pico(v, ini, actual)
    return 0


def test_indice_picos():
    # Test cases
    test_cases = [
        ([1, 2, 3, 1, 0, -2], 2), 
    ]
    
    for arr, expected in test_cases:
        result = posicion_pico(arr, 0, len(arr)-1)
        assert result == expected, f"Failed for arr={arr}. Expected {expected}, but got {result}"
    
    print("All test cases passed!")

test_indice_picos()

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    split_index = len(arr) // 2
    izq = arr[:split_index]
    der = arr[split_index:]
    sorted_izq = merge_sort(izq)
    sorted_der = merge_sort(der)

    return merge(sorted_izq, sorted_der)

def merge(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:  # Change comparison to sort in descending order
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

unsortedArr = [1,5,8,119, 0, 3,6]
sortedArr = merge_sort(unsortedArr)
print("Sorted array:", sortedArr)

def max_subarray(arr):
    n = len(arr)
    if n == 1:
        return arr

    split_index = len(arr) // 2
    izq = arr[:split_index]
    der = arr[split_index:]

    max_izq = max_subarray(izq)
    max_der = max_subarray(der)
    max_cross = get_max_sub(arr, split_index)

    if sum(max_izq) >= sum(max_der) and sum(max_izq) >= sum(max_cross):
        return max_izq
    elif sum(max_der) >= sum(max_izq) and sum(max_der) >= sum(max_cross):
        return max_der
    else:
        return max_cross


def get_max_sub(arr, mid):
    left_sum = float("-inf")
    left_index = mid
    sum=0
    for i in range(mid, -1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum= sum
            left_index= i
    right_sum = float("-inf")
    right_index = mid
    sum = 0
    for i in range(mid-1, len(arr)):
        sum += arr[i]
        if sum > right_sum:
            right_sum= sum
            right_index= i
    return arr[left_index:right_index + 1]

def test_max_subarray():

    # Test cases
    test_cases = [
        ([5, 3, 2, 4, -1], [5, 3, 2, 4]), 
        ([5, 3, -5, 4, -1],  [5, 3]),
        ([5, -4, 2, 4, -1], [5, -4, 2, 4]),# left index 0 y el right index seria 3
        ([5, -4, 2, 4], [5, -4, 2, 4]),
        ([-3, 4, -1, 2, 1, -5], [4, -1, 2, 1])
    ]
    
    for arr, expected in test_cases:
        result = max_subarray(arr)
        assert result == expected, f"Failed for arr={arr}. Expected {expected}, but got {result}"
    
    print("All test cases passed!")




def charlas(horarios):
    horarios_ordenados = ordenar_por_horario_fin(horarios)
    charlas = []
    for horario in horarios_ordenados: 
        if len(charlas) == 0 or not hay_interseccion(charlas[-1], horario):
            charlas.append(horario)
    return charlas

def hay_interseccion(anterior, nueva):
    return anterior[1] >nueva[0]

def ordenar_por_horario_fin(horarios):
    return sorted(horarios, key=lambda x: x[1])
    
def test_horarios():

    # Test cases
    test_cases = [
        ([(5, 10), (12, 15)], [(5, 10), (12, 15)]), 
    ]
    
    for arr, expected in test_cases:
        result = charlas(arr)
        assert result == expected, f"Failed for arr={arr}. Expected {expected}, but got {result}"
    
    print("All test cases passed!")

# test_horarios()

def cambio(monedas, monto):
    monedas.sort(reverse=True)
    cambio = []
    for moneda in monedas:
        count = monto // moneda  # Determine how many times the coin can be used
        if count > 0:
            cambio.extend([moneda] * count)  # Add the coin 'count' times to the list
            monto -= moneda * count  # Subtract the total value of these coins from monto
    if monto == 0:
        return cambio
    else:
        return []
    
def test_cambio():

    # Test cases
    test_cases = [
        ([1, 2, 5], 11, [5, 5, 1]), 
    ]
    
    for monedas,monto , expected in test_cases:
        result = cambio(monedas, monto)
        assert result == expected, f"Failed for monedas={monedas} y  monto{monto}. Expected {expected}, but got {result}"
    
    print("All test cases passed!")

test_cambio()


def precios_inflacion(R):
    r_descendente = sorted(R, reverse=True)
    precio_minimo_total = 0
    j = 0
    for producto in r_descendente:
        precio_producto_con_inflacion = pow(producto, j+1) 
        precio_minimo_total+= precio_producto_con_inflacion
        j += 1
    return precio_minimo_total
precios_inflacion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


#Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación y los precios aumentan todo el tiempo. El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0). Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

def test_precios_inflacion():

    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 49863), 
    ]
    
    for arr, expected in test_cases:
        result = precios_inflacion(arr)
        assert result == expected, f"Failed for arr={arr}. Expected {expected}, but got {result}"
    
    print("All test cases passed!")

#test_precios_inflacion()


def bolsas(capacidad, productos):
    """teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los productos en la menor cantidad posible de bolsas."""
    productos.sort(reverse=False)
    print(productos)
    bolsas = []
    for producto in productos:
        if len(bolsas) == 0 or sum(bolsas[-1]) + producto > capacidad:
            bolsas.append([producto])
        else:
            bolsas[-1].append(producto)
    return bolsas

def test_bolsas():

    # Test cases
    test_cases = [
        (10, [5, 3, 7, 2, 8], [[2,3,5], [7], [8]]), 
    ]
    
    for capacidad, productos, expected in test_cases:
        result = bolsas(capacidad, productos)
        assert result == expected, f"Failed for capacidad={capacidad} y productos{productos}. Expected {expected}, but got {result}"
    
    print("All test cases passed!")


def asignar_mafias(pedidos):
    pedidos.sort(key=lambda x: x[1])
    mafias = []
    for pedido in pedidos:
        if len(mafias)== 0 or not hay_superposicion(mafias[-1], pedido):
            mafias.append(pedido)
    return mafias

def hay_superposicion(tupla1, tupla2):
    return tupla1[1] > tupla2[0]

def test_asignar_mafias():
    test_cases=[
        ([(2, 15), (3, 7), (1, 11), (6, 9), (10, 13), (5, 8), (12, 25), (17, 22), (16, 18), (14, 15), (14, 20)], [(2, 15), (16, 18), (17, 22)]),
    ]
    for pedidos, expected in test_cases:
        result = asignar_mafias(pedidos)
        assert result == expected, f"Failed for pedidos={pedidos}. Expected {expected}, but got {result}"


# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    elementos.sort(key=lambda x: (x[0] / x[1], x[0]), reverse=True)
    print(elementos)
    mochila = []
    peso_actual = 0
    for elemento in elementos:
        if peso_actual + elemento[1] <= W:
            mochila.append(elemento)
            peso_actual += elemento[1]
    return mochila
    
#ME GUARDO LOS ELEMENTOS CON MEJOR RELACION PESO VALOR
def test_mochila():
    test_cases=[
    
        ([(1, 5), (5, 4)], 5, [(5, 4)]),
    ]
    for elementos, capacidad, expected in test_cases:
        result = mochila(elementos, capacidad)
        assert result == expected, f"Failed for pedidos={elementos} y capacidad={capacidad}. Expected {expected}, but got {result}"
test_mochila()





def es_compatible(grafo, puestos):
    for v in puestos:
        for w in puestos:
            if v == w:
                continue
            if grafo.estan_unidos(v, w):
                return False
    return True

def _ubicacion_BT(grafo, vertices, v_actual, puestos, n):
    if len(puestos) == n:
        return es_compatible(grafo, puestos)
    if v_actual == len(vertices):
        return False

    # Mis opciones son poner acá, o no
    puestos.append(vertices[v_actual])
    if _ubicacion_BT(grafo, vertices, v_actual + 1, puestos, n):
        return True
    puestos.remove(vertices[v_actual])
    return _ubicacion_BT(grafo, vertices, v_actual + 1, puestos, n)

def no_adyacentes(grafo, n):
    vertices = grafo.obtener_vertices()
    puestos = []
    if _ubicacion_BT(grafo, vertices, 0, puestos, n):
        return puestos
    return None





def colorear(grafo, n):
    vertices = grafo.obtener_vertices()
    colores = {v: 0 for v in vertices}
    return colorear_backtracking(grafo, vertices, 0, n, colores)

def colorear_backtracking(grafo, vertices, v, n, colores):
    if v == len(vertices):
        return True
    for color in range(1, n + 1):
        if es_valido(grafo, vertices[v], color, colores):
            colores[vertices[v]] = color
            if colorear_backtracking(grafo, vertices, v + 1, n, colores):
                return True
            colores[vertices[v]] = 0
    return False

def es_valido(grafo, vertice, color, colores):
    for vecino in grafo.adyacentes(vertice):
        if colores[vecino] == color:
            return False
    return True



def independent_set(grafo):
    max_independent_set = []
    vertices = grafo.obtener_vertices()
    indep_set_bt(grafo, vertices, 0, [], max_independent_set)
    print(max_independent_set)
    return max_independent_set

def indep_set_bt(grafo, vertices, vertice_actual, current_set, max_independent_set):
    if vertice_actual == len(vertices):
        if es_indep(grafo, current_set) and len(current_set) > len(max_independent_set):
            max_independent_set.clear()
            max_independent_set.extend(current_set)
        return

    # No incluir el vértice actual
    indep_set_bt(grafo, vertices, vertice_actual + 1, current_set, max_independent_set)

    # Incluir el vértice actual
    current_set.append(vertices[vertice_actual])
    indep_set_bt(grafo, vertices, vertice_actual + 1, current_set, max_independent_set)
    current_set.pop()

def es_indep(grafo, puestos):
    for v in puestos:
        for w in puestos:
            if v != w and grafo.estan_unidos(v, w):
                return False
    return True

def sumatoria_dados(n, s):
    resultados = []
    combinacion_actual = []
    backtrack(n, s, combinacion_actual, resultados)
    return resultados

def backtrack(n, s, combinacion_actual, resultados):
    if n == 0 and s == 0:
        resultados.append(combinacion_actual[:])
        return
    if n == 0 or s < 0:
        return
    for i in range(1, 7):
        combinacion_actual.append(i)
        backtrack(n - 1, s - i, combinacion_actual, resultados)
        combinacion_actual.pop()
    
def test_sumatoria_dados():
    test_cases = [
        (2, 7, [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]),
        (2, 11, [[5, 6], [6, 5]]),
        (2, 2, [[1, 1]]),
        (2, 12, [[6, 6]]),
    ]
        
    for n, s, expected in test_cases:
        result = sumatoria_dados(n, s)
        assert result == expected, f"Failed for n={n} y s={s}. Expected {expected}, but got {result}"
    print("All test cases passed!")

test_sumatoria_dados()



def vertex_cover_min(grafo):
    aristas = obtener_aristas(grafo)
    best_vertex_cover = []
    current_vertex_cover = []
    backtracking(grafo, aristas, 0, current_vertex_cover, best_vertex_cover)
    return best_vertex_cover

def obtener_aristas(grafo):
    aristas = []
    for v in grafo.obtener_vertices():
        for u in grafo.adyacentes(v):
            if (u, v) not in aristas and (v, u) not in aristas:
                aristas.append((v, u))
    return aristas

def backtracking(grafo, aristas, indice, current_vertex_cover, best_vertex_cover):
    if all(esta_cubierta(u, v, current_vertex_cover) for u, v in aristas):
        if len(best_vertex_cover) == 0 or len(current_vertex_cover) < len(best_vertex_cover):
            best_vertex_cover.clear()
            best_vertex_cover.extend(current_vertex_cover)
        return

    if indice == len(aristas):
        return

    u, v = aristas[indice]

    # Opción 1: incluimos el vértice u en el Vertex Cover
    if u not in current_vertex_cover:
        current_vertex_cover.append(u)
        backtracking(grafo, aristas, indice + 1, current_vertex_cover, best_vertex_cover)
        current_vertex_cover.pop()  # Retrocedemos
    else:
        backtracking(grafo, aristas, indice + 1, current_vertex_cover, best_vertex_cover)

    # Opción 2: incluimos el vértice v en el Vertex Cover
    if v not in current_vertex_cover:
        current_vertex_cover.append(v)
        backtracking(grafo, aristas, indice + 1, current_vertex_cover, best_vertex_cover)
        current_vertex_cover.pop()  # Retrocedemos
    else:
        backtracking(grafo, aristas, indice + 1, current_vertex_cover, best_vertex_cover)
   
def esta_cubierta(u, v, current_vertex_cover):
    return u in current_vertex_cover or v in current_vertex_cover


def dominating_set_min(grafo):
    best_dom_set = []
    current_dom_set = []
    vertices = grafo.obtener_vertices()
    dom_set_min_backtracking(grafo, 0, current_dom_set, best_dom_set, vertices)
    return best_dom_set


def dom_set_min_backtracking(grafo, indice, current_dom_set, best_dom_set, vertices):
    if es_dominating_set(grafo, current_dom_set):
        if len(best_dom_set) == 0 or len(current_dom_set) < len(best_dom_set):
            best_dom_set.clear()
            best_dom_set.extend(current_dom_set)
        return
    
    if indice == len(vertices):
        return
    
    # Opción 1: incluir el vértice actual en el Dominating Set
    current_dom_set.append(vertices[indice])
    dom_set_min_backtracking(grafo, indice + 1, current_dom_set, best_dom_set, vertices)
    current_dom_set.pop()

    # Opción 2: no incluir el vértice actual en el Dominating Set
    dom_set_min_backtracking(grafo, indice + 1, current_dom_set, best_dom_set, vertices)

def es_dominating_set(grafo, vertices):
    for v in grafo.obtener_vertices():
        if v not in vertices and not any(u in vertices for u in grafo.adyacentes(v)):
            return False
    return True




def fibonacci(n):
   if n == 0:
       return 0
   if n == 1:
       return 1
   anterior = 0
   actual = 1
   for i in range(2, n+1):
       nuevo = actual + anterior
       anterior = actual
       actual = nuevo
   return actual

def test_fibonacci():
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
    ]
    for n, expected in test_cases:
        result = fibonacci(n)
        assert result == expected, f"Failed for n={n}. Expected {expected}, but got {result}"
    print("All test cases passed!")

test_fibonacci()

def juan_el_vago(trabajos):
    memorioso = [0] * len(trabajos)
    for i in range(len(trabajos)):
        if i == 0:
            memorioso[i] = trabajos[i]
        elif i == 1:
            memorioso[i] = max(trabajos[i], memorioso[i-1])
        else:
            memorioso[i] = max(trabajos[i] + memorioso[i-2], memorioso[i-1])
    return construir_elecciones(trabajos, memorioso)
    
def construir_elecciones(G, M):
    elecciones = []
    d = len(G) - 1
    while d >= 0:
        if d == 0:
            elecciones.append(d)
            break
        if d == 1:
            if G[d] > G[d-1]:
                elecciones.append(d)
            else:
                elecciones.append(d-1)
            break
        if M[d] == G[d] + M[d-2]:
            elecciones.append(d)
            d -= 2
        else:
            d -= 1
    elecciones.reverse()
    return elecciones

#Para: [100, 5, 50, 1, 1, 200]
#Devolver: [0, 2, 5]

def test_juan_el_vago():
    test_cases = [
        ([100, 5, 50, 1, 1, 200], [0, 2, 5]),
    ]
    for trabajos, expected in test_cases:
        result = juan_el_vago(trabajos)
        assert result == expected, f"Failed for trabajos={trabajos}. Expected {expected}, but got {result}"
    print("All test cases passed!")

test_juan_el_vago()

def calcular_min_op(k):
    dp = [0] * (k + 1)  # Inicializa dp para almacenar el número mínimo de operaciones
    for i in range(1, k + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i // 2], dp[i - 1]) + 1
        else:
            dp[i] = dp[i - 1] + 1
    return dp

def reconstruir_ops(k, dp):
    ops = []
    while k > 0:
        if k % 2 == 0 and dp[k] == dp[k // 2] + 1:
            ops.append("por2")
            k //= 2
        else:
            ops.append("mas1")
            k -= 1
    ops.reverse()  # Invertir para tener el orden correcto
    return ops

def operaciones(k):
    if k == 0:
        return []
    
    dp = calcular_min_op(k)  # Llama a la función para calcular el mínimo de operaciones
    ops = reconstruir_ops(k, dp)  # Llama a la función para reconstruir las operaciones
    return ops

    
def test_operaciones():
    test_cases = [
        (0, []),
        (1,["mas1"]),
        (2, ["mas1", "por2"]),
        (3, ["mas1", "por2", "mas1"]),
        (4, ["mas1", "por2", "por2"]),
    ]
    for k, expected in test_cases:
        result = operaciones(k)
        assert result == expected, f"Failed for k={k}. Expected {expected}, but got {result}"
    
    print("All test cases passed!")

test_operaciones()


# def carlitos(c_publicitaria, P):
#     memorioso = [0]*len(c_publicitaria)
#     for i in range(len(c_publicitaria)):
#         if i == 0:
#             memorioso[i]=c_publicitaria[i]
#         elif i == 1:
#             memorioso[i] = max(c_publicitaria[i], memorioso[i-1])
#         else:
#             memorioso[i] = max( c_publicitaria[i]+)

# def carlitos_publicidad(P, campañas):
#     # campañas es una lista de tuplas (Ci, Gi) donde Ci es el costo y Gi es la ganancia.
#     n = len(campañas)
#     dp = [[0] * (P + 1) for _ in range(n + 1)]

#     # Llenar la tabla dp
#     for i in range(1, n + 1):
#         Ci, Gi = campañas[i - 1]  # Costo y ganancia de la campaña i-1
#         for p in range(P + 1):
#             if p >= Ci:
#                 dp[i][p] = max(dp[i - 1][p], dp[i - 1][p - Ci] + Gi)
#             else:
#                 dp[i][p] = dp[i - 1][p]

#     # Reconstruir las campañas elegidas
#     campañas_elegidas = []
#     p = P
#     for i in range(n, 0, -1):
#         Ci, Gi = campañas[i - 1]
#         # Si la ganancia actual es distinta a la ganancia sin esta campaña, significa que se eligió
#         if dp[i][p] != dp[i - 1][p]:
#             campañas_elegidas.append(campanias[i - 1])  # Guardar el índice de la campaña elegida
#             p -= Ci  # Reducir el presupuesto disponible

#     # Invertir las campañas elegidas para que estén en el orden correcto
#     campañas_elegidas.reverse()

#     # Retornar la ganancia máxima y las campañas elegidas
#     return  campañas_elegidas



def lunatico(ganancias):
    n = len(ganancias)
    if n == 1:
        return [0]
    
    # Obtener las posiciones pares e impares
    even_positions = list(range(0, n, 2))
    odd_positions = list(range(1, n, 2))
    
    even_sum = sum(ganancias[i] for i in even_positions)
    odd_sum = sum(ganancias[i] for i in odd_positions)
    
    # Comparar entre incluir la posición 0 o la última posición en los casos pares
    if n > 1 and even_sum >= odd_sum and n%2==0:
        return even_positions
    elif n > 1 and even_sum >= odd_sum:
        # Caso 1: Incluir la posición 0 y excluir la última posición
        even_sum_case1 = even_sum - ganancias[-1]
        # Caso 2: Excluir la posición 0 y incluir la última posición
        even_sum_case2 = even_sum - ganancias[0] + ganancias[-1]
        
        if even_sum_case1 >= even_sum_case2:
            return even_positions[:-1]  # Excluir la última posición
        else:
            return even_positions[1:] + [n-1]  # Excluir la primera posición e incluir la última
    else:
        return odd_positions

# Ejemplo de uso
print(lunatico([10, 20, 30, 40, 50]))  # Ejemplo de salida
    
# def test_lunatico():
#     test_cases = [
#         ([10], [0]),
#         ([20, 15], [0]),
#         ([10, 15], [1]),
#         ([100, 150, 100], [0, 2]),
#     ]
 
#     for ganancias, expected in test_cases:
#         result = lunatico(ganancias)
#         assert result == expected, f"Failed for ganancias={ganancias}. Expected {expected}, but got {result}"
#     print("All test cases passed!")

# test_lunatico()


#W = lugares  P[i])= cantidad de personas que integran el grupo i 
def bodegon_dinamico(P, W):
    n = len(P)
    # Crear una tabla dp con (n+1) filas y (W+1) columnas
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Llenar la tabla de programación dinámica
    for i in range(1, n + 1):
        valor = P[i - 1]
        peso = valor
        for w in range(1, W + 1):
            if peso <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - peso] + valor)
            else:
                dp[i][w] = dp[i - 1][w]

    # Encontrar los elementos seleccionados
    resultado = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            resultado.append(P[i - 1])
            w -= P[i - 1]

    # Invertir la lista para que los elementos queden en el orden correcto
    return resultado[::-1]


def test_bodegon_dinamico():
    test_cases = [([6], 7, 0)]
    for P, W, expected in test_cases:
        result = bodegon_dinamico(P, W)
        assert result == expected, f"Failed for P={P} y W={W}. Expected {expected}, but got {result}"

    print("All test cases passed!")

test_bodegon_dinamico()