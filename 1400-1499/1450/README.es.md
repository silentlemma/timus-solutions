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

N y M, luego M líneas A, B, C, y por último S y F.

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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1450_dp.cpp](1450_dp.cpp) | G++ 13.2 x64 | dp | O(N + M) | AC | 0.187 s | 1668 KB |
| [1450_dp.go](1450_dp.go) | Go 1.14 x64 | dp | O(N + M) | AC | 0.203 s | 6332 KB |
| [1450_dp.java](1450_dp.java) | Java 1.8 | dp | O(N + M) | AC | 0.140 s | 2460 KB |
| [1450_dp.py](1450_dp.py) | Python 3.12 x64 | dp | O(N + M) | AC | 0.406 s | 35968 KB |
| [1450_dp.rs](1450_dp.rs) | Rust 1.75 x64 | dp | O(N + M) | AC | 0.046 s | 5760 KB |
