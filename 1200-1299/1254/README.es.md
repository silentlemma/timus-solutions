# 1254. Desactivar bombas en orden por una ciudad

[Timus 1254](https://acm.timus.ru/problem.aspx?space=1&num=1254) · dificultad 646 · shortest_paths

Problema original de Pavel Atnashev, del Concurso Abierto por Equipos de la Universidad Estatal de los Urales, 15 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad es una cuadrícula de N × M (N, M ≤ 75) de manzanas libres `.`
y edificios `#`. John se mueve entre manzanas vecinas, por un lado o en
diagonal, a velocidad V. Desde (x₀, y₀) debe desactivar K bombas
(K ≤ 1000) en el orden dado; una bomba a la que no puede llegar se salta.
Hay que hallar el menor tiempo total, con dos decimales.

Límite de tiempo: 5 segundos. Límite de memoria: 64 MB.

## Entrada

N, M, K y V; el mapa como M líneas de N caracteres; el inicio; las K
bombas como `x y`.

## Salida

El menor tiempo, con dos cifras tras el punto.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3 3 1.23
....
##..
....
1 1
1 3
4 1
4 3
```

Salida:

```
8.66
```

## Solución

Desactivar es instantáneo y el orden está fijado, así que el total es la
suma de los caminos más cortos desde cada posición hasta la siguiente
bomba alcanzable, dividida entre V. Un paso por un lado mide 1 y uno en
diagonal √2; un paso en diagonal puede pasar por la esquina de un
edificio, cosa que el ejemplo necesita al pasar junto a `##`.

Hacen falta hasta 1000 búsquedas de camino mínimo sobre 5625 casillas.
Tres cosas las abaratan:

- la ciudad se divide una vez en partes unidas por movimientos, así que
  una bomba en otra parte se salta enseguida en vez de tras una búsqueda
  completa;
- cada búsqueda es A* con la distancia octil
  `max(dx, dy) + (√2 − 1)·min(dx, dy)` como estimación, que nunca supera
  la longitud real, así que la primera vez que la bomba sale de la cola su
  distancia ya es definitiva, y en ciudad abierta la estimación es exacta;
- los caminos ya hallados se guardan por su par de extremos, en los dos
  sentidos.

El mapa está rodeado de un borde de edificios, así que los movimientos
no necesitan comprobar límites. `O(K · NM log NM)` en el peor caso.

Detalles a tener en cuenta:

- tras una bomba inalcanzable John se queda donde estaba (prueba 03);
- el inicio puede coincidir con una bomba, un camino de longitud 0
  (prueba 02);
- la casilla inicial se considera libre, diga lo que diga el mapa.

Los totales se compararon con un Dijkstra simple en 300 ciudades
pequeñas aleatorias con edificios y bombas inalcanzables.

## Notas por lenguaje

- Python es aquí el más lento: alrededor de 1.5 s en la calle sinuosa
  más grande de las pruebas, con un límite de 5 segundos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1254_shortest_paths.cpp](1254_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(K · NM log NM) | AC | 0.140 s | 312 KB |
| [1254_shortest_paths.go](1254_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(K · NM log NM) | AC | 0.328 s | 6896 KB |
| [1254_shortest_paths.java](1254_shortest_paths.java) | Java 1.8 | shortest_paths | O(K · NM log NM) | AC | 0.531 s | 7204 KB |
| [1254_shortest_paths.py](1254_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(K · NM log NM) | AC | 2.906 s | 1740 KB |
| [1254_shortest_paths.rs](1254_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(K · NM log NM) | AC | 0.140 s | 808 KB |
