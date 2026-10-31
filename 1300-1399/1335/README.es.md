# 1335. La Tesis Blanca

[Timus 1335](https://acm.timus.ru/problem.aspx?space=1&num=1335) · dificultad 182 · math

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado N, 2 ≤ N ≤ 30 000, hay que hallar tres números enteros distintos A,
B y C entre N² y (N + 1)², ambos incluidos, tales que A² + B² sea
divisible por C, o imprimir `No solution` si no los hay. Se acepta
cualquier terna así.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

A, B y C, o `No solution`.

## Comprobación

El comprobador acepta tres números distintos cualesquiera del rango con
A² + B² divisible por C. Siempre existe una terna, así que `No solution`
nunca se acepta.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
8 6 4
```

### Ejemplo 2

Entrada:

```
1000
```

Salida:

```
1000000 1000756 1000976
```

## Solución

Se toma C = N² + 1, A = N² y B = N² + N + 1. Módulo C el primer número
es −1 y el segundo es N, así que A² + B² ≡ 1 + N², que es el propio C,
y la suma es divisible por C. Los tres están entre N² y (N + 1)², ya que
N² + N + 1 < N² + 2N + 1, y son distintos para todo N ≥ 1. Por tanto la
respuesta existe siempre y `No solution` nunca ocurre. `O(1)`.

La terna se encontró listando todas las soluciones con A = N² para N
pequeños y viendo que (N² + N + 1, N² + 1) aparecía siempre.

Detalles a tener en cuenta:

- los números llegan a unos 9 · 10⁸, y sus cuadrados, que solo necesita
  el comprobador, a 8 · 10¹⁷, más de lo que caben en 32 bits;
- los ejemplos muestran otras ternas; se acepta cualquiera correcta.

## Soluciones optimizadas

La solución optimizada en Java imprime la misma terna, pero lee N a mano
de los bytes de la entrada en lugar de con `Scanner`, cuyas expresiones
regulares cuestan tiempo y memoria de preparar incluso para un solo
número: {1335_math_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1335_math_optimized.java`: reducción de tiempo +12.80%; reducción de
  memoria +77.67%; base: `1335_math.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1335_math.cpp](1335_math.cpp).
- [1335_math.go](1335_math.go).
- [1335_math.rs](1335_math.rs).

- Las cinco soluciones imprimen la misma terna.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1335_math.cpp](1335_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11285027 |
| [1335_math.go](1335_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1064 KB | 11285028 |
| [1335_math.java](1335_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1612 KB | 11285030 |
| [1335_math.py](1335_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 392 KB | 11285029 |
| [1335_math.rs](1335_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 244 KB | 11285032 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1335_math_optimized.java](1335_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.109 s | 360 KB | 11307311 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
