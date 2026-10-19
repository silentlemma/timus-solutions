# 2101. Rectángulos inscritos por un punto interior de un triángulo

[Timus 2101](https://acm.timus.ru/problem.aspx?space=1&num=2101) · dificultad 1664 · geometry

Problema original de Alexey Danilyuk, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan un triángulo y un punto estrictamente dentro de él. Un rectángulo
está inscrito en el triángulo si todos sus vértices están en los lados.
Entre los rectángulos inscritos que tienen el punto en su borde, hallar
el área mayor y contar cuántos rectángulos distintos así hay. Los
límites son 1 segundo y 64 MB.

## Entrada

Los tres vértices y el punto, coordenadas enteras de hasta 10⁴ en valor
absoluto; los vértices no están alineados.

## Salida

El área mayor con error absoluto o relativo de a lo sumo 10⁻⁶ y después
el número de rectángulos.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 0
10 0
0 20
4 6
```

Salida:

```
48.0000000000
4
```

### Ejemplo 2

Entrada:

```
-3 0
2 -1
5 7
0 1
```

Salida:

```
9.0697674419
2
```

## Solución

Un rectángulo inscrito tiene un lado sobre un lado del triángulo, su
base, y sus dos vértices superiores en los otros dos lados. Esto solo es
posible cuando la altura sobre la base cae dentro de la base, así que un
lado con un ángulo obtuso adyacente no tiene rectángulos. Para una base
de longitud b y altura H, el rectángulo de altura h tiene anchura
b (1 − h/H). En un triángulo rectángulo los dos catetos describen los
mismos rectángulos, los que tienen una esquina en el ángulo recto, así
que esa familia se cuenta una vez.

Para cada base utilizable el punto puede estar en el lado superior del
rectángulo, lo que fija h como la distancia del punto a la base, o en el
lado izquierdo o derecho, lo que fija la posición de ese lado a lo largo
de la base y con ella h. El caso superior siempre da un rectángulo; el
lateral da otro salvo que el punto esté sobre la propia altura, donde el
lado reduciría el rectángulo a nada. El punto está estrictamente dentro,
así que todos estos rectángulos son distintos. Las áreas son racionales
con datos enteros: el doble del área del triángulo, las distancias y las
proyecciones son enteras, así que cada área es una fracción calculada de
forma exacta y redondeada a 10 decimales. Todo es O(1).

En el primer ejemplo los catetos están sobre los ejes y el punto es
(4, 6): con la esquina en el origen, el rectángulo cuyo lado derecho
pasa por el punto mide 4 de ancho y 12 de alto, área 48, la mayor de las
cuatro.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2101_geometry.cpp](2101_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 412 KB |
| [2101_geometry.go](2101_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1188 KB |
| [2101_geometry.java](2101_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 584 KB |
| [2101_geometry.py](2101_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 612 KB |
| [2101_geometry.rs](2101_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 244 KB |
