# 1623. Laberinto fractal

[Timus 1623](https://acm.timus.ru/problem.aspx?space=1&num=1623) · dificultad 3124 · shortest_paths

Problema original del SPbSU ITMO Contest en el campus de Petrozavodsk, invierno de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una casa tiene N puertas (2 ≤ N ≤ 20) y contiene K casas interiores
(K ≤ 5), cada una copia exacta de la casa entera, así que el anidamiento
no termina nunca. M caminos de longitud 1 unen puertas de la casa
exterior y de las interiores (la casa 0 es la exterior, puertas
`casa.puerta`). Halla el camino más corto entre dos puertas dadas de la
casa exterior, o imprime `no solution`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y K, luego M y los caminos `a.b - c.d`, luego las dos puertas.

## Salida

La longitud del camino más corto, o `no solution`.

## Ejemplos

### Ejemplo 1

Entrada:

```
12 1
11
0.0 - 1.1
0.1 - 0.2
1.2 - 1.3
0.3 - 0.4
1.4 - 1.5
0.5 - 0.6
1.6 - 1.7
0.7 - 0.8
1.8 - 1.9
0.9 - 0.10
1.10 - 0.11
0 11
```

Salida:

```
11
```

### Ejemplo 2

Entrada:

```
8 0
8
0.0 - 0.2
0.1 - 0.3
0.2 - 0.4
0.3 - 0.5
0.4 - 0.6
0.5 - 0.7
0.6 - 0.0
0.7 - 0.1
2 5
```

Salida:

```
no solution
```

## Solución

Sea D(i, j) la distancia entre las puertas i y j de la casa exterior.
Atravesar una casa interior de su puerta i a su puerta j cuesta
exactamente D(i, j), porque la casa interior es una copia. Así que D es
un punto fijo: es la distancia más corta en el grafo de todas las
(K + 1) · N puertas, con los caminos y con una arista de longitud D(i, j)
entre las puertas i y j de cada casa interior.

Se empieza con D = ∞ (casas interiores cerradas) y se recalcula D a
partir del grafo una y otra vez. Tras la ronda t, D cuenta todo camino
que entra a lo sumo t casas de profundidad, así que los valores solo
bajan hacia las distancias reales; cada ronda depende solo de la
anterior, de modo que cuando una ronda no cambia nada, D es definitivo.
Una ronda ejecuta Dijkstra sobre el grafo denso desde cada una de las N
puertas exteriores. `O(R · N · ((K + 1) N)²)` para R rondas.

Detalles a tener en cuenta:

- las dos puertas pueden coincidir: la respuesta es 0 (prueba 03);
- el mejor camino puede necesitar varios niveles de anidamiento, que
  solo aparecen en rondas posteriores (prueba 04: 6 tras una ronda, 5
  tras dos);
- una puerta puede no tener ningún camino (prueba 06).

Las respuestas coinciden con una implementación aceptada independiente
en 360 laberintos aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1623_shortest_paths.cpp](1623_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(R · N · ((K + 1) N)²) | AC | 0.015 s | 552 KB |
| [1623_shortest_paths.go](1623_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(R · N · ((K + 1) N)²) | AC | 0.015 s | 3908 KB |
| [1623_shortest_paths.java](1623_shortest_paths.java) | Java 1.8 | shortest_paths | O(R · N · ((K + 1) N)²) | AC | 0.109 s | 2928 KB |
| [1623_shortest_paths.py](1623_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(R · N · ((K + 1) N)²) | AC | 0.250 s | 952 KB |
| [1623_shortest_paths.rs](1623_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(R · N · ((K + 1) N)²) | AC | 0.031 s | 340 KB |
