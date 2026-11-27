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

Python didáctico mantiene ordenados los valores anteriores. bisect da
el índice de inserción: i-index valores anteriores son mayores y aportan
esas inversiones. list.insert desplaza el sufijo para mantener el orden;
los valores de la fila son distintos. Buscar cuesta O(log N), desplazar
O(N) por inserción: total O(K N^2). Lista/corte de la fila actual usa
O(N) palabras de trabajo; esta implementación además conserva O(KN)
enteros de toda la entrada, aparte de ese estado.

Detalles a tener en cuenta:

- el máximo N(N-1)/2=49 995 000 cabe en 32 bits con signo. Las bases
  C++/Go/Java/Rust suman en 64 bits; C++ optimizado usa int y Go
  optimizado int nativo, seguros con esta cota. Python usa enteros
  sin límite.
- en caso de empate gana la primera fila, así que solo un total
  estrictamente mayor sustituye al mejor;
- el árbol debe vaciarse para cada fila.

Las respuestas se comprobaron con recuentos de inversiones por ordenación
por mezcla, y para `N ≤ 300` también con el doble bucle.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

Las versiones de C++ y Go conservan el árbol de Fenwick y leen la entrada mediante un búfer de tamaño fijo. Cada contador del árbol tiene como máximo N y cabe en 16 bits. La versión para PyPy reemplaza la lista ordenada con un árbol de Fenwick, con consultas de prefijo e inserciones en O(log N). Las tres versiones usan O(K·N log N) tiempo y O(N) espacio adicional.

La caché actual confirma Java simple solo por puesto temporal bajo
1 MiB. Rust simple no pasa ambas métricas de referencia pequeña del
compilador exacto; Rust optimizado separado sí cumple su referencia
temporal bajo 1 MiB. C++ optimizado usa puesto temporal, Go referencia
temporal pequeña, y PyPy exige y pasa ambos puestos ordinarios. Rigen
los [criterios compartidos](../../RATING_CRITERIA.md); se conservan
todas las bases y se reutilizan fuentes que cumplen sin copias iguales.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1090_fenwick_implementation_optimized.rs`. Se leen tokens con un búfer nativo acotado; los cortos se guardan dentro del objeto y solo los largos reservan espacio extra. La conversión decimal conserva las cotas con signo sin guardar toda la entrada de comandos. La entrada de C llama directamente al solucionador y vacía la salida de Rust antes de volver; se conserva la implementación de entrada habitual.

Accepted #11328959 (Rust 1.75 x64): **0.015 s / 224 KB**. Comparación archivada: `1090_fenwick.rs` (Rust 1.75 x64) — 0.015 s / 2120 KB (#11279090).

La revisión actual de 1090_fenwick_implementation_optimized.rs solo
nombra la capacidad intacta de token inline de 32 bytes. Se conservan algoritmo Fenwick, base y comentarios sustantivos.

## Notas por lenguaje

La versión didáctica Python usa una lista ordenada con búsqueda binaria y fue aceptada con PyPy 3.10. El mismo fuente con CPython 3.12 superó el límite de tiempo en la prueba 9 (0,515 s). La versión Python optimizada usa un árbol de Fenwick y también fue aceptada con PyPy 3.10. La tabla indica el intérprete real de cada envío aceptado.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1090_binary_search.py](1090_binary_search.py) | PyPy 3.10 x64 | binary_search | O(K·N^2) | AC | 0.437 s | 20044 KB | 11279088 |
| [1090_fenwick.cpp](1090_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(K·N log N) | AC | 0.156 s | 236 KB | 11279084 |
| [1090_fenwick.go](1090_fenwick.go) | Go 1.14 x64 | fenwick | O(K·N log N) | AC | 0.046 s | 1916 KB | 11279085 |
| [1090_fenwick.java](1090_fenwick.java) | Java 1.8 | fenwick | O(K·N log N) | AC | 0.125 s | 512 KB | 11279089 |
| [1090_fenwick.rs](1090_fenwick.rs) | Rust 1.75 x64 | fenwick | O(K·N log N) | AC | 0.015 s | 2120 KB | 11279090 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1090_fenwick_optimized.cpp](1090_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(K·N log N) | AC | 0.015 s | 104 KB | 11310324 |
| [1090_fenwick_optimized.go](1090_fenwick_optimized.go) | Go 1.14 x64 | fenwick | O(K·N log N) | AC | 0.031 s | 816 KB | 11310344 |
| [1090_fenwick.py](1090_fenwick.py) | PyPy 3.10 x64 | fenwick | O(K·N log N) | AC | 0.156 s | 9076 KB | 11310319 |
| [1090_fenwick_implementation_optimized.rs](1090_fenwick_implementation_optimized.rs) | Rust 1.75 x64 | fenwick, implementation | O(K·N log N) | AC | 0.015 s | 232 KB | 11331115 |
