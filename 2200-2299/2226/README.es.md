# 2226. Dónde termina un paseo por la arista más corta sin usar, desde cada inicio

[Timus 2226](https://acm.timus.ru/problem.aspx?space=1&num=2226) · dificultad 1469 · dp, trees

Problema original de Vadim Barinov, del Campeonato de los Urales 2025.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un árbol tiene N vértices y aristas de longitudes distintas. Un paseo
empieza en algún vértice y siempre toma la arista más corta hacia un
vértice no visitado, hasta que no queda ninguna. Para cada vértice
inicial, imprimir dónde termina el paseo. Los límites son 1 segundo y
256 MB.

## Entrada

N, 2 ≤ N ≤ 10⁵, y luego las N − 1 aristas u v l con longitudes
distintas hasta 10⁹.

## Salida

El vértice final para cada inicio.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1 2 109
2 3 547
2 4 652
5 3 318
```

Salida:

```
5 1 5 1 1
```

## Solución

En un árbol el único vecino visitado del vértice actual es aquel del
que viene el paseo, así que el siguiente paso solo depende del vértice
actual y del anterior: es la arista más corta, o la segunda si la más
corta lleva de vuelta. De cada vértice solo hacen falta sus dos aristas
más cortas.

Se enraíza el árbol y se calculan dos valores por vértice:

- down(v), el final del paseo que acaba de llegar a v desde su padre:
  sigue por la arista más corta a un hijo c y termina en down(c), o en v
  si no hay ninguna;
- up(v), el final del paseo que acaba de pasar de v a su padre p: en p
  toma la arista más corta distinta de la que va a v, que lleva al padre
  de p (dando up(p)), a otro hijo c (dando down(c)), o no existe (el
  paseo termina en p).

down se llena de las hojas hacia arriba y up de la raíz hacia abajo, con
recorridos iterativos. Un paseo que empieza en v toma primero la arista
más corta de v, así que su final es up(v) si esa arista lleva al padre
y down(v) en otro caso.

En el ejemplo el paseo desde 1 va a 2, luego por 547 a 3, luego por 318
a 5, donde se detiene.

Esto cuesta O(N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2226_dp_trees.cpp](2226_dp_trees.cpp) | G++ 13.2 x64 | dp, trees | O(N) | AC | 0.125 s | 7784 KB |
| [2226_dp_trees.go](2226_dp_trees.go) | Go 1.14 x64 | dp, trees | O(N) | AC | 0.093 s | 21936 KB |
| [2226_dp_trees.java](2226_dp_trees.java) | Java 1.8 | dp, trees | O(N) | AC | 0.187 s | 9544 KB |
| [2226_dp_trees.py](2226_dp_trees.py) | Python 3.12 x64 | dp, trees | O(N) | AC | 0.734 s | 51044 KB |
| [2226_dp_trees.rs](2226_dp_trees.rs) | Rust 1.75 x64 | dp, trees | O(N) | AC | 0.078 s | 20468 KB |
