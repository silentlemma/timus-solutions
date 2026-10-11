# 1215. El proyectil más pequeño que aún da en el blanco

[Timus 1215](https://acm.timus.ru/problem.aspx?space=1&num=1215) · dificultad 300 · geometry

Problema original de Anton Botov y Anatoly Uglov, del USU Open Collegiate Programming Contest, octubre de 2002, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un proyectil cae en un punto dado y deja un cráter redondo tan ancho
como él. El blanco es un polígono convexo de 3 a 100 vértices en sentido
antihorario, con todas las coordenadas enteras en `[−2000, 2000]`. Hay
que hallar el menor diámetro del proyectil cuyo cráter toca el blanco,
con tres decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El punto de impacto y `N`, y luego los `N` vértices.

## Salida

El menor diámetro con tres decimales.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 -1 8
0 1
1 0
2 0
3 1
3 2
2 3
1 3
0 2
```

Salida:

```
2.000
```

## Solución

El cráter toca el blanco exactamente cuando su radio es al menos la
distancia del impacto al polígono, así que la respuesta es el doble de
esa distancia. Si el punto está dentro o en el borde, la distancia es 0;
como los vértices van en sentido antihorario, eso ocurre cuando el punto
está a la izquierda de cada arista o sobre ella, lo que deciden con
exactitud productos vectoriales enteros. Si no, el punto más cercano del
polígono está en su borde, así que la distancia es la menor distancia a
una arista como segmento: al pie de la perpendicular si cae dentro del
segmento y, si no, al extremo más cercano. `O(N)`.

Detalles a tener en cuenta:

- un punto en el borde cuenta como impacto con diámetro `0.000`;
- las distancias a las rectas completas de las aristas son demasiado
  pequeñas cuando el punto más cercano es un vértice;
- la respuesta es un diámetro, el doble de la distancia.

Las respuestas se compararon con una solución escrita aparte en 300
blancos aleatorios con disparos fuera, dentro y en los vértices.

## Notas por lenguaje

- Todos los lenguajes comprueban si el punto está dentro con productos
  vectoriales enteros exactos e imprimen tres decimales; Java formatea
  con `Locale.US`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1215_geometry.cpp](1215_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 220 KB |
| [1215_geometry.go](1215_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1084 KB |
| [1215_geometry.java](1215_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.109 s | 2004 KB |
| [1215_geometry.py](1215_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.078 s | 568 KB |
| [1215_geometry.rs](1215_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.031 s | 268 KB |
