# 2109. Ancestro común de un tramo de vértices consecutivos

[Timus 2109](https://acm.timus.ru/problem.aspx?space=1&num=2109) · dificultad 533 · trees, dp

Problema original de Vladimir Leskov, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un árbol de n vértices tiene raíz en el vértice 1. Una ruta [L, R] va de
L a L + 1, luego a L + 2 y así hasta R, siempre por caminos del árbol.
Para cada una de las q rutas, imprimir el vértice visitado más cercano a
la raíz. Los límites son 4 segundos y 300 MB.

## Entrada

n, 1 ≤ n ≤ 2 · 10⁵, las n − 1 aristas, luego q, 0 ≤ q ≤ 10⁶, y las rutas
L ≤ R.

## Salida

La respuesta de cada ruta, una por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
1 2
1 3
2 4
2 5
2 6
3 7
3
4 6
3 4
5 7
```

Salida:

```
2
1
1
```

### Ejemplo 2

Entrada:

```
7
1 3
3 5
5 6
7 5
1 4
2 4
3
4 5
5 6
6 7
```

Salida:

```
1
5
5
```

## Solución

La ruta recorre exactamente el subárbol mínimo que une L, L + 1, …, R, y
el vértice de ese subárbol más cercano a la raíz es el ancestro común
más bajo de todo el tramo. Ese ancestro es el menos profundo de los
ancestros por pares LCA(i, i + 1) con L ≤ i < R: todos ellos están en
su subárbol, y el camino entre dos vértices de ramas hijas distintas
tiene que pasar por él.

Así que c(i) = LCA(i, i + 1) se calcula una vez para todo i, fuera de
línea, con el método de Tarjan: en una búsqueda en profundidad un vértice
terminado se une a su padre, y al entrar en el vértice v el
representante de un vecino ya visitado i ± 1 es su ancestro común. Entre
los ancestros de un vértice el menos profundo tiene el menor número en
preorden, así que se guarda ese número para c(i) y cada ruta se responde
con una consulta de mínimo en rango sobre una tabla dispersa, en O(1).
L = R se responde con el propio L.

La búsqueda es iterativa, porque el árbol puede ser un camino de 2 · 10⁵
vértices. El tiempo total es O(n log n + q).

En el primer ejemplo la ruta 4 → 5 → 6 queda bajo el vértice 2, y las
rutas 3 → 4 y 5 → 6 → 7 pasan por la raíz.

La versión didáctica en C++ calcula profundidades y padres con un recorrido en anchura. Construye una tabla de ancestros a distancias 1, 2, 4 y sucesivas potencias de dos. Para hallar LCA(i, i + 1), eleva primero el vértice más profundo hasta igualar las profundidades. Si coinciden, ese vértice es el LCA. Si quedan separados, se elevan ambos con los saltos más largos que los mantienen distintos y se toma su padre. Un árbol de segmentos guarda los LCA de pares consecutivos y devuelve el de menor profundidad. La consulta [L, R] abarca los pares que empiezan de L a R − 1. Si L = R, responde L. El tiempo es O((n + q) log(n + 1)) y el espacio es O(n log(n + 1)).

## Soluciones optimizadas

Go y CPython conservan Tarjan/DSU iterativo para LCA de IDs consecutivos y sparse table de posiciones de preorden. Al salir, un subárbol apunta al ancestro activo más cercano; consultar al vecino numérico ya visto da su LCA. Sea a el ancestro común más bajo de las ciudades de [L, R]. Si L < R y a está en el intervalo, un par consecutivo lo contiene. Si a queda fuera, algún par consecutivo pasa de un subárbol hijo de a a otro. En ambos casos ese par tiene LCA a. Todos los LCA de pares consecutivos están en el subárbol de a, así que a tiene el menor preorden. Las nuevas versiones usan arreglos de 32 bits para el grafo, los padres, los representantes, el preorden y la tabla de mínimos. Una pila de enteros con signo registra las entradas y salidas. El preorden cero indica que el vértice aún está por visitar. La tabla usa índices desde cero. El grafo y los datos temporales del DFS quedan fuera de alcance antes de construirla. Las consultas y respuestas se procesan por bloques. Si L = R se devuelve L. Si q = 0 se omiten el DFS y la tabla. Go calcula el nivel con bits.Len. Python divide bloques de 65 536 bytes, conserva el número incompleto y escribe cada 8192 respuestas. Su tabla usa arreglos de enteros sin signo. Los índices de aristas llegan a 399 998 y los valores absolutos de los eventos a 200 000. Tiempo O(n log n + q), memoria O(n log n). Las bases de C++, Java y Rust también cubren las versiones rápidas.

El envío aceptado en Python 3.12 x64 tarda 2.984 s frente a 2.875 s de la base y usa 19 348 KB frente a 222288 KB.

Las implementaciones base aceptadas [2109_trees_dp.cpp](2109_trees_dp.cpp), [2109_trees_dp.java](2109_trees_dp.java), [2109_trees_dp.rs](2109_trees_dp.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2109_trees_dp.cpp](2109_trees_dp.cpp) | G++ 13.2 x64 | trees, dp | O(n log n + q) | AC | 0.406 s | 26432 KB | 11294864 |
| [2109_trees_dp.go](2109_trees_dp.go) | Go 1.14 x64 | trees, dp | O(n log n + q) | AC | 0.296 s | 98064 KB | 11294866 |
| [2109_trees_dp.java](2109_trees_dp.java) | Java 1.8 | trees, dp | O(n log n + q) | AC | 0.468 s | 17584 KB | 11294871 |
| [2109_trees_dp.py](2109_trees_dp.py) | Python 3.12 x64 | trees, dp | O(n log n + q) | AC | 2.875 s | 222288 KB | 11294869 |
| [2109_trees_dp.rs](2109_trees_dp.rs) \* | Rust 1.75 x64 | trees, dp | O(n log n + q) | AC | 0.359 s | 77192 KB | 11294872 |
| [2109_trees_segment_tree.cpp](2109_trees_segment_tree.cpp) | G++ 13.2 x64 | trees, segment_tree | O((n + q) log(n + 1)) | AC | 0.953 s | 29604 KB | 11315899 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2109_trees_dp_optimized.go](2109_trees_dp_optimized.go) \* | Go 1.14 x64 | trees, dp | O(n log n + q) | AC | 0.25 s | 21888 KB | 11315683 |
| [2109_trees_dp_optimized.py](2109_trees_dp_optimized.py) \* | Python 3.12 x64 | trees, dp | O(n log n + q) | AC | 2.984 s | 19348 KB | 11315684 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
