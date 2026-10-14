# 1605. La sucesión diabólica

[Timus 1605](https://acm.timus.ru/problem.aspx?space=1&num=1605) · dificultad 611 · math

Problema original de Alexander Ipatov, del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

x₀ = 0, x₁ = 1 y xₙ = (xₙ₋₁ + xₙ₋₂)/2. Para 2 ≤ n ≤ 100000, ¿con cuántos
seises empieza la expansión decimal de xₙ tras la coma? Por ejemplo,
x₁₀ = 0.666015625 empieza con tres.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

n.

## Salida

El número de seises iniciales.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
```

Salida:

```
3
```

## Solución

La recurrencia tiene raíces características 1 y −1/2, y los valores
iniciales dan xₙ = 2/3 − (−1)ⁿ·(2/3)·2⁻ⁿ. Como 2/3 = 0.666…, todo depende
de lo lejos que esté xₙ de ese valor y de qué lado.

Un número empieza exactamente con k seises cuando está en
[0.6…6, 0.6…6 + 10⁻ᵏ) con k seises, es decir, entre 2/3 − (2/3)·10⁻ᵏ y
2/3 + (1/3)·10⁻ᵏ. Para n par, xₙ queda por debajo de 2/3 en (2/3)·2⁻ⁿ,
así que conserva k seises mientras 10ᵏ ≤ 2ⁿ. Para n impar queda por
encima en lo mismo, así que los conserva mientras 2·10ᵏ < 2ⁿ, es decir,
10ᵏ ≤ 2ⁿ⁻¹ (la igualdad es imposible para n ≥ 2). En ambos casos la
respuesta es ⌊m·log₁₀ 2⌋ con m = n o n − 1, uno menos que el número de
cifras decimales de 2ᵐ: `O(1)`.

La fórmula se contrastó con la expansión decimal de las fracciones
exactas para n < 200 y con el número de cifras de 2ᵐ.

Detalles a tener en cuenta:

- el lado importa: x₃ = 0.75 no tiene ningún seis y x₄ = 0.625 tiene
  uno, así que los n impares usan 2ⁿ⁻¹ en vez de 2ⁿ;
- m·log₁₀ 2 puede acercarse a un entero, pero para n hasta 10⁵ nunca a
  menos de 1,5·10⁻⁵ (n = 28738), mucho más que el error de redondeo de un
  double (pruebas 08 a 10);
- simular xₙ en coma flotante pierde la diferencia con 2/3 tras unos 50
  pasos, mucho antes de n = 100000.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1605_math.cpp](1605_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1605_math.go](1605_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1072 KB |
| [1605_math.java](1605_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1620 KB |
| [1605_math.py](1605_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 436 KB |
| [1605_math.rs](1605_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 248 KB |
