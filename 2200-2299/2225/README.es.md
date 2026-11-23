# 2225. Menos golpes de un martillo que cubre dos clavos

[Timus 2225](https://acm.timus.ru/problem.aspx?space=1&num=2225) · dificultad 422 · dsu, sorting

Problema original de Vadim Barinov, del Campeonato de los Urales 2025.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N clavos sobresalen lᵢ centímetros. Un golpe cae sobre dos clavos
vecinos: el más alto baja 1, o ambos si están igual de altos. Hallar el
menor número de golpes para clavarlos todos. Los límites son 1 segundo y
256 MB.

## Entrada

N, 2 ≤ N ≤ 10⁵, y luego l₁ … l_N con 1 ≤ lᵢ ≤ 10⁹.

## Salida

El menor número de golpes.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
4 1 3
```

Salida:

```
7
```

### Ejemplo 2

Entrada:

```
4
2 2 6 6
```

Salida:

```
8
```

## Solución

Se miran los clavos nivel por nivel, desde arriba. En el nivel h los
clavos de altura al menos h forman rachas maximales de vecinos. Un golpe
baja a lo sumo dos clavos, y solo dos clavos de la misma altura que
están juntos, así que una racha de k clavos en ese nivel necesita
⌈k / 2⌉ golpes, y clavar las rachas nivel a nivel desde arriba alcanza
exactamente esa cuenta. La respuesta es la suma de ⌈k / 2⌉ sobre todas
las rachas de todos los niveles, lo que también confirma una fuerza
bruta en casos pequeños.

Hay hasta 10⁹ niveles, pero las rachas solo cambian en las alturas de
los clavos. Se procesan los clavos del más alto hacia abajo y se une
cada uno con los vecinos ya procesados en una unión de conjuntos
disjuntos. Un clavo nuevo es una racha de longitud 1, que suma 1 en cada
nivel hasta su altura, así que suma su altura. Unir dos rachas cambia
⌈a / 2⌉ + ⌈b / 2⌉ por ⌈(a + b) / 2⌉, uno menos exactamente cuando ambas
longitudes son impares, y la racha unida dura en todos los niveles hasta
la altura actual, así que esa unión resta la altura actual.

En el primer ejemplo los niveles tienen la racha {1} en la altura 4,
{1} y {3} en las alturas 3 y 2, y {1, 2, 3} en la altura 1, así que la
respuesta es 1 + 2 + 2 + 2 = 7.

La ordenación da O(N log N).

## Soluciones optimizadas

Go suma el mismo costo por niveles con una pila monótona que construye implícitamente un árbol cartesiano de mínimos. Cada entrada guarda altura y anchura ya fusionada a su izquierda. Si la nueva altura h no supera la cima, se desapilan entradas acumulando anchuras en span. Una altura t aporta (t−max(h,altura de la cima restante))·ceil(span/2): en esos niveles el componente terminado tiene span clavos. Alturas iguales se fusionan sin desnivel adicional. Un centinela cero vacía la pila. Cada entrada entra y sale una vez: O(N) tiempo y espacio, sin ordenar ni DSU. Alturas y anchuras caben en uint32; la respuesta usa int64. Se conservan todas las bases DSU y las otras cuatro cubren el conjunto rápido.

Las implementaciones base aceptadas [2225_dsu_sorting.cpp](2225_dsu_sorting.cpp), [2225_dsu_sorting.java](2225_dsu_sorting.java), [2225_dsu_sorting.py](2225_dsu_sorting.py), [2225_dsu_sorting.rs](2225_dsu_sorting.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`2225_greedy_trees_optimized.py`. Una pila monótona representa el árbol cartesiano mínimo. Cada capa horizontal de un tramo positivo de longitud L cuesta ceil(L/2); al sacar un subárbol se suma la diferencia de alturas por ese coste. Cada valor entra y sale una vez: O(n) tiempo y espacio en lugar de ordenación y DSU. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328777 (Python 3.12 x64): **0.187 s / 3924 KB**. Comparación archivada: `2225_dsu_sorting.py` (PyPy 3.10 x64) — 0.359 s / 19808 KB (#11295847).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2225_dsu_sorting.cpp](2225_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(N log N) | AC | 0.031 s | 1788 KB | 11295843 |
| [2225_dsu_sorting.go](2225_dsu_sorting.go) | Go 1.14 x64 | dsu, sorting | O(N log N) | AC | 0.125 s | 5764 KB | 11295845 |
| [2225_dsu_sorting.java](2225_dsu_sorting.java) | Java 1.8 | dsu, sorting | O(N log N) | AC | 0.14 s | 2776 KB | 11328353 |
| [2225_dsu_sorting.py](2225_dsu_sorting.py) | PyPy 3.10 x64 | dsu, sorting | O(N log N) | AC | 0.359 s | 19808 KB | 11295847 |
| [2225_dsu_sorting.rs](2225_dsu_sorting.rs) | Rust 1.75 x64 | dsu, sorting | O(N log N) | AC | 0.062 s | 4660 KB | 11295852 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2225_trees.go](2225_trees.go) \* | Go 1.14 x64 | trees | O(N) | AC | 0.031 s | 1136 KB | 11314953 |
| [2225_greedy_trees_optimized.py](2225_greedy_trees_optimized.py) | Python 3.12 x64 | greedy, trees | O(n) time and space | AC | 0.187 s | 3924 KB | 11328777 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
