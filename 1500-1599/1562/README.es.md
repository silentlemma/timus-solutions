# 1562. Piña transgénica

[Timus 1562](https://acm.timus.ru/problem.aspx?space=1&num=1562) · dificultad 402 · geometry

Problema original de Denis Musin, del XII Campeonato de Programación de la Universidad Estatal de los Urales, 6 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una piña es un elipsoide de revolución alargado de anchura a y altura b
(1 ≤ a < b ≤ 100, en centímetros). Se tumba de lado y se corta
perpendicularmente a su eje en n trozos del mismo grosor
(1 ≤ n ≤ 100). Un centímetro cúbico pesa un gramo. Hay que imprimir el
peso de cada trozo en el orden en que se corta, con precisión de un
microgramo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

a, b y n en una línea; a y b pueden ser fraccionarios.

## Salida

n líneas, los pesos en gramos con seis cifras tras el punto.

## Ejemplos

### Ejemplo 1

Entrada:

```
15 20.5 8
```

Salida:

```
103.773800
273.585474
386.793256
443.397147
443.397147
386.793256
273.585474
103.773800
```

## Solución

Se pone el eje a lo largo de z con el centro en 0. La sección a la
altura z es un círculo de radio (a/2)·√(1 − (2z/b)²), así que su área
es π·a²/4·(1 − 4z²/b²). Su integral de 0 a z,

V(z) = π·a²/4·(z − 4z³/(3b²)),

da el trozo entre los cortes z₁ y z₂ como V(z₂) − V(z₁), con los cortes
en −b/2 + b·i/n. La piña entera pesa π·a²·b/6, la suma de todos los
trozos. `O(n)`.

Detalles a tener en cuenta:

- a es la anchura completa, no el radio;
- las medidas pueden ser fraccionarias (la prueba 05 y el ejemplo);
- al resolver empates tras redondear, el generador debe mantener 1 ≤ a < b
  (gen1/gen4; semilla de regresión 1318341 en modo 1);
- los trozos de los extremos de una piña larga y fina pesan solo
  centésimas de gramo, y también necesitan seis cifras (prueba 04).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1562_geometry.cpp](1562_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 156 KB |
| [1562_geometry.go](1562_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1100 KB |
| [1562_geometry.java](1562_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.109 s | 2072 KB |
| [1562_geometry.py](1562_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.093 s | 424 KB |
| [1562_geometry.rs](1562_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.015 s | 268 KB |
