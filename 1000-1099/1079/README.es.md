# 1079. El mayor término de la sucesión de Stern hasta n

[Timus 1079](https://acm.timus.ru/problem.aspx?space=1&num=1079) · dificultad 112 · dp

Problema original de Emil Kelevedzhiev, del Torneo de Informática del Festival Matemático de Invierno, Varna 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La sucesión es `a₀ = 0`, `a₁ = 1`, `a₂ᵢ = aᵢ` y `a₂ᵢ₊₁ = aᵢ + aᵢ₊₁` para
`i ≥ 1`. Para cada `n` dado (`1 ≤ n ≤ 99 999`) imprime el mayor de
`a₀, a₁, …, aₙ`.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Hasta diez líneas con `n` y luego una línea con 0.

## Salida

El máximo para cada `n`, uno por línea.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
10
0
```

Salida:

```
3
4
```

## Solución

Cada término solo usa términos de índice menor, así que una pasada de 2 a
99 999 llena toda la tabla, y un máximo acumulado
`best[i] = max(best[i − 1], aᵢ)` responde todas las consultas de una vez.
`O(N)` para la tabla, `O(1)` por consulta.

Es la sucesión diatómica de Stern. Algunos récords son números de Fibonacci,
alcanzados en los índices enteros `n = (2^k ± 1)/3`; el mayor valor hasta 99 999 es
2584, así que los enteros de 32 bits sobran.

Detalles a tener en cuenta:

- las consultas llegan en cualquier orden y terminan con 0, que no es una
  consulta;
- la fórmula para índices impares usa `aᵢ₊₁`, cuyo índice sigue siendo
  menor que `2i + 1`, así que el orden de la pasada es correcto.

Las respuestas se comprobaron con la definición calculada por una
recursión memorizada y un recorrido simple para cada consulta.

## Soluciones optimizadas

La solución optimizada en C++ guarda los términos solo hasta el índice
50 000, porque la fórmula para un índice hasta 99 999 no mira más allá,
y almacena los términos y los máximos acumulados en enteros de 16 bits,
que bastan porque ningún término hasta 99 999 supera 2584:
{1079_dp_optimized.cpp}.

La solución optimizada en Go guarda los términos solo hasta el índice
50 000, porque la fórmula para un índice hasta 99 999 no mira más allá,
almacena los términos y los máximos acumulados en `uint16`, que basta
porque ningún término hasta 99 999 supera 2584, y lee las consultas byte
a byte en lugar de usar `fmt.Fscan`: {1079_dp_optimized.go}.

La solución optimizada en Java guarda los términos solo hasta el índice
50 000, porque la fórmula para un índice hasta 99 999 no mira más allá,
almacena los términos y los máximos acumulados en arreglos `char` de
16 bits, que bastan porque ningún término hasta 99 999 supera 2584, y
analiza las consultas a mano desde un `BufferedInputStream` en lugar de
usar `Scanner`: {1079_dp_optimized.java}.

La solución optimizada en Python guarda los términos solo hasta el
índice 50 000, porque la fórmula para un índice hasta 99 999 no mira más
allá, y almacena los términos y los máximos acumulados en objetos
`array` de enteros de 16 bits en lugar de listas de enteros de Python;
16 bits bastan porque ningún término hasta 99 999 supera 2584:
{1079_dp_optimized.py}.

La solución optimizada en Rust guarda los términos solo hasta el índice
50 000, porque la fórmula para un índice hasta 99 999 no mira más allá,
y almacena los términos y los máximos acumulados como `u16` en lugar de
`u32`; 16 bits bastan porque ningún término hasta 99 999 supera 2584:
{1079_dp_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1079_dp_optimized.cpp`: reducción de tiempo -106.67%; reducción de
  memoria +56.67%; base: `1079_dp.cpp`.

- `1079_dp_optimized.go`: reducción de tiempo +0.00%; reducción de
  memoria +55.72%; base: `1079_dp.go`.

- `1079_dp_optimized.java`: reducción de tiempo +12.80%; reducción de
  memoria +69.20%; base: `1079_dp.java`.

- `1079_dp_optimized.py`: reducción de tiempo -12.00%; reducción de
  memoria +76.46%; base: `1079_dp.py`.

- `1079_dp_optimized.rs`: reducción de tiempo -106.67%; reducción de
  memoria +48.21%; base: `1079_dp.rs`.

## Notas por lenguaje

- Todos los lenguajes construyen ambas tablas antes de leer las
  consultas.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1079_dp.cpp](1079_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 960 KB | 11278996 |
| [1079_dp.go](1079_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 2764 KB | 11278997 |
| [1079_dp.java](1079_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 2364 KB | 11278999 |
| [1079_dp.py](1079_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.125 s | 3280 KB | 11278998 |
| [1079_dp.rs](1079_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 1004 KB | 11279000 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1079_dp_optimized.cpp](1079_dp_optimized.cpp) \* | G++ 13.2 x64 | dp | O(N) | AC | 0.031 s | 416 KB | 11304025 |
| [1079_dp_optimized.go](1079_dp_optimized.go) \* | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1224 KB | 11304026 |
| [1079_dp_optimized.java](1079_dp_optimized.java) \* | Java 1.8 | dp | O(N) | AC | 0.109 s | 728 KB | 11304027 |
| [1079_dp_optimized.py](1079_dp_optimized.py) \* | Python 3.12 x64 | dp | O(N) | AC | 0.140 s | 772 KB | 11304028 |
| [1079_dp_optimized.rs](1079_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 520 KB | 11304337 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
