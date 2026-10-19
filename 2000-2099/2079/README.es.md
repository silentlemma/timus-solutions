# 2079. Los restos de Fibonacci que pueden seguir a uno dado

[Timus 2079](https://acm.timus.ru/problem.aspx?space=1&num=2079) · dificultad 4671 · number_theory

Problema original de Vladislav Isenbaev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los números de Fibonacci se toman módulo un primo p: x₀ = 0, x₁ = 1,
xₙ = (xₙ₋₁ + xₙ₋₂) mod p. Dado un valor x, hallar todos los valores que
pueden seguirle, es decir, todos los x_{k+1} distintos sobre los índices
k con x_k = x (los índices van mucho más allá del periodo). Los límites
son 0.5 segundos y 256 MB.

## Entrada

Un primo p, 2 ≤ p < 10⁹, y x, 0 ≤ x < p.

## Salida

El número de valores siguientes distintos y después los valores en
orden creciente, o solo 0 si x nunca aparece.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 0
```

Salida:

```
2
1 6
```

### Ejemplo 2

Entrada:

```
7 3
```

Salida:

```
1
5
```

### Ejemplo 3

Entrada:

```
11 4
```

Salida:

```
0
```

## Solución

Dos hechos hacen el trabajo. La identidad de Cassini
F(k+1)² − F(k+1) F(k) − F(k)² = (−1)ᵏ vale también módulo p, así que el
valor y que sigue a x resuelve y² − x y − (x² + s) = 0 con s = 1 o −1.
Eso da a lo sumo cuatro candidatos y = (x ± √(5x² + 4s)) / 2, con las
raíces cuadradas calculadas por el algoritmo de Tonelli–Shanks.

Pero un candidato puede no aparecer: para p = 61, x = 14 nunca
sale aunque la ecuación tiene una raíz. Para comprobar uno se
trabaja en el anillo F_p[t] / (t² − t − 1), donde tᵏ = F(k) t + F(k − 1).
El par (x, y) aparece exactamente cuando x t + (y − x) es una potencia
de t, un problema de logaritmo discreto. El periodo de la sucesión
divide a p − 1 cuando p mod 5 es 1 o 4, y a 2(p + 1) en otro caso, así
que el método de paso de bebé y paso de gigante, con m ≈ √p o √(2p)
pasos de bebé tⁱ y pasos de gigante por t⁻ᵐ = (t − 1)ᵐ, tarda O(√p)
esperado con hashing, u O(√p log p) con la tabla ordenada de C++.
Los primos hasta 50 (incluidos 2 y 5, que las fórmulas no
cubren) se resuelven recorriendo todo el periodo, de longitud a lo sumo
4p + 4.

En el primer ejemplo x = 0 da y² = ±1 módulo 7; −1 no es un cuadrado, y
tanto 1 (k = 0) como 6 (k = 8, F(9) = 34) aparecen.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2079_number_theory.cpp](2079_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt p log p) | AC | 0.015 s | 1264 KB |
| [2079_number_theory.go](2079_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt p) | AC | 0.031 s | 2528 KB |
| [2079_number_theory.java](2079_number_theory.java) | Java 1.8 | number_theory | O(sqrt p) | AC | 0.156 s | 4712 KB |
| [2079_number_theory.py](2079_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt p) | AC | 0.140 s | 8656 KB |
| [2079_number_theory.rs](2079_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt p) | AC | 0.062 s | 2436 KB |
