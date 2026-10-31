# 1336. El problema de Ben Betsalel

[Timus 1336](https://acm.timus.ru/problem.aspx?space=1&num=1336) · dificultad 123 · math

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que escribir un número entero n, 1 ≤ n ≤ 10⁹, como cociente de un
cuadrado entre un cubo: hallar enteros m y k de 1 a 10¹⁰⁰ con
m² = k³ · n. Se acepta cualquier par así.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número n.

## Salida

m en la primera línea y k en la segunda.

## Comprobación

El comprobador acepta cualesquiera m y k de 1 a 10¹⁰⁰ con m² = k³ · n.

## Ejemplos

### Ejemplo 1

Entrada:

```
18
```

Salida:

```
12
2
```

### Ejemplo 2

Entrada:

```
1
```

Salida:

```
1
1
```

## Solución

Se toma k = n y m = n². Entonces m² = n⁴ = n³ · n. Así que siempre
existe un par, y por eso el problema siempre tiene solución. `O(1)`.

Detalles a tener en cuenta:

- m llega a 10¹⁸, lo que necesita un entero de 64 bits (prueba 03);
- el primer ejemplo muestra un par más pequeño; se acepta cualquiera
  correcto.

## Soluciones optimizadas

La solución optimizada en Java lee n byte a byte de `System.in` en lugar
de crear un `Scanner`, cuyas expresiones regulares y datos de
configuración regional son el gasto principal de un programa que hace
una sola multiplicación; n² sigue cabiendo en `long`, porque no pasa de
10¹⁸: {1336_math_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1336_math_optimized.java`: reducción de tiempo +0.00%; reducción de
  memoria +77.24%; base: `1336_math.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1336_math.cpp](1336_math.cpp).
- [1336_math.go](1336_math.go).
- [1336_math.rs](1336_math.rs).

- Las cinco soluciones imprimen n² y n.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1336_math.cpp](1336_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11285033 |
| [1336_math.go](1336_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB | 11285034 |
| [1336_math.java](1336_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1564 KB | 11285036 |
| [1336_math.py](1336_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 352 KB | 11285035 |
| [1336_math.rs](1336_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB | 11285038 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1336_math_optimized.java](1336_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 356 KB | 11304378 |
