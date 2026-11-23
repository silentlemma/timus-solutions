# 1550. La pirámide del decano 3

[Timus 1550](https://acm.timus.ru/problem.aspx?space=1&num=1550) · dificultad 594 · geometry

Problema original de Evgeny Krokhalev, del XI Campeonato Universitario por Equipos de Programación de los Urales, Ekaterimburgo, 21 de abril de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una pirámide cuadrada regular de altura H y lado de la base W (ambos
menores que 10⁴) tiene un agujero cilíndrico vertical de radio R
centrado sobre el punto (X, Y) de la base, con el origen en el centro de
la base y los ejes a lo largo de sus lados. El agujero no corta ninguna
arista de la pirámide. Hay que hallar el volumen de la pirámide con el
agujero, con precisión de 10⁻³.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

H y W, luego X e Y, luego R.

## Salida

El volumen.

## Ejemplos

### Ejemplo 1

Entrada:

```
3.0 3.0
-1.00 -0.70
0.1
```

Salida:

```
8.96858
```

## Solución

La pirámide maciza tiene volumen H·W²/3. Sobre un punto (x, y) de la
base su altura es H·(1 − max(|x|, |y|)/(W/2)). Como el agujero no toca
ninguna arista, su disco queda dentro de un triángulo de la base bajo
una sola cara, donde la altura es una función lineal de (x, y). La
integral de una función lineal sobre un disco es su valor en el centro
por el área, así que el agujero quita πR²·H·(1 − max(|X|, |Y|)/(W/2)).
`O(1)`.

Detalles a tener en cuenta:

- los números pueden venir sin punto decimal (prueba 02);
- el volumen llega a unos 3·10¹¹, que la doble precisión aún guarda con
  mucho menos de 10⁻³ de error (prueba 04);
- C++ no tiene un M_PI estándar, y el compilador del juez no lo tiene,
  así que la solución en C++ usa acos(−1).

## Soluciones optimizadas

La versión optimizada en C++ usa la misma fórmula con una constante de compilación para π y funciones de entrada y salida de C. Calcula en long double e imprime cinco decimales. El envío 11317021 tardó 0,015 s y usó 136 KB. La versión sencilla tardó 0,015 s y usó 444 KB.

Java usa la misma fórmula de volumen, con lectura decimal directa y salida de precisión fija. El envío 11318321 tardó 0,093 s y usó 464 KB frente a 0,093 s y 1964 KB de la versión sencilla.

Go aplica la misma fórmula de volumen y usa búferes pequeños para leer números y escribir el resultado con precisión fija. Go 1.14 x64, envío 11322933. Tiempo 0,031 → 0,015 s, memoria 1080 → 320 KB.

La versión de Python lee los cinco valores de un flujo de bytes y calcula la fracción de la altura a partir de la distancia al lado más cercano de la base. Python 3.12 x64, envío 11322022. Tiempo 0,093 → 0,109 s, memoria 444 → 452 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322273 · Go 1.14 x64 №11322275 · Java 1.8 №11322277 · Python 3.12 x64 №11322278 · Rust 1.75 x64 №11322279.

Rust conserva la fórmula del volumen y usa búferes fijos para las entradas habituales y la salida de cinco decimales. Rust 1.75 x64, envío 11323247. Tiempo 0,015 → 0,031 s, memoria 244 → 68 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1550_geometry_parsing_optimized.py`. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328762 (Python 3.12 x64): **0.062 s / 740 KB**. Comparación archivada: `1550_geometry.py` (Python 3.12 x64) — 0.093 s / 444 KB (#11322278).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1550_geometry.cpp](1550_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 444 KB | 11322273 |
| [1550_geometry.go](1550_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1080 KB | 11322275 |
| [1550_geometry.java](1550_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 1964 KB | 11322277 |
| [1550_geometry.py](1550_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 444 KB | 11322278 |
| [1550_geometry.rs](1550_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 244 KB | 11322279 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1550_geometry_optimized.cpp](1550_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 136 KB | 11317021 |
| [1550_geometry_optimized.go](1550_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 320 KB | 11322933 |
| [1550_geometry_optimized.java](1550_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 464 KB | 11318321 |
| [1550_geometry_optimized.py](1550_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 452 KB | 11322022 |
| [1550_geometry_optimized.rs](1550_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 68 KB | 11323247 |
| [1550_geometry_parsing_optimized.py](1550_geometry_parsing_optimized.py) | Python 3.12 x64 | geometry, parsing | O(1) | AC | 0.062 s | 740 KB | 11328762 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
