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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2109_trees_dp.cpp](2109_trees_dp.cpp) | G++ 13.2 x64 | trees, dp | O(n log n + q) | AC | 0.406 s | 26432 KB |
| [2109_trees_dp.go](2109_trees_dp.go) | Go 1.14 x64 | trees, dp | O(n log n + q) | AC | 0.296 s | 98064 KB |
| [2109_trees_dp.java](2109_trees_dp.java) | Java 1.8 | trees, dp | O(n log n + q) | AC | 0.468 s | 17584 KB |
| [2109_trees_dp.py](2109_trees_dp.py) | Python 3.12 x64 | trees, dp | O(n log n + q) | AC | 2.875 s | 222288 KB |
| [2109_trees_dp.rs](2109_trees_dp.rs) | Rust 1.75 x64 | trees, dp | O(n log n + q) | AC | 0.359 s | 77192 KB |
