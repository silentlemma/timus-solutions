# 1057. Sumas de K potencias distintas de B en un intervalo

[Timus 1057](https://acm.timus.ru/problem.aspx?space=1&num=1057) · dificultad 718 · combinatorics

Problema original de la Academia Estatal de Aviación de Rybinsk.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuenta los enteros de `[X, Y]` (`1 ≤ X ≤ Y ≤ 2^31 − 1`) que son suma de
exactamente `K` potencias distintas de `B` con exponentes enteros
(`1 ≤ K ≤ 20`, `2 ≤ B ≤ 10`).

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`X` e `Y`, luego `K` y luego `B`.

## Salida

La cantidad.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
15 20
2
2
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
1 100
1
10
```

Salida:

```
3
```

## Solución

Las potencias negativas distintas de `B` suman menos que 1, así que una
suma entera usa solo exponentes no negativos. Un número así es
exactamente uno cuyas cifras en base `B` son todas 0 o 1, con `K` unos. Se
cuentan en `[0, n]` con una función `f(n)`; la respuesta es
`f(Y) − f(X − 1)`.

Para `f(n)` se escribe `n` en base `B` (como mucho 31 cifras):

1. se toma la cifra más significativa mayor que 1, si la hay: toda cadena de ceros
   y unos que coincide con `n` por encima es menor que `n` siga como
   siga, así que esa cifra y todas las inferiores pueden cambiarse por 1
   sin cambiar la cuenta;
2. ahora todas las cifras son 0 o 1: se recorre desde arriba contando los
   unos tomados; en una cifra 1, elegir 0 deja libres las `i` posiciones
   inferiores, lo que da `C(i, K − ones)` números; elegir 1 continúa;
3. al final, la cota resultante cuenta si tiene exactamente `K` unos.

`O(log_B Y)` con una pequeña tabla de coeficientes binomiales.

Detalles a tener en cuenta:

- las cifras en base `B` deben ser 0 o 1; una cifra 2 o mayor ya no es una
  suma de potencias *distintas*;
- `f(X − 1)` con `X = 1` es `f(0) = 0`;
- para `B = 10` solo hay 10 posiciones por debajo de `2^31`, así que
  `K > 10` da 0.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: un triángulo de Pascal hasta 32.
  **Python**: `math.comb`, que devuelve 0 cuando `k > n`.

## Soluciones optimizadas

Rust recorre los dígitos en base B y usa un triángulo de Pascal precalculado para las opciones restantes. Rust 1.75 x64, envío 11323261. Tiempo 0,015 → 0,015 s, memoria 236 → 44 KB.

El envío 11321721 en Python tardó 0.093 s y usó 460 KB. La versión sencilla tardó 0.078 s y usó 500 KB.

Python recorre los dígitos del límite desde el más significativo y calcula los coeficientes binomiales cuando hacen falta. Un dígito mayor que uno termina el recorrido porque todas las combinaciones restantes quedan por debajo del límite.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321895 · Java 1.8 №11321896 · Go 1.14 x64 №11322186 · Python 3.12 x64 №11322187 · Rust 1.75 x64 №11322188.

Go recorre los dígitos del más al menos significativo y actualiza en cada paso el coeficiente binomial para las posiciones restantes. Go 1.14 x64, envío 11322843. Tiempo 0,031 → 0,015 s, memoria 1072 → 276 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1057_combinatorics.cpp](1057_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(log Y) | AC | 0.015 s | 188 KB | 11321895 |
| [1057_combinatorics.go](1057_combinatorics.go) | Go 1.14 x64 | combinatorics | O(log Y) | AC | 0.031 s | 1072 KB | 11322186 |
| [1057_combinatorics.java](1057_combinatorics.java) | Java 1.8 | combinatorics | O(log Y) | AC | 0.109 s | 1624 KB | 11321896 |
| [1057_combinatorics.py](1057_combinatorics.py) | Python 3.12 x64 | combinatorics | O(log Y) | AC | 0.078 s | 500 KB | 11322187 |
| [1057_combinatorics.rs](1057_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(log Y) | AC | 0.015 s | 236 KB | 11322188 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1057_combinatorics_optimized.rs](1057_combinatorics_optimized.rs) \* | Rust 1.75 x64 | combinatorics | O(log_B X) | AC | 0.015 s | 44 KB | 11323261 |
| [1057_combinatorics_optimized.py](1057_combinatorics_optimized.py) \* | Python 3.12 x64 | combinatorics | O((log Y)²) | AC | 0.093 s | 460 KB | 11321721 |
| [1057_combinatorics_optimized.go](1057_combinatorics_optimized.go) \* | Go 1.14 x64 | combinatorics | O(log Y) | AC | 0.015 s | 276 KB | 11322843 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
