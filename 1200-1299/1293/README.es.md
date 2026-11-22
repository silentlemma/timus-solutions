# 1293. Eniya

[Timus 1293](https://acm.timus.ru/problem.aspx?space=1&num=1293) · dificultad 14 · math

Problema original de Den Raskovalov, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que tratar por ambas caras N paneles rectangulares de A por B
metros, y cada metro cuadrado necesita un nanogramo de producto
(1 ≤ N, A, B ≤ 100). ¿Cuántos nanogramos hacen falta?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, A y B en una línea.

## Salida

El número de nanogramos.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 2 3
```

Salida:

```
60
```

## Solución

Cada panel tiene dos caras de A · B metros cuadrados, así que la
respuesta es 2 · N · A · B. `O(1)`.

Detalles a tener en cuenta:

- cuentan las dos caras: sin el factor 2 el ejemplo da 30 en vez de 60
  (prueba 01);
- la mayor respuesta es 2 000 000, que cabe de sobra en 32 bits
  (prueba 03).

## Soluciones optimizadas

`1293_math_optimized.go`. Conserva área int64 exacta 2*N*A*B, como máximo 2000000. Sustituye envoltorios os.File por syscall.Read/Write y búferes fijos de 64 bytes. Lecturas reintentan EINTR; escrituras tratan progreso parcial/EINTR antes de reutilizar almacenamiento. Análisis/formato exactos incluso entre recargas. O(1) tiempo/estado; conserva fórmula Go sencilla.

Accepted exacto Go 1.14 #11326972: 0.015 s / 272 KB. Comparación guardada 2026-11-20 con compiladores actuales de la familia: tiempo 1/32, memoria 1/32. Por debajo de 1024 KB, admisión estricta solo por tiempo.

- `1293_math_optimized.go`: 0.015 s / 272 KB; base didáctica conservada `1293_math.go` (Go 1.14 x64): 0.031 s / 1152 KB; cambio de tiempo -51.6%; cambio de memoria -76.4%.

`1293_math_optimized.py` se reutiliza byte por byte, sin otro archivo ni un algoritmo nuevo. Su Accepted de fuente exacto en CPython 3.12 #11327023 mide 0.062 s / 596 KB. En el grupo guardado de compiladores actuales de la familia Python, 2026-11-20: puesto temporal 35/1017, memoria 897/1017. Al usar menos de 1024 KB, el criterio estricto de diez primeros o 15% superior usa solo tiempo; el asterisco conserva la meta de clasificación propia del lenguaje. El mismo archivo tiene también el Accepted anterior en PyPy 3.10 #11324826, 0.109 s / 188 KB. Son pares medidos en ejecuciones distintas: se elige el tiempo y puesto de CPython, mientras PyPy usa menos memoria. Las observaciones anteriores sobre ahorro de memoria en esta sección se refieren a esa medición PyPy, no a la fila CPython. Todos los fuentes didácticos siguen intactos.

Frente a `1293_math.go`: tiempo 0.031 s → 0.031 s; memoria 1152 KB → 796 KB.

`1293_math_optimized.py`. Conserva el área de dos caras2*N*A*B. Las tres entradas no superan100 y el resultado2000000, sin flotantes. Lee los números directamente, sin escáner de formato ni entrada decodificada; Rust elimina además el vector. Tiempo y estado aritmético acotado O(1); mantiene intactas las fórmulas didácticas. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1293_math.py`: tiempo 0.078 s → 0.109 s; memoria 344 KB → 188 KB.

`1293_math_optimized.rs`. Conserva el área de dos caras2*N*A*B. Las tres entradas no superan100 y el resultado2000000, sin flotantes. Lee los números directamente, sin escáner de formato ni entrada decodificada; Rust elimina además el vector. Tiempo y estado aritmético acotado O(1); mantiene intactas las fórmulas didácticas. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1293_math.rs`: tiempo 0.031 s → 0.015 s; memoria 224 KB → 48 KB.

La solución optimizada en Java analiza los tres números byte a byte
desde `System.in` en lugar de usar `Scanner`: 312 KB en lugar de
1596 KB, con el mismo tiempo.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

Comparación PyPy anterior: `1293_math_optimized.py`: puesto de tiempo 935/1017 y de memoria 3/1017 en esta muestra comparable.

`1293_math_optimized.rs`: puesto de tiempo 1/12 y de memoria 1/12 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1293_math.cpp](1293_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 124 KB | 11303289 |
| [1293_math.go](1293_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1152 KB | 11284602 |
| [1293_math.java](1293_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1596 KB | 11284606 |
| [1293_math.py](1293_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 344 KB | 11284604 |
| [1293_math.rs](1293_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 224 KB | 11284608 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1293_math_optimized.java](1293_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 312 KB | 11303733 |
| [1293_math_optimized.go](1293_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 272 KB | 11326972 |
| [1293_math_optimized.py](1293_math_optimized.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 596 KB | 11327023 |
| [1293_math_optimized.rs](1293_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 48 KB | 11324850 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
