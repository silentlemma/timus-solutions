# 1498. Golpe a toda carrera

[Timus 1498](https://acm.timus.ru/problem.aspx?space=1&num=1498) · dificultad 884 · bfs

Problema original de Alex Samsonov, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un caballero está en un campo de N × M (N, M ≤ 100) y puede dar como
mucho L pasos (L ≤ 1000) a casillas vecinas, sin salir del campo ni
entrar en la casilla del demonio. Después, desde una casilla junto al
demonio, golpea una vez con fuerza K + 1, donde K es la longitud del
tramo recto recorrido justo antes del golpe. Hay que hallar la mayor
fuerza posible, o 0 si no puede llegar junto al demonio.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, M y L, luego la casilla del caballero y luego la del demonio.

## Salida

La mayor fuerza.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4 4
1 1
3 4
```

Salida:

```
4
```

## Solución

El golpe se da desde una de las como mucho cuatro casillas A junto al
demonio, tras un tramo recto de k pasos en una de cuatro direcciones,
así que el tramo empieza en S = A − k·d y todas sus casillas deben
estar en el campo y no ser la del demonio. Antes del tramo basta con
llegar a S, lo que cuesta la distancia de una búsqueda en anchura desde
el inicio con la casilla del demonio cerrada. El plan sirve cuando esa
distancia más k no pasa de L. Se prueban todas las A, todas las
direcciones y todos los k hasta que el tramo sale del campo, y se
guarda el mayor k + 1. Si el caballero llega a S moviéndose ya en la
dirección del tramo, el tramo real solo es más largo, y ese tramo más
largo también se prueba. `O(NM)`.

Detalles a tener en cuenta:

- el último tramo no tiene que apuntar al demonio: en el ejemplo el
  caballero corre a lo largo de una fila y golpea hacia abajo;
- el demonio corta tanto el camino como la carrera, así que a veces hay
  que correr por la fila o columna vecina (prueba 08);
- si ninguna casilla junto al demonio está al alcance la respuesta es 0,
  y un caballero que ya está al lado golpea con fuerza al menos 1
  (pruebas 02, 03, 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1498_bfs.cpp](1498_bfs.cpp) | G++ 13.2 x64 | bfs | O(NM) | AC | 0.015 s | 240 KB |
| [1498_bfs.go](1498_bfs.go) | Go 1.14 x64 | bfs | O(NM) | AC | 0.031 s | 2052 KB |
| [1498_bfs.java](1498_bfs.java) | Java 1.8 | bfs | O(NM) | AC | 0.125 s | 1880 KB |
| [1498_bfs.py](1498_bfs.py) | Python 3.12 x64 | bfs | O(NM) | AC | 0.109 s | 1744 KB |
| [1498_bfs.rs](1498_bfs.rs) | Rust 1.75 x64 | bfs | O(NM) | AC | 0.046 s | 276 KB |
