# 1428. Acertijo Jedi

[Timus 1428](https://acm.timus.ru/problem.aspx?space=1&num=1428) · dificultad 499 · math

Problema original de Ilya Grebnov, Dmitry Kovalioff y Nikita Rybak, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados A, B y C (1 ≤ A, B, C ≤ 32) tales que C − 1 es divisible por A y
por B, hay que hallar enteros X, Y y Z de 1 a 10⁵⁰ con
X^A + Y^B = Z^C. Vale cualquier terna así.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

A, B y C.

## Salida

X, Y y Z, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2 3
```

Salida:

```
10
5
5
```

## Solución

Dos mitades iguales hacen un entero: 2^(C−1) + 2^(C−1) = 2^C. Como A y B
dividen a C − 1, se toma X = 2^((C−1)/A) e Y = 2^((C−1)/B), de modo que
X^A = Y^B = 2^(C−1), y Z = 2. Los números son como mucho 2³¹, muy por
debajo de 10⁵⁰, y caben en 64 bits. `O(1)`.

Detalles a tener en cuenta:

- C = 1 da X = Y = 1 y 1 + 1 = 2¹ (pruebas 03, 08);
- el ejemplo imprime otra terna, así que las pruebas usan un
  verificador con enteros grandes (prueba 01).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1428_math.cpp](1428_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1428_math.go](1428_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1064 KB |
| [1428_math.java](1428_math.java) | Java 1.8 | math | O(1) | AC | 0.156 s | 1600 KB |
| [1428_math.py](1428_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 408 KB |
| [1428_math.rs](1428_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 208 KB |
