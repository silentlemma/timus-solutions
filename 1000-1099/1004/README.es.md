# 1004. Ciclo más corto en un multigrafo no dirigido

[Timus 1004](https://acm.timus.ru/problem.aspx?space=1&num=1004) · dificultad 580 · shortest_paths, graphs

Problema original de la Olimpiada Centroeuropea de Informática 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo no dirigido tiene `N` vértices (`3 ≤ N ≤ 100`) y `M` aristas
(`3 ≤ M ≤ N·(N-1)`) con longitudes enteras positivas `1 ≤ l ≤ 300`. Puede
haber varias aristas entre el mismo par de vértices, pero no lazos.

Encuentra un ciclo simple de al menos 3 vértices con la menor longitud total:
vértices distintos `x1, ..., xk` (`k ≥ 3`) tales que `x1-x2, ..., x(k-1)-xk` y
`xk-x1` sean aristas. Su longitud es la suma de las longitudes de esas aristas.
Informa si no existe tal ciclo.

La entrada contiene `T ≤ 5` pruebas de este tipo.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

Las pruebas van una tras otra. Una prueba es una línea `N M` y `M` líneas
`a b l`: una arista entre `a` y `b` (`a ≠ b`) de longitud `l`. Una línea `-1`
termina la entrada.

## Salida

Para cada prueba, una línea: los vértices `x1 ... xk` de un ciclo más corto en
orden, separados por espacios simples, o `No solution.` si el grafo no tiene
ningún ciclo de al menos 3 vértices.

## Evaluación

Se acepta cualquier ciclo más corto, empezando en cualquier vértice y en
cualquier dirección: el verificador comprueba que los vértices sean distintos,
que los consecutivos estén unidos por aristas y que la longitud total sea
mínima.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 7
1 2 2
2 3 2
3 1 2
3 4 1
4 5 1
5 3 1
1 5 10
4 3
1 2 5
2 3 5
3 4 5
-1
```

Salida:

```
4 5 3
No solution.
```

### Ejemplo 2

Entrada:

```
3 3
1 2 1
1 2 1
2 1 3
-1
```

Salida:

```
No solution.
```

## Solución

Solo importa la arista más corta entre dos vértices, así que se guarda una
matriz de las aristas directas más ligeras; las aristas paralelas por sí solas
nunca forman un ciclo válido (hacen falta 3 vértices distintos).

Se ejecuta Floyd-Warshall y, justo antes de permitir el vértice `k` como
intermedio, se revisan todos los pares `i < j < k` unidos a `k` por aristas: en
ese momento `dist[i][j]` es el camino más corto entre `i` y `j` usando solo
vértices menores que `k`, así que ese camino más las aristas `j-k` y `k-i` es
un ciclo simple cuyo vértice mayor es `k`. Todo ciclo simple se encuentra así
al procesar su vértice mayor, por lo que el mínimo entre todos los candidatos
es la respuesta. Una matriz `next` (el primer paso del camino más corto)
permite reconstruir el camino. Tiempo `O(N^3)` por prueba, memoria `O(N^2)`.

Detalles a tener en cuenta:

- dos aristas paralelas no son un recorrido: un ciclo necesita al menos 3
  vértices;
- de las aristas paralelas hay que usar solo la más corta;
- los ciclos candidatos deben revisarse antes de relajar a través de `k`; si
  no, el camino `i..j` podría pasar por el propio `k`.

## Notas por lenguaje

- **C++**, **Go**, **Rust**: los bucles simples `O(N^3)` quedan muy por debajo
  del límite.
- **Python**: `5 · 100^3` pasos del bucle interno son justos para 0.5 segundos;
  el bucle sobre `j` usa referencias locales a las filas (`di`, `dk`) y omite
  las filas con `dist[i][k]` infinito. Aun así, con CPython 3.12 supera el
  límite de tiempo en la prueba 4 (0,531 s); el mismo archivo se acepta con
  PyPy 3.10 en 0,187 s, así que la solución en Python solo pasa con PyPy.
- **Java**: un lector de bytes propio para las hasta 50 000 líneas de entrada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1004_shortest_paths_graphs.cpp](1004_shortest_paths_graphs.cpp) | G++ 13.2 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.046 s | 360 KB |
| [1004_shortest_paths_graphs.go](1004_shortest_paths_graphs.go) | Go 1.14 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.031 s | 3356 KB |
| [1004_shortest_paths_graphs.java](1004_shortest_paths_graphs.java) | Java 1.8 | shortest_paths, graphs | O(N^3) per test | AC | 0.125 s | 1384 KB |
| [1004_shortest_paths_graphs.py](1004_shortest_paths_graphs.py) | PyPy 3.10 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.187 s | 9912 KB |
| [1004_shortest_paths_graphs.rs](1004_shortest_paths_graphs.rs) | Rust 1.75 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.015 s | 1096 KB |
