# 1814. Fracción continua

[Timus 1814](https://acm.timus.ru/problem.aspx?space=1&num=1814) · dificultad 2928 · math

Problema original del Tavrida NU Akai Contest, sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Escribir √x como fracción continua infinita [a₀; a₁, a₂, …] e imprimir
su reducida de orden k, [a₀; a₁, …, aₖ], como fracción irreducible con
numerador y denominador módulo 10⁹ + 7.

## Entrada

x y k (2 ≤ x ≤ 10⁶, 0 ≤ k ≤ 10⁹); x no es un cuadrado perfecto.

## Salida

La reducida como p/q, ambos módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
```

Salida:

```
17/12
```

## Solución

Los cocientes parciales de √x son periódicos tras a₀. La recurrencia
habitual m ← d·a − m, d ← (x − m²)/d, a ← ⌊(a₀ + m)/d⌋ los produce, y el
periodo termina en el primer término igual a 2a₀. Para x ≤ 10⁶ tiene
como mucho unos pocos miles de términos. Las reducidas crecen por
productos de matrices: la matriz [[pₖ, pₖ₋₁], [qₖ, qₖ₋₁]] es
M(a₀)·M(a₁)·…·M(aₖ) con M(a) = [[a, 1], [1, 0]]. Así que se multiplica
M(a₀), luego el producto de un periodo completo elevado a ⌊k/L⌋ por
cuadrados repetidos, y luego los primeros k mod L términos del periodo,
todo módulo 10⁹ + 7. La primera columna es (p, q). Las reducidas
siempre son irreducibles, pues pₖqₖ₋₁ − pₖ₋₁qₖ = ±1, así que no hace
falta reducir antes de tomar los restos. `O(L + log k)`.

En el ejemplo √2 = [1; 2, 2, 2, …], y las reducidas son 1, 3/2, 7/5 y
17/12.

Trampas:

- la fracción debe ser irreducible antes de tomar los restos, y las
  reducidas ya lo son;
- el orden k cuenta desde 0, así que el orden 0 es a₀/1;
- d nunca llega a 0 si x no es un cuadrado, pero un cuadrado rompería
  la recurrencia del periodo.

Las respuestas coinciden con una implementación aceptada independiente
en 300 casos aleatorios y con fracciones exactas para las veinte
primeras reducidas de ocho raíces cuadradas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1814_math.cpp](1814_math.cpp) | G++ 13.2 x64 | math | O(L + log k) | AC | 0.015 s | 216 KB |
| [1814_math.go](1814_math.go) | Go 1.14 x64 | math | O(L + log k) | AC | 0.015 s | 1168 KB |
| [1814_math.java](1814_math.java) | Java 1.8 | math | O(L + log k) | AC | 0.125 s | 1984 KB |
| [1814_math.py](1814_math.py) | Python 3.12 x64 | math | O(L + log k) | AC | 0.078 s | 596 KB |
| [1814_math.rs](1814_math.rs) | Rust 1.75 x64 | math | O(L + log k) | AC | 0.015 s | 248 KB |
