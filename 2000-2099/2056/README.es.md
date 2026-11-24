# 2056. Determinar la categoría de beca

[Timus 2056](https://acm.timus.ru/problem.aspx?space=1&num=2056) · difficulty 41 · implementation

Problema popular, del Campeonato de Programación Deportiva de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un estudiante aprobó n exámenes con notas de 3 a 5. Indicar la beca:
`None` si hay algún 3; si no, `Named` si todas las notas son 5; si no,
`High` si la media es al menos 4,5; y `Common` en los demás casos. Los
límites son 1 segundo y 64 MB.

## Entrada

El número de exámenes n, 1 ≤ n ≤ 10, y después n líneas con una nota
cada una.

## Salida

Una palabra, respetando mayúsculas.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3
5
5
4
```

```
High
```

```
3
3
3
3
```

```
None
```

En el primero la suma es catorce y `2·14≥9·3`, por lo que el promedio
supera 4,5. No hay tres, pero tampoco son todas cinco: corresponde
`High`. En el segundo hay tres y la regla prioritaria determina `None`.

## Solución

Se leen las notas guardando su suma S y su mínimo. Luego se aplican las
reglas en orden: cualquier 3 da `None`; todo cincos da `Named`; una
media de al menos 4.5 da `High`, comprobado en enteros como 2S ≥ 9n; lo
demás es `Common`. `O(n)`.

Detalles a tener en cuenta:

- un 3 pesa más que cualquier media;
- todo cincos es `Named`, no `High`;
- el umbral 4.5 es inclusivo: un 4 y un 5 dan `High`.

## Soluciones optimizadas

`2056_implementation_optimized.py`. Analiza notas como enteros, guardando presencia de 3 y cantidad de 4. Para notas 3,4,5 sin ningún 3, media al menos 4.5 equivale a que el doble de cuatros no supere n. Conserva los cuatro textos de beca. Evita actualizar mínimo y suma; a diferencia del experimento descartado por escritura de bytes, interpreta numéricamente signos más y ceros iniciales. O(n) tiempo, O(I) tokens retenidos; conserva la sencilla basada en media. La fila Accepted indica el runtime real y sus medidas emparejadas. Vacía salida antes de os._exit(0), que omite cierre del intérprete; la mejora medida de memoria depende del runtime y no implica aceleración asintótica.

Frente a `2056_implementation.py`: tiempo 0.078 s → 0.125 s; memoria 472 KB → 228 KB.

La solución optimizada en C++ lee con `scanf` e imprime con `puts` en
lugar de `iostream` y `std::string`: 116 KB en lugar de 420 KB, con el
mismo tiempo.

`2056_parsing_optimized.go`. Se analizan las notas decimales con un búfer de bytes acotado, lectura directa de la entrada estándar y escritura completa. Una nota de 3 determina None inmediatamente, sin leer las restantes. En otro caso se mantienen el mínimo, la suma y la comparación entera con el umbral de 4,5. Tiempo máximo O(n) y espacio auxiliar O(1); se conserva la implementación sencilla.

Accepted #11329388 (Go 1.14 x64): **0.015 s / 260 KB**.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`2056_implementation_optimized.py`: puesto de tiempo 272/297 y de memoria 1/297 en esta muestra comparable.

La admisión y los asteriscos actuales siguen los [criterios compartidos](../../RATING_CRITERIA.md): diez primeros o 15% superior, sustituidos por la comparación de referencia indicada en muestras pequeñas del mismo compilador. Si nuestra memoria es inferior a 1024 KB, solo se compara el tiempo. Las mediciones anteriores describen sus propias ejecuciones históricas.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2056_implementation.cpp](2056_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 420 KB | 11293663 |
| [2056_implementation.go](2056_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.046 s | 1096 KB | 11293666 |
| [2056_implementation.java](2056_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 420 KB | 11303532 |
| [2056_implementation.py](2056_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 472 KB | 11293667 |
| [2056_implementation.rs](2056_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 224 KB | 11293678 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2056_implementation_optimized.cpp](2056_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 116 KB | 11303966 |
| [2056_implementation_optimized.py](2056_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(n) time; O(I) space | AC | 0.125 s | 228 KB | 11325602 |
| [2056_parsing_optimized.go](2056_parsing_optimized.go) | Go 1.14 x64 | parsing | O(n) time; O(1) auxiliary space | AC | 0.015 s | 260 KB | 11329388 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
