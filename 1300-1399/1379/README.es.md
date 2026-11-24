# 1379. Transporte de tazas

[Timus 1379](https://acm.timus.ru/problem.aspx?space=1&num=1379) · dificultad 581 · graphs

Problema original de Pavel Egorov, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un camión de 3000 kg debe llevar tantas tazas como pueda, de 100 g cada
una y no más de los 10 000 000 encargadas, del cruce 1 al cruce N,
N ≤ 500, en 24 horas. Cada carretera de doble sentido tiene un tiempo de
recorrido en minutos y un peso máximo permitido del camión en gramos.
Hay que imprimir el mayor número de tazas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, luego M líneas: los extremos de una carretera, su tiempo y su
límite de peso.

## Salida

El número de tazas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
1 2 10 3000220
2 3 20 3000201
1 3 1 3000099
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
1 0
```

Salida:

```
10000000
```

## Solución

Un camión más pesado puede usar menos carreteras, así que llegar a
tiempo solo empeora al crecer la carga. El peso máximo de una ruta es el
límite de alguna de sus carreteras, así que se hace una búsqueda binaria
entre los límites de carretera de al menos 3 000 000 g. Para
cada uno, el algoritmo de Dijkstra usa solo las carreteras que aguantan
ese peso y nunca guarda tiempos de más de 1440 minutos. Con el mayor
peso W que llega a tiempo, la respuesta es
min(10 000 000, ⌊(W − 3 000 000) / 100⌋). `O((N + M log M) · log M)`.

Detalles a tener en cuenta:

- con N = 1 las tazas ya están en la sede: las 10 000 000 (ejemplo 2);
- exactamente 24 horas, 1440 minutos, aún es a tiempo (prueba 03);
- el camino más rápido puede aguantar menos que uno más lento
  (prueba 05);
- una carretera que aguanta justo el camión vacío no permite ninguna
  taza (prueba 06);
- hay carreteras que no llevan tiempo (prueba 07).

Las respuestas se compararon con probar todos los caminos simples en
400 grafos aleatorios de hasta 6 cruces.

## Soluciones optimizadas

La versión C++ optimizada busca por bisección entre cargas distintas expresadas en tazas
enteras. Para cada carga, Dijkstra usa un cubo por minuto de 0 a 1440. Si mejora la llegada
a un cruce, se mueve su entrada al cubo anterior que corresponda. Una carretera de duración
cero puede añadir cruces al cubo actual, que se procesa hasta quedar vacío. Cada búsqueda
tarda O(N + M + D), con D = 1440, y usa O(N + M + D) de espacio. El envío 11316958 tardó
0,031 s y usó 3464 KB frente a 0,281 s y 7564 KB de la base.

## Notas por lenguaje

- Python necesita PyPy: una cadena de carreteras cortas dentro de un
  grafo completo de carreteras de un día obliga a las búsquedas a
  recorrer muchas carreteras, unos 0,5 s con CPython y 0,25 s con
  PyPy.
- Java guarda su montículo en un arreglo de long simples, con el tiempo
  y el vértice empaquetados en un número: una cola de prioridad de
  arreglos pequeños excedía el límite de tiempo en la prueba 46 del juez.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322140 · Go 1.14 x64 №11322141 · Java 1.8 №11322142 · Rust 1.75 x64 №11322143 · PyPy 3.10 x64 №11322144.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1379_graphs.cpp](1379_graphs.cpp) | G++ 13.2 x64 | graphs | O((N + M log M) · log M) | AC | 0.281 s | 7564 KB | 11322140 |
| [1379_graphs.go](1379_graphs.go) | Go 1.14 x64 | graphs | O((N + M log M) · log M) | AC | 0.562 s | 24828 KB | 11322141 |
| [1379_graphs.java](1379_graphs.java) | Java 1.8 | graphs | O((N + M log M) · log M) | AC | 0.5 s | 11552 KB | 11322142 |
| [1379_graphs.py](1379_graphs.py) | PyPy 3.10 x64 | graphs | O((N + M log M) · log M) | AC | 0.453 s | 58612 KB | 11322144 |
| [1379_graphs.rs](1379_graphs.rs) | Rust 1.75 x64 | graphs | O((N + M log M) · log M) | AC | 0.046 s | 14532 KB | 11322143 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1379_graphs_optimized.cpp](1379_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O((N + M + D) log(M + 1)) | AC | 0.031 s | 3464 KB | 11316958 |
| [1379_graphs_optimized.go](1379_graphs_optimized.go) | Go 1.14 x64 | graphs | O((N + M + D) log(M + 2)) | AC | 0.093 s | 5748 KB | 11317150 |
| [1379_graphs_optimized.java](1379_graphs_optimized.java) | Java 1.8 | graphs | O((N + M + D) log(M + 2)) | AC | 0.140 s | 6740 KB | 11317007 |
| [1379_graphs_optimized.py](1379_graphs_optimized.py) | PyPy 3.10 x64 | graphs | O((N + M + D) log(M + 2)) | AC | 0.250 s | 16008 KB | 11317003 |
| [1379_graphs_optimized.rs](1379_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O((N + M + D) log(M + 2)) | AC | 0.031 s | 8372 KB | 11317009 |

La versión en PyPy empaqueta el destino, el tiempo de viaje y la carga en un entero por arista. Las listas de adyacencia se ordenan por carga, de modo que el recorrido puede detenerse en la primera arista que no soporta el camión. Las cubetas por minuto omiten entradas sustituidas por rutas más cortas. Las métricas corresponden al envío 11317003.

La versión Java también empaqueta cada arista en un entero y ordena las listas de adyacencia por carga. Cuando encuentra una llegada más temprana, mueve la entrada a la cubeta correspondiente. Cada cruce ocupa como máximo una entrada. Las métricas corresponden al envío 11317007.

La versión Rust ordena las aristas compactas por carga y deja de recorrer la lista al llegar a la primera arista que no soporta la carga. Mover las entradas entre cubetas por minuto conserva una por cruce. Las métricas corresponden al envío 11317009.

La versión en Go empaqueta cada arista en un entero y ordena las listas de adyacencia por carga. La búsqueda deja de recorrer una lista cuando encuentra una arista con carga insuficiente. El envío 11317150 tardó 0,093 s y usó 5748 KB frente a 0,562 s y 24828 KB en la base.
