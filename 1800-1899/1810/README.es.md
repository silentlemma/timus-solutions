# 1810. Antiecuaciones

[Timus 1810](https://acm.timus.ru/problem.aspx?space=1&num=1810) · dificultad 4022 · math

Problema original del Tavrida NU Akai Contest, sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Contar los vectores x de {0, 1, 2}ⁿ tales que cada una de k formas
lineales módulo 3 difiere de su valor dado:
aᵢ₁x₁ + … + aᵢₙxₙ ≢ bᵢ (mod 3) para todo i.

## Entrada

k y n (1 ≤ k, n ≤ 30), luego k líneas aᵢ₁ … aᵢₙ bᵢ con valores de 0 a
2.

## Salida

El número de soluciones.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
2 2 1 1
2 1 0 0
1 2 2 2
```

Salida:

```
8
```

### Ejemplo 2

Entrada:

```
4 3
2 2 1 1
2 1 0 0
1 2 2 2
1 0 1 2
```

Salida:

```
6
```

## Solución

Se mira y = Ax en lugar de x. Si A tiene rango r sobre GF(3), cada y
de la imagen de A proviene de exactamente 3^(n−r) vectores x, así que
la respuesta es 3^(n−r) por el número de vectores de la imagen con
yᵢ ≠ bᵢ para todo i. La eliminación gaussiana sobre la matriz
traspuesta da una base de su núcleo, los vectores w ortogonales a cada
columna; y está en la imagen exactamente cuando su síndrome, la lista
de productos w·y, es cero.

Cada yᵢ tiene dos valores permitidos, así que hay 2ᵏ ≤ 2³⁰ candidatos
y, demasiados para probarlos, pero se dividen en dos mitades de como
mucho 2¹⁵ opciones cada una. El síndrome es aditivo: se listan los
síndromes de todas las opciones de la primera mitad y, para cada opción
de la segunda, se cuentan los síndromes de la primera iguales a menos
el suyo. Un síndrome sobre GF(3) de como mucho 30 coordenadas se guarda
como dos máscaras de bits, las coordenadas iguales a 1 y a 2. Así la
suma cuesta unas pocas operaciones de bits, y el negativo intercambia
las máscaras. `O(nk min(n,k) + 2^(k/2) · k)`.

En el primer ejemplo 8 de las 27 asignaciones evitan los tres valores;
el segundo añade una antiecuación más y deja 6.

Trampas:

- las filas iguales o proporcionales son dependientes; cada vector de
  la imagen tiene varias preimágenes si y solo si r < n;
- una fila de ceros con bᵢ = 0 lo descarta todo;
- la respuesta puede llegar a 3³⁰ y necesita 64 bits.

Las respuestas coinciden con un recuento directo de las 3ⁿ asignaciones
en 100 sistemas pequeños, y con una implementación aceptada
independiente en sistemas cuadrados, de rango bajo, repetitivos y
estrechos con 30 antiecuaciones.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1810_math.cpp](1810_math.cpp) | G++ 13.2 x64 | math | O(nk min(n,k) + 2^(k/2) k) | AC | 0.015 s | 748 KB |
| [1810_math.go](1810_math.go) | Go 1.14 x64 | math | O(nk min(n,k) + 2^(k/2) k) | AC | 0.109 s | 6272 KB |
| [1810_math.java](1810_math.java) | Java 1.8 | math | O(nk min(n,k) + 2^(k/2) k) | AC | 0.156 s | 3500 KB |
| [1810_math.py](1810_math.py) | Python 3.12 x64 | math | O(nk min(n,k) + 2^(k/2) k) | AC | 0.171 s | 10228 KB |
| [1810_math.rs](1810_math.rs) | Rust 1.75 x64 | math | O(nk min(n,k) + 2^(k/2) k) | AC | 0.031 s | 1540 KB |
