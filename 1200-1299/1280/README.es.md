# 1280. Ordenación topológica

[Timus 1280](https://acm.timus.ru/problem.aspx?space=1&num=1280) · dificultad 140 · graphs

Problema original de Sergey Volchenkov, Vladimir Pinaev y Michael Kopachev, del cuarto de final de la región central de Rusia del ACM ICPC 2003–2004, Rybinsk, 15–16 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay 1 ≤ N ≤ 1000 asignaturas y 0 ≤ M ≤ 100 000 reglas "s u": la
asignatura s debe estudiarse antes que la u. ¿Es el orden dado de las N
asignaturas compatible con todas las reglas?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, las M reglas y luego el orden de las N asignaturas. Las
asignaturas se numeran de 1 a N.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 6
1 3
1 4
3 5
5 2
4 2
1 2
1 3 4 5 2
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
5 6
1 3
1 4
3 5
5 2
4 2
1 2
1 2 4 5 3
```

Salida:

```
NO
```

## Solución

No hace falta ordenar nada: se guarda el lugar de cada asignatura en el
orden dado y se comprueba que cada regla va hacia delante, es decir, que
s está antes que u. Si las reglas tienen un ciclo, alguna regla del
ciclo va hacia atrás en cualquier orden, así que la comprobación ya
dice `NO`, como pide el enunciado. `O(N + M)`.

Detalles a tener en cuenta:

- basta incumplir una regla para responder `NO`; el plan de la prueba 02
  incumple tres reglas: 3 → 5, 5 → 2 y 4 → 2;
- una regla puede ir de una asignatura a sí misma, y ningún orden la
  cumple (prueba 04);
- las reglas pueden repetirse (prueba 07);
- sin reglas cualquier orden vale (prueba 06).

## Soluciones optimizadas

La solución optimizada en C++ analiza los números a mano desde un búfer
de 4 KB en lugar de `scanf` y guarda las reglas como una matriz de bits,
una fila `std::bitset` por asignatura, en lugar de dos arreglos de `int`
para hasta 100 000 reglas. Con `N ≤ 1000` la matriz ocupa unos 125 KB, y
las reglas repetidas comparten un bit. La comprobación recorre luego los
`N²` pares de asignaturas, como mucho un millón de bits:
{1280_graphs_optimized.cpp}.

La solución optimizada en Go analiza los números byte a byte desde el
`bufio.Reader` en lugar de `fmt.Fscan` y guarda los extremos de las
reglas en dos slices de `uint16`, que admiten números de asignatura
hasta 1000, en lugar de slices de `int` cuatro veces más grandes:
{1280_graphs_optimized.go}.

La solución optimizada en Java analiza los números a mano desde un búfer
de 4 KB en lugar de `StreamTokenizer` y guarda las reglas como una
matriz de bits en un arreglo de `long`, `N` filas de `⌈N / 64⌉`
palabras, unos 125 KB con `N ≤ 1000`, en lugar de dos arreglos de `int`
para hasta 100 000 reglas. La comprobación recorre luego los `N²` pares
de asignaturas: {1280_graphs_optimized.java}.

La solución optimizada en Python lee la entrada en trozos de 8 KB y
convierte los tokens trozo a trozo en lugar de partir toda la entrada de
una vez, y guarda los extremos de las reglas en un `array("H")` de
números sin signo de 16 bits, que admiten números de asignatura hasta
1000, en lugar de una lista de tuplas: {1280_graphs_optimized.py}.

La solución optimizada en Rust analiza los números a mano desde un búfer
de 4 KB en lugar de leer toda la entrada en un `String`, y guarda las
reglas como pares `(u16, u16)`, que admiten números de asignatura hasta
1000, en lugar de pares `(usize, usize)` cuatro veces más grandes:
{1280_graphs_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1280_graphs_optimized.cpp`: reducción de tiempo +86.24%; reducción de
  memoria +76.23%; base: `1280_graphs.cpp`.

- `1280_graphs_optimized.go`: reducción de tiempo +75.20%; reducción de
  memoria +61.24%; base: `1280_graphs.go`.

- `1280_graphs_optimized.java`: reducción de tiempo +0.00%; reducción de
  memoria +57.10%; base: `1280_graphs.java`.

- `1280_graphs_optimized.py`: reducción de tiempo +0.00%; reducción de
  memoria +92.63%; base: `1280_graphs.py`.

- `1280_graphs_optimized.rs`: reducción de tiempo +0.00%; reducción de
  memoria +84.16%; base: `1280_graphs.rs`.

## Notas por lenguaje

- Todos los lenguajes guardan los lugares en un arreglo y comprueban con
  él cada regla.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1280_graphs.cpp](1280_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.109 s | 976 KB | 11284403 |
| [1280_graphs.go](1280_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.125 s | 3416 KB | 11284414 |
| [1280_graphs.java](1280_graphs.java) | Java 1.8 | graphs | O(N + M) | AC | 0.140 s | 1324 KB | 11284421 |
| [1280_graphs.py](1280_graphs.py) | Python 3.12 x64 | graphs | O(N + M) | AC | 0.171 s | 24372 KB | 11284417 |
| [1280_graphs.rs](1280_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.015 s | 3688 KB | 11284425 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1280_graphs_optimized.cpp](1280_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(N² + M) | AC | 0.015 s | 232 KB | 11304469 |
| [1280_graphs_optimized.go](1280_graphs_optimized.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.031 s | 1324 KB | 11304470 |
| [1280_graphs_optimized.java](1280_graphs_optimized.java) \* | Java 1.8 | graphs | O(N² + M) | AC | 0.140 s | 568 KB | 11304471 |
| [1280_graphs_optimized.py](1280_graphs_optimized.py) \* | Python 3.12 x64 | graphs | O(N + M) | AC | 0.171 s | 1796 KB | 11304472 |
| [1280_graphs_optimized.rs](1280_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.015 s | 584 KB | 11304473 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
