# 1264. Días de trabajo

[Timus 1264](https://acm.timus.ru/problem.aspx?space=1&num=1264) · dificultad 21 · math

Problema original de Den Raskovalov, de la Competición Abierta por Equipos de Programación para Escolares de la Región de Sverdlovsk, 11 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una función cuenta cuántas veces aparece cada valor de 0 a M en un
arreglo de N elementos, escrita con una línea `if` por cada elemento y
cada valor (0 ≤ N, M ≤ 40 000). Escribir una línea lleva un segundo.
¿Cuántos segundos lleva toda la función?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M.

## Salida

El número de segundos.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 1
```

Salida:

```
6
```

## Solución

Hay N elementos y M + 1 valores, así que la respuesta es N · (M + 1).
`O(1)`.

Detalles a tener en cuenta:

- los valores van de 0 a M, así que son M + 1, no M;
- la respuesta llega a 40 000 · 40 001 = 1 600 040 000, cerca del
  límite de 32 bits con signo; C++, Go, Java y Rust usan 64 bits (prueba 05);
- con N = 0 la respuesta es 0 sea cual sea M (pruebas 02, 03).

## Soluciones optimizadas

`1264_math_optimized.go`. Conserva N*(M+1), incluidos cero elementos y el valor cero entre las M+1 opciones. No simula un arreglo. N,M<=40000 acotan el producto a1600040000; Go mantiene int64 y Python enteros exactos. Entrada numérica por bytes y salida directa reducen sobrecarga, con O(1) tiempo y estado auxiliar. os.Stdin.Read/os.Stdout.Write portables y conversión entera directa usan búferes fijos de entrada y salida de 4096 bytes. Se atienden escrituras parciales antes de reutilizar el búfer de salida. Se conserva la fuente sencilla original con Accepted.

Frente a `1264_math.go`: tiempo 0.031 s → 0.015 s; memoria 1060 KB → 796 KB.

`1264_math_optimized.py`. Conserva N*(M+1), incluidos cero elementos y el valor cero entre las M+1 opciones. No simula un arreglo. N,M<=40000 acotan el producto a1600040000; Go mantiene int64 y Python enteros exactos. Entrada numérica por bytes y salida directa reducen sobrecarga, con O(1) tiempo y estado auxiliar. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1264_math.py`: tiempo 0.093 s → 0.109 s; memoria 320 KB → 208 KB.

La solución optimizada en Java analiza los dos números byte a byte desde
`System.in` en lugar de usar `Scanner`: 296 KB en lugar de 1552 KB,
aunque el tiempo sube de 0.109 s a 0.140 s.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1264_math_optimized.go`: puesto de tiempo 1/16 y de memoria 1/16 en esta muestra comparable.

`1264_math_optimized.py`: puesto de tiempo 539/597 y de memoria 1/597 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1264_math.cpp](1264_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11284168 |
| [1264_math.go](1264_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB | 11284172 |
| [1264_math.java](1264_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1552 KB | 11284181 |
| [1264_math.py](1264_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 320 KB | 11284180 |
| [1264_math.rs](1264_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 232 KB | 11284182 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1264_math_optimized.java](1264_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.140 s | 296 KB | 11303732 |
| [1264_math_optimized.go](1264_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 796 KB | 11325046 |
| [1264_math_optimized.py](1264_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 208 KB | 11324828 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
