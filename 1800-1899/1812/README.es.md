# 1812. La isla de la mala suerte 2

[Timus 1812](https://acm.timus.ru/problem.aspx?space=1&num=1812) · dificultad 2729 · math

Problema original del Tavrida NU Akai Contest, sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos circunferencias de radios r₁ y r₂ tocan una recta y se tocan entre
sí. En cada una de n rondas se inscribe, entre cada dos circunferencias
vecinas, una que toca la recta y a ambas. Se numeran todas a lo largo
de la recta empezando por la de radio r₁. Imprimir el radio de la
i-ésima como fracción irreducible, o "Irrational".

## Entrada

r₁, r₂, n e i (1 ≤ r₁, r₂ ≤ 1000, 0 ≤ n ≤ 30, 1 ≤ i ≤ 2ⁿ + 1).

## Salida

El radio como p/q, o "Irrational".

## Ejemplos

### Ejemplo 1

Entrada:

```
1 1 1 2
```

Salida:

```
1/4
```

### Ejemplo 2

Entrada:

```
3 5 2 4
```

Salida:

```
Irrational
```

## Solución

Dos circunferencias de radios r y s que tocan una recta y se tocan
entre sí distan 2√(rs) a lo largo de ella, y la inscrita entre ambas
cumple 1/√t = 1/√r + 1/√s. Así cada circunferencia tiene
1/√r = a/√r₁ + b/√r₂, donde los pares (a, b) se comportan como la
sucesión diatómica de Stern: los extremos tienen (1, 0) y (0, 1), y
una nueva recibe la suma de los pares de sus vecinas. El par en la
posición x tras n rondas viene del nivel anterior: una x par es una
circunferencia antigua, una x impar es la suma de las dos de al lado.
Escribiendo el valor como α·f(x) + β·f(x + 1) y dividiendo x a la
mitad n veces se obtiene (a, b) en n pasos.

Las circunferencias de los extremos conservan r₁ y r₂. Para una
interior a y b son positivos, y 1/r = a²/r₁ + b²/r₂ + 2ab/√(r₁r₂) es
racional exactamente cuando r₁r₂ es un cuadrado. Con g = mcd(r₁, r₂)
eso significa r₁ = g·p² y r₂ = g·q², y entonces
r = g·p²·q² / (a·q + b·p)². `O(n)`.

En el primer ejemplo la circunferencia central entre dos unitarias
tiene 1/√r = 2, así que r = 1/4. En el segundo 3·5 = 15 no es un
cuadrado.

Trampas:

- las circunferencias de los extremos son racionales aunque r₁r₂ no sea
  un cuadrado;
- a y b crecen como números de Fibonacci, así que (a·q + b·p)² necesita
  64 bits;
- la fracción debe reducirse.

Las respuestas coinciden con una implementación aceptada independiente
en 430 entradas, entre ellas todas las circunferencias tras hasta 3
rondas y posiciones profundas tras 30 rondas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1812_math.cpp](1812_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 128 KB |
| [1812_math.go](1812_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1080 KB |
| [1812_math.java](1812_math.java) | Java 1.8 | math | O(n) | AC | 0.109 s | 1636 KB |
| [1812_math.py](1812_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 500 KB |
| [1812_math.rs](1812_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 232 KB |
