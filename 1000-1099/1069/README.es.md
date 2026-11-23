# 1069. Reconstruir un árbol a partir de su código de Prüfer

[Timus 1069](https://acm.timus.ru/problem.aspx?space=1&num=1069) · dificultad 513 · trees

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
El contador `1 + (las veces que v aparece en el código)` es el grado para
`v != N` y el grado más uno para `N`. Antes de cada paso, los vértices que
aún quedan con contador 1 son exactamente las hojas distintas de `N`.

El decodificador repite la codificación paso a paso. Se empieza con esos
contadores y un montículo de mínimos con los vértices de contador 1. Para cada
número `c` del código, la hoja más pequeña es el vértice eliminado: se une
a `c` y se reduce el contador de `c`; cuando baja a 1, se mete `c` en el
montículo. Al final se ordena cada lista de adyacencia.
`O(N log N)`.

Detalles a tener en cuenta:

- este código tiene `N − 1` números y termina en `N`, uno más que el código
  de Prüfer habitual, así que `N` es la cantidad de números más uno;
- el vértice `N` nunca sale del montículo antes de tiempo: un árbol siempre
  tiene al menos dos hojas, así que siempre hay una menor;
- los números pueden repartirse entre líneas de cualquier forma, así que se
  leen como tokens;
- los límites son estrictos (0.25 segundos y 8 MB), así que la salida
  usa un búfer y las listas se guardan de forma compacta.

Las respuestas se comprobaron al revés: el árbol impreso, codificado de
nuevo según la definición, devuelve la entrada.

## Soluciones optimizadas

Go elimina montón de hojas y ordenar adyacencias. Un puntero monótono busca la siguiente etiqueta ausente del código restante. Tras conectar la hoja, usar inmediatamente la etiqueta del código si se agotó y es menor que el puntero. Las etiquetas anteriores ya se quitaron o aún aparecían en el código, y solo cambió ese contador. En otro caso se avanza hasta la menor hoja disponible. Se guarda el padre de cada hoja retirada. El código termina en N, que queda como raíz. Preinsertar vértices en orden decreciente deja hijos crecientes; fusionarlos con el padre al imprimir produce adyacencias ordenadas en tiempo lineal. N≤7500 permite uint16. Tiempo y espacio O(N), E/S acotada. Se conservan versiones de montón; las otras familias reutilizan las admitidas.

Las implementaciones base aceptadas [1069_trees.cpp](1069_trees.cpp), [1069_trees.java](1069_trees.java), [1069_trees.py](1069_trees.py), [1069_trees.rs](1069_trees.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1069_trees_optimized.rs`. Se mantienen el algoritmo y los tipos enteros. Los tokens decimales se convierten directamente; los negativos se acumulan con su signo para representar también el mínimo entero con signo. No cambian el almacenamiento de entrada ni la complejidad del algoritmo.

Accepted #11328491 (Rust 1.75 x64): **0.046 s / 1204 KB**. Comparación archivada: `1069_trees.rs` (Rust 1.75 x64) — 0.062 s / 1188 KB (#11278902).

## Notas por lenguaje

C++/Rust conservan montones mínimos, Java PriorityQueue y arreglos ajustados, Python heapq. Go original usa container/heap; Go nuevo usa puntero monótono y fusión de hijos/padre, uint16 y E/S acotada.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1069_trees.cpp](1069_trees.cpp) | G++ 13.2 x64 | trees | O(N log N) | AC | 0.015 s | 420 KB | 11278893 |
| [1069_trees.go](1069_trees.go) | Go 1.14 x64 | trees | O(N log N) | AC | 0.031 s | 2564 KB | 11278897 |
| [1069_trees.java](1069_trees.java) | Java 1.8 | trees | O(N log N) | AC | 0.125 s | 1972 KB | 11278900 |
| [1069_trees.py](1069_trees.py) | Python 3.12 x64 | trees | O(N log N) | AC | 0.109 s | 3176 KB | 11278899 |
| [1069_trees.rs](1069_trees.rs) | Rust 1.75 x64 | trees | O(N log N) | AC | 0.062 s | 1188 KB | 11278902 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1069_trees_two_pointers.go](1069_trees_two_pointers.go) | Go 1.14 x64 | trees, two_pointers | O(N) | AC | 0.015 s | 912 KB | 11315466 |
| [1069_trees_optimized.rs](1069_trees_optimized.rs) | Rust 1.75 x64 | trees | O(N log N) | AC | 0.046 s | 1204 KB | 11328491 |
