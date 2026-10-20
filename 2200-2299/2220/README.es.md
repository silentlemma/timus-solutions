# 2220. Media de 1 / mcd sobre todos los pares hasta N

[Timus 2220](https://acm.timus.ru/problem.aspx?space=1&num=2220) · dificultad 1465 · number_theory

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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2220_number_theory.cpp](2220_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N + N^(3/4)) | AC | 0.062 s | 1000 KB |
| [2220_number_theory.go](2220_number_theory.go) | Go 1.14 x64 | number_theory | O(N + N^(3/4)) | AC | 0.093 s | 1704 KB |
| [2220_number_theory.java](2220_number_theory.java) | Java 1.8 | number_theory | O(N + N^(3/4)) | AC | 0.437 s | 1064 KB |
| [2220_number_theory.py](2220_number_theory.py) | PyPy 3.10 x64 | number_theory | O(N + N^(3/4)) | AC | 1.265 s | 4892 KB |
| [2220_number_theory.rs](2220_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N + N^(3/4)) | AC | 0.062 s | 800 KB |
