# 1924. Un juego de signos con paridad invariable

[Timus 1924](https://acm.timus.ru/problem.aspx?space=1&num=1924) · difficulty 39 · math

Problema original de folclore, del concurso escolar regional de los Urales de 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los enteros de 1 a n están en orden. Dos equipos alternan colocando
un signo + o − en un espacio aún libre entre enteros consecutivos. El primero,
`black`, desea un resultado par; `grimy` desea uno impar. Ambos juegan
óptimamente y black empieza. Determinar quién gana. Para n=1 no hay
espacios y la expresión vale 1. Límites: 1 segundo y 64 MB.

## Entrada

Un entero n, 1≤n≤50.

## Salida

Escribir exactamente `black` si gana el objetivo par; en otro caso `grimy`.

## Evaluación

Se compara exactamente el único token, escrito en minúsculas.

## Ejemplos

```
1
```

```
grimy
```

```
4
```

```
black
```

## Solución

Cambiar el signo delante de un número x de + a − cambia el resultado en
2x, un número par. Así que toda expresión que puedan formar los
jugadores tiene la misma paridad que 1 + 2 + … + n = n(n + 1)/2, y
ninguna jugada cambia el ganador: gana black si esta suma es par y grimy
si es impar. `O(1)`.

Detalle: con n = 1 no hay ninguna jugada, y aun así decide la paridad
de 1.

## Soluciones optimizadas

La solución optimizada en C++ lee con `scanf` e imprime con `puts` en
lugar de `iostream`: 116 KB en lugar de 380 KB. La fórmula es la
misma.

La solución optimizada en Java analiza el número byte a byte desde
`System.in` en lugar de usar `Scanner`: 336 KB en lugar de 1616 KB, con
el mismo tiempo.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1924_math.cpp](1924_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 380 KB | 11291523 |
| [1924_math.go](1924_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1100 KB | 11291530 |
| [1924_math.java](1924_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1616 KB | 11291534 |
| [1924_math.py](1924_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 396 KB | 11291532 |
| [1924_math.rs](1924_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 236 KB | 11291542 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1924_math_optimized.cpp](1924_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 116 KB | 11303649 |
| [1924_math_optimized.java](1924_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 336 KB | 11303788 |
