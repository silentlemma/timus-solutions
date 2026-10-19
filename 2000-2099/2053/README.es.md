# 2053. Generar un grafo plano con más de trescientos mil ciclos

[Timus 2053](https://acm.timus.ru/problem.aspx?space=1&num=2053) · difficulty 3448 · constructive

Problema original de Alexander Ipatov, del Campeonato de Programación Deportiva de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dibujar un grafo plano con dieciséis vértices en puntos enteros
distintos y aristas rectas que solo se tocan en extremos comunes y no
pasan por otros vértices, de modo que tenga más de 300 000 ciclos
simples. Un ciclo cuenta una vez, sin importar el vértice inicial ni el
sentido. Los límites son 1 segundo y 64 MB.

## Entrada

No hay entrada.

## Salida

Dieciséis líneas con las coordenadas de los vértices, cada una en
[−1000, 1000], y después la matriz de adyacencia 16 × 16 como filas de 0
y 1, simétrica y con diagonal nula.

## Evaluación

Un comprobador verifica los puntos, la matriz y la geometría de las
aristas y cuenta exactamente los ciclos simples; se acepta cualquier
grafo válido. El ejemplo del problema original solo muestra el formato y
no es una respuesta correcta, así que su salida guardada se marca como
`format_only` y no se comprueba.

## Ejemplos

Este ejemplo solo muestra el formato: sus seis vértices dan apenas 21
ciclos, así que no es una respuesta correcta.

```

```

```
0 0
5 -6
-5 -6
-9 3
0 8
9 3
011111
101001
110100
101010
100101
110010
```

La ilustración es un borde de cinco vértices unido a un centro. Sus
triángulos y ciclos mayores suman 21 y no cumplen ni tamaño ni cantidad.
Nuestra construcción tiene 16 vértices, 42 aristas y exactamente 301843
ciclos.

## Solución

### Construir el grafo mediante reglas

Numeramos desde cero como `v=4r+c` en una cuadrícula conceptual de
cuatro por cuatro. Añadimos todos los vecinos horizontales y verticales,
24 aristas, y la diagonal de arriba izquierda a abajo derecha de cada
celda, nueve más. La cuadrícula nombra vértices, no sus coordenadas
finales.

Los lados tienen secuencias `(0,1,2,3)`, `(3,7,11,15)`, `(15,14,13,12)`
y `(12,8,4,0)`. Para cada lado `(a,b,c,d)` añadimos `a-d` y `a-c`;
finalmente `3-12`. Todas son distintas y quedan 42 aristas. El triángulo
exterior usa los vértices cero, tres y doce. Los programas generan estas
reglas con bucles, sin guardar una matriz respuesta.

### Calcular coordenadas enteras

Fijamos cero en `(-900,-900)`, tres en `(900,-900)` y doce en `(0,900)`.
Cada vértice restante debe ser el promedio de sus vecinos. Para cada
coordenada, las trece incógnitas satisfacen `degree(v)·p_v -
sum_{vecinos internos u} p_u = sum_{vecinos fijos u} p_u`. Construimos
una matriz aumentada de trece filas con dos términos independientes y la
resolvemos por eliminación gaussiana con selección de pivote.
Redondeamos con `floor(value+0.5)`.

El sistema no es singular. Extendemos por cero a la frontera un vector
de los vértices internos. Su forma cuadrática suma `(x_u-x_v)²` en
aristas internas y `x_v²` en aristas hacia la frontera fija. Si se
anula, todos los valores vecinos son iguales y los fronterizos cero; la
conectividad fuerza el vector nulo. La matriz es definida positiva.
Además, cada coordenada exacta queda entre los extremos fronterizos: un
máximo interno estricto no puede ser un promedio y una meseta máxima se
propaga hasta la frontera.

Redondear un dibujo armónico arbitrario no es automáticamente seguro.
Aquí el grafo es fijo y se verifica exactamente su dibujo entero real.
La eliminación racional produce los dieciséis puntos del certificado
ejecutable siguiente. Cada coordenada racional está al menos a
`513/46262` de una frontera semientera de redondeo; la doble precisión
tiene margen en este sistema pequeño. Los cinco programas producen este
certificado entero. Pruebas exactas de orientación y pertenencia a
segmentos confirman puntos distintos, límites, ausencia de puntos en
aristas ajenas e intersecciones prohibidas. Tampoco hay triples
colineales entre estos puntos.

### Demostrar el número de ciclos

`DP[M][v]` cuenta caminos que visitan exactamente `M`, terminan en `v` y
comienzan en el menor vértice de `M`. Inicializamos `DP[{v}][v]=1`.
Extendemos hacia un vecino no visitado mayor que el inicio, manteniendo
ese mínimo. Todo camino simple aparece una vez: se elimina su última
arista y se aplica inducción en la longitud.

Para al menos tres vértices, el camino se cierra en un ciclo simple
exactamente cuando el extremo es adyacente al inicio. Sumamos dichos
estados. Cada ciclo no dirigido aparece dos veces por los dos sentidos;
el inicio mínimo ya elimina las rotaciones, así que dividimos por dos.
La incrustación rectilínea verificada no tiene cruces o contactos de
vértices prohibidos; por eso estos ciclos son precisamente polígonos
válidos.

Las cantidades para longitudes de tres a dieciséis son
`28,46,116,365,1140,3174,7922,17578,33714,53732,67908,63842,39852,12426`.
Su suma exacta es `301843>300000`. La verificación finita completa
siguiente genera el grafo y comprueba geometría y todas las longitudes.
Es un verificador del certificado, no el programa enviado: el generador
calcula sus coordenadas mediante el sistema lineal.

```python
from array import array

GRID = 4
COORDINATE_BOUND = 1000
MIN_CYCLE_LENGTH = 3
points = [(-900, -900), (-275, -647), (12, -731), (900, -900),
          (-258, -48), (-239, -415), (27, -541), (310, -669),
          (-77, 241), (-74, -67), (49, -285), (301, -502),
          (0, 900), (25, 178), (56, -72), (222, -114)]
adjacency = [0] * (GRID * GRID)

def link(a, b):
    adjacency[a] |= 1 << b
    adjacency[b] |= 1 << a

for r in range(GRID):
    for c in range(GRID):
        v = GRID * r + c
        if c + 1 < GRID:
            link(v, v + 1)
        if r + 1 < GRID:
            link(v, v + GRID)
        if r + 1 < GRID and c + 1 < GRID:
            link(v, v + GRID + 1)
corners = [0, GRID - 1, GRID * GRID - 1, GRID * GRID - GRID]
for side, a in enumerate(corners):
    d = corners[(side + 1) % GRID]
    step = (d - a) // (GRID - 1)
    link(a, d)
    link(a, d - step)
link(corners[1], corners[-1])

def orientation(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def on_segment(a, b, p):
    return orientation(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and (min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))

def geometric(points, adjacency):
    size = len(points)
    if len(set(points)) != size or any((abs(x) > COORDINATE_BOUND for p in points for x in p)):
        return False
    edges = [(a, b) for a in range(size) for b in range(a + 1, size) if adjacency[a] & 1 << b]
    for a, b in edges:
        if any((v not in (a, b) and on_segment(points[a], points[b], p) for v, p in enumerate(points))):
            return False
    for index, (a, b) in enumerate(edges):
        for c, d in edges[index + 1:]:
            if len({a, b, c, d}) < 4:
                continue
            pa, pb, pc, pd = (points[a], points[b], points[c], points[d])
            x, y = (orientation(pa, pb, pc), orientation(pa, pb, pd))
            z, w = (orientation(pc, pd, pa), orientation(pc, pd, pb))
            if x * y < 0 and z * w < 0:
                return False
            if on_segment(pa, pb, pc) or on_segment(pa, pb, pd):
                return False
            if on_segment(pc, pd, pa) or on_segment(pc, pd, pb):
                return False
    return True

def cycle_histogram(adjacency):
    size = len(adjacency)
    full = (1 << size) - 1
    paths = array('Q', [0]) * ((1 << size) * size)
    for vertex in range(size):
        paths[(1 << vertex) * size + vertex] = 1
    totals = [0] * (size + 1)
    for mask in range(1, 1 << size):
        anchor = mask & -mask
        allowed = full ^ (anchor << 1) - 1
        length = mask.bit_count()
        endpoints = mask
        while endpoints:
            bit = endpoints & -endpoints
            endpoints ^= bit
            last = bit.bit_length() - 1
            value = paths[mask * size + last]
            if not value:
                continue
            if length >= MIN_CYCLE_LENGTH and adjacency[last] & anchor:
                totals[length] += value
            choices = adjacency[last] & ~mask & allowed
            while choices:
                new_bit = choices & -choices
                choices ^= new_bit
                end = new_bit.bit_length() - 1
                paths[(mask | new_bit) * size + end] += value
    return [value // 2 for value in totals]

assert geometric(points, adjacency)
histogram = cycle_histogram(adjacency)
assert histogram[3:] == [28, 46, 116, 365, 1140, 3174, 7922,
                        17578, 33714, 53732, 67908, 63842, 39852, 12426]
assert sum(histogram) == 301843 > 300000
```

Todas las aserciones se cumplen. Un DFS literal independiente de caminos
simples obtiene el mismo histograma; no es una inferencia a partir de
pruebas aleatorias ni solo de caras.

No se puede enviar la ilustración de seis vértices. No basta contar
triángulos, caras o ciclos hamiltonianos. La desigualdad es estricta.
Una matriz simétrica no garantiza una incrustación rectilínea válida:
comprobar puntos en aristas, cruces no incidentes y solapamientos
colineales. La cuadrícula solo nombra vértices; sus coordenadas antiguas
con la arista final producirían cruces. Mantener los tres puntos
exteriores y usar `floor(x+0.5)` también en coordenadas negativas.
Contar una sola vez cada ciclo salvo rotación e inversión.

## Notas por lenguaje

Los programas enviados generan el grafo y resuelven un sistema de tamaño
`V-3`, en `O(V^3)` tiempo y `O(V^2)` espacio, con `V=16` fijo. No
cuentan ciclos durante su ejecución. El verificador separado requiere
`O(V^2·2^V)` tiempo y `O(V·2^V)` espacio; su tabla ocupa ocho MiB para
dieciséis vértices.

Todos usan eliminación de doble precisión y salida entera. Java y Rust usan arrays numéricos primitivos,
C++ y Go arrays fijos del grafo. No hay lector de entrada ni tabla de
coordenadas respuesta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2053_constructive.cpp](2053_constructive.cpp) | G++ 13.2 x64 | constructive | O(V^3) | AC | 0.001 s | 356 KB |
| [2053_constructive.go](2053_constructive.go) | Go 1.14 x64 | constructive | O(V^3) | AC | 0.001 s | 1024 KB |
| [2053_constructive.java](2053_constructive.java) | Java 1.8 | constructive | O(V^3) | AC | 0.015 s | 368 KB |
| [2053_constructive.py](2053_constructive.py) | Python 3.12 x64 | constructive | O(V^3) | AC | 0.062 s | 668 KB |
| [2053_constructive.rs](2053_constructive.rs) | Rust 1.75 x64 | constructive | O(V^3) | AC | 0.001 s | 204 KB |
