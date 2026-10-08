# 1009. Contar números en base K sin dos ceros seguidos

[Timus 1009](https://acm.timus.ru/problem.aspx?space=1&num=1009) · dificultad 94 · dp, combinatorics

Problema original del Campeonato de la Universidad Estatal de los Urales 1997.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuenta los números de `N` dígitos en base `K` (el primer dígito no es cero)
cuyos dígitos no contienen dos ceros seguidos. `2 ≤ K ≤ 10`, `N ≥ 2`,
`N + K ≤ 18`.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `K`, cada uno en su propia línea.

## Salida

La cantidad.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
10
```

Salida:

```
891
```

### Ejemplo 2

Entrada:

```
2
2
```

Salida:

```
2
```

## Solución

**Programación dinámica.** Se cuentan los prefijos válidos según su último
dígito: `zero` terminan en `0`, `other` en un dígito no nulo. Con un dígito,
`zero = 0` y `other = K - 1`. Al añadir un dígito:

- un cero solo puede ir tras un dígito no nulo: `zero' = other`;
- un dígito no nulo puede ir tras cualquiera:
  `other' = (zero + other) · (K - 1)`.

Tras `N` dígitos la respuesta es `zero + other`. Tiempo `O(N)`.

**Combinatoria.** Un número con `z` ceros los tiene entre las `N - 1`
posiciones posteriores a la primera, sin dos adyacentes: `C(N - z, z)` formas;
cada uno de los otros `N - z` dígitos toma uno de `K - 1` valores. La respuesta
es `Σ C(N - z, z) · (K - 1)^(N - z)` sobre `0 ≤ z ≤ N / 2`.

Detalles a tener en cuenta:

- la mayor respuesta, `1 434 392 064` (`N = 11`, `K = 7`), está cerca del
  límite de 32 bits, y los valores intermedios de una fórmula descuidada pueden
  desbordarse: usa enteros de 64 bits;
- con `K = 2` la respuesta es un número de Fibonacci, una comprobación útil.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: la DP de dos estados.
- **C++** y **Python** tienen además la suma cerrada; `math.comb` de Python
  calcula los coeficientes binomiales de forma exacta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1009_combinatorics.cpp](1009_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N^2) | AC | 0.001 s | 128 KB |
| [1009_combinatorics.py](1009_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N^2) | AC | 0.078 s | 404 KB |
| [1009_dp.cpp](1009_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 128 KB |
| [1009_dp.go](1009_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1104 KB |
| [1009_dp.java](1009_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 1576 KB |
| [1009_dp.rs](1009_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 216 KB |
