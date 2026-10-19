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

Todas las comprobaciones son exactas en enteros. El producto mixto llega
a 1,6·10¹⁹ en valor absoluto, más de 64 bits con signo, así que C++ y Rust
lo calculan con enteros de 128 bits y Go y Java con enteros grandes.

En el ejemplo la primera recta es el eje x, la segunda el eje y, el giro
ocurre en el origen tras B = (−1, 0, 0), y C = (0, 1, 0) viene después:
Valid.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2099_geometry.cpp](2099_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 128 KB |
| [2099_geometry.go](2099_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1160 KB |
| [2099_geometry.java](2099_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1720 KB |
| [2099_geometry.py](2099_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 548 KB |
| [2099_geometry.rs](2099_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 240 KB |
