# 1512. Zinium

[Timus 1512](https://acm.timus.ru/problem.aspx?space=1&num=1512) · dificultad 886 · constructive

Problema original de Ilya Grebnov, Nikita Rybak y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que colocar N reinas (4 ≤ N ≤ 100000) en un tablero de N × N de
modo que ningún par comparta fila, columna o diagonal.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

La columna y la fila de cada reina, una reina por línea, en cualquier
orden. Se acepta cualquier colocación válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
```

Salida:

```
1 5
2 1
3 8
4 4
5 2
6 7
7 3
8 6
```

## Solución

A este tamaño la búsqueda es inútil, pero se conocen colocaciones
explícitas. Para N par con N mod 6 ≠ 2, la reina de la columna i ≤ N/2
va en la fila 2i y la de la columna N/2 + i en la fila 2i − 1: cada
reina de la mitad izquierda está en una diagonal distinta de cualquier
reina de la derecha, y dentro de cada mitad las filas crecen de 2 en 2
por columna, así que tampoco comparten diagonal. Para N par con
N mod 6 = 2 eso falla; en su lugar, con s = (2(i − 1) + N/2 − 1) mod N,
la columna i va en la fila 1 + s y la columna N + 1 − i en la fila
N − s. Ninguna de las dos colocaciones usa la diagonal principal, así
que un N impar toma la colocación de N − 1 y añade una reina en la
esquina (N, N). Comprobado para todo N de 4 a 3000 y para los más
grandes. `O(N)`.

Detalles a tener en cuenta:

- el patrón simple de pares e impares falla justo cuando N mod 6 = 2,
  como con N = 8 en el ejemplo (pruebas 01, 05, gen2, gen7);
- un N impar necesita la esquina libre del tablero de N − 1 (pruebas
  03, 06, gen3, gen6);
- hay muchas colocaciones correctas, así que las pruebas usan un
  comprobador (todas las pruebas);
- la salida de 100000 líneas conviene armarla en un solo búfer (gen5).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1512_constructive.cpp](1512_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.031 s | 3232 KB |
| [1512_constructive.go](1512_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 4076 KB |
| [1512_constructive.java](1512_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.093 s | 7808 KB |
| [1512_constructive.py](1512_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.140 s | 13344 KB |
| [1512_constructive.rs](1512_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 3960 KB |
