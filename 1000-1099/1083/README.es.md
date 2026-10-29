# 1083. Un factorial con k signos de exclamación

[Timus 1083](https://acm.timus.ru/problem.aspx?space=1&num=1083) · dificultad 68 · math

Problema original de Oleg Kats, de la Tercera Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 4 de marzo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Con `k` signos de exclamación, `n!…!` es el producto `n(n − k)(n − 2k)…`
que termina en `n mod k`, o en `k` cuando `k` divide a `n`. Por ejemplo,
`10!!! = 10 · 7 · 4 · 1`. Dados `n` (`1 ≤ n ≤ 10`) y `k` signos
(`1 ≤ k ≤ 20`), imprime el valor.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n`, un espacio y luego `k` signos de exclamación.

## Salida

El valor de `n!…!`.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
9 !!
```

Salida:

```
945
```

## Solución

Los dos finales de la definición son el último término positivo de
`n, n − k, n − 2k, …`, así que se multiplican los términos mientras sean
positivos. `O(n/k)`.

Detalles a tener en cuenta:

- `k` no es un número en la entrada sino la longitud de la cadena de
  signos;
- cuando `k ≥ n` hay un solo factor, el propio `n`;
- el mayor valor es `10! = 3 628 800`, que cabe en enteros de 32 bits.

Las respuestas se comprobaron con una lectura directa de la definición
con sus dos finales.

## Soluciones optimizadas

La solución optimizada en C++ lee `n` con `scanf` y después cuenta los
caracteres `!` uno a uno con `getchar` hasta el final de la entrada, en
lugar de leer los signos como una cadena con `iostream`: 128 KB en lugar
de 396 KB, con el mismo tiempo.

La solución optimizada en Java lee la entrada en bloques de 1 KB,
analiza `n` a mano y cuenta los signos de exclamación byte a byte en
lugar de usar `Scanner`: 0.093 s en lugar de 0.125 s y 360 KB en lugar
de 1544 KB.

## Notas por lenguaje

- Las soluciones simples en C++, Go, Java y Rust leen los signos como un
  solo token y toman su longitud; Python cuenta los caracteres `!` tras el
  espacio.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1083_math.cpp](1083_math.cpp) | G++ 13.2 x64 | math | O(n/k) | AC | 0.015 s | 396 KB | 11279022 |
| [1083_math.go](1083_math.go) | Go 1.14 x64 | math | O(n/k) | AC | 0.031 s | 1076 KB | 11279024 |
| [1083_math.java](1083_math.java) | Java 1.8 | math | O(n/k) | AC | 0.125 s | 1544 KB | 11279029 |
| [1083_math.py](1083_math.py) | Python 3.12 x64 | math | O(n/k) | AC | 0.093 s | 340 KB | 11279027 |
| [1083_math.rs](1083_math.rs) | Rust 1.75 x64 | math | O(n/k) | AC | 0.015 s | 232 KB | 11279031 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1083_math_optimized.cpp](1083_math_optimized.cpp) | G++ 13.2 x64 | math | O(n/k) | AC | 0.015 s | 128 KB | 11303546 |
| [1083_math_optimized.java](1083_math_optimized.java) | Java 1.8 | math | O(n/k) | AC | 0.093 s | 360 KB | 11303706 |
