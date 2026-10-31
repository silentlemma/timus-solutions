# 1740. ¡Mejor los renos!

[Timus 1740](https://acm.timus.ru/problem.aspx?space=1&num=1740) · dificultad 138 · math

Problema original de Sergey Pupyrev (preparado por Daniil Ayzenshteyn), del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El camino al colegio electoral mide l km. Los renos pueden correr como
quieran, siempre que cada tramo de k km tarde exactamente h horas.
Hallar el menor y el mayor tiempo posible para todo el camino.

## Entrada

Los enteros l, k y h (1 ≤ k ≤ l ≤ 1000, 1 ≤ h ≤ 1000).

## Salida

El menor y el mayor tiempo, con un error de a lo sumo 10⁻⁵.

## Ejemplos

### Ejemplo 1

Entrada:

```
30 10 1
```

Salida:

```
3.00000000 3.00000000
```

## Solución

Sea t(x) el tiempo para llegar al kilómetro x. Cada tramo de k km tarda
h horas, así que t(x + k) = t(x) + h: t crece h cada k km más una parte
que se repite cada k km. Con l = nk + r, el camino entero tarda
nh + t(r), y t(r) está entre t(0) = 0 y t(k) = h. Los renos pueden
gastar casi nada en los primeros r km de cada tramo, o casi todo, así
que las respuestas son nh y, si r > 0, (n + 1)h. `O(1)`.

En el ejemplo 30 km son tres tramos de 10 km, 3 horas en cualquier caso.

Trampas:

- cuando k divide a l las dos respuestas coinciden;
- los tiempos son enteros; el código los imprime con ocho decimales.

## Soluciones optimizadas

La solución optimizada en C++ lee los tres números con `scanf` en lugar
de `std::cin`, así que el programa no lleva la maquinaria de `iostream`;
el cálculo y la salida son los mismos: {1740_math_optimized.cpp}.

La solución optimizada en Java lee los números con un `StreamTokenizer`
en lugar de un `Scanner` y no formatea números de coma flotante: las dos
respuestas son enteros de hasta 1000 · 1000 = 10⁶, así que las calcula
en `int` y añade `.00000000` a cada una, en lugar de llamar a `printf`
con `%.8f`, cuyo formateador y datos de configuración regional cuestan
más que el resto del programa: {1740_math_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1740_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +72.28%; base: `1740_math.cpp`.

- `1740_math_optimized.java`: reducción de tiempo +0.00%; reducción de
  memoria +75.89%; base: `1740_math.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1740_math.go](1740_math.go).
- [1740_math.rs](1740_math.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1740_math.cpp](1740_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 404 KB | 11289483 |
| [1740_math.go](1740_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1092 KB | 11289484 |
| [1740_math.java](1740_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1792 KB | 11304069 |
| [1740_math.py](1740_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 404 KB | 11289486 |
| [1740_math.rs](1740_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 252 KB | 11304070 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1740_math_optimized.cpp](1740_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 112 KB | 11304455 |
| [1740_math_optimized.java](1740_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.140 s | 432 KB | 11304456 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
