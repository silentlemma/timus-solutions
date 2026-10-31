# 1135. Contar los giros de reclutas cara a cara hasta que la fila se estabiliza

[Timus 1135](https://acm.timus.ru/problem.aspx?space=1&num=1135) · dificultad 160 · math

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`1 ≤ N ≤ 30000` reclutas están en fila, cada uno mirando a la izquierda
(`<`) o a la derecha (`>`). Cada segundo, todas las parejas de vecinos
que se miran (`><`) se dan la vuelta a la vez. Cuenta los giros de
parejas hasta que nada cambia, o imprime `NO` si el proceso no termina
nunca.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego exactamente `N` caracteres `<` y `>` repartidos en líneas de
hasta 255 caracteres.

## Salida

El número de giros de parejas.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
>><<><
```

Salida:

```
7
```

## Solución

Una pareja que gira, `><`, se convierte en `<>`: en cuanto a las
direcciones, es un intercambio de dos vecinos. Cada intercambio elimina
exactamente un par de reclutas (no necesariamente vecinos) con un `>`
antes de un `<`, y no crea ninguno. La fila es estable justo cuando no
queda ningún `><`, es decir, cuando todos los `<` están antes de todos los
`>`, y entonces no hay ningún par así. Por tanto el proceso siempre
termina, `NO` nunca se imprime, y el número de giros es el número de
pares con `>` antes de `<`. Una pasada los cuenta: se lleva el número de
`>` vistos hasta el momento y se suma en cada `<`. `O(N)`.

Detalles a tener en cuenta:

- se cuentan giros de parejas, no segundos transcurridos: la prueba `01`
  tiene siete giros de parejas en cuatro segundos;
- la fila está repartida en varias líneas, quizá con alguna vacía, así
  que se leen caracteres hasta reunir `N`;
- la respuesta llega a `15000² = 2,25·10⁸`, que aún cabe en 32 bits, pero
  los contadores de 64 bits no cuestan nada;
- el orden de los giros dentro de un segundo no afecta a la cuenta.

Las respuestas se compararon con una simulación segundo a segundo en 200
filas aleatorias de hasta 300 reclutas.

## Soluciones optimizadas

La implementación rápida de Java conserva el conteo de inversiones, pero lee directamente con un búfer reutilizable de 4 KB en lugar de lectores de caracteres. Omite los saltos de línea y cuenta exactamente `N` direcciones. Mantiene tiempo `O(N)` y espacio auxiliar constante. La versión con lectores de caracteres sigue siendo la básica.

{1135_math_optimized.java}.

Ejecuciones Accepted correspondientes al código: versión básica 0.125 s / 532 KB; esta versión 0.078 s / 364 KB (envío 11307457). Cumple el objetivo de clasificación en la instantánea del 2026-10-31.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1135_math_optimized.java`: reducción de tiempo +37.60%; reducción de
  memoria +31.58%; base: `1135_math.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1135_math.cpp](1135_math.cpp).
- [1135_math.go](1135_math.go).
- [1135_math.rs](1135_math.rs).

- Todos los lenguajes saltan los saltos de línea y llevan la misma cuenta
  acumulada.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1135_math.cpp](1135_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 132 KB | 11279403 |
| [1135_math.go](1135_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1100 KB | 11279405 |
| [1135_math.java](1135_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 532 KB | 11279408 |
| [1135_math.py](1135_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 420 KB | 11279406 |
| [1135_math.rs](1135_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 248 KB | 11279409 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1135_math_optimized.java](1135_math_optimized.java) | Java 1.8 | math | O(N) | AC | 0.078 s | 364 KB | 11307457 |
