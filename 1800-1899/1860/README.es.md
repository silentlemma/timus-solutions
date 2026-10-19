# 1860. Fiborial

[Timus 1860](https://acm.timus.ru/problem.aspx?space=1&num=1860) · dificultad 469 · number_theory

Problema original de Denis Dublennykh (idea de Grigoriy Nazarov), del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sean F₀ = F₁ = 1 y Fᵢ = i·Fᵢ₋₁·Fᵢ₋₂. Hallar el número de divisores de
Fₙ módulo 10⁹ + 7.

## Entrada

n (1 ≤ n ≤ 10⁶).

## Salida

El número de divisores de Fₙ módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
4
```

## Solución

Cada paso multiplica una vez por i y repite los dos productos
anteriores, así que el factor k entra en Fₙ exactamente fib(n − k + 1)
veces, con fib(1) = fib(2) = 1: aparece una vez en F_k, una en F_{k+1},
dos en F_{k+2}, y así según la regla de Fibonacci. Por tanto
Fₙ = Π k^fib(n−k+1) para k = 1 … n.

El número de divisores es Π (e_p + 1) sobre los primos p, donde e_p es
el exponente de p en Fₙ. Un número k aporta v_p(k) por su peso
fib(n − k + 1), y v_p(k) cuenta cuántos de p, p², p³, … dividen a k,
así que e_p es la suma de los pesos de todos los múltiplos de p, de p²,
etcétera. Solo importa e_p módulo 10⁹ + 7, así que los pesos también se
guardan reducidos. Recorrer los múltiplos de cada potencia de primo
lleva unos n·ln ln n pasos; la solución en Python suma cada progresión
con un solo corte. `O(n log log n)`.

En el ejemplo F₃ = 3·F₂·F₁ = 3·2·1 = 6, que tiene los divisores 1, 2, 3
y 6.

Trampas:

- los exponentes son enormes, pero la respuesta solo los necesita
  módulo 10⁹ + 7;
- una potencia de primo que pasa de n debe parar el bucle antes de
  desbordarse;
- la solución en Python corre en PyPy.

Las respuestas coinciden con una factorización directa de Fₙ para n
hasta 14 y con una implementación aceptada independiente hasta 10⁶.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1860_number_theory.cpp](1860_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log log n) | AC | 0.031 s | 15508 KB |
| [1860_number_theory.go](1860_number_theory.go) | Go 1.14 x64 | number_theory | O(n log log n) | AC | 0.046 s | 18860 KB |
| [1860_number_theory.java](1860_number_theory.java) | Java 1.8 | number_theory | O(n log log n) | AC | 0.140 s | 18448 KB |
| [1860_number_theory.py](1860_number_theory.py) | PyPy 3.10 x64 | number_theory | O(n log log n) | AC | 0.187 s | 34144 KB |
| [1860_number_theory.rs](1860_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log log n) | AC | 0.062 s | 16688 KB |
