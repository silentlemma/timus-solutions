# 1031. El conjunto más barato de billetes de tren con tres tarifas

[Timus 1031](https://acm.timus.ru/problem.aspx?space=1&num=1031) · dificultad 390 · dp, two_pointers

Problema original del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` estaciones (`2 ≤ N ≤ 10 000`) están sobre una línea; la estación 1 está
a distancia 0 y las demás a distancias crecientes dadas (como mucho `10^9`, y
estaciones vecinas a como mucho `L3`). Un billete cubre un viaje entre dos
estaciones a distancia `X`: cuesta `C1` si `X ≤ L1`, `C2` si `L1 < X ≤ L2`,
`C3` si `L2 < X ≤ L3`, y los viajes más largos requieren varios billetes,
cambiando en estaciones (`1 ≤ L1 < L2 < L3 ≤ 10^9`,
`1 ≤ C1 < C2 < C3 ≤ 10^9`). Encuentra la forma más barata de viajar entre dos
estaciones dadas; la respuesta no supera `10^9`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`L1 L2 L3 C1 C2 C3`, luego `N`, luego las dos estaciones (en cualquier
orden) y luego las `N - 1` distancias de las estaciones 2..`N` a la
estación 1.

## Salida

El menor precio total.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 6 8 20 30 40
7
2 6
3
5
9
12
17
19
```

Salida:

```
70
```

### Ejemplo 2

Entrada:

```
1 2 3 1 2 3
2
2 1
1
```

Salida:

```
1
```

## Solución

Se intercambian las estaciones para que `a < b`; ir hacia atrás nunca
ayuda. Sea `cost[i]` la forma más barata de ir de `a` a la estación `i`,
con `cost[a] = 0`; el último billete va de alguna estación `j` a `i` y cuesta
la tarifa de la distancia `x[i] - x[j]`.

**DP cuadrática.** Se prueban todas las `j` con `x[i] - x[j] ≤ L3`. Son hasta
`N^2 / 2 = 5·10^7` pasos cuando un billete llega lejos: suficiente en C++,
no en Python.

**Tres punteros.** `cost` nunca decrece a lo largo de la línea: un camino a
la estación `i + 1` termina con un billete desde alguna `j`, y el billete de
`j` a `i` no es más largo, así que no es más caro. Por tanto, para un billete
de la tarifa `k` el mejor origen es la estación **más lejana** `j` con
`x[i] - x[j] ≤ Lk`: tiene el menor `cost` entre todos los orígenes que
alcanza esa tarifa. Al crecer `i`, esos orígenes más lejanos solo avanzan,
así que se guarda un puntero por tarifa y se adelanta mientras la distancia
supere `Lk`. Cada paso prueba tres candidatos: `O(N)` en total.

Detalles a tener en cuenta:

- las estaciones pueden venir en orden decreciente;
- un billete de una tarifa barata sirve para cualquier viaje más corto, así
  que un viaje de longitud `X ≤ L1` cuesta `C1`, no `C3`;
- la respuesta cabe en 32 bits, pero usa enteros de 64 bits para las sumas.

## Notas por lenguaje

- **C++**, **Go**, **Python**, **Java**, **Rust**: tres punteros.
- **C++** tiene además la DP cuadrática.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1031_dp.cpp](1031_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.078 s | 284 KB |
| [1031_dp_two_pointers.cpp](1031_dp_two_pointers.cpp) | G++ 13.2 x64 | dp, two_pointers | O(N) | AC | 0.015 s | 280 KB |
| [1031_dp_two_pointers.go](1031_dp_two_pointers.go) | Go 1.14 x64 | dp, two_pointers | O(N) | AC | 0.031 s | 1440 KB |
| [1031_dp_two_pointers.java](1031_dp_two_pointers.java) | Java 1.8 | dp, two_pointers | O(N) | AC | 0.093 s | 668 KB |
| [1031_dp_two_pointers.py](1031_dp_two_pointers.py) | Python 3.12 x64 | dp, two_pointers | O(N) | AC | 0.078 s | 1684 KB |
| [1031_dp_two_pointers.rs](1031_dp_two_pointers.rs) | Rust 1.75 x64 | dp, two_pointers | O(N) | AC | 0.031 s | 516 KB |
