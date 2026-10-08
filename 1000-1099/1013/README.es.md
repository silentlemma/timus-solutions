# 1013. Contar números en base K sin dos ceros seguidos, módulo M

[Timus 1013](https://acm.timus.ru/problem.aspx?space=1&num=1013) · dificultad 196 · matrix

Problema original: la versión más difícil de los [problemas 1009](../1009/README.es.md) y [1012](../1012/README.es.md).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuenta, módulo `M`, los números de `N` dígitos en base `K` (el primer dígito
no es cero) cuyos dígitos no contienen dos ceros seguidos.
`2 ≤ N, K, M ≤ 10^18`.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N`, `K` y `M`, cada uno en su propia línea.

## Salida

La cantidad módulo `M`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
2
1000
```

Salida:

```
8
```

### Ejemplo 2

Entrada:

```
3
10
7
```

Salida:

```
2
```

## Solución

La recurrencia del [problema 1009](../1009/README.es.md) cuenta los prefijos
válidos según su último dígito: `zero' = other`,
`other' = (zero + other) · (K - 1)`, empezando con
`(zero, other) = (0, K - 1)` tras el primer dígito. Es una aplicación lineal
del par, así que un paso es multiplicar por la matriz

```text
A = | 0      1     |
    | K - 1  K - 1 |
```

y tras `N` dígitos el par es `A^(N-1) · (0, K - 1)`. Con `N` hasta `10^18`
los pasos no pueden hacerse uno a uno, pero `A^(N-1)` se calcula por
**exponenciación binaria**: se eleva la matriz al cuadrado y se multiplica
en el resultado por cada bit activo de `N - 1`, todo módulo `M`. Son unas
60 elevaciones al cuadrado de una matriz 2×2, `O(log N)`.

La respuesta es `(A^(N-1)[0][1] + A^(N-1)[1][1]) · (K - 1) mod M`.

Detalles a tener en cuenta:

- `K - 1` y `M` llegan a `10^18`, así que el producto de dos restos llega a
  `10^36` y no cabe en 64 bits: multiplica en 128 bits (`__int128`, `u128`,
  `bits.Mul64`) o con enteros grandes;
- reduce `K - 1` módulo `M` primero: puede ser mayor que `M`.

## Notas por lenguaje

- **C++** (`unsigned __int128`) y **Rust** (`u128`) multiplican en 128 bits.
- **Go** usa `bits.Mul64` y `bits.Div64` para el producto de 128 bits y su
  resto.
- **Java** 8 no tiene multiplicación de 128 bits, así que usa `BigInteger`;
  los enteros de **Python** no tienen límite.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1013_matrix.cpp](1013_matrix.cpp) | G++ 13.2 x64 | matrix | O(log N) | AC | 0.015 s | 136 KB |
| [1013_matrix.go](1013_matrix.go) | Go 1.14 x64 | matrix | O(log N) | AC | 0.031 s | 1072 KB |
| [1013_matrix.java](1013_matrix.java) | Java 1.8 | matrix | O(log N) | AC | 0.125 s | 1868 KB |
| [1013_matrix.py](1013_matrix.py) | Python 3.12 x64 | matrix | O(log N) | AC | 0.078 s | 400 KB |
| [1013_matrix.rs](1013_matrix.rs) | Rust 1.75 x64 | matrix | O(log N) | AC | 0.031 s | 220 KB |
