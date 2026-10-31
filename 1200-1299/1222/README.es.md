# 1222. El mayor producto de números con una suma dada

[Timus 1222](https://acm.timus.ru/problem.aspx?space=1&num=1222) · dificultad 144 · math

Problema original del folclore, propuesto por Leonid Volkov, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grupo de águilas con `1 ≤ N ≤ 3000` cabezas en total tiene un CI
igual al producto de las cabezas de sus águilas. Hay que hallar el mayor
CI posible; es decir, el mayor producto de enteros positivos que suman
`N`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

El mayor producto.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
```

Salida:

```
6
```

## Solución

Una parte de 4 o más se puede partir en 2 y el resto sin bajar el
producto, y una de 5 o más lo sube así (`2(k − 2) > k` para `k > 4`),
mientras que una parte de 1 solo desperdicia una cabeza. Así que un
reparto óptimo usa solo doses, treses y cuatros, y un 4 es lo mismo que
2 + 2. Tres doses son peores que dos treses (`8 < 9`), así que hay como
mucho dos doses. Queda: todo treses cuando 3 divide a `N`, un 2 más cuando
el resto es 2, y dos doses (o un 4) en lugar de un 3 cuando el resto es 1.
Para `N` hasta 3 lo mejor es el águila sola. El producto tiene hasta 478
cifras. `O(N²)` operaciones con cifras para la multiplicación repetida por
3.

Detalles a tener en cuenta:

- `N = 1` da 1, y `N = 4` da 4;
- un resto de 1 no debe quedarse como factor 1;
- la respuesta va mucho más allá de 64 bits.

Las respuestas se comprobaron con una fuerza bruta sobre todos los
repartos para cada `N` hasta 59, y se compararon con una solución escrita
aparte en todas las pruebas.

## Soluciones optimizadas

La solución optimizada en C++ multiplica un arreglo global fijo de 1000
dígitos decimales en lugar de un `std::vector` que crece con el
producto, así que el programa no necesita memoria dinámica; con
`N ≤ 3000` el producto tiene como mucho 478 dígitos:
{1222_math_optimized.cpp}.

La solución optimizada en Java lee el único número byte a byte con
`System.in.read` en lugar de crear un `Scanner`, así que la JVM no carga
el escáner ni sus expresiones regulares; la potencia con `BigInteger` es
la misma: {1222_math_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1222_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +45.83%; base: `1222_math.cpp`.

- `1222_math_optimized.java`: reducción de tiempo -34.41%; reducción de
  memoria +71.66%; base: `1222_math.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1222_math.go](1222_math.go).
- [1222_math.rs](1222_math.rs).

- Python usa sus propios enteros, Go `math/big` y Java `BigInteger`;
  C++ y Rust multiplican por 3 una y otra vez un arreglo de cifras
  decimales.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math.cpp](1222_math.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.015 s | 192 KB | 11283695 |
| [1222_math.go](1222_math.go) | Go 1.14 x64 | math | O(N²) | AC | 0.015 s | 1184 KB | 11283696 |
| [1222_math.java](1222_math.java) | Java 1.8 | math | O(N²) | AC | 0.093 s | 1708 KB | 11283698 |
| [1222_math.py](1222_math.py) | Python 3.12 x64 | math | O(N²) | AC | 0.078 s | 396 KB | 11283697 |
| [1222_math.rs](1222_math.rs) | Rust 1.75 x64 | math | O(N²) | AC | 0.031 s | 208 KB | 11283699 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math_optimized.cpp](1222_math_optimized.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.001 s | 104 KB | 11304484 |
| [1222_math_optimized.java](1222_math_optimized.java) \* | Java 1.8 | math | O(N²) | AC | 0.125 s | 484 KB | 11304486 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
