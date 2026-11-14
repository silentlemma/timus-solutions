# 2220. Media de 1 / mcd sobre todos los pares hasta N

[Timus 2220](https://acm.timus.ru/problem.aspx?space=1&num=2220) · dificultad 685 · number_theory

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2025.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hallar la media de 1 / gcd(i, j) sobre todos los pares 1 ≤ i ≤ j ≤ N,
módulo 10⁹ + 7. Los límites son 1.5 segundos y 512 MB.

## Entrada

N, 1 ≤ N ≤ 10⁷.

## Salida

La media como p · q⁻¹ módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
833333340
```

### Ejemplo 2

Entrada:

```
3
```

Salida:

```
805555562
```

### Ejemplo 3

Entrada:

```
1
```

Salida:

```
1
```

## Solución

Se agrupan los pares por su mcd d. Escribiendo i = da y j = db, los
pares con mcd d son los pares coprimos a ≤ b ≤ ⌊N / d⌋, y hay
Φ(⌊N / d⌋) de ellos, donde Φ(m) = φ(1) + … + φ(m). Así la suma es

Σ sobre d de Φ(⌊N / d⌋) / d,

que al final se divide entre los N(N + 1) / 2 pares.

⌊N / d⌋ toma O(√N) valores distintos, y en cada bloque de d con el mismo
cociente la suma necesita Φ de ese cociente por la diferencia de números
armónicos H(right) − H(left − 1) módulo el primo.

- Φ en todos los cocientes sale de una criba de φ hasta una cota y, por
  encima, de la identidad Φ(x) = x(x + 1) / 2 − Σ sobre d ≥ 2 de
  Φ(⌊x / d⌋), de nuevo agrupada por cocientes, empezando por los
  argumentos menores.
- Los números armónicos necesitarían un inverso para cada d hasta 10⁷.
  La solución guarda en cambio F = d! y W = d! · H(d), actualizados con
  W ← W · d + F y F ← F · d, y toma un inverso de F por bloque. La
  versión en Python junta ocho pasos consecutivos en uno usando el
  producto de los ocho factores y su derivada.

En el primer ejemplo los pares (1, 1), (1, 2) y (2, 2) dan
1 + 1 + 1/2 = 5/2, y la media es 5/6.

Esto cuesta O(N) multiplicaciones para los números armónicos más unas
O(N^(3/4)) para las sumas de la función de Euler.

## Soluciones optimizadas

Go agrupa cuatro actualizaciones consecutivas del factorial y de la suma armónica. Usa la regla del producto para hallar el producto del bloque y su derivada, y actualiza una sola vez la suma ponderada. El envío 11317204 tardó 0,046 s y usó 1504 KB frente a 0,078 s y 1908 KB en la base.

PyPy empareja los factores de los extremos de cada bloque de ocho y usa los cuatro pares para calcular el producto del bloque y su derivada. Calcula las sumas de la función de Euler para los cocientes grandes en orden creciente y las guarda en un arreglo. El envío 11317253 tardó 0,343 s y usó 4016 KB frente a 1,328 s y 5096 KB en la base.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321803 · Go 1.14 x64 №11322081 · Java 1.8 №11318205 · Rust 1.75 x64 №11321807 · PyPy 3.10 x64 №11322169.

Rust agrupa cuatro actualizaciones de la suma armónica y guarda las sumas de totientes pequeñas como residuos de 32 bits. Rust 1.75 x64, envío 11322387. Tiempo 0,062 → 0,046 s, memoria 1000 → 612 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2220_number_theory.cpp](2220_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N + N^(3/4)) | AC | 0.046 s | 1196 KB | 11321803 |
| [2220_number_theory.go](2220_number_theory.go) | Go 1.14 x64 | number_theory | O(N + N^(3/4)) | AC | 0.078 s | 1908 KB | 11322081 |
| [2220_number_theory.java](2220_number_theory.java) | Java 1.8 | number_theory | O(N + N^(3/4)) | AC | 0.421 s | 1252 KB | 11318205 |
| [2220_number_theory.py](2220_number_theory.py) | PyPy 3.10 x64 | number_theory | O(N + N^(3/4)) | AC | 1.328 s | 5096 KB | 11322169 |
| [2220_number_theory.rs](2220_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N + N^(3/4)) | AC | 0.062 s | 1000 KB | 11321807 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2220_number_theory_optimized.go](2220_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(N + N^(3/4)) | AC | 0.046 s | 1504 KB | 11317204 |
| [2220_number_theory_optimized.py](2220_number_theory_optimized.py) | PyPy 3.10 x64 | number_theory | O(N + N^(3/4)) | AC | 0.343 s | 4016 KB | 11317253 |
| [2220_number_theory_optimized.rs](2220_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(N + N^(3/4)) | AC | 0.046 s | 612 KB | 11322387 |

\* El corte de clasificación no contiene envíos comparables en Go de otros autores.
