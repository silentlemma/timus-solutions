# 1402. Cócteles

[Timus 1402](https://acm.timus.ru/problem.aspx?space=1&num=1402) · dificultad 130 · combinatorics

Problema original de Sergey Pupyrev, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cóctel mezcla dos o más de N ≤ 21 bebidas, cada una a lo sumo una
vez, y el orden de las bebidas importa. Hay que contar los cócteles
distintos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N (1 ≤ N ≤ 21).

## Salida

El número de cócteles.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
12
```

## Solución

Un cóctel de k bebidas es una elección ordenada de k bebidas distintas,
y hay N·(N − 1)·…·(N − k + 1) de ellas. Se suman para k de 2 a N,
obteniendo cada producto a partir del anterior. `O(N)`.

Detalles a tener en cuenta:

- con una sola bebida no hay ningún cóctel (prueba 02);
- para N = 21 la respuesta es de unos 1,4·10²⁰, más de 64 bits, así que
  las soluciones usan enteros de 128 bits o enteros grandes (prueba 07).

Las pruebas se juzgan por comparación exacta.

## Soluciones optimizadas

La solución optimizada en C++ suma en el mismo entero de 128 bits, pero
escribe las cifras de atrás hacia delante en un arreglo fijo de
23 caracteres en lugar de insertar cada una al principio de un
`std::string`: como `N ≤ 21`, la respuesta es menor que 21·21! < 10²²,
así que 22 cifras y el cero final siempre caben. Sin `<string>` el
propio programa no reserva memoria dinámica:
{1402_combinatorics_optimized.cpp}.

La solución optimizada en Java lee N byte a byte de `System.in` en lugar
de crear un `Scanner`, cuyas expresiones regulares y datos de
configuración regional cuestan más que las propias multiplicaciones, que
no pasan de veinte; la suma sigue siendo un `BigInteger`:
{1402_combinatorics_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1402_combinatorics_optimized.cpp`: reducción de tiempo +0.00%;
  reducción de memoria +48.94%; base: `1402_combinatorics.cpp`.

- `1402_combinatorics_optimized.java`: reducción de tiempo +0.00%;
  reducción de memoria +73.70%; base: `1402_combinatorics.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1402_combinatorics.go](1402_combinatorics.go).
- [1402_combinatorics.rs](1402_combinatorics.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1402_combinatorics.cpp](1402_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N) | AC | 0.015 s | 188 KB | 11286026 |
| [1402_combinatorics.go](1402_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N) | AC | 0.031 s | 1176 KB | 11286027 |
| [1402_combinatorics.java](1402_combinatorics.java) | Java 1.8 | combinatorics | O(N) | AC | 0.109 s | 1688 KB | 11286031 |
| [1402_combinatorics.py](1402_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N) | AC | 0.078 s | 388 KB | 11286029 |
| [1402_combinatorics.rs](1402_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N) | AC | 0.031 s | 232 KB | 11286032 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1402_combinatorics_optimized.cpp](1402_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(N) | AC | 0.001 s | 96 KB | 11304432 |
| [1402_combinatorics_optimized.java](1402_combinatorics_optimized.java) | Java 1.8 | combinatorics | O(N) | AC | 0.109 s | 444 KB | 11304433 |
