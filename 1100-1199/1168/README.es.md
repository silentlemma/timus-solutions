# 1168. Contar los lugares donde un receptor oye todas las emisoras

[Timus 1168](https://acm.timus.ru/problem.aspx?space=1&num=1168) · dificultad 721 · geometry

Problema original de Mugurel Ionut Andreica, del Romanian Open Contest de diciembre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un mapa es una cuadrícula `M×N` (`M, N ≤ 50`) de altitudes enteras de 0 a
32000. `K ≤ 1000` emisoras están en los centros de casillas distintas, a
la altitud de su casilla, cada una con un radio real de emisión `R` de
hasta 100000. Un receptor puede ponerse en el centro de cualquier casilla
sin emisora, a la altitud de la casilla o cualquier número entero de
metros más arriba. Hay que contar las colocaciones (casilla y altitud) en
las que la distancia en 3D a cada emisora es a lo sumo su radio.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`M`, `N` y `K`, luego las `M` filas de altitudes y luego `K` líneas con
la fila, la columna y el radio de una emisora.

## Salida

El número de colocaciones.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 5 3
1 2 3 4 5
6 7 8 9 10
1 2 3 4 5
6 7 8 9 10
5 4 3 2 1
1 1 4.3
5 5 4.3
5 1 4.3
```

Salida:

```
4
```

## Solución

Todas las coordenadas salvo los radios son enteras, así que la distancia
al cuadrado de una colocación a una emisora es un entero, y la condición
`distancia² ≤ R²` solo depende de `⌊R²⌋`. Los pasos en coma flotante son
`⌊R² + ε⌋` por emisora y, salvo en Python, las estimaciones de raíces;
el resto de la aritmética es entera.

Para una casilla a distancia horizontal al cuadrado `d` de una emisora de
altura `z`, el receptor a altitud `a` la oye exactamente cuando
`(a − z)² ≤ ⌊R²⌋ − d`, es decir, cuando `a` está en `[z − s, z + s]` con
`s = ⌊√(⌊R²⌋ − d)⌋`, o nunca si `⌊R²⌋ < d`. Se intersecan esos
intervalos sobre todas las emisoras, empezando abajo por la altitud de la
propia casilla, y se suma el número de altitudes enteras que quedan.
`O(M·N·K)`, a lo sumo 1,5 millones de pasos.

Detalles a tener en cuenta:

- el receptor no puede bajar de su casilla, así que el extremo inferior
  empieza en la altitud de la casilla, no en 0;
- una distancia exactamente igual al radio cuenta, por eso `⌊R²⌋` se toma
  con una pequeña tolerancia;
- las casillas con emisora no se permiten aunque todas las emisoras
  lleguen a ellas.

Las respuestas se compararon en 150 mapas pequeños aleatorios con un
conteo directo sobre todas las altitudes usando fracciones exactas para
los radios, y en una de las pruebas generadas.

## Notas por lenguaje

- C++, Go, Java y Rust calculan la raíz cuadrada entera a partir de una en
  coma flotante y la corrigen un paso si hace falta; Python usa
  `math.isqrt`.

## Soluciones optimizadas

Se omiten las estaciones cuya esfera de cobertura contiene la esfera más pequeña. Se reutiliza la contribución de cada fila y se evita la raíz cuadrada si ambos extremos del intervalo ya están cubiertos. Las celdas con estaciones siguen excluidas.

El envío 11318011 en Python tardó 0.437 s y usó 1452 KB. La versión sencilla tardó 0.781 s y usó 1076 KB.

El envío 11318028 en Java tardó 0.093 s y usó 732 KB. La versión sencilla tardó 0.125 s y usó 1208 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321897 · Rust 1.75 x64 №11321898 · Go 1.14 x64 №11322196 · Java 1.8 №11322197 · Python 3.12 x64 №11322198.

Go guarda el terreno y los datos de las estaciones en arreglos fijos y reutiliza las máscaras de cobertura por fila. Go 1.14 x64, envío 11321943. Tiempo 0,046 → 0,015 s, memoria 1172 → 392 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1168_geometry.cpp](1168_geometry.cpp) | G++ 13.2 x64 | geometry | O(M·N·K) | AC | 0.015 s | 244 KB | 11321897 |
| [1168_geometry.go](1168_geometry.go) | Go 1.14 x64 | geometry | O(M·N·K) | AC | 0.046 s | 1172 KB | 11322196 |
| [1168_geometry.java](1168_geometry.java) | Java 1.8 | geometry | O(M·N·K) | AC | 0.125 s | 1208 KB | 11322197 |
| [1168_geometry.py](1168_geometry.py) | Python 3.12 x64 | geometry | O(M·N·K) | AC | 0.781 s | 1076 KB | 11322198 |
| [1168_geometry.rs](1168_geometry.rs) | Rust 1.75 x64 | geometry | O(M·N·K) | AC | 0.031 s | 280 KB | 11321898 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1168_geometry_optimized.py](1168_geometry_optimized.py) | Python 3.12 x64 | geometry | O(M·N·K) | AC | 0.437 s | 1452 KB | 11318011 |
| [1168_geometry_optimized.java](1168_geometry_optimized.java) | Java 1.8 | geometry | O(M·N·K) | AC | 0.093 s | 732 KB | 11318028 |
| [1168_geometry_optimized.go](1168_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(M·N·K) | AC | 0.015 s | 392 KB | 11321943 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
