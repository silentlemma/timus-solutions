# 1064. Longitudes de arreglo para las que una búsqueda binaria termina en un paso dado

[Timus 1064](https://acm.timus.ru/problem.aspx?space=1&num=1064) · dificultad 659 · simulation

Problema original del concurso regional ACM ICPC del noreste de Europa 2000–2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La búsqueda binaria clásica sobre un arreglo no decreciente `A[0 … N−1]`
mantiene los límites `p = 0`, `q = N − 1`; mientras `p ≤ q` mira
`i = ⌊(p + q)/2⌋`, cuenta una comparación, se detiene si `A[i] = x` y, si
no, mueve `q` a `i − 1` (cuando `x < A[i]`) o `p` a `i + 1`. Se detuvo en el
índice `i` tras exactamente `L` comparaciones (`0 ≤ i ≤ 9999`,
`1 ≤ L ≤ 14`). Halla todas las longitudes `N` de 1 a 10000 para las que
esto es posible, agrupadas en tramos de valores consecutivos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`i` y `L`.

## Salida

El número `K` de tramos y luego `K` líneas con la primera y la última
longitud de cada tramo en orden creciente; `0` si no hay ninguno.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
9000 2
```

Salida:

```
0
```

### Ejemplo 2

Entrada:

```
10 3
```

Salida:

```
4
12 12
17 18
29 30
87 94
```

## Solución

Con una longitud `N` fija, las comparaciones no dependen de los valores,
solo de hacia dónde va la búsqueda. Para terminar en el índice `i`, cada
elemento inspeccionado antes de `i` debe mandar la búsqueda a la derecha y
cada uno después de `i` a la izquierda, lo que consigue un arreglo con
valores menores antes de `i` y mayores después. Así que el camino de la
búsqueda está forzado: se empieza con `[0, N − 1]`, se toma el centro, se
para si es `i` y, si no, se conserva la mitad que contiene a `i`. `N` sirve
cuando este camino alcanza `i` exactamente en la comparación `L` (e
`i < N`).

Se prueban todas las `N`: como mucho 14 pasos cada una,
`O(10000 · log 10000)`, y se juntan las longitudes buenas consecutivas en
tramos.

Detalles a tener en cuenta:

- `i` debe ser un índice del arreglo: `N > i`;
- la búsqueda puede llegar a `i` antes o después de `L`; solo cuenta
  exactamente `L`;
- la respuesta puede estar vacía: imprime solo `0`.

## Notas por lenguaje

- Todos los lenguajes simulan el mismo camino para cada longitud.

## Soluciones optimizadas

Para una ruta de búsqueda fija, el índice del punto medio no disminuye al crecer la longitud. Dos búsquedas binarias dividen las longitudes según si ese índice es menor, igual o mayor que el buscado. Se guardan las longitudes que lo alcanzan por primera vez en el paso `L` y se unen los intervalos contiguos.

Los dos intervalos exteriores siguen ramas distintas. Si el pivote está por debajo del índice buscado, la búsqueda va a la derecha. Si está por encima, va a la izquierda. El intervalo central ya ha encontrado el objetivo y solo se conserva en el paso L.

**Envíos de las versiones optimizadas en Timus**

`1064_binary_search.cpp` (G++ 13.2 x64) №11317375 · `1064_binary_search.go` (Go 1.14 x64) №11322862 · `1064_binary_search.py` (Python 3.12 x64) №11317377 · `1064_binary_search.rs` (Rust 1.75 x64) №11322383.

Go busca por binario los límites de cada intervalo válido y sigue solo las ramas compatibles con las posiciones observadas. Go 1.14 x64, envío 11322862. Tiempo 0,015 → 0,015 s, memoria 1128 → 416 KB.

**Envíos de las versiones sencillas en Timus**

Java 1.8 №11321771 · Rust 1.75 x64 №11321773 · G++ 13.2 x64 №11322100 · Go 1.14 x64 №11322101 · Python 3.12 x64 №11322103.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1064_binary_search_optimized.rs`. Se mantienen el algoritmo y los tipos enteros. Los tokens decimales se convierten directamente; los negativos se acumulan con su signo para representar también el mínimo entero con signo. No cambian el almacenamiento de entrada ni la complejidad del algoritmo.

Accepted #11328490 (Rust 1.75 x64): **0.015 s / 240 KB**. Comparación archivada: `1064_binary_search.rs` (Rust 1.75 x64) — 0.031 s / 240 KB (#11322383).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1064_simulation.cpp](1064_simulation.cpp) | G++ 13.2 x64 | simulation | O(10000 · log 10000) | AC | 0.015 s | 188 KB | 11322100 |
| [1064_simulation.go](1064_simulation.go) | Go 1.14 x64 | simulation | O(10000 · log 10000) | AC | 0.015 s | 1128 KB | 11322101 |
| [1064_simulation.java](1064_simulation.java) | Java 1.8 | simulation | O(10000 · log 10000) | AC | 0.109 s | 1700 KB | 11321771 |
| [1064_simulation.py](1064_simulation.py) | Python 3.12 x64 | simulation | O(10000 · log 10000) | AC | 0.109 s | 516 KB | 11322103 |
| [1064_simulation.rs](1064_simulation.rs) | Rust 1.75 x64 | simulation | O(10000 · log 10000) | AC | 0.046 s | 268 KB | 11321773 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1064_binary_search.cpp](1064_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(2^L · L · log 10000) | AC | 0.015 s | 192 KB | 11317375 |
| [1064_binary_search.py](1064_binary_search.py) | Python 3.12 x64 | binary_search | O(2^L · L · log 10000) | AC | 0.078 s | 696 KB | 11317377 |
| [1064_binary_search.go](1064_binary_search.go) \* | Go 1.14 x64 | binary_search | O(2^L · L · log 10000) | AC | 0.015 s | 416 KB | 11322862 |
| [1064_binary_search.rs](1064_binary_search.rs) \* | Rust 1.75 x64 | binary_search | O(2^L · L · log 10000) | AC | 0.031 s | 240 KB | 11322383 |
| [1064_binary_search_optimized.rs](1064_binary_search_optimized.rs) | Rust 1.75 x64 | binary_search | O(2^L · L · log 10000) | AC | 0.015 s | 240 KB | 11328490 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
