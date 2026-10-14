# 1594. El tesoro azteca

[Timus 1594](https://acm.timus.ru/problem.aspx?space=1&num=1594) · dificultad 4014 · math

Problema original de Igor Chevdar, del Ural SU Contest en el campus de invierno de Petrozavodsk, febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que contar las formas de embaldosar un rectángulo l × w
(1 ≤ l, w ≤ 100) con fichas de dominó 1 × 2, módulo 10⁹ + 7.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

l y w.

## Salida

El número de embaldosados módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4
```

Salida:

```
11
```

## Solución

Un perfil sobre un lado de 100 casillas tiene 2¹⁰⁰ estados, así que la
programación dinámica habitual no sirve. La fórmula de Kasteleyn cuenta
exactamente los embaldosados de un tablero m × n:

T = ∏ ∏ (4cos²(jπ/(m + 1)) + 4cos²(kπ/(n + 1))), con j de 1 a ⌈m/2⌉ y
k de 1 a ⌈n/2⌉.

Los factores pueden quedar fuera del cuerpo primo, pero su producto es entero.
Los valores 2cos(jπ/(m + 1)), j = 1..m, son las raíces de
Sₘ(x) = Uₘ(x/2), el polinomio de Chebyshov con S₀ = 1, S₁ = x y
Sₖ₊₁ = x·Sₖ − Sₖ₋₁, de coeficientes enteros. Las raíces van en pares
±x, más 0 cuando m es impar, así que tras un factor x extra para m
impar todas las potencias son pares, y cambiar x² por y da un polinomio
mónico entero Pₘ cuyas raíces aⱼ son justo los valores
4cos²(jπ/(m + 1)) del producto. Si Q es el polinomio mónico con raíces
−bₖ para las raíces bₖ de Pₙ,

T = ∏ ∏ (aⱼ + bₖ) = Res(Pₘ, Q),

la resultante, que es el determinante de la matriz de Sylvester de los
dos polinomios. Su tamaño es como mucho 50 + 50, así que la eliminación
de Gauss módulo 10⁹ + 7 cuesta `O((l + w)³)`.

Los resultados se contrastaron con una programación dinámica por
perfiles en todos los tableros hasta 9 × 14, y en el tablero 8 × 8 dan
el conocido 12988816.

Detalles a tener en cuenta:

- con l·w impar la respuesta es 0, y la fórmula la da sola: ambos
  polinomios tienen la raíz 0;
- Q(y) = (−1)ᵉ·Pₙ(−y), e = deg Pₙ, es mónico; sin el signo, la respuesta
  cambia de signo solo si ambos grados son impares;
- los coeficientes de Sₘ crecen deprisa, así que se reducen módulo
  10⁹ + 7 en cada paso.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1594_math.cpp](1594_math.cpp) | G++ 13.2 x64 | math | O((l + w)³) | AC | 0.015 s | 392 KB |
| [1594_math.go](1594_math.go) | Go 1.14 x64 | math | O((l + w)³) | AC | 0.031 s | 1300 KB |
| [1594_math.java](1594_math.java) | Java 1.8 | math | O((l + w)³) | AC | 0.156 s | 1780 KB |
| [1594_math.py](1594_math.py) | Python 3.12 x64 | math | O((l + w)³) | AC | 0.125 s | 816 KB |
| [1594_math.rs](1594_math.rs) | Rust 1.75 x64 | math | O((l + w)³) | AC | 0.046 s | 320 KB |
