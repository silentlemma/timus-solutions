# 1863. Átomo pacífico

[Timus 1863](https://acm.timus.ru/problem.aspx?space=1&num=1863) · dificultad 1087 · meet_in_middle

Problema original de Alexander Klepinin (preparado por Daniil Ayzenshteyn), del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las barras de control de un reactor pueden estar a cualquier
profundidad de 0 a n mm y empezaron a la profundidad s. Un registro
anota k movimientos de las barras, pero solo sus longitudes, no si cada
uno fue hacia arriba o hacia abajo; las barras nunca salieron de
[0, n]. Hallar la menor y la mayor profundidad a la que pueden estar
ahora.

## Entrada

n, s y k (0 ≤ s ≤ n ≤ 10⁹, n > 0, 1 ≤ k ≤ 40), luego las k longitudes.
Alguna elección de sentidos mantiene las barras dentro del rango.

## Salida

La menor y la mayor profundidad final posibles.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 3 3
4 5 1
```

Salida:

```
1 3
```

## Solución

Probar los 2⁴⁰ sentidos es demasiado lento, así que el registro se
parte por la mitad. Para la primera mitad se guarda el conjunto de
profundidades alcanzables sin salir de [0, n], ampliándolo movimiento a
movimiento y fusionando profundidades iguales; tiene como mucho 2²⁰
elementos.

Para la segunda mitad se recorren todas las elecciones de sentido con
una búsqueda en profundidad siguiendo tres números: el desplazamiento
total t y las sumas parciales menor y mayor, low y high. Empezando a la
profundidad x, la segunda mitad sigue en rango exactamente cuando
x + low ≥ 0 y x + high ≤ n, así que x debe estar en [−low, n − high], y
termina en x + t. Una elección se poda en cuanto high − low supera n,
pues ya no cabe ningún x. En cada elección completa, una búsqueda
binaria en las profundidades ordenadas de la primera mitad halla el
menor y el mayor x de ese intervalo, que dan la profundidad final menor
y mayor para esa elección. `O(2^(k/2)·k)`.

En el ejemplo el primer movimiento lleva de 3 a 7 (−4 bajaría de 0), y
luego 7 ± 5 da 2 o 12, donde solo 2 sigue en rango; el último movimiento
de 1 termina en 1 o 3.

Trampas:

- el rango debe cumplirse tras cada movimiento, no solo al final, y por
  eso la segunda mitad necesita sus extremos parciales y no solo su
  total;
- guardar las 2²⁰ elecciones de la segunda mitad con tres números cada
  una ocupa demasiado para 64 MB; la búsqueda en profundidad no
  necesita memoria;
- la solución en Python corre en PyPy, guarda los valores que alcanza
  cada mitad en arreglos ordenados de 32 bits en lugar de conjuntos hash
  y poda con cotas aritméticas y simetría: 11 MB en el juez, donde una
  versión anterior con conjuntos ocupaba 70 MB en la prueba 10.

Las respuestas coinciden con seguir el conjunto de profundidades
alcanzables por todo el registro en trescientos registros cortos y con
una implementación aceptada independiente en registros de 40
movimientos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1863_meet_in_middle.cpp](1863_meet_in_middle.cpp) | G++ 13.2 x64 | meet_in_middle | O(2^(k/2) k) | AC | 0.203 s | 21256 KB |
| [1863_meet_in_middle.go](1863_meet_in_middle.go) | Go 1.14 x64 | meet_in_middle | O(2^(k/2) k) | AC | 0.593 s | 43488 KB |
| [1863_meet_in_middle.java](1863_meet_in_middle.java) | Java 1.8 | meet_in_middle | O(2^(k/2) k) | AC | 0.468 s | 20896 KB |
| [1863_meet_in_middle.py](1863_meet_in_middle.py) | PyPy 3.10 x64 | meet_in_middle | O(2^(k/2) k) | AC | 0.234 s | 11232 KB |
| [1863_meet_in_middle.rs](1863_meet_in_middle.rs) | Rust 1.75 x64 | meet_in_middle | O(2^(k/2) k) | AC | 0.234 s | 13384 KB |
