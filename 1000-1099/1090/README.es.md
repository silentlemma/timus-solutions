# 1090. La fila de reclutas que más salta: contar inversiones

[Timus 1090](https://acm.timus.ru/problem.aspx?space=1&num=1090) · dificultad 365 · fenwick, binary_search

Problema original de Nikita Shamgunov, del USU Open Collegiate Programming Contest, marzo de 2001, Senior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `K` filas (`1 ≤ K ≤ 20`) de `N` reclutas cada una (`2 ≤ N ≤ 10000`),
numerados por altura de 1 (el más alto) a `N`; cada fila es una
permutación de `1 … N`. Cada recluta salta una vez por cada recluta que
está delante de él en la fila con un número mayor. Imprime la fila con
más saltos en total, la de menor número en caso de empate.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `K`, y luego `K` líneas con `N` números cada una.

## Salida

El número de la fila.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
1 2 3
2 1 3
3 2 1
```

Salida:

```
3
```

## Solución

El total de saltos de una fila es el número de inversiones de la
permutación: pares de posiciones `i < j` con `a[i] > a[j]`. Con
`N = 10000` el doble bucle es demasiado lento, así que se cuentan
mientras se lee la fila. Delante del recluta `x` en la posición `i` hay
`i` reclutas, y cuántos de ellos tienen un número menor es una suma de
prefijo en un árbol de Fenwick sobre los números `1 … N`; los saltos de
`x` son `i` menos esa suma. Después se añade `x` al árbol.
`O(K · N log N)`.

Detalles a tener en cuenta:

- el total de una fila llega a `N(N − 1)/2 ≈ 5 · 10^7`; cabe en 32 bits,
  pero las soluciones suman en 64 bits;
- en caso de empate gana la primera fila, así que solo un total
  estrictamente mayor sustituye al mejor;
- el árbol debe vaciarse para cada fila.

Las respuestas se comprobaron con recuentos de inversiones por ordenación
por mezcla, y para `N ≤ 300` también con el doble bucle.

## Notas por lenguaje

- Python guarda los números anteriores de la fila en una lista ordenada,
  halla la cuenta con `bisect` e inserta cada número con `list.insert`.
  Las inserciones mueven memoria, `O(N²)` en teoría, pero se ejecutan en C
  y superan a un árbol de Fenwick escrito en Python con `N = 10000`.
- Con CPython 3.12 la solución en Python supera el límite de tiempo en la
  prueba 9 (0,515 s); el mismo archivo se acepta con PyPy 3.10 en 0,437 s,
  así que la solución en Python solo pasa con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1090_binary_search.py](1090_binary_search.py) | PyPy 3.10 x64 | binary_search | O(K·N^2) | AC | 0.437 s | 20044 KB |
| [1090_fenwick.cpp](1090_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(K·N log N) | AC | 0.156 s | 236 KB |
| [1090_fenwick.go](1090_fenwick.go) | Go 1.14 x64 | fenwick | O(K·N log N) | AC | 0.046 s | 1916 KB |
| [1090_fenwick.java](1090_fenwick.java) | Java 1.8 | fenwick | O(K·N log N) | AC | 0.125 s | 512 KB |
| [1090_fenwick.rs](1090_fenwick.rs) | Rust 1.75 x64 | fenwick | O(K·N log N) | AC | 0.015 s | 2120 KB |
