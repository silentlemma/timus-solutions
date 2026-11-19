# 1327. Fusibles

[Timus 1327](https://acm.timus.ru/problem.aspx?space=1&num=1327) · dificultad 47 · math

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un ordenador pierde un fusible cada día laborable impar: el día 1,
luego el día 3, el día 5 y así sucesivamente. Hay que contar los
fusibles perdidos del día A al día B, ambos incluidos,
1 ≤ A ≤ B ≤ 10 000.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

A en la primera línea y B en la segunda.

## Salida

El número de fusibles.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
5
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
100
200
```

Salida:

```
50
```

## Solución

Los días 1 a x contienen ⌊(x + 1) / 2⌋ días impares. Los días impares
de A a B son los que hay hasta B menos los que hay hasta A − 1, lo que
da ⌊(B + 1) / 2⌋ − ⌊A / 2⌋. `O(1)`.

Detalles a tener en cuenta:

- un intervalo de un solo día da 1 si el día es impar y 0 si es par
  (pruebas 03 y 04);
- los dos extremos cuentan cuando son impares (pruebas 01 y 07).

## Soluciones optimizadas

La solución optimizada en Java analiza los dos números byte a byte desde
`System.in` en lugar de usar `Scanner`: 0.078 s en lugar de 0.109 s y
304 KB en lugar de 1624 KB.

`1327_math_optimized.py`. Conserva la diferencia de prefijos de días impares, (B+1)//2-A//2. Analiza ambos extremos acotados como tokens de bytes en vez de dos llamadas de entrada de texto. La aritmética ocupa O(1) tiempo y espacio auxiliar. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1327_math.py`: tiempo 0.062 s → 0.125 s; memoria 404 KB → 208 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1327_math_optimized.py`: puesto de tiempo 90/102 y de memoria 1/102 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1327_math.cpp](1327_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11284981 |
| [1327_math.go](1327_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB | 11284982 |
| [1327_math.java](1327_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1624 KB | 11284984 |
| [1327_math.py](1327_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 404 KB | 11284983 |
| [1327_math.rs](1327_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 236 KB | 11284985 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1327_math_optimized.java](1327_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 304 KB | 11303741 |
| [1327_math_optimized.py](1327_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 208 KB | 11324836 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
