# 1325. Barro

[Timus 1325](https://acm.timus.ru/problem.aspx?space=1&num=1325) · dificultad 537 · bfs

Problema original con idea de Stanislav Vasiliev, preparado por Stanislav Vasiliev y Pavel Egorov, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un piso es una cuadrícula de N × M (N, M ≤ 500) con celdas limpias (1),
sucias (2) y paredes (0). Desde una celda se puede pasar a cualquiera
de las ocho celdas que comparten un vértice con ella, y cada paso entre
una celda limpia y una sucia obliga a cambiarse de calzado. Hay que
hallar un camino del ordenador a la nevera con el menor número de
cambios y, entre esos, con el menor número de celdas. Se imprime su
longitud en celdas, contando ambos extremos, y el número de cambios, o
0 0 si no se puede llegar a la nevera.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

N y M, la fila y la columna del ordenador, la fila y la columna de la
nevera, y luego N filas de M cifras. La celda superior izquierda es
(1, 1).

## Salida

La longitud del camino en celdas y el número de cambios.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 7
1 1
3 7
1200121
1212020
1112021
```

Salida:

```
8 4
```

### Ejemplo 2

Entrada:

```
5 5
1 5
5 1
00001
00000
00000
00000
20000
```

Salida:

```
0 0
```

## Solución

El coste de un camino es el par (cambios, pasos), comparado primero por
los cambios. Cada cambio alterna entre limpio y sucio, así que todas
las celdas alcanzadas por primera vez tras exactamente c cambios son
del mismo tipo: el del inicio si c es par y el otro si c es impar. Eso
divide la búsqueda en capas c = 0, 1, 2, ….

Dentro de la capa c, una búsqueda en anchura normal por las celdas de
ese tipo da el menor número de pasos. Sus celdas de partida, las
semillas, son las celdas de ese tipo vecinas de la capa c − 1, cada una
con el número de pasos con que se tocó por primera vez. La capa c − 1
se trató en orden de pasos, así que las semillas ya llegan ordenadas.
La búsqueda avanza nivel a nivel: en cada número de pasos primero
recoge las semillas de ese número aún no alcanzadas y luego expande las
celdas del nivel. Una celda del otro tipo que se toca pasa a ser
semilla de la capa c + 1 solo la primera vez en esta capa, que es
también su menor número de pasos. La primera capa que llega a la nevera
da la respuesta. Cada celda se fija una vez y mira ocho vecinas,
`O(N · M)`.

Detalles a tener en cuenta:

- también se puede ir en diagonal (prueba 05);
- menos cambios ganan a un camino más corto: un rodeo limpio de 9
  celdas es mejor que un camino recto de 7 con dos cambios (prueba 06);
- el ordenador y la nevera pueden estar en la misma celda: 1 0
  (prueba 03);
- sin la regla de una vez por capa, una celda puede entrar como semilla
  hasta ocho veces, lo que en un piso de 500 × 500 gasta demasiada
  memoria.

Las respuestas se compararon con el algoritmo de Dijkstra sobre el par
(cambios, pasos) en 500 pisos aleatorios de hasta 8 × 8 celdas.

## Notas por lenguaje

- CPython necesita unos 0,3 segundos con un piso completo de 500 × 500,
  demasiado cerca del límite de 0,5 segundos, así que la solución en
  Python se envía con PyPy 3.10.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1325_bfs.cpp](1325_bfs.cpp) | G++ 13.2 x64 | bfs | O(N·M) | AC | 0.031 s | 3860 KB |
| [1325_bfs.go](1325_bfs.go) | Go 1.14 x64 | bfs | O(N·M) | AC | 0.078 s | 17476 KB |
| [1325_bfs.java](1325_bfs.java) | Java 1.8 | bfs | O(N·M) | AC | 0.156 s | 9092 KB |
| [1325_bfs.py](1325_bfs.py) | PyPy 3.10 x64 | bfs | O(N·M) | AC | 0.250 s | 16492 KB |
| [1325_bfs.rs](1325_bfs.rs) | Rust 1.75 x64 | bfs | O(N·M) | AC | 0.046 s | 7628 KB |
