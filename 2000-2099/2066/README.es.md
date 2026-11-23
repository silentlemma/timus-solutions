# 2066. El menor valor con tres números

[Timus 2066](https://acm.timus.ru/problem.aspx?space=1&num=2066) · dificultad 28 · bruteforce

Problema original de Kirill Borozdin, del Concurso Regional por Equipos de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres enteros no negativos pueden escribirse en cualquier orden con uno
de los signos +, − o × entre cada dos vecinos; la multiplicación va
primero y no hay paréntesis ni menos unario. Hallar el menor valor
posible de una expresión así. Los límites son 1 segundo y 64 MB.

## Entrada

Los números a ≤ b ≤ c, 0 ≤ a, cada uno en su línea, c ≤ 100.

## Salida

El menor valor.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
2
3
```

Salida:

```
-5
```

## Solución

Hay como máximo 6 órdenes y 9 pares de signos, así que los programas prueban
hasta 54 expresiones. Se evalúa x op₁ y op₂ z con la precedencia usual: si
solo el segundo signo es ×, primero se calcula y × z; si no, se va de
izquierda a derecha.

La búsqueda siempre termina con la misma forma: el menor número menos el
mayor de b + c y b × c, es decir, a − max(b + c, b × c). Restar al menor
número tanto como sea posible es lo mejor, y b + c supera a b × c solo
cuando uno de ellos es 0 o 1. Comprobar las 176 851 entradas confirma la
fórmula, pero la búsqueda directa no necesita ninguna demostración.

En el ejemplo 1 − 2 × 3 = −5.

## Soluciones optimizadas

La solución optimizada en Java analiza los números byte a byte desde
`System.in` en lugar de usar `Scanner`: 0.093 s en lugar de 0.140 s y
400 KB en lugar de 1584 KB.

`2066_math.py`. Sustituye la enumeración de permutaciones y operadores por dos expresiones. Para a<=b<=c no negativos, el mínimo aditivo es a-b-c. Si se resta un producto, conviene incluir los dos mayores, dando a-b*c; productos positivos y otras posiciones mixtas no mejoran a ambos candidatos. Devuelve el mínimo. El nombre math distingue esta prueba de la fuerza bruta didáctica conservada. Tiempo y espacio O(1). El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `2066_bruteforce.py`: tiempo 0.078 s → 0.14 s; memoria 532 KB → 208 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`2066_math_implementation_optimized.rs`. La entrada de C llama directamente al solucionador y vacía la salida de Rust antes de volver; se conserva la implementación de entrada habitual.

Accepted #11328943 (Rust 1.75 x64): **0.031 s / 152 KB**. Comparación archivada: `2066_bruteforce.rs` (Rust 1.75 x64) — 0.046 s / 224 KB (#11303808).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`2066_math.py`: puesto de tiempo 330/341 y de memoria 3/341 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2066_bruteforce.cpp](2066_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 176 KB | 11303806 |
| [2066_bruteforce.go](2066_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1080 KB | 11294375 |
| [2066_bruteforce.java](2066_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.140 s | 1584 KB | 11303807 |
| [2066_bruteforce.py](2066_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.078 s | 532 KB | 11294380 |
| [2066_bruteforce.rs](2066_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.046 s | 224 KB | 11303808 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2066_bruteforce_optimized.java](2066_bruteforce_optimized.java) | Java 1.8 | bruteforce | O(1) | AC | 0.093 s | 400 KB | 11303798 |
| [2066_math.py](2066_math.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.14 s | 208 KB | 11324830 |
| [2066_math_implementation_optimized.rs](2066_math_implementation_optimized.rs) | Rust 1.75 x64 | math, implementation | O(1) | AC | 0.031 s | 152 KB | 11328943 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
