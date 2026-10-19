# 1869. Crucero de Año Nuevo

[Timus 1869](https://acm.timus.ru/problem.aspx?space=1&num=1869) · dificultad 239 · prefix_sums

Problema original de Denis Dublennykh, del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tren va de Vladivostok (estación 1) a Moscú (estación n) parando en
las estaciones 1, …, n, y luego vuelve por el mismo camino. aᵢⱼ
personas compraron billete de la estación i a la j: viajan en el tren
de ida si i < j y en el de vuelta si i > j. Cada vagón tiene 36
asientos. ¿Cuántos vagones necesita el tren para que todos tengan
asiento?

## Entrada

n (2 ≤ n ≤ 100), luego la matriz n × n de aᵢⱼ (0 ≤ aᵢⱼ ≤ 1000,
aᵢᵢ = 0).

## Salida

El menor número de vagones.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 180 180
0 0 180
360 0 0
```

Salida:

```
10
```

## Solución

El tren debe llevar el mayor número de personas a bordo a la vez, en
cualquier tramo y en cualquier sentido. Para cada sentido se suma aᵢⱼ
en la estación de menor número y se resta en la de mayor número. La suma acumulada de
estos cambios por orden de estación es la carga de cada tramo. La
respuesta es la mayor carga dividida entre 36 y redondeada hacia
arriba. `O(n²)`.

En el ejemplo viajan 360 personas en el tren de ida en ambos tramos
(los 180 de la estación 1 a la 3 junto con los 180 de la 1 a la 2 o de
la 2 a la 3), y 360 vuelven todo el camino: 10 vagones.

Trampas:

- los dos sentidos son viajes distintos, así que sus cargas no se
  suman;
- la división redondea hacia arriba: 37 personas necesitan dos vagones;
- sin ningún billete la respuesta es 0.

Las respuestas coinciden con una implementación aceptada independiente
en 150 matrices aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1869_prefix_sums.cpp](1869_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 196 KB |
| [1869_prefix_sums.go](1869_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(n^2) | AC | 0.031 s | 1244 KB |
| [1869_prefix_sums.java](1869_prefix_sums.java) | Java 1.8 | prefix_sums | O(n^2) | AC | 0.109 s | 448 KB |
| [1869_prefix_sums.py](1869_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(n^2) | AC | 0.093 s | 1440 KB |
| [1869_prefix_sums.rs](1869_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 344 KB |
