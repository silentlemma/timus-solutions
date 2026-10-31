# 1206. Pares de números cuyas sumas de cifras se suman

[Timus 1206](https://acm.timus.ru/problem.aspx?space=1&num=1206) · dificultad 124 · combinatorics

Problema original de Leonid Volkov, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sea `S(N)` la suma de las cifras de `N`. Para `2 ≤ K ≤ 50`, hay que
contar los pares ordenados de números de `K` cifras `A` y `B`, sin ceros
a la izquierda, con `S(A + B) = S(A) + S(B)`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`K`.

## Salida

El número de pares.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
1980
```

## Solución

Cada acarreo en la suma convierte un 10 en una posición en un 1 en la
siguiente, y baja la suma de cifras en 9. Así que la igualdad se cumple
exactamente cuando no hay acarreos, es decir, cuando las cifras de cada
posición suman como mucho 9. Entonces las posiciones son independientes.
En la posición más alta ambas cifras van de 1 a 9, lo que da
`8 + 7 + … + 1 = 36` pares; en cada una de las otras `K − 1` posiciones
las cifras van de 0 a 9, lo que da `10 + 9 + … + 1 = 55` pares. La
respuesta es `36 · 55^(K−1)`, un número de hasta 87 cifras. `O(K²)` con
la multiplicación escolar.

Detalles a tener en cuenta:

- la respuesta supera los 64 bits ya con `K = 12`;
- las cifras más altas no pueden ser 0, así que su número de pares es
  distinto.

La fórmula se comprobó por fuerza bruta sobre todos los pares para
`K = 2` y `K = 3`, y cada `K` se comparó con una solución escrita aparte.

## Soluciones optimizadas

La solución optimizada en C++ multiplica igualmente las cifras decimales
por 55, pero en un arreglo fijo de 100 elementos en la pila en lugar de
un `std::vector` que crece: como `K ≤ 50`, la respuesta `36 · 55^(K−1)`
es menor que `100^K` y tiene como mucho 100 cifras (en realidad, como
mucho 87). Sin `<vector>` el programa no lleva código de contenedores:
{1206_combinatorics_optimized.cpp}.

La solución optimizada en Java lee `K` byte a byte de `System.in` en
lugar de crear un `Scanner`, cuyas expresiones regulares y datos de
configuración regional cuestan más que la propia potencia; la respuesta
se sigue calculando con `BigInteger`:
{1206_combinatorics_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1206_combinatorics_optimized.cpp`: reducción de tiempo +0.00%;
  reducción de memoria +46.81%; base: `1206_combinatorics.cpp`.

- `1206_combinatorics_optimized.java`: reducción de tiempo +10.71%;
  reducción de memoria +74.37%; base: `1206_combinatorics.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1206_combinatorics.rs](1206_combinatorics.rs).

- Python usa sus propios enteros, Go `math/big` y Java `BigInteger`;
  C++ y Rust multiplican `K − 1` veces por 55 un arreglo de cifras
  decimales.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1206_combinatorics.cpp](1206_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 188 KB | 11283595 |
| [1206_combinatorics.go](1206_combinatorics.go) | Go 1.14 x64 | combinatorics | O(K²) | AC | 0.031 s | 1200 KB | 11283596 |
| [1206_combinatorics.java](1206_combinatorics.java) | Java 1.8 | combinatorics | O(K²) | AC | 0.140 s | 1748 KB | 11283601 |
| [1206_combinatorics.py](1206_combinatorics.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.109 s | 416 KB | 11283600 |
| [1206_combinatorics.rs](1206_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(K²) | AC | 0.015 s | 212 KB | 11283602 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1206_combinatorics_optimized.cpp](1206_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 100 KB | 11304421 |
| [1206_combinatorics_optimized.java](1206_combinatorics_optimized.java) \* | Java 1.8 | combinatorics | O(K²) | AC | 0.125 s | 448 KB | 11304422 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
