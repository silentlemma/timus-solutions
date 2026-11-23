# 1336. El problema de Ben Betsalel

[Timus 1336](https://acm.timus.ru/problem.aspx?space=1&num=1336) · dificultad 123 · math

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que escribir un número entero n, 1 ≤ n ≤ 10⁹, como cociente de un
cuadrado entre un cubo: hallar enteros m y k de 1 a 10¹⁰⁰ con
m² = k³ · n. Se acepta cualquier par así.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número n.

## Salida

m en la primera línea y k en la segunda.

## Comprobación

El comprobador del repositorio exige dos tokens enteros de dígitos m,k, ambos en [1,10^100], y verifica m²=k³*n con aritmética entera exacta.

## Ejemplos

### Ejemplo 1

Entrada:

```
18
```

Salida:

```
12
2
```

### Ejemplo 2

Entrada:

```
1
```

Salida:

```
1
1
```

## Solución

Se toma k = n y m = n². Entonces m² = n⁴ = n³ · n. Así que siempre
existe un par, y por eso el problema siempre tiene solución. `O(1)`.

Detalles a tener en cuenta:

- m llega a 10¹⁸, lo que necesita un entero de 64 bits (prueba 03);
- el primer ejemplo muestra un par más pequeño; se acepta cualquiera
  correcto.

## Soluciones optimizadas

La solución optimizada en Java lee n byte a byte de `System.in` en lugar
de crear un `Scanner`, cuyas expresiones regulares y datos de
configuración regional son el gasto principal de un programa que hace
una sola multiplicación; n² sigue cabiendo en `long`, porque no pasa de
10¹⁸: {1336_math_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1336_math_optimized.java`: reducción de tiempo +0.00%; reducción de
  memoria +77.24%; base: `1336_math.java`.

`1336_math_optimized.py`. Conserva m=n², k=n exactamente: m²=n⁴=k³*n. Cumple los límites sin factorizar n. Con n<=10^9 el mayor valor emitido es 10^18, seguro incluso en i64 con signo. Aritmética acotada y espacio O(1). Usa una llamada a print con separador de salto de línea en vez de dos; toda la aritmética sigue siendo entera. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1336_math.py`: tiempo 0.062 s → 0.109 s; memoria 352 KB → 196 KB.

`1336_math_optimized.rs`. Conserva m=n², k=n exactamente: m²=n⁴=k³*n. Cumple los límites sin factorizar n. Con n<=10^9 el mayor valor emitido es 10^18, seguro incluso en i64 con signo. Aritmética acotada y espacio O(1). Emite los dos enteros directamente en líneas separadas, sin formato Rust ni String de entrada decodificada. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1336_math.rs`: tiempo 0.015 s → 0.031 s; memoria 240 KB → 60 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1336_parsing_optimized.go`. Se usa conversión directa por tipos con un búfer recargable de 256 bytes y salida compacta con escrituras completas. Los negativos se acumulan con signo, incluido el mínimo entero, sin reflexión de entrada ni despacho genérico de salida. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios.

Accepted #11329107 (Go 1.14 x64): **0.015 s / 792 KB**. Comparación archivada: `1336_math.go` (Go 1.14 x64) — 0.031 s / 1068 KB (#11285034).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1336_math_optimized.py`: puesto de tiempo 25/45 y de memoria 1/45 en esta muestra comparable.

`1336_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1336_math.cpp](1336_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11285033 |
| [1336_math.go](1336_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB | 11285034 |
| [1336_math.java](1336_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1564 KB | 11285036 |
| [1336_math.py](1336_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 352 KB | 11285035 |
| [1336_math.rs](1336_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB | 11285038 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1336_math_optimized.java](1336_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 356 KB | 11304378 |
| [1336_math_optimized.py](1336_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 196 KB | 11324908 |
| [1336_math_optimized.rs](1336_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 60 KB | 11324871 |
| [1336_parsing_optimized.go](1336_parsing_optimized.go) | Go 1.14 x64 | parsing | O(1) | AC | 0.015 s | 792 KB | 11329107 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
