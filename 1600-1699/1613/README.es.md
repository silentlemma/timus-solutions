# 1613. Para los aficionados a la estadística

[Timus 1613](https://acm.timus.ru/problem.aspx?space=1&num=1613) · dificultad 141 · binary_search

Problema original de Alexander Ipatov, del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los tranvías de cada una de n ciudades (1 ≤ n ≤ 69 999) llevaron cierto
número de pasajeros, de 1 a 10⁹ − 1. Para cada una de q consultas
(1 ≤ q ≤ 69 999) `l r x`, di si alguna ciudad numerada de l a r llevó
exactamente x pasajeros. Imprime una cadena de q caracteres, `1` para sí
y `0` para no.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n, los n números, q, y luego q líneas `l r x` con 1 ≤ l ≤ r ≤ n y
1 ≤ x < 10⁹.

## Salida

La cadena de respuestas.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1234567 666666 3141593 666666 4343434
5
1 5 3141593
1 5 578202
2 4 666666
4 4 7135610
1 1 1234567
```

Salida:

```
10101
```

## Solución

Ordena los pares (número, ciudad). Las ciudades con número x forman
entonces un bloque, ordenado por número de ciudad. Para una consulta, una
búsqueda binaria halla el primer par no menor que (x, l): la respuesta es
sí si su número es x y su ciudad es a lo sumo r. `O((n + q) log n)`.

Detalles a tener en cuenta:

- la respuesta es una sola cadena sin separadores;
- la ciudad debe encontrarse en l o después, no solo en algún sitio con
  número x (prueba 04).

## Soluciones optimizadas

La solución optimizada en C++ analiza los números a mano desde un búfer
de 4 KB en lugar de `scanf` y empaqueta cada par en un solo `uint64_t`:
el número de pasajeros, menor que 10⁹ < 2³⁰, encima de 17 bits para el
número de ciudad, porque `n ≤ 69 999 < 2¹⁷`. Un arreglo fijo de estas
claves se ordena como números simples, una consulta es un `lower_bound`
de `(x << 17) + l` seguido de una comparación con `(x << 17) + r`, y
cada respuesta sale con `putchar` en lugar de ir a un `std::string`:
{1613_binary_search_optimized.cpp}.

La solución optimizada en Go analiza los números byte a byte desde un
`bufio.Reader` en lugar de un `bufio.Scanner` con búfer de 1 MB y
`strconv.Atoi`, y sustituye los cuatro slices de `int` de pasajeros,
ciudades y orden por un solo slice de `uint64` con los pares
empaquetados: el número de pasajeros, menor que 10⁹ < 2³⁰, encima de
17 bits para el número de ciudad, porque `n ≤ 69 999 < 2¹⁷`. Una
consulta es un `sort.Search` de `(x << 17) + l` y una comparación con
`(x << 17) + r`, y las respuestas van directamente al `bufio.Writer`:
{1613_binary_search_optimized.go}.

La solución optimizada en Java analiza los números a mano desde un búfer
de 64 KB en lugar de `StreamTokenizer` y empaqueta cada par en un solo
`long`, el número de pasajeros encima de 17 bits para el número de
ciudad (`n ≤ 69 999 < 2¹⁷`). Ordenar un arreglo simple de `long` no
necesita un objeto `int[]` por ciudad ni comparador, y una consulta es
un solo `Arrays.binarySearch` de `(x << 17) | l`:
{1613_binary_search_optimized.java}.

La solución optimizada en Python lee la entrada en trozos de 8 KB y
convierte los tokens trozo a trozo en lugar de partir toda la entrada de
una vez. Empaqueta cada par en un solo entero, el número de pasajeros
encima de 17 bits para el número de ciudad (`n ≤ 69 999 < 2¹⁷`), así que
la lista ordenada guarda enteros simples en lugar de tuplas, y reúne las
respuestas en un `bytearray` en lugar de una lista de cadenas:
{1613_binary_search_optimized.py}.

La solución optimizada en Rust analiza los números a mano desde un búfer
de 4 KB en lugar de leer toda la entrada, hasta unos 2 MB, en un
`String`; los pares ordenados y la búsqueda binaria son los mismos:
{1613_binary_search_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1613_binary_search_optimized.cpp`: reducción de tiempo +81.87%;
  reducción de memoria +18.18%; base: `1613_binary_search.cpp`.

- `1613_binary_search_optimized.go`: reducción de tiempo +25.81%;
  reducción de memoria +74.47%; base: `1613_binary_search.go`.

- `1613_binary_search_optimized.java`: reducción de tiempo +30.13%;
  reducción de memoria +45.22%; base: `1613_binary_search.java`.

- `1613_binary_search_optimized.py`: reducción de tiempo +31.78%;
  reducción de memoria +83.68%; base: `1613_binary_search.py`.

- `1613_binary_search_optimized.rs`: reducción de tiempo +0.00%;
  reducción de memoria +79.96%; base: `1613_binary_search.rs`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1613_binary_search.cpp](1613_binary_search.cpp) | G++ 13.2 x64 | binary_search | O((n + q) log n) | AC | 0.171 s | 748 KB | 11288259 |
| [1613_binary_search.go](1613_binary_search.go) | Go 1.14 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 5876 KB | 11288261 |
| [1613_binary_search.java](1613_binary_search.java) | Java 1.8 | binary_search | O((n + q) log n) | AC | 0.156 s | 3388 KB | 11304478 |
| [1613_binary_search.py](1613_binary_search.py) | Python 3.12 x64 | binary_search | O((n + q) log n) | AC | 0.343 s | 26612 KB | 11288262 |
| [1613_binary_search.rs](1613_binary_search.rs) | Rust 1.75 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 3692 KB | 11288265 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1613_binary_search_optimized.cpp](1613_binary_search_optimized.cpp) | G++ 13.2 x64 | binary_search | O((n + q) log n) | AC | 0.031 s | 612 KB | 11304474 |
| [1613_binary_search_optimized.go](1613_binary_search_optimized.go) | Go 1.14 x64 | binary_search | O((n + q) log n) | AC | 0.046 s | 1500 KB | 11304475 |
| [1613_binary_search_optimized.java](1613_binary_search_optimized.java) | Java 1.8 | binary_search | O((n + q) log n) | AC | 0.109 s | 1856 KB | 11304479 |
| [1613_binary_search_optimized.py](1613_binary_search_optimized.py) \* | Python 3.12 x64 | binary_search | O((n + q) log n) | AC | 0.234 s | 4344 KB | 11304476 |
| [1613_binary_search_optimized.rs](1613_binary_search_optimized.rs) | Rust 1.75 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 740 KB | 11304477 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
