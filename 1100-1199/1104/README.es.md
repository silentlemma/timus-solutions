# 1104. La menor base en la que un número es divisible por la base menos uno

[Timus 1104](https://acm.timus.ru/problem.aspx?space=1&num=1104) · dificultad 95 · number_theory

Problema original de Igor Goldberg, del Tetrahedron Team Contest, mayo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número está escrito con los dígitos `0`–`9` y las letras `A`–`Z`
(`A` = 10, …, `Z` = 35), como mucho `10^6` de ellos. Halla la menor base
`k`, `2 ≤ k ≤ 36`, en la que esta cadena es un número válido divisible
por `k − 1`. Imprime `No solution.` si no la hay.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Una línea con los dígitos.

## Salida

`k` en decimal, o `No solution.`

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
A1A
```

Salida:

```
22
```

## Solución

Como `k ≡ 1 (mod k − 1)`, toda potencia de `k` da resto 1 módulo
`k − 1`, y un número en base `k` tiene el mismo resto que la suma de sus
dígitos: la misma regla que la divisibilidad por 9 en decimal. Así que se
calculan una vez la suma de dígitos `S` y el dígito mayor `m`, y se
prueba `k` desde `max(m + 1, 2)` hasta 36, imprimiendo el primero para el
que `k − 1` divide a `S`. `O(L)` para `L` dígitos.

Detalles a tener en cuenta:

- la base tiene que superar todos los dígitos, así que la búsqueda empieza
  en `m + 1`;
- en base 2 todo es divisible por 1, así que un número de ceros y unos
  siempre tiene respuesta 2, incluido un `0` solo;
- la suma de dígitos es como mucho `35 · 10^6` y cabe en 32 bits.

Las respuestas se comprobaron convirtiendo la cadena entera en cada base
con los enteros grandes de Python y tomando el resto directamente.

## Notas por lenguaje

- Python y Java leen cada dígito como dígito en base 36 con `int(ch, 36)`
  y `Character.digit`; Rust usa `to_digit(36)`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1104_number_theory.cpp](1104_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L) | AC | 0.093 s | 2640 KB |
| [1104_number_theory.go](1104_number_theory.go) | Go 1.14 x64 | number_theory | O(L) | AC | 0.031 s | 6608 KB |
| [1104_number_theory.java](1104_number_theory.java) | Java 1.8 | number_theory | O(L) | AC | 0.109 s | 5448 KB |
| [1104_number_theory.py](1104_number_theory.py) | Python 3.12 x64 | number_theory | O(L) | AC | 0.265 s | 17808 KB |
| [1104_number_theory.rs](1104_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L) | AC | 0.015 s | 7048 KB |
