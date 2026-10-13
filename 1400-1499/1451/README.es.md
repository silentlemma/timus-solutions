# 1451. La fábula del quiosco

[Timus 1451](https://acm.timus.ru/problem.aspx?space=1&num=1451) · dificultad 994 · geometry

Problema original de Ilya Grebnov, Dmitry Kovalioff y Nikita Rybak, de Timus Top Coders: Second Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres programadores viven en tres puntos distintos de coordenadas reales
entre −1000 y 1000, dadas con siete decimales como mucho. Hay que hallar
un sitio para un quiosco de cerveza con la menor suma de distancias a
las tres casas; la suma debe coincidir con la mínima hasta seis
decimales, y se acepta cualquier sitio así.

Límite de tiempo: 0.25 segundos. Límite de memoria: 64 MB.

## Entrada

X1, Y1, X2, Y2, X3, Y3 en una línea.

## Salida

Las coordenadas del quiosco.

## Ejemplos

### Ejemplo 1

Entrada:

```
1.1 3.1 5.1 1.1 4.1 5.1
```

Salida:

```
3.37423161 3.38281356
```

## Solución

Es el punto de Fermat del triángulo. Si un ángulo del triángulo mide al
menos 120°, la respuesta es esa misma casa: alejarse no compensa,
porque las otras dos casas tiran formando un ángulo de 120° o más y su
tirón conjunto no supera el coste unitario del paso. Tres casas en
una recta caen en este caso, con un ángulo de 180° en la casa del medio.

Si no, desde el mejor punto cada lado se ve bajo 120°. Sus coordenadas
baricéntricas son a / sin(A + 60°), b / sin(B + 60°), c / sin(C + 60°),
con a, b, c los lados opuestos a los ángulos A, B, C; los tres pesos son
positivos porque cada ángulo es menor que 120°. Los ángulos salen de
atan2 de los productos vectorial y escalar, que sigue siendo preciso en
triángulos muy planos, y el punto es la media ponderada de las casas.
`O(1)`.

Detalles a tener en cuenta:

- tres casas en una recta (pruebas 02, 12);
- ángulos justo por debajo y por encima de 120° (pruebas 05, 10, 11);
- un triángulo fino como una aguja, donde los cosenos pierden precisión
  (pruebas 08, 13).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1451_geometry.cpp](1451_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 156 KB |
| [1451_geometry.go](1451_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1112 KB |
| [1451_geometry.java](1451_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 2012 KB |
| [1451_geometry.py](1451_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 672 KB |
| [1451_geometry.rs](1451_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.062 s | 268 KB |
