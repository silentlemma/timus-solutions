# 1120. La racha más larga de enteros positivos consecutivos con una suma dada

[Timus 1120](https://acm.timus.ru/problem.aspx?space=1&num=1120) · dificultad 86 · math

Problema original de Leonid Volkov, del USU Open Collegiate Programming Contest, octubre de 2001, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado `1 ≤ S ≤ 10^9`, halla enteros positivos `A` y `N` con
`S = A + (A + 1) + … + (A + N − 1)` y `N` lo mayor posible.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`S`.

## Salida

`A N`.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
14
```

Salida:

```
2 4
```

## Solución

La racha suma `N·A + N(N − 1)/2`, así que para un `N` dado el inicio es
`A = (S − N(N − 1)/2) / N`, que debe ser un entero positivo. `A ≥ 1`
significa `N(N + 1)/2 ≤ S`, así que `N` es como mucho unos
`√(2S) ≈ 44721`. Se prueba `N` hacia abajo desde esa cota y se para en el
primero que divide; `N = 1` siempre sirve. `O(√S)`.

Detalles a tener en cuenta:

- una raíz cuadrada puede redondear hacia arriba: se empieza en
  `⌊√(2S)⌋` y se baja `N` mientras `N(N + 1)/2 > S`;
- `N(N + 1)/2` para `N ≈ 44721` es cerca de `10^9` y cabe en 32 bits,
  pero las soluciones usan 64 bits en todo;
- una potencia de dos no tiene divisores impares, así que solo sirve
  `N = 1`.

Las respuestas se comprobaron probando todo inicio y longitud para
`S ≤ 3000`, y para `S` mayores con la vista de divisores: existe una
racha de longitud `N` exactamente cuando `N` divide a `2S` y
`2S/N − N + 1` es positivo y par.

## Notas por lenguaje

- Todos los lenguajes hacen el mismo bucle descendente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1120_math.cpp](1120_math.cpp) | G++ 13.2 x64 | math | O(√S) | AC | 0.015 s | 128 KB |
| [1120_math.go](1120_math.go) | Go 1.14 x64 | math | O(√S) | AC | 0.031 s | 1064 KB |
| [1120_math.java](1120_math.java) | Java 1.8 | math | O(√S) | AC | 0.109 s | 1640 KB |
| [1120_math.py](1120_math.py) | Python 3.12 x64 | math | O(√S) | AC | 0.078 s | 444 KB |
| [1120_math.rs](1120_math.rs) | Rust 1.75 x64 | math | O(√S) | AC | 0.046 s | 220 KB |
