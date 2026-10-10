# 1168. Contar los lugares donde un receptor oye todas las emisoras

[Timus 1168](https://acm.timus.ru/problem.aspx?space=1&num=1168) · dificultad 727 · geometry

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
`distancia² ≤ R²` solo depende de `⌊R²⌋`. Esto convierte todo el problema
en aritmética entera; el único paso en coma flotante es `⌊R² + ε⌋` por
emisora.

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

- Todos los lenguajes calculan la raíz cuadrada entera a partir de una en
  coma flotante y la corrigen un paso si hace falta; Python usa
  `math.isqrt`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1168_geometry.cpp](1168_geometry.cpp) | G++ 13.2 x64 | geometry | O(M·N·K) | AC | 0.015 s | 256 KB |
| [1168_geometry.go](1168_geometry.go) | Go 1.14 x64 | geometry | O(M·N·K) | AC | 0.031 s | 1180 KB |
| [1168_geometry.java](1168_geometry.java) | Java 1.8 | geometry | O(M·N·K) | AC | 0.171 s | 1176 KB |
| [1168_geometry.py](1168_geometry.py) | Python 3.12 x64 | geometry | O(M·N·K) | AC | 0.765 s | 940 KB |
| [1168_geometry.rs](1168_geometry.rs) | Rust 1.75 x64 | geometry | O(M·N·K) | AC | 0.046 s | 288 KB |
