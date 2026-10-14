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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1550_geometry.cpp](1550_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 456 KB |
| [1550_geometry.go](1550_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB |
| [1550_geometry.java](1550_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1964 KB |
| [1550_geometry.py](1550_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 460 KB |
| [1550_geometry.rs](1550_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 256 KB |
