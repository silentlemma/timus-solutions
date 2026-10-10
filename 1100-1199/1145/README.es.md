# 1145. El camino más largo entre dos celdas de un laberinto en forma de árbol

[Timus 1145](https://acm.timus.ru/problem.aspx?space=1&num=1145) · dificultad 353 · bfs

Problema original de Timus; no se indican autor ni fuente.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un laberinto de `n × m` celdas, `3 ≤ n, m ≤ 820`, tiene celdas libres
(`.`) y muros (`#`); se pasa entre celdas libres que comparten un lado, y
entre dos celdas libres cualesquiera hay exactamente un camino. Se atará
un hilo entre dos celdas libres que no se conocen de antemano. Halla el
hilo más corto que alcance para dos celdas libres cualesquiera, es decir,
el más largo de todos esos caminos.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`n` (el ancho) y `m` (el alto), y luego `m` filas de `n` caracteres.

## Salida

La longitud del hilo en lados de celda.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 6
#######
#.#.###
#.#.###
#.#.#.#
#.....#
#######
```

Salida:

```
8
```

## Solución

Las celdas libres con sus lados compartidos forman un árbol, y la
respuesta es el diámetro de ese árbol. Dos búsquedas en anchura lo
encuentran: desde cualquier celda libre, la celda más lejana `u` es un
extremo de algún camino más largo; desde `u`, la celda más lejana es el
otro extremo, y su distancia es la respuesta.

Por qué la primera búsqueda cae en un extremo: sea `a … b` un camino más
largo y `u` la celda más lejana del inicio `s`. El camino de `s` a `u`
encuentra el camino `a … b` (o el camino hacia él), y si `u` no estuviera
al menos tan lejos de ese punto de encuentro como `a` o `b`, uno de ellos
estaría más lejos de `s` que `u`. Así que cambiar un extremo de `a … b`
por `u` da un camino no más corto.

La cuadrícula recibe un borde de muros, así que cada celda tiene cuatro
vecinas en el array, y las celdas se numeran `r·(n + 2) + c`. Una búsqueda
es `O(n·m)`.

Detalles a tener en cuenta:

- el laberinto tiene hasta 672400 celdas, así que la búsqueda usa un
  array plano y una cola explícita, sin recursión;
- el primer número es el ancho y el segundo el alto;
- puede haber celdas libres en el borde del laberinto, de lo que se ocupa
  el borde de muros.

Las respuestas se compararon con una búsqueda en anchura desde cada celda
libre en 120 laberintos aleatorios pequeños, que además comprobó que las
celdas libres forman un árbol.

## Notas por lenguaje

- Todos los lenguajes hacen las mismas dos búsquedas sobre una cuadrícula
  plana con borde.
- Python tarda alrededor de un cuarto de segundo en los laberintos más
  grandes en nuestras ejecuciones, pero con CPython 3.12 en Timus supera
  el límite de 0,5 s en la prueba 9 (0,515 s); el mismo archivo se acepta
  con PyPy 3.10 en 0,218 s, así que la solución en Python solo pasa con
  PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1145_bfs.cpp](1145_bfs.cpp) | G++ 13.2 x64 | bfs | O(n·m) | AC | 0.046 s | 6112 KB |
| [1145_bfs.go](1145_bfs.go) | Go 1.14 x64 | bfs | O(n·m) | AC | 0.062 s | 21300 KB |
| [1145_bfs.java](1145_bfs.java) | Java 1.8 | bfs | O(n·m) | AC | 0.125 s | 9544 KB |
| [1145_bfs.py](1145_bfs.py) | PyPy 3.10 x64 | bfs | O(n·m) | AC | 0.218 s | 11572 KB |
| [1145_bfs.rs](1145_bfs.rs) | Rust 1.75 x64 | bfs | O(n·m) | AC | 0.031 s | 9556 KB |
