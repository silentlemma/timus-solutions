# 2113. Menor altura de salto para escapar de una inundación

[Timus 2113](https://acm.timus.ru/problem.aspx?space=1&num=2113) · dificultad 425 · bfs, binary_search

Problema original de Anton Lipin, de la Olimpiada Académica Universitaria Escolar de Informática 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una liebre y el agua empiezan en casillas distintas de una cuadrícula
n × m de alturas. Juegan por turnos y empieza la liebre. La liebre se
queda quieta o salta a una casilla vecina por un lado que sea a lo sumo J
más alta que la actual. El agua inunda cada casilla que tenga una vecina
inundada al menos igual de alta. Hallar la menor altura de salto J con la
que la liebre puede no estar nunca en el agua, o −1 si ninguna sirve.
Los límites son 2 segundos y 256 MB.

## Entrada

n y m, 1 ≤ n, m ≤ 100, n · m ≠ 1, las alturas 0 ≤ hᵢⱼ ≤ 10⁵, la casilla
de la liebre y la del agua.

## Salida

La menor J, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
6 5 4
1 2 3
2 1
1 3
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
1 3
0 0 0
1 1
1 3
```

Salida:

```
-1
```

## Solución

El agua no depende de la liebre, así que una búsqueda en anchura desde
su casilla da el turno F(c) tras el que cada casilla c queda inundada
(las casillas a las que nunca llega reciben infinito). La liebre da su
paso k antes del turno k del agua y sigue allí durante él, así que puede
estar en c tras k pasos solo si F(c) > k. Esperar no ayuda: llegar antes
nunca es peor.

Para una J fija, una segunda búsqueda desde la casilla de la liebre
avanza por pasos permitidos con esos plazos. La liebre sobrevive
exactamente cuando la búsqueda llega a una casilla que nunca se inunda:
cualquier otra casilla acaba inundada. Una J mayor permite más pasos, así
que sobrevivir es monótono en J. Si ni siquiera J = 10⁵ sirve, la
respuesta es −1; si no, una búsqueda binaria sobre J halla la menor. El
tiempo total es O(n m log H).

En el primer ejemplo el agua de la esquina superior derecha inunda toda
la fila de abajo, pero nunca las casillas de altura 5 y 6. La liebre
pasa de la altura 1 a la 2 y luego sube tres unidades, a la altura 5,
justo antes de que llegue el agua.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2113_bfs_binary_search.cpp](2113_bfs_binary_search.cpp) | G++ 13.2 x64 | bfs, binary_search | O(n m log H) | AC | 0.015 s | 432 KB |
| [2113_bfs_binary_search.go](2113_bfs_binary_search.go) | Go 1.14 x64 | bfs, binary_search | O(n m log H) | AC | 0.031 s | 3712 KB |
| [2113_bfs_binary_search.java](2113_bfs_binary_search.java) | Java 1.8 | bfs, binary_search | O(n m log H) | AC | 0.125 s | 648 KB |
| [2113_bfs_binary_search.py](2113_bfs_binary_search.py) | Python 3.12 x64 | bfs, binary_search | O(n m log H) | AC | 0.125 s | 2492 KB |
| [2113_bfs_binary_search.rs](2113_bfs_binary_search.rs) | Rust 1.75 x64 | bfs, binary_search | O(n m log H) | AC | 0.046 s | 364 KB |
