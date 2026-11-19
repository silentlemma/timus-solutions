# 1139. Contar las manzanas que sobrevuela un vuelo en diagonal sobre una cuadrícula de calles

[Timus 1139](https://acm.timus.ru/problem.aspx?space=1&num=1139) · dificultad 78 · number_theory

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` avenidas y `M` calles, `1 < N, M < 32000`, dividen una ciudad en
manzanas cuadradas. Un helicóptero vuela en línea recta de la esquina
suroeste a la noreste. Cuenta las manzanas que sobrevuela; una manzana es
el interior abierto de su cuadrado, así que tocar una esquina no cuenta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `M`.

## Salida

El número de manzanas.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
3 3
```

Salida:

```
2
```

## Solución

Las manzanas forman una cuadrícula de `a × b`, con `a = N − 1` y
`b = M − 1`, y el vuelo es su diagonal. Entra primero en una
manzana, y cada vez que cruza una línea de la cuadrícula entra en una
manzana nueva. Cruza las `a − 1` líneas verticales interiores y las
`b − 1` horizontales interiores, pero en una esquina interior cruza una de
cada tipo a la vez y entra en una sola manzana nueva. La diagonal pasa
por los puntos `(k·a/g, k·b/g)`, así que encuentra exactamente `g − 1`
esquinas interiores, con `g = gcd(a, b)`. En total
`1 + (a − 1) + (b − 1) − (g − 1) = a + b − gcd(a, b)`. `O(log min(a, b))`.

Detalles a tener en cuenta:

- la entrada cuenta líneas, no manzanas: hay que restar uno a cada una;
- en una cuadrícula cuadrada la diagonal pasa por todas las esquinas de
  su camino y cruza solo `a` manzanas;
- con una sola fila o columna, el vuelo cruza todas sus manzanas.

Las respuestas se compararon con un recuento columna a columna de las
manzanas bajo la diagonal, con redondeos exactos hacia abajo y hacia
arriba, para todos los `N, M ≤ 40` y en todas las pruebas.

## Soluciones optimizadas

`1139_number_theory_optimized.py`. Conserva a+b-gcd(a,b), con a=N-1,b=M-1. Calcula el mcd mediante el bucle iterativo de Euclides. Mantiene la corrección por esquinas, con O(log min(N,M)) pasos enteros acotados y estado auxiliar O(1); no es otro algoritmo geométrico. Incluye el bucle en lugar de importar math.gcd y analiza dos tokens de bytes. La mejora medida es de memoria del juez, sin afirmar que el bucle Python sea más rápido que la biblioteca nativa. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1139_number_theory.py`: tiempo 0.078 s → 0.125 s; memoria 400 KB → 220 KB.

`1139_number_theory_optimized.rs`. Conserva a+b-gcd(a,b), con a=N-1,b=M-1. Calcula el mcd mediante el bucle iterativo de Euclides. Mantiene la corrección por esquinas, con O(log min(N,M)) pasos enteros acotados y estado auxiliar O(1); no es otro algoritmo geométrico. El bucle reemplaza el mcd recursivo y la E/S numérica directa elimina el String de entrada retenido. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1139_number_theory.rs`: tiempo 0.015 s → 0.031 s; memoria 248 KB → 56 KB.

La solución optimizada en Java lee los dos números byte a byte con
`System.in.read` en lugar de `Scanner` y calcula el mcd con un bucle en
lugar de recursión. La fórmula es la misma; la solución ocupa 360 KB en
lugar de 1592 KB, con el mismo tiempo.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1139_number_theory_optimized.py`: puesto de tiempo 47/57 y de memoria 1/57 en esta muestra comparable.

`1139_number_theory_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1139_number_theory.cpp](1139_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 128 KB | 11279432 |
| [1139_number_theory.go](1139_number_theory.go) | Go 1.14 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 1060 KB | 11279433 |
| [1139_number_theory.java](1139_number_theory.java) | Java 1.8 | number_theory | O(log min(N, M)) | AC | 0.109 s | 1592 KB | 11279436 |
| [1139_number_theory.py](1139_number_theory.py) | Python 3.12 x64 | number_theory | O(log min(N, M)) | AC | 0.078 s | 400 KB | 11279435 |
| [1139_number_theory.rs](1139_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 248 KB | 11279438 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1139_number_theory_optimized.java](1139_number_theory_optimized.java) | Java 1.8 | number_theory | O(log min(N, M)) | AC | 0.093 s | 360 KB | 11303570 |
| [1139_number_theory_optimized.py](1139_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(log min(N,M)) | AC | 0.125 s | 220 KB | 11324847 |
| [1139_number_theory_optimized.rs](1139_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(log min(N,M)) | AC | 0.031 s | 56 KB | 11324856 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
