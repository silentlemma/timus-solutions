# 1120. La racha más larga de enteros positivos consecutivos con una suma dada

[Timus 1120](https://acm.timus.ru/problem.aspx?space=1&num=1120) · dificultad 87 · math

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
  pero las soluciones en C++, Go, Java y Rust usan enteros de 64 bits;
  Python usa enteros de precisión arbitraria;
- una potencia de dos no tiene divisores impares mayores que 1, así que
  solo sirve `N = 1` (prueba 08).

Las respuestas se comprobaron probando todo inicio y longitud para
`S ≤ 3000`, y para `S` mayores con la vista de divisores: existe una
racha de longitud `N` exactamente cuando `N` divide a `2S` y
`2S/N − N + 1` es positivo y par.

## Soluciones optimizadas

`1120_number_theory.py`. Factoriza parte impar de S y enumera divisores en vez de toda longitud. Cada divisor impar da d y2S/d; exige length(length+1)≤2S para inicio positivo y maximiza. División por impares, generador recursivo e enteros exactos. Desactiva JIT PyPy opcional y vacía antes de salir. Cota O(√S+τ(S)) trabajo aritmético y O(log S) estado; conserva barrido sencillo.

Frente a `1120_math.py`: tiempo 0.078 s → 0.109 s; memoria 444 KB → 308 KB.

La solución optimizada en Java analiza el número byte a byte desde
`System.in` en lugar de usar `Scanner` y actualiza el resto para la
siguiente longitud más corta en O(1): 368 KB en lugar de 1640 KB, con el
mismo tiempo.

`1120_math_optimized.rs`. Busca por bisección entera la mayor longitud con N(N+1)/2<=S y prueba longitudes descendentes hasta que S-N(N-1)/2 sea divisible por N. Elimina la raíz flotante y conserva la búsqueda descendente. Para S<=10^9 todos los productos de la bisección caben en i64. Tiempo O(log S+√S)=O(√S), espacio auxiliar O(1). La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1120_math.rs`: tiempo 0.046 s → 0.031 s; memoria 220 KB → 56 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1120_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1120_math.cpp](1120_math.cpp) | G++ 13.2 x64 | math | O(√S) | AC | 0.015 s | 128 KB | 11279266 |
| [1120_math.go](1120_math.go) | Go 1.14 x64 | math | O(√S) | AC | 0.031 s | 1064 KB | 11279268 |
| [1120_math.java](1120_math.java) | Java 1.8 | math | O(√S) | AC | 0.109 s | 1640 KB | 11279273 |
| [1120_math.py](1120_math.py) | Python 3.12 x64 | math | O(√S) | AC | 0.078 s | 444 KB | 11279271 |
| [1120_math.rs](1120_math.rs) | Rust 1.75 x64 | math | O(√S) | AC | 0.046 s | 220 KB | 11279275 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1120_math_optimized.java](1120_math_optimized.java) | Java 1.8 | math | O(√S) | AC | 0.093 s | 368 KB | 11303709 |
| [1120_math_optimized.rs](1120_math_optimized.rs) \* | Rust 1.75 x64 | math | O(√S) | AC | 0.031 s | 56 KB | 11324861 |
| [1120_number_theory.py](1120_number_theory.py) \* | PyPy 3.10 x64 | number_theory | O(√S+τ(S)) arithmetic work; O(log S) state | AC | 0.109 s | 308 KB | 11325855 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
