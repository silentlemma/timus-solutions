# 2215. Contar puntos en rectángulos mientras todo el plano gira

[Timus 2215](https://acm.timus.ru/problem.aspx?space=1&num=2215) · dificultad 2164 · geometry, fenwick

Problema original de Vadim Barinov, de la Olimpiada Académica Universitaria Escolar de Informática 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N puntos distintos reciben Q eventos en orden: girar todos los puntos
90°, 180° o 270° en sentido antihorario alrededor de un punto dado, o
contar los puntos dentro de un rectángulo de lados paralelos a los ejes.
Los límites son 3 segundos y 256 MB.

## Entrada

N, 1 ≤ N ≤ 4 · 10⁴, luego los puntos, luego Q, 1 ≤ Q ≤ 4 · 10⁴, y los
eventos "r90 x y", "r180 x y", "r270 x y" o "ask x1 y1 x2 y2", con todas
las coordenadas de valor absoluto hasta 10⁹.

## Salida

La cuenta de cada "ask".

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1 1
2 2
3 3
4 4
4
r90 0 0
ask -2 -1 0 4
r180 1 1
ask 3 -3 6 0
```

Salida:

```
2
3
```

## Solución

Cualquier sucesión de cuartos de vuelta alrededor de puntos es un giro
de cuartos de vuelta alrededor del origen seguido de una traslación: la
posición actual de un punto original p es Rᵏ p + t. Un nuevo giro de j
cuartos alrededor de c lo lleva a Rʲ(Rᵏ p + t − c) + c, así que basta
actualizar k y t.

Un rectángulo de consulta en coordenadas actuales se lleva a las
originales restando t y girando −k cuartos. Un cuarto de vuelta lleva un
rectángulo de lados paralelos a los ejes a otro igual, así que basta
llevar dos esquinas opuestas y ordenar sus coordenadas. Todas las
consultas preguntan entonces por el mismo conjunto fijo de puntos.

Eso se responde fuera de línea: cada rectángulo da dos eventos, en su
lado derecho y justo a la izquierda de su lado izquierdo, los eventos y
los puntos se barren en orden de x, y un árbol de Fenwick sobre las y
comprimidas cuenta los puntos insertados en cada rango de y.

En el ejemplo, tras el primer giro los puntos son (−1, 1) … (−4, 4), y
el primer rectángulo contiene (−1, 1) y (−2, 2).

Esto cuesta O((N + Q) log N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2215_geometry_fenwick.cpp](2215_geometry_fenwick.cpp) | G++ 13.2 x64 | geometry, fenwick | O((N + Q) log N) | AC | 0.078 s | 5076 KB |
| [2215_geometry_fenwick.go](2215_geometry_fenwick.go) | Go 1.14 x64 | geometry, fenwick | O((N + Q) log N) | AC | 0.296 s | 10672 KB |
| [2215_geometry_fenwick.java](2215_geometry_fenwick.java) | Java 1.8 | geometry, fenwick | O((N + Q) log N) | AC | 0.421 s | 12104 KB |
| [2215_geometry_fenwick.py](2215_geometry_fenwick.py) | Python 3.12 x64 | geometry, fenwick | O((N + Q) log N) | AC | 0.718 s | 37016 KB |
| [2215_geometry_fenwick.rs](2215_geometry_fenwick.rs) | Rust 1.75 x64 | geometry, fenwick | O((N + Q) log N) | AC | 0.062 s | 8496 KB |
