# 1705. Liebres gánsteres

[Timus 1705](https://acm.timus.ru/problem.aspx?space=1&num=1705) · dificultad 948 · math

Problema original de Alexander Ipatov, del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una banda de k liebres robó n coles y las repartió a partes iguales; el
resto, menor que k, fue para un zorro. Una liebre más se unió al
reparto sin que nadie lo notara: con k + 1 liebres cada una recibió
exactamente lo mismo que con k. Para cada n, hallar el menor k posible.

## Entrada

El número de pruebas t (1 ≤ t ≤ 30000) y luego t líneas con n
(1 ≤ n ≤ 10^18).

## Salida

Para cada prueba, el menor k en su propia línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
9
11
18
```

Salida:

```
5
4
5
```

## Solución

Buscamos el menor k con ⌊n/k⌋ = ⌊n/(k + 1)⌋. Con q = ⌊n/k⌋ y
r = n mod k, esto se cumple justo cuando la liebre extra puede comer
del resto, es decir r ≥ q. Como r < k, hace falta q < k, así que k
supera a s = ⌊√n⌋.

Escribimos n = s² + e y k = s + x con x ≥ 1. Como (s + x)(s − x) =
s² − x², resulta n = k(s − x) + x² + e, y el cociente es s − x o
s − x + 1:

- cociente s − x, resto x² + e: la condición es x² + x ≥ s − e;
- cociente s − x + 1, resto x² + e − s − x: la condición es
  x² ≥ 2s − e + 1.

Cada desigualdad da su menor x con una raíz cuadrada entera. Cerca de
la frontera entre los dos casos la estimación puede fallar por uno, así
que para ambos valores de x se comprueban directamente k = s + x − 1,
s + x y s + x + 1, y la respuesta es el menor k que sirve. Los n
pequeños (menores que 100) se recorren sin más. `O(1)` por prueba.

Trampas:

- n llega a 10^18, así que todo va en 64 bits; ahí la raíz en coma
  flotante no es exacta y se corrige con comparaciones enteras;
- los n más pequeños se comportan distinto: n = 1 da 2 y n = 2 da 3
  (el test 02 tiene todos los n hasta 100);
- hay hasta 30000 pruebas, así que la entrada y la salida deben ser
  rápidas.

Las respuestas coinciden con una búsqueda exhaustiva para todo n hasta
200000 y con una implementación aceptada independiente en 15000 valores
hasta 10^18, incluidos los números junto a cuadrados y productos
s(s + 1).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1705_math.cpp](1705_math.cpp) | G++ 13.2 x64 | math | O(1) per test | AC | 0.062 s | 144 KB |
| [1705_math.go](1705_math.go) | Go 1.14 x64 | math | O(1) per test | AC | 0.031 s | 3152 KB |
| [1705_math.java](1705_math.java) | Java 1.8 | math | O(1) per test | AC | 0.156 s | 5284 KB |
| [1705_math.py](1705_math.py) | Python 3.12 x64 | math | O(1) per test | AC | 0.234 s | 5496 KB |
| [1705_math.rs](1705_math.rs) | Rust 1.75 x64 | math | O(1) per test | AC | 0.046 s | 2532 KB |
