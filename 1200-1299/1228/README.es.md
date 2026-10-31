# 1228. Los límites de un arreglo a partir de sus multiplicadores de índice

[Timus 1228](https://acm.timus.ru/problem.aspx?space=1&num=1228) · dificultad 109 · math

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arreglo de `n` dimensiones `array[0..k1, 0..k2, …, 0..kn]`, `n ≤ 20`,
se dispone con el último índice cambiando más rápido, así que el elemento
`X[i1, …, in]` tiene número `1 + D1·i1 + … + Dn·in` para ciertos
multiplicadores `Di`. Dados los multiplicadores y el número total de
elementos `s`, hay que hallar los límites superiores `k1, …, kn`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` (`1 ≤ n ≤ 20`) y `s` (`1 ≤ s < 2³¹ − 1`), y luego `D1, …, Dn`.

## Salida

`k1, …, kn` (`0 < ki ≤ 1000`) separados por espacios o saltos de
línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 24
8
4
1
```

Salida:

```
2 1 3
```

## Solución

Aumentar en uno el índice `i` salta un bloque entero de las dimensiones
siguientes, así que `D(i−1) = Di · (ki + 1)`, y el arreglo entero es un
bloque de la primera dimensión: `s = D1 · (k1 + 1)`. Leyendo los
multiplicadores con `s` delante, cada límite es uno menos que el
cociente de dos vecinos: `k1 = s/D1 − 1` y `ki = D(i−1)/Di − 1`. `O(n)`.

Detalles a tener en cuenta:

- el último multiplicador es siempre 1, y el primer límite sale de `s`,
  no de un multiplicador;
- los productos son menores que `2³¹ − 1`, así que bastan enteros de
  32 bits con signo para las cuentas.

Los límites se comprobaron multiplicando `ki + 1` hasta `s` en 59
arreglos generados, y se compararon con una solución escrita aparte en
todas las pruebas.

## Soluciones optimizadas

La solución optimizada en C++ lee los multiplicadores de uno en uno y
guarda solo el anterior, imprimiendo cada cota en cuanto llega su
divisor, en lugar de guardar `s` y todos los multiplicadores en un
`std::vector`: {1228_math_optimized.cpp}.

La solución optimizada en Java analiza los números cifra a cifra
directamente desde `System.in` en lugar de crear un `Scanner`, y guarda
solo el multiplicador anterior en lugar de un arreglo con todos:
{1228_math_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1228_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +36.00%; base: `1228_math.cpp`.

- `1228_math_optimized.java`: reducción de tiempo +50.40%; reducción de
  memoria +78.22%; base: `1228_math.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1228_math.go](1228_math.go).
- [1228_math.rs](1228_math.rs).

- Todos los lenguajes ponen `s` delante de los multiplicadores y dividen
  vecinos.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1228_math.cpp](1228_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 200 KB | 11283732 |
| [1228_math.go](1228_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.001 s | 1136 KB | 11283735 |
| [1228_math.java](1228_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1616 KB | 11283739 |
| [1228_math.py](1228_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 424 KB | 11283737 |
| [1228_math.rs](1228_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 216 KB | 11283740 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1228_math_optimized.cpp](1228_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.001 s | 128 KB | 11304270 |
| [1228_math_optimized.java](1228_math_optimized.java) | Java 1.8 | math | O(n) | AC | 0.062 s | 352 KB | 11304271 |
