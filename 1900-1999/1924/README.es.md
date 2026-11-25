# 1924. Un juego de signos con paridad invariable

[Timus 1924](https://acm.timus.ru/problem.aspx?space=1&num=1924) · difficulty 39 · math

Problema original de folclore, del concurso escolar regional de los Urales de 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los enteros de 1 a n están en orden. Dos equipos alternan colocando
un signo + o − en un espacio aún libre entre enteros consecutivos. El primero,
`black`, desea un resultado par; `grimy` desea uno impar. Ambos juegan
óptimamente y black empieza. Determinar quién gana. Para n=1 no hay
espacios y la expresión vale 1. Límites: 1 segundo y 64 MB.

## Entrada

Un entero n, 1≤n≤50.

## Salida

Escribir exactamente `black` si gana el objetivo par; en otro caso `grimy`.

## Evaluación

Se compara exactamente el único token, escrito en minúsculas.

## Ejemplos

```
1
```

```
grimy
```

```
4
```

```
black
```

## Solución

Cambiar el signo delante de un número x de + a − cambia el resultado en
2x, un número par. Así que toda expresión que puedan formar los
jugadores tiene la misma paridad que 1 + 2 + … + n = n(n + 1)/2, y
ninguna jugada cambia el ganador: gana black si esta suma es par y grimy
si es impar. `O(1)`.

Detalle: con n = 1 no hay ninguna jugada, y aun así decide la paridad
de 1.

## Soluciones optimizadas

`1924_math_optimized.py` se reutiliza byte por byte, sin otro archivo ni un algoritmo nuevo. Su Accepted de fuente exacto en CPython 3.12 #11327041 mide 0.078 s / 684 KB. En el grupo guardado de compiladores actuales de la familia Python, 2026-11-20: puesto temporal 4/125, memoria 118/125. Al usar menos de 1024 KB, el criterio estricto de diez primeros o 15% superior usa solo tiempo; el asterisco conserva la meta de clasificación propia del lenguaje. El mismo archivo tiene también el Accepted anterior en PyPy 3.10 #11325078, 0.125 s / 192 KB. Son pares medidos en ejecuciones distintas: se elige el tiempo y puesto de CPython, mientras PyPy usa menos memoria. Las observaciones anteriores sobre ahorro de memoria en esta sección se refieren a esa medición PyPy, no a la fila CPython. Todos los fuentes didácticos siguen intactos.

La solución optimizada en C++ lee con `scanf` e imprime con `puts` en
lugar de `iostream`: 116 KB en lugar de 380 KB. La fórmula es la
misma.

La solución optimizada en Java analiza el número byte a byte desde
`System.in` en lugar de usar `Scanner`: 336 KB en lugar de 1616 KB, con
el mismo tiempo.

`1924_math_optimized.py`. Usa el período de paridad de cuatro valores en vez de formar N(N+1)/2: es par exactamente si N mod 4 es 0 o 3. Cambiar suma por resta modifica el total en un número par, así que las jugadas no alteran al ganador. Simplifica el mismo argumento de paridad, con O(1) tiempo y espacio. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1924_math.py`: tiempo 0.093 s → 0.125 s; memoria 396 KB → 192 KB.


`1924_math_parsing_optimized.go`. Se lee el entero acotado con un pequeño autómata y se clasifica su residuo módulo cuatro. Equivale a comprobar la paridad de la suma triangular sin multiplicación ni análisis numérico general. Se escribe la respuesta completa antes de salir.

Este código exacto tiene su propio Accepted y cumple los [criterios compartidos](../../RATING_CRITERIA.md). El tiempo y la memoria siguientes proceden de una misma ejecución; las mediciones repetidas pueden variar. Se conservan las versiones sencillas y optimizadas distintas existentes.

Accepted #11329532 (Go 1.14 x64): **0.015 s / 276 KB**.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

Comparación PyPy anterior: `1924_math_optimized.py`: puesto de tiempo 110/125 y de memoria 2/125 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1924_math.cpp](1924_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 380 KB | 11291523 |
| [1924_math.go](1924_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1100 KB | 11291530 |
| [1924_math.java](1924_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1616 KB | 11291534 |
| [1924_math.py](1924_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 396 KB | 11291532 |
| [1924_math.rs](1924_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 236 KB | 11291542 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1924_math_optimized.cpp](1924_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 116 KB | 11303649 |
| [1924_math_optimized.java](1924_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 336 KB | 11303788 |
| [1924_math_optimized.py](1924_math_optimized.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 684 KB | 11327041 |
| [1924_math_parsing_optimized.go](1924_math_parsing_optimized.go) | Go 1.14 x64 | math, parsing | O(1) time and space | AC | 0.015 s | 276 KB | 11329532 |
