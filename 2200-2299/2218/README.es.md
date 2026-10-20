# 2218. Contar puntos a una distancia Manhattan exacta

[Timus 2218](https://acm.timus.ru/problem.aspx?space=1&num=2218) · dificultad 817 · geometry, binary_search

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2025.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N computadoras distintas están en puntos enteros. Un corredor en (x, y)
debe recorrer exactamente d moviéndose según los ejes, y no puede ir a
una computadora más cercana que d. Para cada uno de Q corredores, contar
las computadoras a distancia Manhattan exactamente d. Los límites son
3 segundos y 256 MB.

## Entrada

N, 1 ≤ N ≤ 10⁵, luego las computadoras, luego Q, 1 ≤ Q ≤ 10⁵, y los
corredores x, y, d con coordenadas de valor absoluto hasta 10⁹ y
0 ≤ d ≤ 4 · 10⁹.

## Salida

La cuenta para cada corredor.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
0 0
1 1
2 0
1 -1
1 0
4
1 0 1
2 2 2
5 1 5
0 1 4
```

Salida:

```
4
2
1
0
```

## Solución

Se giran las coordenadas: u = x + y y v = x − y. La distancia Manhattan
se vuelve max(|Δu|, |Δv|), así que los puntos a distancia exactamente d
están en el borde de un cuadrado de lados paralelos a los ejes: dos
lados verticales u = U ± d con |v − V| ≤ d y dos horizontales v = V ± d
con |u − U| < d, contando las esquinas con los lados verticales.

Se ordenan los puntos por (u, v) y, por separado, por (v, u). Así cada
lado es un tramo contiguo de una de las listas, y dos búsquedas
binarias lo cuentan. Con d = 0 solo puede coincidir el propio punto del
corredor.

En el ejemplo el corredor en (1, 0) con d = 1 alcanza los cuatro
vecinos (0, 0), (1, 1), (2, 0) y (1, −1).

La ordenación cuesta O(N log N) y cada corredor requiere como máximo
ocho búsquedas binarias: ocho con d > 0 y dos con d = 0. Cuidado
(pruebas 02 y 09): con d = 0 el cuadrado se reduce a un punto, por lo
que se comprueba ese punto una sola vez en lugar de contar cuatro lados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2218_geometry_binary_search.cpp](2218_geometry_binary_search.cpp) | G++ 13.2 x64 | geometry, binary_search | O((N + Q) log N) | AC | 0.203 s | 2880 KB |
| [2218_geometry_binary_search.go](2218_geometry_binary_search.go) | Go 1.14 x64 | geometry, binary_search | O((N + Q) log N) | AC | 0.250 s | 19016 KB |
| [2218_geometry_binary_search.java](2218_geometry_binary_search.java) | Java 1.8 | geometry, binary_search | O((N + Q) log N) | AC | 0.562 s | 11280 KB |
| [2218_geometry_binary_search.py](2218_geometry_binary_search.py) | PyPy 3.10 x64 | geometry, binary_search | O((N + Q) log N) | AC | 1.453 s | 61836 KB |
| [2218_geometry_binary_search.rs](2218_geometry_binary_search.rs) | Rust 1.75 x64 | geometry, binary_search | O((N + Q) log N) | AC | 0.140 s | 12772 KB |
