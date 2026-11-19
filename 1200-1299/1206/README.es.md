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

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

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

`1206_combinatorics_optimized.py`. Conserva la fórmula exacta 36*55^(K-1) y los enteros arbitrarios de Python. Tanto ** en la base como pow aquí ya calculan potencias enteras; no se atribuye un algoritmo nuevo de conteo. Una cota conservadora con aritmética escolar y conversión decimal es O(K²) de tiempo y O(K) bits de respuesta. Lee el único token y evita la función envolvente y la finalización normal. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1206_combinatorics.py`: tiempo 0.109 s → 0.14 s; memoria 416 KB → 252 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1206_combinatorics_optimized.py`: puesto de tiempo 65/76 y de memoria 2/76 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

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
| [1206_combinatorics_optimized.py](1206_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O(K²) | AC | 0.14 s | 252 KB | 11324911 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
