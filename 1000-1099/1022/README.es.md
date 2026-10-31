# 1022. Ordenar una familia para que los antepasados vayan primero

[Timus 1022](https://acm.timus.ru/problem.aspx?space=1&num=1022) · dificultad 142 · graphs, bfs, dfs

Problema original de la Segunda Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 7 de octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` miembros (`1 ≤ N ≤ 100`), numerados `1..N`, están unidos por relaciones
padre-hijo: un miembro puede tener cualquier número de padres e hijos, y no
hay ciclos. Imprime un orden de todos los miembros en el que cada uno vaya
antes que todos sus descendientes. Se acepta cualquier orden así.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas: la `i`-ésima enumera los hijos del miembro `i` en
cualquier orden y termina en `0` (una línea con solo `0` significa que no
tiene hijos).

## Salida

Los `N` números en el orden elegido, separados por espacios.

## Evaluación

Se acepta cualquier orden válido. El verificador comprueba que la salida es
una permutación de `1..N` y que cada miembro va antes que cada uno de sus
hijos (lo que por inducción da «antes que todos sus descendientes»).

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0
1 0
1 4 0
1 0
```

Salida:

```
2 3 4 1
```

### Ejemplo 2

Entrada:

```
1
0
```

Salida:

```
1
```

## Solución

Los miembros y las relaciones forman un grafo dirigido acíclico, y el orden
pedido es un **orden topológico** suyo.

**Algoritmo de Kahn (BFS).** Se cuentan los padres de cada miembro. Los que
no tienen padres pueden hablar primero; van a una cola. Se sacan miembros de
la cola uno a uno; para cada hijo se reduce su contador de padres, y el hijo
cuyo contador llega a cero entra en la cola: todos sus padres ya hablaron.
La cola en orden de inserción es la respuesta.

**Búsqueda en profundidad.** Se lanza una DFS desde cada miembro no visitado
y se añade un miembro a una lista cuando su DFS termina, es decir, después de
todos sus descendientes. La lista invertida pone a cada miembro antes que
sus descendientes.

Ambos son `O(N + E)`, donde `E` es el número de relaciones, aquí como mucho
unas 5 000.

Detalles a tener en cuenta:

- la entrada enumera hijos, no padres: cuenta los grados de entrada a partir
  de las listas;
- una línea con solo `0` es una lista vacía, no el final de la entrada.

## Soluciones optimizadas

La solución optimizada en C++ con el algoritmo de Kahn guarda las
relaciones en una matriz fija de `bool` de 101 × 101 celdas, unos 10 KB
porque `N ≤ 100`, y la cola en un arreglo fijo, en lugar de un `vector`
de `vector` que crece con cada relación. Al sacar un miembro de la cola
recorre toda su fila de la matriz, `O(N²)` en total, lo que no cuesta
nada con 100 miembros: {1022_bfs_graphs_optimized.cpp}.

La solución optimizada en Java con el algoritmo de Kahn analiza los
números a mano desde un búfer de 4 KB en lugar de `Scanner`, guarda las
relaciones en una matriz de `boolean` de (N + 1) × (N + 1) celdas,
pequeña porque `N ≤ 100`, y la cola en un arreglo de `int`, en lugar de
listas de objetos `Integer`. Al sacar un miembro de la cola recorre toda
su fila de la matriz, `O(N²)` en total:
{1022_bfs_graphs_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1022_bfs_graphs_optimized.cpp`: reducción de tiempo +0.00%; reducción
  de memoria +45.10%; base: `1022_bfs_graphs.cpp`.

- `1022_bfs_graphs_optimized.java`: reducción de tiempo +25.60%;
  reducción de memoria +80.31%; base: `1022_bfs_graphs.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1022_bfs_graphs.go](1022_bfs_graphs.go).
- [1022_dfs_graphs.rs](1022_dfs_graphs.rs).

- **C++**, **Go**, **Java**: algoritmo de Kahn.
- **C++**, **Rust**: DFS recursiva (la profundidad es como mucho 100);
  **Python**: la misma DFS con una pila explícita de iteradores.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1022_bfs_graphs.cpp](1022_bfs_graphs.cpp) | G++ 13.2 x64 | bfs, graphs | O(N + E) | AC | 0.015 s | 204 KB | 11278266 |
| [1022_dfs_graphs.cpp](1022_dfs_graphs.cpp) | G++ 13.2 x64 | dfs, graphs | O(N + E) | AC | 0.015 s | 196 KB | 11278269 |
| [1022_bfs_graphs.go](1022_bfs_graphs.go) | Go 1.14 x64 | bfs, graphs | O(N + E) | AC | 0.015 s | 1124 KB | 11278272 |
| [1022_bfs_graphs.java](1022_bfs_graphs.java) | Java 1.8 | bfs, graphs | O(N + E) | AC | 0.125 s | 1828 KB | 11278276 |
| [1022_dfs_graphs.py](1022_dfs_graphs.py) | Python 3.12 x64 | dfs, graphs | O(N + E) | AC | 0.078 s | 512 KB | 11278274 |
| [1022_dfs_graphs.rs](1022_dfs_graphs.rs) | Rust 1.75 x64 | dfs, graphs | O(N + E) | AC | 0.015 s | 236 KB | 11278277 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1022_bfs_graphs_optimized.cpp](1022_bfs_graphs_optimized.cpp) | G++ 13.2 x64 | bfs, graphs | O(N²) | AC | 0.015 s | 112 KB | 11304480 |
| [1022_bfs_graphs_optimized.java](1022_bfs_graphs_optimized.java) \* | Java 1.8 | bfs, graphs | O(N²) | AC | 0.093 s | 360 KB | 11304481 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
