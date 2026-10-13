# 1407. Un-dos, un-dos

[Timus 1407](https://acm.timus.ru/problem.aspx?space=1&num=1407) · dificultad 388 · constructive

Problema original de Sergey Pupyrev, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para 1 ≤ N ≤ 100, hay que imprimir un número de a lo sumo 10 000 cifras,
todas 1 o 2, divisible por 2ᴺ, o «No solution» si no existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

Un número así; se acepta cualquiera.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
12
```

## Solución

Siempre hay uno de exactamente N cifras, construido desde la derecha.
Sea aₖ de k cifras 1 y 2 divisible por 2ᵏ; se pone delante la cifra d:
d·10ᵏ + aₖ = 2ᵏ·(d·5ᵏ + aₖ / 2ᵏ). Como 5ᵏ es impar, exactamente una de
d = 1 y d = 2 hace par el paréntesis, lo que da aₖ₊₁ divisible por
2ᵏ⁺¹. Se empieza de la nada y se repite N veces. `O(N²)` en Go/Java,
`O(N³)` en Python.

Solo los N + 1 bits más bajos deciden la elección, así que C++ y Rust
guardan el número en 128 bits y dejan que las sumas den la vuelta; Go y
Java usan enteros grandes y miran el bit encendido más bajo.

Detalles a tener en cuenta:

- la respuesta nunca es «No solution»;
- 2¹⁰⁰ pasa de 64 bits con mucho (pruebas 07 a 09).

Se comprobó cada N de 1 a 100: el número tiene N cifras 1 y 2 y 2ᴺ lo
divide. Las pruebas se juzgan por comparación exacta, ya que la
respuesta de N cifras es única.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1407_constructive.cpp](1407_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 188 KB |
| [1407_constructive.go](1407_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.015 s | 1140 KB |
| [1407_constructive.java](1407_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.109 s | 1668 KB |
| [1407_constructive.py](1407_constructive.py) | Python 3.12 x64 | constructive | O(N^3) | AC | 0.078 s | 416 KB |
| [1407_constructive.rs](1407_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 216 KB |
