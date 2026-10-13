# 1480. Cupones

[Timus 1480](https://acm.timus.ru/problem.aspx?space=1&num=1480) · dificultad 471 · constructive

Problema original de Sergey Pupyrev, del Campeonato de la Universidad Estatal de los Urales, 7 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que colocar los números 1 … N² (2 ≤ N ≤ 50) en una tabla N × N de
modo que la mayor suma de dos casillas con un lado común sea lo más
pequeña posible. Se escribe esa suma y una tabla que la alcanza;
escritos en orden fila a fila, la suma sería 2N² − 1.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

La menor mayor suma posible y luego las N filas de la tabla. Se acepta
cualquier tabla válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
6
1 4
3 2
```

## Solución

Se colorea la tabla como un tablero de ajedrez. Dos números grandes no
deben tocarse, así que N², N² − 1, … van en las casillas de un color en
orden de lectura, y 1, 2, … en las del otro color, también en orden de
lectura. Así cada suma junta un número pequeño con uno grande, y el peor
par es un número pequeño con el grande justo encima: entre ellos, en
orden de lectura, hay unas N/2 casillas de cada color, y la suma resulta
N² + ⌊N/2⌋ + 1 (comprobado para cada N hasta 50).

Ninguna tabla lo mejora. Una búsqueda exhaustiva que coloca los números
desde el mayor y da a cada casilla el tope que dejan sus vecinas ya
colocadas no encuentra ninguna tabla con suma menor para ningún N hasta
9, y ese es el valor que espera el juez. `O(N²)`.

Detalles a tener en cuenta:

- la primera línea es la suma, no N; la tabla va después (todas las
  pruebas);
- el coloreado funciona igual para N par e impar, pero ⌊N/2⌋ redondea
  hacia abajo (pruebas 05, 06, 07);
- la tabla obvia en orden de lectura da 2N² − 1, como señala el
  enunciado, muy lejos del óptimo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1480_constructive.cpp](1480_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.031 s | 128 KB |
| [1480_constructive.go](1480_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.031 s | 1108 KB |
| [1480_constructive.java](1480_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.125 s | 1640 KB |
| [1480_constructive.py](1480_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.078 s | 432 KB |
| [1480_constructive.rs](1480_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.031 s | 256 KB |
