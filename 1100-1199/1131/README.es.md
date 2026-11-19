# 1131. Copiar un programa a N ordenadores con K cables, una copia por cable y hora

[Timus 1131](https://acm.timus.ru/problem.aspx?space=1&num=1131) · dificultad 77 · math

Problema original de Stanislav Vasiliev y Alexander Mironenko, del sexto concurso universitario de programación de la Universidad Estatal de los Urales, 21 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un programa está en uno de `N` ordenadores. En una hora, un ordenador que
lo tiene puede copiarlo a otro por un cable, y hay `K` cables. Halla el
menor número de horas hasta que los `N` ordenadores tengan el programa,
con `1 ≤ N, K ≤ 10⁹`.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `K` en una línea.

## Salida

El menor número de horas.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
8 3
```

Salida:

```
4
```

## Solución

En una hora reciben el programa `min(have, K, N − have)` ordenadores
nuevos, donde `have` es el número de ordenadores que ya lo tienen; copiar
lo máximo posible cada hora es claramente lo mejor. Mientras
`have < min(N, K)`, se duplica `have` y se cuenta una hora. Si se alcanza o
supera `N`, todos los ordenadores restantes pueden recibir el programa en
esa hora y el bucle termina; que el contador supere `N` no cambia la
respuesta. Esta fase dura como mucho 30 horas. En caso contrario, cuando
`have ≥ K`, cada hora se añaden hasta `K` ordenadores, así que los
`N − have` restantes necesitan `⌈(N − have) / K⌉` horas más.
`O(log min(N, K))`.

Detalles a tener en cuenta:

- con `N = 1` no hacen falta horas;
- con `K = 1` y `N = 10⁹` la respuesta es casi `10⁹`, así que las horas
  tras la duplicación se calculan con una división, no una a una;
- en la última hora pueden recibir el programa menos de `K` ordenadores
  (prueba 11), por lo que la división se redondea hacia arriba;
- el contador puede superar `N` durante la duplicación (prueba 05), pero
  llega como máximo a `2³⁰`; los enteros de 64 bits son seguros, aunque
  bastan los enteros de 32 bits con signo.

Las respuestas se compararon con una búsqueda binaria sobre el número de
horas en todas las pruebas y con una simulación hora a hora para todos los
`N < 200` y `K < 70`.

## Soluciones optimizadas

La solución optimizada en Java analiza los dos números byte a byte desde
`System.in` en lugar de usar `Scanner`: 0.093 s en lugar de 0.125 s y
344 KB en lugar de 1592 KB.

`1131_math_optimized.py`. Sustituye el bucle de duplicación por d=(min(N,K)-1).bit_length(), techo exacto de log2(min(N,K)), con d=0 para un equipo o cable. Tras llegar a 2^d equipos añade max(0,ceil((N-2^d)/K)) horas. Calcula el mismo modelo de dos fases sin logaritmos flotantes. Con N,K<=10^9 la entrada cruda y aritmética acotada usan O(1) tiempo y estado. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1131_math.py`: tiempo 0.078 s → 0.125 s; memoria 424 KB → 196 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1131_math_optimized.py`: puesto de tiempo 53/66 y de memoria 1/66 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1131_math.cpp](1131_math.cpp) | G++ 13.2 x64 | math | O(log min(N, K)) | AC | 0.015 s | 128 KB | 11279375 |
| [1131_math.go](1131_math.go) | Go 1.14 x64 | math | O(log min(N, K)) | AC | 0.015 s | 1076 KB | 11279376 |
| [1131_math.java](1131_math.java) | Java 1.8 | math | O(log min(N, K)) | AC | 0.125 s | 1592 KB | 11279379 |
| [1131_math.py](1131_math.py) | Python 3.12 x64 | math | O(log min(N, K)) | AC | 0.078 s | 424 KB | 11279378 |
| [1131_math.rs](1131_math.rs) | Rust 1.75 x64 | math | O(log min(N, K)) | AC | 0.046 s | 216 KB | 11279381 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1131_math_optimized.java](1131_math_optimized.java) | Java 1.8 | math | O(log min(N, K)) | AC | 0.093 s | 344 KB | 11303712 |
| [1131_math_optimized.py](1131_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 196 KB | 11324846 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
