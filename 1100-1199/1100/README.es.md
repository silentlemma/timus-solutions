# 1100. Una tabla de resultados ordenada como lo haría el método de la burbuja

[Timus 1100](https://acm.timus.ru/problem.aspx?space=1&num=1100) · dificultad 44 · sorting

Problema original de Pavel Atnashev, del Tetrahedron Team Contest, mayo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan `N` equipos (`1 < N ≤ 150 000`) como pares de un identificador
único (`1 ≤ ID ≤ 10^7`) y un número de problemas resueltos `M`
(`0 ≤ M ≤ 100`). El programa antiguo los ordenaba con el método de la
burbuja, intercambiando vecinos mientras `A[i] < A[i+1]` por `M`. Imprime
la misma tabla, pero rápido.

Límite de tiempo: 1 segundo. Límite de memoria: 16 MB.

## Entrada

`N` y luego `N` líneas con `ID` y `M`.

## Salida

`N` líneas con `ID` y `M` en el orden que da el método de la burbuja.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
1 2
16 3
11 2
20 3
3 5
26 4
7 1
22 4
```

Salida:

```
3 5
26 4
22 4
16 3
20 3
1 2
11 2
7 1
```

## Solución

El método de la burbuja solo intercambia vecinos con distinta
puntuación, así que dos equipos con igual `M` nunca se adelantan: el
resultado es una ordenación estable por `M` de mayor a menor. Como `M`
solo toma 101 valores, una ordenación por conteo lo hace en una pasada:
cada equipo va al cubo de su puntuación en el orden de entrada, y luego
se imprimen los cubos de 100 a 0. `O(N)`.

Detalles a tener en cuenta:

- una ordenación no estable mezcla los equipos con igual puntuación, y
  la respuesta cambia;
- el límite de memoria es de 16 MB, así que los equipos se guardan de
  forma compacta y, en Python, la entrada se lee línea a línea y la salida
  se escribe por partes;
- 150 000 líneas de salida necesitan escritura con búfer.

Las respuestas se comprobaron con el propio método de la burbuja para
hasta 300 equipos y con una ordenación estable de biblioteca para tablas
mayores.

## Soluciones optimizadas

Las soluciones optimizadas (C++, Java, Rust) leen y escriben los números a
mano a través de búferes de 8 KB en lugar de `scanf` y `printf`,
`StreamTokenizer` y `PrintWriter`, o `parse` y `writeln!`: con 150 000
líneas, la conversión entre números y texto ocupa la mayor parte del tiempo.
La ordenación es el mismo conteo; Java guarda los problemas resueltos como
bytes, ya que son a lo sumo 100. C++: 0.031 s en lugar de 0.265 s, con
casi la misma memoria (1388 KB frente a 1404 KB); Java: 0.109 s en lugar
de 0.218 s y 1736 KB en lugar de 6844 KB; Rust: 1688 KB en lugar de
6528 KB, con el mismo tiempo.

## Notas por lenguaje

- Go lee las palabras con `bufio.Scanner` en lugar de `fmt.Scan`: la
  entrada tiene hasta 150 000 líneas.
- Python guarda los identificadores en cubos `array("i")`, de cuatro
  bytes cada uno.
- Java hace una ordenación estable por conteo con sumas de prefijos sobre
  las puntuaciones en lugar de listas.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1100_sorting.cpp](1100_sorting.cpp) | G++ 13.2 x64 | sorting | O(N) | AC | 0.265 s | 1404 KB | 11279152 |
| [1100_sorting.go](1100_sorting.go) | Go 1.14 x64 | sorting | O(N) | AC | 0.062 s | 6852 KB | 11303071 |
| [1100_sorting.java](1100_sorting.java) | Java 1.8 | sorting | O(N) | AC | 0.218 s | 6844 KB | 11279155 |
| [1100_sorting.py](1100_sorting.py) | Python 3.12 x64 | sorting | O(N) | AC | 0.234 s | 3308 KB | 11279154 |
| [1100_sorting.rs](1100_sorting.rs) | Rust 1.75 x64 | sorting | O(N) | AC | 0.062 s | 6528 KB | 11279156 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1100_sorting_optimized.cpp](1100_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(N) | AC | 0.031 s | 1388 KB | 11303548 |
| [1100_sorting_optimized.java](1100_sorting_optimized.java) | Java 1.8 | sorting | O(N) | AC | 0.109 s | 1736 KB | 11303549 |
| [1100_sorting_optimized.rs](1100_sorting_optimized.rs) | Rust 1.75 x64 | sorting | O(N) | AC | 0.046 s | 1688 KB | 11303550 |
