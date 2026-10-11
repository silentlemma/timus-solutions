# 1285. Hilo en el hiperespacio

[Timus 1285](https://acm.timus.ru/problem.aspx?space=1&num=1285) · dificultad 1584 · geometry

Problema original de Alexander Mironenko y Alexey Lakhtin, del Concurso Individual de la Universidad Estatal de los Urales 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En el espacio de ocho dimensiones hay dos puntos A y B y una bola de
radio entero positivo R ≤ 3000 con centro C; todas las coordenadas son
enteras con valor absoluto como mucho 1000, y A y B están estrictamente
fuera de la bola.
Hay que hallar la longitud del camino más corto de A a B que nunca
entra en la bola (puede ir por su superficie), con dos cifras tras el
punto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

A, B y C, ocho enteros cada uno, y luego R.

## Salida

La longitud más corta.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0
10 10 10 10 5 5 5 5
3
```

Salida:

```
1.00
```

## Solución

Si el segmento AB no entra en la bola, la respuesta es |AB|. El punto de
la recta más cercano a C está en t = (C − A)·(B − A) / |AB|². Cuando t
está estrictamente entre 0 y 1, el segmento entra en la bola justo
cuando

```text
|AC|² · |AB|² − ((C − A)·(B − A))² < R² · |AB|²
```

Para t fuera de (0, 1), el punto más cercano es un extremo, y los extremos
están fuera. Todo esto es exacto en enteros de 64 bits.

Cuando el segmento sí entra, el camino más corto está en el plano por A,
B y C, donde la bola corta un disco. Va por una tangente desde A, rodea
la circunferencia y sigue por una tangente hasta B. Con d = |CA| y
e = |CB| las tangentes miden √(d² − R²) y √(e² − R²). El arco abarca el
ángulo ACB menos arccos(R/d) y arccos(R/e), los ángulos que forman, vistos
desde C, cada punto y su punto de tangencia. `O(1)`.

Detalles a tener en cuenta:

- un segmento que solo toca la bola está permitido y sigue recto
  (prueba 03);
- A y B pueden coincidir (prueba 04);
- C puede estar sobre el propio segmento, y entonces el plano es
  cualquiera que contenga la recta; la fórmula no depende de él
  (prueba 02);
- el enunciado exige redondear hacia arriba los empates a media centésima;
  las pruebas locales comparan con una tolerancia de 0,01.

Las respuestas se compararon en 150 casos aleatorios con el camino más
corto alrededor de un polígono de 20 000 lados trazado justo fuera de la
circunferencia en ese plano.

## Notas por lenguaje

- Todos los lenguajes hacen la misma prueba con enteros y la misma
  fórmula en doble precisión.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1285_geometry.cpp](1285_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 152 KB |
| [1285_geometry.go](1285_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1136 KB |
| [1285_geometry.java](1285_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1532 KB |
| [1285_geometry.py](1285_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 636 KB |
| [1285_geometry.rs](1285_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 260 KB |
