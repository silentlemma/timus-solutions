# 1740. ¡Mejor los renos!

[Timus 1740](https://acm.timus.ru/problem.aspx?space=1&num=1740) · dificultad 138 · math

Problema original de Sergey Pupyrev (preparado por Daniil Ayzenshteyn), del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El camino al colegio electoral mide l km. Los renos pueden correr como
quieran, siempre que cada tramo de k km tarde exactamente h horas.
Hallar el menor y el mayor tiempo posible para todo el camino.

## Entrada

l, k y h (1 ≤ k ≤ l ≤ 1000, 1 ≤ h ≤ 1000).

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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1740_math.cpp](1740_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 404 KB |
| [1740_math.go](1740_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1092 KB |
| [1740_math.java](1740_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1800 KB |
| [1740_math.py](1740_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 404 KB |
| [1740_math.rs](1740_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 252 KB |
