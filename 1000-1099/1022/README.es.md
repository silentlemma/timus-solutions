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

`1022_bfs_graphs_optimized.java`. Java conserva la ordenación topológica de Kahn, pero empaqueta cada fila de adyacencia en palabras long en lugar de celdas boolean. Un hijo repetido no incrementa otra vez el grado de entrada. Al extraer un vértice de grado cero, recorre solo los bits activos mediante numberOfTrailingZeros y bits&=bits-1; añade cada hijo cuando su grado llega a cero. Un arreglo int sirve de cola y respuesta, sin listas de objetos ni StringBuilder. Búferes separados de entrada y salida de 4096 bytes convierten decimales por flujos ordinarios. Con E aristas listadas: tiempo O(N*ceil(N/64)+E), almacenamiento O(N*ceil(N/64)+N), más búferes fijos. Conserva las bases Kahn y DFS.

Accepted exacto Java 1.8 #11327520: 0.078 s / 380 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 5/179, memoria 2/179. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11304481 era 0.093 s / 360 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1022_bfs_graphs_optimized.java`: 0.078 s / 380 KB; base didáctica conservada `1022_bfs_graphs.java`: 0.125 s / 1828 KB.

`1022_bfs_graphs.py`. Conserva Kahn, indegrados y una lista creciente como FIFO y respuesta. Con hasta 100 vértices, divide una vez la entrada acotada de bytes en lugar de generadores Python por bloques/tokens. Cada arista/vértice se procesa una vez: O(V+E) tiempo y espacio con entrada. Vacía antes de salir; conserva el DFS didáctico.

Accepted exacto CPython 3.12 #11327003: 0.062 s / 724 KB. Comparación guardada 2026-11-20 con compiladores actuales de la familia: tiempo 4/54, memoria 44/54. Por debajo de 1024 KB, admisión estricta solo por tiempo.

- `1022_bfs_graphs.py`: 0.062 s / 724 KB; base didáctica conservada `1022_dfs_graphs.py` (Python 3.12 x64): 0.078 s / 512 KB; cambio de tiempo -20.5%; cambio de memoria +41.4%.

Frente a `1022_dfs_graphs.py`: tiempo 0.078 s → 0.093 s; memoria 512 KB → 256 KB.

La solución optimizada en C++ con el algoritmo de Kahn guarda las
relaciones en una matriz fija de `bool` de 101 × 101 celdas, unos 10 KB
porque `N ≤ 100`, y la cola en un arreglo fijo, en lugar de un `vector`
de `vector` que crece con cada relación. Al sacar un miembro de la cola
recorre toda su fila de la matriz, `O(N²)` en total, lo que no cuesta
nada con 100 miembros: {1022_bfs_graphs_optimized.cpp}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1022_bfs_graphs_optimized.cpp`: reducción de tiempo +0.00%; reducción
  de memoria +45.10%; base: `1022_bfs_graphs.cpp`.

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
| [1022_bfs_graphs_optimized.java](1022_bfs_graphs_optimized.java) \* | Java 1.8 | bfs, graphs | O(N ceil(N/64) + E) time; O(N ceil(N/64) + N) space | AC | 0.078 s | 380 KB | 11327520 |
| [1022_bfs_graphs.py](1022_bfs_graphs.py) \* | Python 3.12 x64 | bfs, graphs | O(V+E) time; O(V+E) space | AC | 0.062 s | 724 KB | 11327003 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
