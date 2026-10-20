# 2160. Permutaciones con el mismo árbol cartesiano

[Timus 2160](https://acm.timus.ru/problem.aspx?space=1&num=2160) · dificultad 1117 · combinatorics, trees

Problema original de Vadim Barinov, del Concurso Escolar de Programación de los Urales 2021.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos permutaciones son equivalentes cuando ambas están vacías, o sus
menores elementos están en la misma posición y las partes a su izquierda
y a su derecha son a su vez equivalentes. Contar las permutaciones de
1 … N equivalentes a la dada, módulo 10⁹ + 7. Los límites son 2 segundos
y 256 MB.

## Entrada

N, 1 ≤ N ≤ 10⁵, y luego la permutación.

## Salida

El número de permutaciones equivalentes módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
2 1 3
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
12
12 5 3 11 2 8 4 9 1 6 10 7
```

Salida:

```
34650
```

## Solución

La definición recursiva es exactamente la forma del árbol cartesiano de
la permutación: la raíz es el menor elemento, y sus subárboles izquierdo
y derecho se construyen con los dos lados. Así que hay que contar los
etiquetados de un árbol binario fijo con 1 … N en los que cada nodo es
menor que todos los nodos de su subárbol.

En un etiquetado así la raíz de cada subárbol de tamaño s debe llevar la
menor de sus s etiquetas, lo que ocurre con probabilidad 1 / s, y estos
sucesos son independientes. Por tanto la cuenta es N! dividido entre el
producto de los tamaños de todos los subárboles. El árbol cartesiano, y
con él los tamaños, sale de la pasada habitual con pila: cuando llega un
elemento menor, los elementos desapilados completan sus subárboles, y
sus tamaños se acumulan en el hijo izquierdo del elemento nuevo. La
división es una multiplicación por el inverso módulo el primo. El
trabajo es O(N).

En el primer ejemplo el árbol tiene raíz 1 con dos hojas, así que la
cuenta es 3! / (3 · 1 · 1) = 2.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2160_combinatorics_trees.cpp](2160_combinatorics_trees.cpp) | G++ 13.2 x64 | combinatorics, trees | O(N) | AC | 0.015 s | 1208 KB |
| [2160_combinatorics_trees.go](2160_combinatorics_trees.go) | Go 1.14 x64 | combinatorics, trees | O(N) | AC | 0.031 s | 5160 KB |
| [2160_combinatorics_trees.java](2160_combinatorics_trees.java) | Java 1.8 | combinatorics, trees | O(N) | AC | 0.109 s | 1196 KB |
| [2160_combinatorics_trees.py](2160_combinatorics_trees.py) | Python 3.12 x64 | combinatorics, trees | O(N) | AC | 0.125 s | 11584 KB |
| [2160_combinatorics_trees.rs](2160_combinatorics_trees.rs) | Rust 1.75 x64 | combinatorics, trees | O(N) | AC | 0.046 s | 3692 KB |
