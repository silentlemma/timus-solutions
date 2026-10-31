# 1731. Eneldo

[Timus 1731](https://acm.timus.ru/problem.aspx?space=1&num=1731) · dificultad 106 · constructive

Problema original de Eugene Kurpilyansky (preparado por Sofia Tekhazheva), del Concurso Regional de Programación por Equipos de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elegir las masas de n cajas de eneldo de la primera clase y m cajas de
la segunda, todas enteros positivos distintos hasta 10⁹, de modo que no
haya forma de regalar a dos vecinos una caja de cada clase con pesos
totales iguales.

## Entrada

n y m (2 ≤ n, m ≤ 50).

## Salida

Las n masas de la primera clase en una línea y las m de la segunda en
la siguiente. Se acepta cualquier elección válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
```

Salida:

```
1 2
5 10 12
```

## Solución

Dos regalos a + b y a′ + b′ no comparten cajas, y dos sumas con una
caja en común ya difieren porque todas las masas son distintas. Así
que la condición es que las n·m sumas a_i + b_j sean todas distintas.

Se toma a_i = i para i = 1..n y b_j = (j + 1)·n + 1 para
j = 0..m − 1. Entonces a_i + b_j = (j + 1)·n + 1 + i, y como i recorre
1..n, la suma determina tanto i como j, igual que un número en base n
determina su última cifra y el resto. Todas las masas son distintas y
la mayor es menor que 3000. `O(n + m)`.

Para el ejemplo salen 1 2 y 3 5 7, con sumas 4, 6, 8, 5, 7, 9.

Trampas:

- la respuesta siempre existe, así que nunca se imprime
  "It is a lie!";
- la segunda clase no debe repetir masas de la primera, por eso empieza
  por encima de n.

El comprobador verifica las cantidades, el rango, que las masas sean
distintas y que todas las sumas difieran.

## Soluciones optimizadas

La solución optimizada en C++ lee n y m con `scanf` en lugar de
`std::cin`, así que el programa no incluye `iostream` en absoluto; las
masas se imprimen igual: {1731_constructive_optimized.cpp}.

La solución optimizada en Java lee n y m cifra a cifra directamente
desde `System.in` en lugar de crear un `Scanner`, cuya preparación
cuesta más que el resto del programa; la salida se construye igual:
{1731_constructive_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1731_constructive_optimized.cpp`: reducción de tiempo +0.00%;
  reducción de memoria +67.02%; base: `1731_constructive.cpp`.

- `1731_constructive_optimized.java`: reducción de tiempo +45.61%;
  reducción de memoria +76.20%; base: `1731_constructive.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1731_constructive.go](1731_constructive.go).
- [1731_constructive.rs](1731_constructive.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1731_constructive.cpp](1731_constructive.cpp) | G++ 13.2 x64 | constructive | O(n + m) | AC | 0.015 s | 376 KB | 11304041 |
| [1731_constructive.go](1731_constructive.go) | Go 1.14 x64 | constructive | O(n + m) | AC | 0.046 s | 1104 KB | 11289416 |
| [1731_constructive.java](1731_constructive.java) | Java 1.8 | constructive | O(n + m) | AC | 0.171 s | 1580 KB | 11289419 |
| [1731_constructive.py](1731_constructive.py) | Python 3.12 x64 | constructive | O(n + m) | AC | 0.093 s | 416 KB | 11289417 |
| [1731_constructive.rs](1731_constructive.rs) | Rust 1.75 x64 | constructive | O(n + m) | AC | 0.046 s | 220 KB | 11304042 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1731_constructive_optimized.cpp](1731_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(n + m) | AC | 0.015 s | 124 KB | 11304262 |
| [1731_constructive_optimized.java](1731_constructive_optimized.java) | Java 1.8 | constructive | O(n + m) | AC | 0.093 s | 376 KB | 11304040 |
