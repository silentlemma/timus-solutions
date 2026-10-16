# 1817. Tiovivo

[Timus 1817](https://acm.timus.ru/problem.aspx?space=1&num=1817) · dificultad 1008 · probability

Problema original del Tavrida NU Akai Contest, sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tiovivo tiene n caballos y gira un caballo por segundo. Un niño se
acerca a un caballo al azar; si está ocupado, espera al siguiente, y
así hasta que llega uno libre. Nadie se baja. Para cada número de
jinetes de 0 a n − 1, hallar la espera esperada del siguiente niño, con
error de como mucho 10⁻⁶.

## Entrada

n (2 ≤ n ≤ 20).

## Salida

n líneas: la espera esperada en segundos cuando montan 0, 1, …, n − 1
niños.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
0.000000
0.250000
0.687500
1.500000
```

## Solución

Un niño toma el primer caballo libre desde una posición aleatoria, que
es justo una inserción en una tabla hash circular con sondeo lineal, y
la espera es el número de caballos ocupados que pasan. El análisis de
Knuth del sondeo lineal en una tabla de n celdas con k claves da como
número medio de sondeos de una búsqueda fallida (1 + Q)/2 con
Q = Σⱼ (j + 1)·k(k − 1)…(k − j + 1)/nʲ, sumando j = 0 … k. La espera es
un sondeo menos: (Q − 1)/2. Cada línea es una suma corta. `O(n²)`.

Para n = 4 y dos jinetes, Q = 1 + 2·(2/4) + 3·(2·1/16) = 2,375, así que
la espera es 0,6875.

Trampas:

- la esperanza es sobre cómo se sentaron los niños anteriores, no sobre
  caballos ocupados uniformemente al azar: los tramos ocupados crecen
  más deprisa;
- con k jinetes la suma se detiene en j = k;
- una simulación directa sobre las 2²⁰ ocupaciones vale en un lenguaje
  compilado pero requiere cuidado en los demás; la fórmula la evita.

Las respuestas coinciden, para todo n de 2 a 20, con una
implementación aceptada independiente que sigue la probabilidad de cada
conjunto de caballos ocupados, salvo en la última cifra donde el valor
exacto 0,3419875 se redondea distinto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1817_probability.cpp](1817_probability.cpp) | G++ 13.2 x64 | probability | O(n^2) | AC | 0.015 s | 140 KB |
| [1817_probability.go](1817_probability.go) | Go 1.14 x64 | probability | O(n^2) | AC | 0.046 s | 1088 KB |
| [1817_probability.java](1817_probability.java) | Java 1.8 | probability | O(n^2) | AC | 0.140 s | 1792 KB |
| [1817_probability.py](1817_probability.py) | Python 3.12 x64 | probability | O(n^2) | AC | 0.093 s | 452 KB |
| [1817_probability.rs](1817_probability.rs) | Rust 1.75 x64 | probability | O(n^2) | AC | 0.015 s | 276 KB |
