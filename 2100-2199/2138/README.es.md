# 2138. Invertir el orden de bytes de un número de 32 bits

[Timus 2138](https://acm.timus.ru/problem.aspx?space=1&num=2138) · dificultad 111 · math

Problema original de Aidar Islamov, del Concurso de Programación por Equipos de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número de hasta 2³² − 1 se envía como cuatro cifras en base 256. Los
ordenadores "buenos" leen las cifras desde la más significativa y los
"malos" desde la menos significativa. Un ordenador de un tipo recibió un
número de uno del otro tipo y lo leyó como v. Imprimir el número que se
envió en realidad. Los límites son 0.5 segundos y 256 MB.

## Entrada

El tipo del emisor, GOOD o BAD, y luego v, 0 ≤ v ≤ 4 294 967 295.

## Salida

El número enviado.

## Ejemplos

### Ejemplo 1

Entrada:

```
GOOD
16777216
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
BAD
1000
```

Salida:

```
3892510720
```

## Solución

Sea quien sea el emisor, el receptor lee las mismas cuatro cifras en el
orden opuesto. Así que la respuesta es v con sus cuatro cifras en base
256 invertidas, y el tipo del emisor no importa. Se toman las cifras de v
desde la más baja con % 256 y / 256 y se construye el resultado desde
arriba, o se usa un intercambio de bytes.

En el primer ejemplo 16 777 216 tiene las cifras 1;0;0;0, que invertidas
dan 1.

## Soluciones optimizadas

La solución optimizada en Java lee la entrada byte a byte directamente
desde `System.in` en lugar de crear un `Scanner`, y como GOOD y BAD no
contienen cifras, simplemente acumula en v, de tipo `long`, cada cifra
que encuentra; un `long` basta para cualquier valor hasta 2³² − 1:
{2138_math_optimized.java}.

### Mejora medida

Cada versión optimizada conservada tiene Accepted. Cumple por situarse entre las diez primeras o el 15% superior en ambas métricas, por estar en el 30% superior en ambas y mejorar la posición base en al menos una, o por reducir al menos un 30% el tiempo o la memoria respecto a la base del mismo lenguaje. Una reducción negativa indica mayor coste. El asterisco se refiere al objetivo de clasificación específico del lenguaje.

- `2138_math_optimized.java`: reducción de tiempo +0.00%; reducción de
  memoria +78.23%; base: `2138_math.java`.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`2138_math_optimized.rs`. Se mantienen el algoritmo y los tipos enteros. Los tokens decimales se convierten directamente; los negativos se acumulan con su signo para representar también el mínimo entero con signo. No cambian el almacenamiento de entrada ni la complejidad del algoritmo.

Accepted #11328633 (Rust 1.75 x64): **0.015 s / 224 KB**. Comparación archivada: `2138_math.rs` (Rust 1.75 x64) — 0.031 s / 236 KB (#11294921).

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [2138_math.cpp](2138_math.cpp).

Extraer uno a uno los cuatro bytes inferiores y añadirlos al valor invertido con desplazamientos y una máscara. El envío aceptado 11324232 tardó 0.078 s y usó 348 KB. La versión sencilla tardó 0.078 s y usó 424 KB.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2138_math.cpp](2138_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 132 KB | 11304054 |
| [2138_math.go](2138_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB | 11294918 |
| [2138_math.java](2138_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1580 KB | 11304060 |
| [2138_math.py](2138_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 424 KB | 11294919 |
| [2138_math.rs](2138_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 236 KB | 11294921 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2138_math_optimized.java](2138_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 344 KB | 11304333 |
| [2138_bitmask.py](2138_bitmask.py) | Python 3.12 x64 | bitmask | O(1) | AC | 0.078 s | 348 KB | 11324232 |
| [2138_math_optimized.rs](2138_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 224 KB | 11328633 |
