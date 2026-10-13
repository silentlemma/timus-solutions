# 1441. De la historia del banco Gringotts

[Timus 1441](https://acm.timus.ru/problem.aspx?space=1&num=1441) · dificultad 1132 · graphs

Problema original de Magaz Asanov (idea), Stanislav Vasiliev (texto) y Pavel Zuev (preparación), del Décimo Campeonato Universitario de Programación por Equipos de los Urales, 24–25 de marzo de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los duendes cavaron M túneles entre N salas del banco
(2 ≤ N ≤ 20000, 1 ≤ M ≤ 20000); ningún túnel une una sala consigo misma,
no hay dos túneles entre el mismo par de salas, y todas las salas están
conectadas. Cada túnel lo cavó un hipergusano, y un hipergusano puede
cavar toda una cadena de túneles en la que cada uno empieza en la sala
donde acabó el anterior, pero nunca recorre un túnel ya existente. Hay
que hallar el menor número K de hipergusanos que pudieron cavar todos
los túneles y la ruta de cada uno.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N y M, y luego M pares de salas unidas por túneles.

## Salida

K, y luego K líneas, cada una con las salas que recorre un hipergusano
en orden. Se acepta cualquier plan válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 7
1 2
4 1
6 7
5 7
7 4
2 3
4 2
```

Salida:

```
3
5 7 4 2 1 4
2 3
6 7
```

## Solución

La ruta de cada hipergusano es un camino que usa cada túnel como mucho
una vez. Una sala con un número impar de túneles tiene que ser extremo
de algún camino, así que con 2k salas impares hacen falta al menos k
caminos, y al menos uno en todo caso. Con esos basta siempre: se añade
un vértice auxiliar unido a cada sala impar, con lo que todos los grados
son pares y el grafo conexo tiene un circuito euleriano. Quitar las k
aristas auxiliares corta el circuito en k caminos de túneles reales; sin
salas impares, el propio circuito es la única ruta.

El circuito sale del algoritmo de Hierholzer con una pila explícita:
desde el vértice de la cima se toma la siguiente arista sin usar o, si
no queda ninguna, el vértice pasa de la pila al circuito; un puntero por
vértice hace que cada arista se mire una sola vez. Una ruta por 20000
salas sería demasiado profunda para la recursión. `O(N + M)`.

Detalles a tener en cuenta:

- sin salas impares la respuesta es una ruta cerrada, no cero (pruebas
  03, 07, gen2);
- una estrella hace impares casi todas las salas (pruebas 04, gen3);
- la ruta puede pasar varias veces por una sala (pruebas 05, 09).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1441_graphs.cpp](1441_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.046 s | 2604 KB |
| [1441_graphs.go](1441_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.062 s | 8992 KB |
| [1441_graphs.java](1441_graphs.java) | Java 1.8 | graphs | O(N + M) | AC | 0.140 s | 5212 KB |
| [1441_graphs.py](1441_graphs.py) | Python 3.12 x64 | graphs | O(N + M) | AC | 0.140 s | 13552 KB |
| [1441_graphs.rs](1441_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.031 s | 4688 KB |
