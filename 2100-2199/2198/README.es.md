# 2198. Altura total de todos los árboles enraizados ordenados de N vértices

[Timus 2198](https://acm.timus.ru/problem.aspx?space=1&num=2198) · dificultad 1241 · math, combinatorics

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sumar las alturas de todos los árboles enraizados ordenados de N
vértices, módulo 10⁹ + 7. Los límites son 1 segundo y 256 MB.

## Entrada

N, 1 ≤ N ≤ 400.

## Salida

La suma módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
3
```

## Solución

Recorrer un árbol ordenado de e = N − 1 aristas, bajando y subiendo cada
arista una vez, da un camino de Dyck de 2e pasos, y es una biyección en
la que la altura del árbol es el nivel más alto del camino. La altura
total es la suma sobre h ≥ 1 del número de caminos que llegan al nivel
h.

Los caminos que se quedan en la franja de los niveles 0 a h − 1 se
cuentan reflejando respecto a las dos rectas −1 y h, lo que da una suma
alternada de coeficientes binomiales de periodo w = h + 1. Restándola de
todos los caminos y reagrupando, el número de caminos de Dyck que llegan
al nivel h es

Σ sobre k ≥ 1 de C(2e, e + kw − 1) − 2 C(2e, e + kw) + C(2e, e + kw + 1),

y solo los términos con kw ≤ e + 1 no son nulos. Así la respuesta es una
suma doble sobre los anchos w = 2 … e + 1 y sus múltiplos, unos e ln e
términos, con los binomiales C(2e, j) calculados una vez mediante
inversos modulares.

En el ejemplo los dos árboles de 3 vértices son un camino de altura 2 y
una raíz con dos hojas de altura 1, así que la respuesta es 3.

Esto cuesta O(N log N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2198_math_combinatorics.cpp](2198_math_combinatorics.cpp) | G++ 13.2 x64 | math, combinatorics | O(N log N) | AC | 0.015 s | 188 KB |
| [2198_math_combinatorics.go](2198_math_combinatorics.go) | Go 1.14 x64 | math, combinatorics | O(N log N) | AC | 0.031 s | 880 KB |
| [2198_math_combinatorics.java](2198_math_combinatorics.java) | Java 1.8 | math, combinatorics | O(N log N) | AC | 0.140 s | 216 KB |
| [2198_math_combinatorics.py](2198_math_combinatorics.py) | Python 3.12 x64 | math, combinatorics | O(N log N) | AC | 0.078 s | 272 KB |
| [2198_math_combinatorics.rs](2198_math_combinatorics.rs) | Rust 1.75 x64 | math, combinatorics | O(N log N) | AC | 0.031 s | 24 KB |
