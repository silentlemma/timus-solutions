# 1405. La cabra en el huerto 5

[Timus 1405](https://acm.timus.ru/problem.aspx?space=1&num=1405) · dificultad 715 · geometry

Problema original de Vladimir Yakovlev, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un huerto tiene 2 ≤ N ≤ 1000 árboles, dados al centímetro. Dos cabras
se atan a dos árboles distintos. Una cabra no debe alcanzar ningún otro
árbol, las dos cabras no deben alcanzarse entre sí, y una cuerda mide
entre 1 y 50 metros. Hay que imprimir la mayor área total que alcanzan
las cabras, con precisión de 1 cm². Se garantiza que hay una forma
válida de atarlas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego las coordenadas de los árboles.

## Salida

La mayor área en m² con cuatro cifras decimales.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
1 1
-2 0
5 3
-2 3
8 3.10
-2 -1
-2 2
8 4.10
```

Salida:

```
36.8060
```

## Solución

En el árbol i la cuerda no puede alcanzar el árbol más cercano, así que
con el tope de 50 metros mide a lo sumo topᵢ = min(50, distancia al
otro árbol más cercano). Para cabras en los árboles i y j a distancia d,
las cuerdas a y b deben cumplir

1 ≤ a ≤ topᵢ, 1 ≤ b ≤ topⱼ, a + b ≤ d,

y el área es π(a² + b²). Es una función convexa sobre un polígono, así
que su máximo está en un vértice: una esquina del rectángulo o un punto
donde la recta a + b = d corta un lado. Se prueban esos siete puntos, se
quedan los que están en la región y se toma el mejor sobre todos los
pares de árboles. `O(N²)`. La solución en Python recorre los árboles por
su top y corta una fila en cuanto top² de ambos árboles juntos no puede
superar al mejor.

Detalles a tener en cuenta:

- los límites de 1 y 50 metros son fáciles de pasar por alto: dos
  árboles a 141 m dan 5000π, no el cuadrado de la distancia (prueba 02);
- un árbol con un vecino a menos de 1 m no puede llevar cabra (pruebas
  03 y 06);
- los casos justos están permitidos: una cuerda de exactamente 1 m, o
  dos cuerdas que suman exactamente la distancia (prueba 05 y prueba
  generada 4);
- en el juez C++ no tiene M_PI, así que π es acos(-1).

La búsqueda de vértices se comparó con una rejilla fina sobre la región
en 3 000 casos aleatorios, y los ejemplos del foro dan las respuestas
esperadas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1405_geometry.cpp](1405_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2) | AC | 0.046 s | 240 KB |
| [1405_geometry.go](1405_geometry.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.078 s | 1152 KB |
| [1405_geometry.java](1405_geometry.java) | Java 1.8 | geometry | O(N^2) | AC | 0.140 s | 5560 KB |
| [1405_geometry.py](1405_geometry.py) | Python 3.12 x64 | geometry | O(N^2) | AC | 0.640 s | 1248 KB |
| [1405_geometry.rs](1405_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2) | AC | 0.046 s | 304 KB |
