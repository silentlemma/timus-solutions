# 1450. Gasoductos rusos

[Timus 1450](https://acm.timus.ru/problem.aspx?space=1&num=1450) · dificultad 149 · dp

Problema original de Dmitry Kovalioff, Ilya Grebnov y Nikita Rybak, de Timus Top Coders: Second Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una red de gas tiene N estaciones (2 ≤ N ≤ 500) y M gasoductos de un
solo sentido (0 ≤ M ≤ 124750), cada uno de A a B con beneficio C
(1 ≤ C ≤ 10000); cada par de estaciones tiene como mucho un gasoducto y
la red no tiene ciclos: si el gas puede ir de X a Y, no puede volver.
Hay que hallar la ruta más rentable de la estación S a la F, siendo el
beneficio de una ruta la suma de sus gasoductos, o imprimir «No
solution» si F no se alcanza.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N y M en la primera línea, luego M líneas A, B, C con 1 ≤ A, B ≤ N, y
por último S y F en la última línea, donde 1 ≤ S, F ≤ N y S ≠ F.

## Salida

El mayor beneficio o «No solution».

## Ejemplos

### Ejemplo 1

Entrada:

```
6 7
6 5 10
1 4 11
1 2 4
3 1 5
2 4 5
6 3 1
6 1 3
6 4
```

Salida:

```
17
```

La mejor ruta del ejemplo es 6, 3, 1, 4.

## Solución

Sin ciclos, el camino más largo es una programación dinámica sencilla.
Se ordenan las estaciones topológicamente con el método de Kahn: se
empieza por las estaciones sin gasoductos de entrada y se libera una
estación cuando ya se han tomado todos los que llegan a ella. En ese
orden cada estación está terminada antes de usar sus gasoductos, así
que best[w] = max(best[v] + C) sobre los gasoductos v → w, con
best[S] = 0 y las estaciones inalcanzables desde S vacías. La respuesta
es best[F]. `O(N + M)`.

Detalles a tener en cuenta:

- F inalcanzable, también cuando los gasoductos llevan de F a S
  (pruebas 02, 03, 06);
- la ruta más rentable puede tener más gasoductos que la directa
  (prueba 07);
- las estaciones inalcanzables desde S no deben transmitir beneficio,
  aunque igualmente hay que ordenarlas.

## Soluciones optimizadas

La solución optimizada en C++ analiza los números a mano desde un búfer
de 4 KB en lugar de `scanf` y guarda la red como una matriz de
beneficios `uint16_t` de 16 bits, unos 490 KB con `N = 500`, en lugar de
un `vector` de `vector` de pares. Los beneficios valen al menos 1 y cada
par de estaciones tiene como mucho un gasoducto, así que una celda a
cero significa que no hay gasoducto; una estación que sale de la cola
recorre toda su fila, `O(N²)` en total. Los mejores beneficios son `int`
en lugar de `long long`: una ruta tiene como mucho 499 gasoductos, así
que su beneficio no pasa de 4 990 000: {1450_dp_optimized.cpp}.

La solución optimizada en Go analiza los números byte a byte desde un
`bufio.Reader` en lugar de `fmt.Fscan` y guarda la red como una matriz
de beneficios `uint16`, unos 490 KB con `N = 500`, en lugar de slices de
estructuras con dos campos `int`. Los beneficios valen al menos 1 y cada
par de estaciones tiene como mucho un gasoducto, así que una celda a
cero significa que no hay gasoducto; una estación que sale de la cola
recorre toda su fila, `O(N²)` en total: {1450_dp_optimized.go}.

La solución optimizada en Java analiza los números a mano desde un búfer
de 4 KB en lugar de `StreamTokenizer` y guarda la red como una matriz de
beneficios `short`, que admite valores hasta 10 000, en lugar de tres
arreglos de `int` con los gasoductos y los arreglos que los agrupan por
estación. Los beneficios valen al menos 1 y cada par de estaciones tiene
como mucho un gasoducto, así que una celda a cero significa que no hay
gasoducto; una estación que sale de la cola recorre toda su fila,
`O(N²)` en total. Los mejores beneficios son `int` en lugar de `long`:
una ruta tiene como mucho 499 gasoductos, así que su beneficio no pasa
de 4 990 000: {1450_dp_optimized.java}.

La solución optimizada en Python aprovecha la disposición por líneas de
la entrada y la lee línea a línea en lugar de partirla entera en una
lista. Guarda la red como una fila `array("H")` de beneficios sin signo
de 16 bits por estación en lugar de listas de tuplas; los beneficios
valen al menos 1 y cada par de estaciones tiene como mucho un gasoducto,
así que una celda a cero significa que no hay gasoducto, y una estación
que sale de la cola recorre toda su fila con `enumerate`:
{1450_dp_optimized.py}.

La solución optimizada en Rust analiza los números a mano desde un búfer
de 4 KB en lugar de leer toda la entrada en un `String` y guarda la red
como una matriz de beneficios `u16`, unos 490 KB con `N = 500`, en lugar
de vectores de pares `(usize, i64)`. Los beneficios valen al menos 1 y
cada par de estaciones tiene como mucho un gasoducto, así que una celda
a cero significa que no hay gasoducto; una estación que sale de la cola
recorre toda su fila, `O(N²)` en total. Los mejores beneficios son `i32`
simples con -1 para las inalcanzables en lugar de `Option<i64>`: una
ruta tiene como mucho 499 gasoductos, así que su beneficio no pasa de
4 990 000: {1450_dp_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1450_dp_optimized.cpp`: reducción de tiempo +91.98%; reducción de
  memoria +62.59%; base: `1450_dp.cpp`.

- `1450_dp_optimized.go`: reducción de tiempo +84.73%; reducción de
  memoria +75.87%; base: `1450_dp.go`.

- `1450_dp_optimized.java`: reducción de tiempo -11.43%; reducción de
  memoria +62.93%; base: `1450_dp.java`.

- `1450_dp_optimized.py`: reducción de tiempo +38.42%; reducción de
  memoria +96.92%; base: `1450_dp.py`.

- `1450_dp_optimized.rs`: reducción de tiempo +67.39%; reducción de
  memoria +87.71%; base: `1450_dp.rs`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1450_dp.cpp](1450_dp.cpp) | G++ 13.2 x64 | dp | O(N + M) | AC | 0.187 s | 1668 KB | 11286341 |
| [1450_dp.go](1450_dp.go) | Go 1.14 x64 | dp | O(N + M) | AC | 0.203 s | 6332 KB | 11286345 |
| [1450_dp.java](1450_dp.java) | Java 1.8 | dp | O(N + M) | AC | 0.140 s | 2460 KB | 11286355 |
| [1450_dp.py](1450_dp.py) | Python 3.12 x64 | dp | O(N + M) | AC | 0.406 s | 35968 KB | 11286349 |
| [1450_dp.rs](1450_dp.rs) | Rust 1.75 x64 | dp | O(N + M) | AC | 0.046 s | 5760 KB | 11286358 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1450_dp_optimized.cpp](1450_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N² + M) | AC | 0.015 s | 624 KB | 11304540 |
| [1450_dp_optimized.go](1450_dp_optimized.go) | Go 1.14 x64 | dp | O(N² + M) | AC | 0.031 s | 1528 KB | 11304541 |
| [1450_dp_optimized.java](1450_dp_optimized.java) \* | Java 1.8 | dp | O(N² + M) | AC | 0.156 s | 912 KB | 11304542 |
| [1450_dp_optimized.py](1450_dp_optimized.py) \* | Python 3.12 x64 | dp | O(N² + M) | AC | 0.250 s | 1108 KB | 11304544 |
| [1450_dp_optimized.rs](1450_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N² + M) | AC | 0.015 s | 708 KB | 11304543 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
