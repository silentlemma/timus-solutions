# 1462. El oro del tío Scrooge

[Timus 1462](https://acm.timus.ru/problem.aspx?space=1&num=1462) · dificultad 846 · math

Problema original de Alexander Ipatov, del concurso de la Universidad Estatal de los Urales en el campus de invierno de Petrozavodsk, enero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El tío Scrooge tiene un lingote de oro por cada cadena de 0 y 1 de
longitud 2N − 2 sin dos ceros seguidos, y una caja fuerte por cada
cadena así de longitud N − 2 (3 ≤ N ≤ 70000). Cada caja recibe el mismo
número de lingotes, y los sobrantes, menos que las cajas, van a
beneficencia. Hay que hallar cuántos lingotes hay en cada caja.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

El número de lingotes de cada caja.

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

Las cadenas de longitud k sin dos ceros seguidos se cuentan con números
de Fibonacci: una cadena termina en 1 tras otra con una letra menos, o en
10 tras una dos letras más corta, así que hay F(k + 2) con
F(1) = F(2) = 1. Hay F(2N) lingotes y F(N) cajas, y la identidad
F(2N) = F(N) · L(N), con los números de Lucas L(0) = 2, L(1) = 1,
L(k + 1) = L(k) + L(k − 1), muestra que los lingotes se reparten
exactamente: la respuesta es L(N) y nada va a beneficencia.

L(70000) tiene 14630 cifras, así que se construye sumando repetidamente
números largos: Python y Java tienen enteros grandes, Go tiene math/big,
y en C++ y Rust los números se guardan en bloques de 18 cifras
decimales. `O(N²)` operaciones con bloques en total, unas decenas de
millones.

Detalles a tener en cuenta:

- la respuesta no cabe en enteros de 64 bits con signo desde N = 91,
  ni sin signo desde N = 93 (pruebas 06, 07);
- Python 3.12 se niega a imprimir enteros de más de 4300 cifras si no se
  levanta ese límite (pruebas 09, 10).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1462_math.cpp](1462_math.cpp) | G++ 13.2 x64 | math | O(N^2) | AC | 0.156 s | 444 KB |
| [1462_math.go](1462_math.go) | Go 1.14 x64 | math | O(N^2) | AC | 0.046 s | 2400 KB |
| [1462_math.java](1462_math.java) | Java 1.8 | math | O(N^2) | AC | 0.375 s | 6220 KB |
| [1462_math.py](1462_math.py) | Python 3.12 x64 | math | O(N^2) | AC | 0.125 s | 4672 KB |
| [1462_math.rs](1462_math.rs) | Rust 1.75 x64 | math | O(N^2) | AC | 0.093 s | 4272 KB |
