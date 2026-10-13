# 1385. Número interesante

[Timus 1385](https://acm.timus.ru/problem.aspx?space=1&num=1385) · dificultad 246 · math

Problema original de Alexander Ipatov, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número de 2N cifras sin cero inicial es interesante si es divisible
tanto por el número formado por sus primeras N cifras como por el
formado por sus últimas N cifras. Hay que contar los números
interesantes de 2N cifras, 1 ≤ N ≤ 10 000.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

La cantidad.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
14
```

Los catorce números son 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77,
88 y 99.

## Solución

Se escribe el número como A·10ᴺ + B, con A de N cifras y B < 10ᴺ. A
divide el número justo cuando divide a B, así que B = kA, y de
B < 10ᴺ ≤ 10A queda k de 1 a 9 (B = 0 no puede dividir nada). Después,
B divide el número cuando kA divide a A·10ᴺ, es decir, cuando k divide a
10ᴺ: k vale 1, 2 o 5, más 4 desde N = 2 y 8 desde N = 3. Para cada k, A
va desde 10ᴺ⁻¹ mientras kA < 10ᴺ, lo que da ⌈10ᴺ/k⌉ − 10ᴺ⁻¹ números.

Así, la respuesta es 14 para N = 1 y 155 para N = 2. Desde N = 3 es
900 + 400 + 150 + 100 + 25 = 1575 por 10ᴺ⁻³: las cifras 1575 y N − 3
ceros. `O(N)` para la salida.

Detalles a tener en cuenta:

- la respuesta tiene hasta 10 001 cifras, así que se imprime como texto
  (prueba 05);
- 4 y 8 no dividen a 10 ni a 100, así que N = 1 y N = 2 son casos
  especiales (pruebas 01 y 02).

Las respuestas para N hasta 3 se comprobaron probando todos los números.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1385_math.cpp](1385_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 372 KB |
| [1385_math.go](1385_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1116 KB |
| [1385_math.java](1385_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 1648 KB |
| [1385_math.py](1385_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 392 KB |
| [1385_math.rs](1385_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 224 KB |
