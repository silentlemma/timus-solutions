# 1012. Contar números en base K sin dos ceros seguidos, con aritmética de precisión arbitraria

[Timus 1012](https://acm.timus.ru/problem.aspx?space=1&num=1012) · dificultad 181 · dp

Problema original: una versión más difícil del [problema 1009](../1009/README.es.md).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuenta los números de `N` dígitos en base `K` (el primer dígito no es cero)
cuyos dígitos no contienen dos ceros seguidos. `2 ≤ K ≤ 10`, `N ≥ 2`,
`N + K ≤ 1800`.

Límite de tiempo: 0.5 segundos. Límite de memoria: 16 MB.

## Entrada

`N` y `K`, cada uno en su propia línea.

## Salida

La cantidad completa.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
2
```

Salida:

```
5
```

### Ejemplo 2

Entrada:

```
3
10
```

Salida:

```
891
```

## Solución

La recurrencia es la del [problema 1009](../1009/README.es.md): se cuentan
los prefijos válidos según su último dígito, `zero` terminan en `0` y
`other` en un dígito no nulo:

- `zero' = other`;
- `other' = (zero + other) · (K - 1)`;

empezando con `zero = 0`, `other = K - 1`; la respuesta es `zero + other`
tras `N` dígitos.

Lo que cambia es el tamaño: la respuesta tiene
hasta unas 1 800 cifras decimales, así que hace falta aritmética de
precisión arbitraria. Solo se usan dos operaciones —la suma de dos números
grandes y el producto de un número grande por uno pequeño—, ambas lineales
en la longitud. Un número grande se guarda como un arreglo de «dígitos» en
base `10^9`, el menos significativo primero: un dígito por `K - 1` más el
acarreo cabe en 64 bits. Son `N` pasos de trabajo `O(L)`, donde `L` es la
longitud de la respuesta en bloques: unas `1800 · 200` operaciones.

Solo se guardan los dos valores actuales, así que la memoria es `O(L)`;
la tabla completa de `N` números grandes también cabría, pero no hace falta.

Detalles a tener en cuenta:

- los enteros de 64 bits se desbordan pasadas unas 20 cifras: la solución
  de la versión fácil aquí es incorrecta;
- al imprimir bloques en base `10^9`, todos salvo el más significativo
  deben rellenarse con ceros a la izquierda hasta 9 cifras.

## Soluciones optimizadas

La solución optimizada en C++ guarda `zero` y `other` en dos arreglos
estáticos de 201 bloques en base `10^9`, suficientes porque la respuesta
es menor que `K^N ≤ 10^N` con `N < 1800`, y da cada paso de la
recurrencia en una sola pasada por los bloques, en el mismo sitio: el
bloque de `zero` toma el de `other`, y el de `other` pasa a ser la suma
de `(zero + other) · (K - 1)` y el acarreo, módulo `10^9`; la suma misma
queda por debajo de `18 · 10^9` y cabe en 64 bits. No se reservan ni
crecen vectores temporales en cada paso: {1012_dp_optimized.cpp}.

La solución optimizada en Go sustituye `math/big` por dos arreglos fijos
de 201 bloques en base `10^9`, suficientes porque la respuesta es menor
que `K^N ≤ 10^N` con `N < 1800`, y da cada paso de la recurrencia en una
sola pasada por los bloques, en el mismo sitio, con la suma y el
producto por `K - 1` fusionados: el valor intermedio queda por debajo de
`18 · 10^9` y cabe en 64 bits. No se crean enteros grandes nuevos en
cada paso, y los bloques se imprimen rellenados con ceros a través de
una salida con búfer: {1012_dp_optimized.go}.

La solución optimizada en Java sustituye `BigInteger` por dos arreglos
`long` de 201 bloques en base `10^9`, suficientes porque la respuesta es
menor que `K^N ≤ 10^N` con `N < 1800`, y da cada paso de la recurrencia
en una sola pasada por los bloques, en el mismo sitio, con la suma y el
producto por `K - 1` fusionados: el valor intermedio queda por debajo de
`18 · 10^9` y cabe en un `long`. Además lee los dos números byte a byte
en lugar de con `Scanner` y rellena los bloques con ceros a mano:
{1012_dp_optimized.java}.

La solución optimizada en Rust guarda `zero` y `other` en dos arreglos
fijos de 201 bloques en base `10^9`, suficientes porque la respuesta es
menor que `K^N ≤ 10^N` con `N < 1800`, y da cada paso de la recurrencia
en una sola pasada por los bloques, en el mismo sitio: el valor
intermedio `(zero + other) · (K - 1)` más el acarreo queda por debajo de
`18 · 10^9` y cabe en un `u64`. No se reservan vectores nuevos para cada
suma y producto, y los bloques van directamente a un `BufWriter` en
lugar de a una cadena más: {1012_dp_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1012_dp_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +58.21%; base: `1012_dp.cpp`.

- `1012_dp_optimized.go`: reducción de tiempo -106.67%; reducción de
  memoria +48.83%; base: `1012_dp.go`.

- `1012_dp_optimized.java`: reducción de tiempo +25.60%; reducción de
  memoria +89.02%; base: `1012_dp.java`.

- `1012_dp_optimized.rs`: reducción de tiempo +0.00%; reducción de
  memoria +58.46%; base: `1012_dp.rs`.

## Notas por lenguaje

- **Python**, **Go** (`math/big`) y **Java** (`BigInteger`) ofrecen enteros
  grandes.
- **C++** y **Rust** implementan las dos operaciones con bloques en base
  `10^9`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1012_dp.cpp](1012_dp.cpp) | G++ 13.2 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 268 KB | 11278066 |
| [1012_dp.go](1012_dp.go) | Go 1.14 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 2056 KB | 11278067 |
| [1012_dp.java](1012_dp.java) | Java 1.8 | dp | O(N·L), L = length of the answer | AC | 0.125 s | 3860 KB | 11278076 |
| [1012_dp.py](1012_dp.py) | Python 3.12 x64 | dp | O(N·L), L = length of the answer | AC | 0.062 s | 340 KB | 11278071 |
| [1012_dp.rs](1012_dp.rs) | Rust 1.75 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 520 KB | 11278084 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1012_dp_optimized.cpp](1012_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 112 KB | 11307305 |
| [1012_dp_optimized.go](1012_dp_optimized.go) \* | Go 1.14 x64 | dp | O(N·L), L = length of the answer | AC | 0.031 s | 1052 KB | 11307309 |
| [1012_dp_optimized.java](1012_dp_optimized.java) \* | Java 1.8 | dp | O(N·L), L = length of the answer | AC | 0.093 s | 424 KB | 11307307 |
| [1012_dp_optimized.rs](1012_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 216 KB | 11307310 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
