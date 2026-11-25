# 2099. Un giro en ángulo recto a través de cuatro puntos

[Timus 2099](https://acm.timus.ru/problem.aspx?space=1&num=2099) · dificultad 574 · geometry

Problema original de Denis Dublennykh, del Concurso Individual Abierto de la UrFU 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

¿Puede un punto que vuela en línea recta pasar por A y luego por B,
girar 90° y luego volar en línea recta por C y después por D? El punto
de giro puede ser B o C. Los límites son 1 segundo y 64 MB.

## Entrada

Las coordenadas enteras de A, B, C, D en el espacio, hasta 10⁶ en valor
absoluto; los puntos son distintos dos a dos.

## Salida

`Valid` o `Invalid`.

## Ejemplos

### Ejemplo 1

Entrada:

```
-2 0 0
-1 0 0
0 1 0
0 2 0
```

Salida:

```
Valid
```

## Solución

La primera recta es A + t·AB y la segunda pasa por C con dirección CD,
ambas recorridas hacia delante. El vuelo es posible exactamente cuando:

- AB · CD = 0, el giro es un ángulo recto;
- AC · (AB × CD) = 0, las dos rectas están en un plano y, al ser
  perpendiculares, se cortan en un punto P;
- P = A + t·AB con t = (AC · AB) / |AB|² (el pie de la segunda recta en
  la primera, pues CD ⊥ AB) no está antes de B: AC · AB ≥ |AB|²;
- C no está antes de P en la segunda recta: (C − P) · CD = AC · CD ≥ 0,
  porque la parte de C − P a lo largo de AB es ortogonal a CD.

El producto mixto coincide, salvo el signo, con el determinante de
AB, AC y AD. El determinante es afín en cada punto, así que el
máximo absoluto se alcanza en los vértices del cubo y vale
1,6·10¹⁹. Este valor excede el rango de los enteros con signo de
64 bits. Las versiones sencillas de C++ y Rust usan enteros de
128 bits, mientras que Go y Java usan enteros grandes.

En el ejemplo la primera recta es el eje x, la segunda el eje y, el giro
ocurre en el origen tras B = (−1, 0, 0), y C = (0, 1, 0) viene después:
Valid.

## Soluciones optimizadas

Java divide cada coordenada de AC entre 65 536 y acumula por
separado las contribuciones del cociente y del resto. Cada componente
de AB × CD tiene valor absoluto de hasta 8·10¹², así que las dos sumas
H y L caben en 64 bits con signo. El producto mixto es cero si y solo
si L es divisible entre 65 536 y H + L / 65 536 es cero.

Python comprueba cada condición directamente con las diferencias de coordenadas.

**Envíos de Timus**

- Versiones sencillas · G++ 13.2 x64, №11318402 · Java 1.8, №11318403 · Python 3.12 x64, №11318407 · Rust 1.75 x64, №11318409.
- Versiones optimizadas · Java 1.8, №11318393 · Python 3.12 x64, №11318399.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11318402 · Java 1.8 №11318403 · Python 3.12 x64 №11318407 · Rust 1.75 x64 №11318409 · Go 1.14 x64 №11322396.

Rust calcula los productos escalares con 64 bits y amplía el producto triple escalar a 128 bits. Rust 1.75 x64, envío 11323329. Tiempo 0,015 → 0,046 s, memoria 232 → 48 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2099_geometry.cpp](2099_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 108 KB | 11318402 |
| [2099_geometry.go](2099_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1168 KB | 11322396 |
| [2099_geometry.java](2099_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.14 s | 1672 KB | 11318403 |
| [2099_geometry.py](2099_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 520 KB | 11318407 |
| [2099_geometry.rs](2099_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 232 KB | 11318409 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2099_geometry_optimized.java](2099_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 360 KB | 11318393 |
| [2099_geometry_optimized.py](2099_geometry_optimized.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 472 KB | 11318399 |
| [2099_geometry_optimized.rs](2099_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 48 KB | 11323329 |

\* Las soluciones marcadas aún pueden mejorar su clasificación.
