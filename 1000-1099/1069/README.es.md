# 1069. Reconstruir un árbol a partir de su código de Prüfer

[Timus 1069](https://acm.timus.ru/problem.aspx?space=1&num=1069) · dificultad 517 · trees

Problema original de Magaz Asanov, del Ural State University Personal Contest Online, febrero de 2001, Students Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un árbol con vértices `1 … N` (`2 ≤ N ≤ 7500`) se codifica así: se toma la
hoja de menor número, se elimina y se anota su vecino; se repite hasta que
queda un solo vértice (siempre es `N`). Los `N − 1` números anotados son el
código. Dado el código, imprime la lista de adyacencia de cada vértice.

Límite de tiempo: 0.25 segundos. Límite de memoria: 8 MB.

## Entrada

El código: `N − 1` números separados por espacios y saltos de línea.

## Salida

Para cada vértice en orden creciente, una línea `v: a b c …` con sus
vecinos en orden creciente.

## Evaluación

La salida se compara línea a línea; dentro de una línea, token a token.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 1 6 2 6
```

Salida:

```
1: 4 6
2: 3 5 6
3: 2
4: 1
5: 2
6: 1 2
```

## Solución

Durante la codificación un vértice se anota una vez por cada vecino
eliminado antes que él, y se vuelve hoja cuando le queda un solo vecino.
Así que el vértice `v` tiene grado `1 + (las veces que v aparece en el
código)`, y en cada paso las hojas actuales son exactamente los vértices
que aún no se han eliminado y ya no aparecen en el resto del código.

El decodificador repite la codificación paso a paso. Se empieza con esos
grados y un montículo de mínimos con los vértices de grado 1. Para cada
número `c` del código, la hoja más pequeña es el vértice eliminado: se une
a `c` y se reduce el grado de `c`; cuando baja a 1, `c` se ha vuelto hoja y
entra en el montículo. Al final se ordena cada lista de adyacencia.
`O(N log N)`.

Detalles a tener en cuenta:

- este código tiene `N − 1` números y termina en `N`, uno más que el código
  de Prüfer habitual, así que `N` es la cantidad de números más uno;
- el vértice `N` nunca sale del montículo antes de tiempo: un árbol siempre
  tiene al menos dos hojas, así que siempre hay una menor;
- los números pueden repartirse entre líneas de cualquier forma, así que se
  leen como tokens;
- los límites son estrictos (0.25 segundos y 8 MB), así que la salida se
  arma en un solo búfer y las listas se guardan de forma compacta.

Las respuestas se comprobaron al revés: el árbol impreso, codificado de
nuevo según la definición, devuelve la entrada.

## Notas por lenguaje

- C++ convierte `std::priority_queue` en un montículo de mínimos con
  `std::greater`; Rust hace lo mismo con `Reverse` en un `BinaryHeap`.
- Go usa `container/heap` con un pequeño tipo `[]int`.
- Java guarda cada lista de adyacencia en un arreglo `int` del tamaño del
  grado, y las hojas en una `PriorityQueue`.
- Python usa `heapq`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1069_trees.cpp](1069_trees.cpp) | G++ 13.2 x64 | trees | O(N log N) | AC | 0.015 s | 420 KB |
| [1069_trees.go](1069_trees.go) | Go 1.14 x64 | trees | O(N log N) | AC | 0.031 s | 2564 KB |
| [1069_trees.java](1069_trees.java) | Java 1.8 | trees | O(N log N) | AC | 0.125 s | 1972 KB |
| [1069_trees.py](1069_trees.py) | Python 3.12 x64 | trees | O(N log N) | AC | 0.109 s | 3176 KB |
| [1069_trees.rs](1069_trees.rs) | Rust 1.75 x64 | trees | O(N log N) | AC | 0.062 s | 1188 KB |
