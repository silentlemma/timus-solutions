# 2119. Peso del subárbol que abarca un conjunto cambiante de vértices

[Timus 2119](https://acm.timus.ru/problem.aspx?space=1&num=2119) · dificultad 800 · trees, fenwick

Problema original de Alexey Danilyuk, del concurso t.me/umnik_team, campamento de Petrozavodsk, verano de 2018.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay un árbol con aristas con peso y un conjunto A de vértices que
empieza vacío. Cada consulta añade un vértice a A o lo quita. Tras cada
consulta, imprimir el peso total del menor subárbol que contiene todo A
(0 si A está vacío). Los límites son 5 segundos y 256 MB.

## Entrada

n, 1 ≤ n ≤ 3 · 10⁵, las n − 1 aristas "u v w" con 0 ≤ w ≤ 10⁹, luego q,
1 ≤ q ≤ 3 · 10⁵, y las consultas "+ v" o "− v". Un vértice solo se añade
si no está en A y solo se quita si está.

## Salida

El peso tras cada consulta, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1 2 1
2 3 10
3 4 100
3 5 1000
8
+ 2
+ 5
+ 4
- 5
+ 1
- 4
- 2
- 1
```

Salida:

```
0
1010
1110
110
111
1
0
0
```

## Solución

Se ordenan los vértices de A por su número en preorden de una búsqueda
en profundidad: v₁, v₂, …, vₖ. Recorrer v₁ → v₂ → … → vₖ → v₁ por
caminos del árbol pasa por cada arista del subárbol exactamente dos
veces, como una vuelta cerrada alrededor del subárbol, así que el peso
es la mitad de d(v₁, v₂) + … + d(vₖ, v₁). Al insertar v entre sus
vecinos cíclicos a y b en ese orden, la suma crece en
d(a, v) + d(v, b) − d(a, b); quitarlo resta lo mismo.

Los vecinos salen de un árbol de Fenwick sobre las posiciones en
preorden que marca los miembros de A: el número de posiciones marcadas
antes de v da el rango de a, y un descenso por el árbol encuentra el
elemento de un rango dado, dando la vuelta en ambos extremos. Las
distancias usan profundidades con peso, d(u, v) = D(u) + D(v) − 2 D(LCA).
Para u ≠ v con tin(u) < tin(v), el LCA es el vértice cuyo número en
preorden es el menor entre los padres de los vértices de las posiciones
tin(u) + 1 … tin(v). Una tabla dispersa sobre esos números de padre lo
responde en O(1).

La búsqueda es iterativa, porque el árbol puede ser un camino. Los pesos
llegan a 3 · 10¹⁴, así que las sumas necesitan enteros de 64 bits. El
tiempo total es O((n + q) log n).

En el ejemplo, tras "+ 2", "+ 5" y "+ 4" el subárbol es 2 – 3 – 4 más
3 – 5, con peso 10 + 100 + 1000 = 1110.

## Notas por lenguaje

La solución en Python corre en PyPy 3.10: los mismos bucles tardan varios
segundos en CPython.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2119_trees_fenwick.cpp](2119_trees_fenwick.cpp) | G++ 13.2 x64 | trees, fenwick | O((n + q) log n) | AC | 0.343 s | 46600 KB |
| [2119_trees_fenwick.go](2119_trees_fenwick.go) | Go 1.14 x64 | trees, fenwick | O((n + q) log n) | AC | 0.453 s | 47972 KB |
| [2119_trees_fenwick.java](2119_trees_fenwick.java) | Java 1.8 | trees, fenwick | O((n + q) log n) | AC | 0.546 s | 76516 KB |
| [2119_trees_fenwick.py](2119_trees_fenwick.py) | PyPy 3.10 x64 | trees, fenwick | O((n + q) log n) | AC | 1.953 s | 224172 KB |
| [2119_trees_fenwick.rs](2119_trees_fenwick.rs) | Rust 1.75 x64 | trees, fenwick | O((n + q) log n) | AC | 0.406 s | 94224 KB |
