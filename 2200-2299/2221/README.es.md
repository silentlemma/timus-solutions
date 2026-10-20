# 2221. Tamaños de envolvente de cada subárbol de un árbol cartesiano de puntos

[Timus 2221](https://acm.timus.ru/problem.aspx?space=1&num=2221) · dificultad 1753 · geometry, trees

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2025.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N puntos con x distintas e y distintas se dividen recursivamente: el
punto más alto de un conjunto es su delegado, y los puntos a su
izquierda y a su derecha forman dos conjuntos nuevos. Para cada punto,
dar el número de vértices de la envolvente convexa del conjunto del que
es delegado (1 para un punto, 2 para un segmento). Los límites son
2 segundos y 512 MB.

## Entrada

N, 1 ≤ N ≤ 10⁵, y luego los puntos con coordenadas de valor absoluto
hasta 10⁹.

## Salida

El tamaño de la envolvente de cada punto, en el orden de entrada.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
0 0
6 4
4 7
8 9
12 1
```

Salida:

```
1
1
3
4
1
```

## Solución

Esta división es exactamente un árbol cartesiano con x como clave e y
como prioridad de montículo, construido con una pila tras ordenar por x;
el conjunto de un delegado es su subárbol, un rango contiguo de x.

La envolvente de un subárbol es su cadena inferior y su cadena
superior, construidas como en la cadena monótona de Andrew. Un punto
que no está en la envolvente del conjunto de un hijo no puede estar en
la del conjunto del padre, así que un padre solo necesita las cadenas de
sus hijos y su propio punto. Subiendo por el árbol, el padre conserva la
cadena del hijo mayor como lista enlazada e inserta al delegado y luego
los puntos de la cadena del hijo menor por el extremo más cercano de la
lista: añadiendo a la derecha si la base es izquierda, o al principio si
es derecha. Cada inserción quita los puntos que ya no hacen un giro
estricto, así que los puntos colineales desaparecen.

Menor en mayor significa que cada punto se inserta O(log n) veces, y
las extracciones nunca superan a las inserciones. El tamaño de la
envolvente es la longitud de la cadena inferior más la de la superior
menos los dos extremos compartidos, y al menos 1.

En el ejemplo el punto más alto (8, 9) es delegado de los cinco puntos,
cuya envolvente tiene 4 vértices, y (4, 7) es delegado de los tres
puntos a su izquierda, un triángulo.

Esto cuesta O(n log n).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2221_geometry_trees.cpp](2221_geometry_trees.cpp) | G++ 13.2 x64 | geometry, trees | O(n log n) | AC | 0.093 s | 6508 KB |
| [2221_geometry_trees.go](2221_geometry_trees.go) | Go 1.14 x64 | geometry, trees | O(n log n) | AC | 0.109 s | 21892 KB |
| [2221_geometry_trees.java](2221_geometry_trees.java) | Java 1.8 | geometry, trees | O(n log n) | AC | 0.328 s | 12136 KB |
| [2221_geometry_trees.py](2221_geometry_trees.py) | Python 3.12 x64 | geometry, trees | O(n log n) | AC | 0.859 s | 45392 KB |
| [2221_geometry_trees.rs](2221_geometry_trees.rs) | Rust 1.75 x64 | geometry, trees | O(n log n) | AC | 0.078 s | 15152 KB |
