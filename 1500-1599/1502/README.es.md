# 1502. Puntos de dominó

[Timus 1502](https://acm.timus.ru/problem.aspx?space=1&num=1502) · dificultad 74 · math

Problema original del folclore, preparado por Stanislav Vasiliev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un juego de dominó tiene una ficha por cada par no ordenado de números
de puntos de 0 a N (1 ≤ N ≤ 10000), dobles incluidos. Hay que hallar el
total de puntos del juego.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

El total de puntos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
12
```

## Solución

Se cuenta cuántas veces aparece cada valor en un extremo. Un valor v
está en un extremo de cada ficha v–w con w ≠ v, que son N fichas, y en
los dos extremos del doble v–v: N + 2 extremos en total. Así que los
puntos suman (N + 2)·(0 + 1 + … + N) = (N + 2)·N·(N + 1)/2. `O(1)`.

Detalles a tener en cuenta:

- el doble cuenta su valor dos veces (prueba 02);
- para N = 10⁴ la respuesta ronda 5·10¹¹ y necesita 64 bits
  (prueba 04).

## Soluciones optimizadas

La solución optimizada en Java usa la misma fórmula y analiza el número
byte a byte desde `System.in` en lugar de usar `Scanner`: 0.078 s en
lugar de 0.125 s y 344 KB en lugar de 1584 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1502_math.cpp](1502_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11287258 |
| [1502_math.go](1502_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1100 KB | 11287259 |
| [1502_math.java](1502_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1584 KB | 11287261 |
| [1502_math.py](1502_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 368 KB | 11287260 |
| [1502_math.rs](1502_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 244 KB | 11287262 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1502_math_optimized.java](1502_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 344 KB | 11303756 |
