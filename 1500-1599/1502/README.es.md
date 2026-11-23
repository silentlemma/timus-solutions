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

`1502_math_optimized.py`. Conserva fórmula exacta N(N+1)(N+2)/2, divide producto par N(N+1) antes de multiplicar. Lee/escribe descriptores binarios directamente al nivel de módulo, sin imports ni salida anticipada explícita. Sin tabla ni flotantes. N≤10000 implica trabajo aritmético constante y enteros acotados; conserva fórmula didáctica.

Fuente exacto: Python 3.12 x64 Accepted #11327845: 0.062 s / 284 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 2/76; 11/76. Admisión estricta usa solo tiempo bajo 1024 KB: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. Conserva asterisco por la meta propia de primer puesto en ambas. La variante anterior conservada tiene su par propio #11302199 (Python 3.12 x64): 0.078 s / 320 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `1502_math_optimized.py`: 0.062 s / 284 KB; base didáctica conservada `1502_math.py`: 0.078 s / 368 KB.

La solución optimizada en Java usa la misma fórmula y analiza el número
byte a byte desde `System.in` en lugar de usar `Scanner`: 0.078 s en
lugar de 0.125 s y 344 KB en lugar de 1584 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1502_math_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328562 (Go 1.14 x64): **0.015 s / 940 KB**. Comparación archivada: `1502_math.go` (Go 1.14 x64) — 0.015 s / 1100 KB (#11287259).

`1502_math_optimized.rs`. Se conserva la misma recurrencia matemática. Se leen los números desde bytes y se escribe directamente la respuesta numérica de tamaño acotado, evitando el formato numérico general. Se mantiene la implementación más sencilla.

Accepted #11328563 (Rust 1.75 x64): **0.015 s / 208 KB**. Comparación archivada: `1502_math.rs` (Rust 1.75 x64) — 0.031 s / 244 KB (#11287262).

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
| [1502_math_optimized.py](1502_math_optimized.py) | Python 3.12 x64 | math | O(1) bounded arithmetic | AC | 0.062 s | 284 KB | 11327845 |
| [1502_math_optimized.go](1502_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 940 KB | 11328562 |
| [1502_math_optimized.rs](1502_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 208 KB | 11328563 |
