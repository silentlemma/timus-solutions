# 1456. Acertijo Jedi 2

[Timus 1456](https://acm.timus.ru/problem.aspx?space=1&num=1456) · dificultad 746 · number_theory

Problema original de Ilya Grebnov, Dmitry Kovalioff y Nikita Rybak, de Timus Top Coders: Second Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados A y N (2 ≤ A < N ≤ 10⁹), se calculan uno a uno los restos
Z[1] = A mod N, Z[i + 1] = Z[i] · A mod N. Hay que hallar el menor X
positivo con Z[X] = 1, es decir, el menor X con A^X ≡ 1 (mod N), o
imprimir 0 si no existe.

Límite de tiempo: 0.25 segundos. Límite de memoria: 64 MB.

## Entrada

A y N.

## Salida

X, o 0.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 20
```

Salida:

```
4
```

Los restos son 7, 9, 3 y 1.

## Solución

Si A y N comparten un factor > 1, todos los restos lo conservan y nunca
valen 1, así que la respuesta es 0. Si no, X es el orden multiplicativo
de A módulo N y, por el teorema de Euler, divide a φ(N). Se factoriza N
por división de prueba hasta √N para obtener φ(N), se factoriza φ(N) del
mismo modo y se empieza con x = φ(N): para cada primo p de φ(N) se divide
x entre p mientras A^(x / p) siga valiendo 1 módulo N. Lo que queda es
el orden, porque todo exponente que da 1 módulo N es múltiplo del
orden. Todos los productos son menores que 10¹⁸, así que bastan enteros
de 64 bits con exponenciación rápida. `O(√N + log² N)`.

Detalles a tener en cuenta:

- un factor común de A y N, incluidos A y N pares (pruebas 02, 08, 11);
- simular los restos uno a uno es demasiado lento cuando el orden se
  acerca a N (prueba 13);
- A = N − 1 tiene orden 2 (pruebas 04, 10).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1456_number_theory.cpp](1456_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt N + log^2 N) | AC | 0.031 s | 192 KB |
| [1456_number_theory.go](1456_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt N + log^2 N) | AC | 0.031 s | 1072 KB |
| [1456_number_theory.java](1456_number_theory.java) | Java 1.8 | number_theory | O(sqrt N + log^2 N) | AC | 0.140 s | 1628 KB |
| [1456_number_theory.py](1456_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt N + log^2 N) | AC | 0.078 s | 472 KB |
| [1456_number_theory.rs](1456_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt N + log^2 N) | AC | 0.015 s | 232 KB |
