# 1686. Nave fotovoltaica

[Timus 1686](https://acm.timus.ru/problem.aspx?space=1&num=1686) · dificultad 1456 · geometry

Problema original de Pavel Atnashev, del X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una nave tetraédrica está cubierta de paneles solares. Cada estrella
brilla desde una dirección dada con una intensidad igual a la longitud
del vector de dirección; un metro cuadrado iluminado con intensidad I
y ángulo de incidencia α da I · cos α vatios. Hallar la potencia total,
duplicada como exige la historia.

## Entrada

Los cuatro vértices (enteros de valor absoluto a lo sumo 100, no
coplanarios), luego n (1 ≤ n ≤ 10) y los n vectores de las estrellas,
enteros, de longitud mayor que 0 y a lo sumo 2500 y con direcciones distintas.

## Salida

La potencia duplicada, con un error de a lo sumo 10⁻⁵.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 -1 0
0 1 0
0 0 2
1 0 0
2
0 0 -1358
21 0 0
```

Salida:

```
2800.00000
```

## Solución

El tetraedro es convexo, así que ninguna cara da sombra a otra, y una
cara recibe luz de una estrella exactamente cuando su normal exterior
apunta hacia ella. Una cara de normal exterior unitaria n̂ y área A
recibe de un vector de estrella d la potencia A · max(0, n̂ · d). En su
lugar se toma el producto vectorial N de dos aristas de la cara,
orientado lejos del cuarto vértice: es la normal exterior de longitud
2A, así que la cara da max(0, N · d) / 2. Duplicar cancela la mitad, y
la respuesta es el entero Σ max(0, N · d) sobre las cuatro caras y
todas las estrellas, impreso con cinco decimales cero. `O(n)`.

Trampas:

- cada normal se orienta respecto al vértice opuesto: el orden de los
  vértices en la entrada no dice nada de la orientación;
- una estrella en el plano de una cara no le da nada (test 03).

Las respuestas coinciden con una implementación aceptada independiente
que proyecta el tetraedro sobre el plano perpendicular a cada estrella
y toma el área de la silueta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1686_geometry.cpp](1686_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 132 KB |
| [1686_geometry.go](1686_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1132 KB |
| [1686_geometry.java](1686_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.093 s | 472 KB |
| [1686_geometry.py](1686_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.078 s | 684 KB |
| [1686_geometry.rs](1686_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.046 s | 236 KB |
