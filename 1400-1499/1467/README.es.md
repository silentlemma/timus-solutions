# 1467. Suma de potencias

[Timus 1467](https://acm.timus.ru/problem.aspx?space=1&num=1467) · dificultad 1215 · math

Problema original de Alexander Ipatov, del concurso de la Universidad Estatal de los Urales en el campus de invierno de Petrozavodsk, enero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para todo k la suma 1^k + 2^k + ... + N^k es un polinomio P(N) de grado
k + 1 con coeficientes racionales; por ejemplo, 1 + ... + N =
N(N + 1)/2. Dado 0 ≤ k ≤ 30, hay que imprimir sus k + 2 coeficientes de
la potencia mayor a la menor, como fracciones irreducibles «a/b» o
«-a/b» con b ≥ 1, y el cero como «0/1».

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

k.

## Salida

Los coeficientes de P separados por un espacio.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
1/2 1/2 0/1
```

## Solución

Es la fórmula de Faulhaber. Con los números de Bernoulli en el convenio
B₁ = +1/2,
P(N) = 1/(k + 1) · Σ C(k + 1, j) · B_j · N^(k + 1 − j) para j = 0..k,
así que el coeficiente de N^(k + 1 − j) es C(k + 1, j) B_j / (k + 1), y
el término independiente es 0. Los números de Bernoulli salen de la
identidad Σ C(m + 1, j) B_j = m + 1 para j = 0..m, que en este convenio
da B_m a partir de los anteriores:
B_m = (m + 1 − Σ_{j < m} C(m + 1, j) B_j) / (m + 1).

Toda la aritmética es exacta. Los coeficientes reducidos son pequeños,
pero las sumas intermedias no caben en 32 bits para k cerca de 30:
Python usa Fraction, Go big.Rat, Java BigInteger, y C++ y Rust enteros
de 128 bits, reduciendo cada fracción por el máximo común divisor.
`O(k²)` operaciones con fracciones; Go hace `O(k³)` operaciones
aritméticas al recalcular los coeficientes binomiales.

Detalles a tener en cuenta:

- los coeficientes de N^(k − 2), N^(k − 4), ... son cero para k ≥ 3 y
  aun así se imprimen como 0/1 (pruebas 04, 10);
- B₁ debe ser +1/2 para sumas hasta N (con −1/2 llegarían hasta N − 1);
- los productos intermedios desbordan 32 bits para k cerca de 30
  (pruebas 09, 10).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1467_math.cpp](1467_math.cpp) | G++ 13.2 x64 | math | O(k^2) | AC | 0.015 s | 232 KB |
| [1467_math.go](1467_math.go) | Go 1.14 x64 | math | O(k^3) | AC | 0.031 s | 1628 KB |
| [1467_math.java](1467_math.java) | Java 1.8 | math | O(k^2) | AC | 0.125 s | 2292 KB |
| [1467_math.py](1467_math.py) | Python 3.12 x64 | math | O(k^2) | AC | 0.078 s | 868 KB |
| [1467_math.rs](1467_math.rs) | Rust 1.75 x64 | math | O(k^2) | AC | 0.031 s | 280 KB |
