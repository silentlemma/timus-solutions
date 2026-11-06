# 1090. La fila de reclutas que más salta: contar inversiones

[Timus 1090](https://acm.timus.ru/problem.aspx?space=1&num=1090) · dificultad 366 · fenwick, binary_search

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
  pero las soluciones con Fenwick suman en 64 bits;
- en caso de empate gana la primera fila, así que solo un total
  estrictamente mayor sustituye al mejor;
- el árbol debe vaciarse para cada fila.

Las respuestas se comprobaron con recuentos de inversiones por ordenación
por mezcla, y para `N ≤ 300` también con el doble bucle.

## Soluciones optimizadas

Las versiones de C++ y Go conservan el árbol de Fenwick y leen la entrada mediante un búfer de tamaño fijo. Cada contador del árbol tiene como máximo N y cabe en 16 bits. La versión para PyPy reemplaza la lista ordenada con un árbol de Fenwick, con consultas de prefijo e inserciones en O(log N). Las tres versiones usan O(K·N log N) tiempo y O(N) espacio adicional.

Las implementaciones base aceptadas [1090_fenwick.java](1090_fenwick.java), [1090_fenwick.rs](1090_fenwick.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

La versión didáctica Python usa una lista ordenada con búsqueda binaria y fue aceptada con PyPy 3.10. El mismo fuente con CPython 3.12 superó el límite de tiempo en la prueba 9 (0,515 s). La versión Python optimizada usa un árbol de Fenwick y también fue aceptada con PyPy 3.10. La tabla indica el intérprete real de cada envío aceptado.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1090_binary_search.py](1090_binary_search.py) | PyPy 3.10 x64 | binary_search | O(K·N^2) | AC | 0.437 s | 20044 KB | 11279088 |
| [1090_fenwick.cpp](1090_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(K·N log N) | AC | 0.156 s | 236 KB | 11279084 |
| [1090_fenwick.go](1090_fenwick.go) | Go 1.14 x64 | fenwick | O(K·N log N) | AC | 0.046 s | 1916 KB | 11279085 |
| [1090_fenwick.java](1090_fenwick.java) \* | Java 1.8 | fenwick | O(K·N log N) | AC | 0.125 s | 512 KB | 11279089 |
| [1090_fenwick.rs](1090_fenwick.rs) \* | Rust 1.75 x64 | fenwick | O(K·N log N) | AC | 0.015 s | 2120 KB | 11279090 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1090_fenwick_optimized.cpp](1090_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(K·N log N) | AC | 0.015 s | 104 KB | 11310324 |
| [1090_fenwick_optimized.go](1090_fenwick_optimized.go) \* | Go 1.14 x64 | fenwick | O(K·N log N) | AC | 0.031 s | 816 KB | 11310344 |
| [1090_fenwick.py](1090_fenwick.py) \* | PyPy 3.10 x64 | fenwick | O(K·N log N) | AC | 0.156 s | 9076 KB | 11310319 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
