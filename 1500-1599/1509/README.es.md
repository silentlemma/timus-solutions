# 1509. Reconocimiento de dominó

[Timus 1509](https://acm.timus.ru/problem.aspx?space=1&num=1509) · dificultad 3218 · geometry

Problema original de Ekaterina Ovechkina y Stanislav Vasiliev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ficha de dominó es un rectángulo L × 2L (1 ≤ L ≤ 100) formado por
dos cuadrados, cada uno con 0 a 6 puntos en la disposición habitual.
Sea el cuadrado de lado mitad alrededor del centro de un cuadrado: un
punto va en el centro, dos en dos esquinas opuestas de ese cuadrado
pequeño, tres añaden el centro, cuatro ocupan todas sus esquinas, cinco
añaden el centro y seis añaden los puntos medios de sus dos lados
paralelos a los lados largos de la ficha. Una foto muestra los N puntos
(1 ≤ N ≤ 12) de una ficha boca abajo a tamaño real, girada y desplazada
de forma arbitraria, con coordenadas precisas hasta 0.0001. L no se da.
Hay que escribir todos los pares posibles A ≤ B de números de puntos,
en orden lexicográfico.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego las coordenadas de los N puntos.

## Salida

Los pares posibles «A B», uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1.12 2.2
7 -3.0001
```

Salida:

```
0 2
1 1
```

## Solución

Se prueba cada par A ≤ B con A + B = N. Se construyen sus puntos para
L = 1, con la ficha a lo largo del eje x, y se busca una semejanza que
los lleve sobre la foto. Se toma un punto g0 de la foto y el punto g1
más lejano a él. Viendo los puntos como números complejos, para cada
par ordenado (a, b) de puntos de la plantilla la aplicación
z ↦ g0 + (z − a)·(g1 − g0)/(b − a) lleva a a g0 y b a g1; el módulo de
su factor es L, que debe estar entre 1 y 100. El par encaja si cada
punto de la plantilla cae, con una pequeña tolerancia, sobre un punto
distinto de la foto. Se repite con la plantilla reflejada. Un solo
punto solo puede ser 0-1. Con 12 puntos como mucho la búsqueda es
mínima.

Las soluciones aceptan también la imagen especular de cada
disposición. La observación de que la ficha está boca abajo no aclara
hacia qué lado se refleja la imagen; el juez acepta esta lectura.

Detalles a tener en cuenta:

- dos puntos encajan tanto en un 0-2 como en un 1-1, con tamaños
  distintos (prueba 01);
- entonces deciden los límites de L: dos puntos a 0.8 no pueden ser
  1-1, y dos puntos a 80 no pueden ser 0-2 (pruebas 03, 04, gen4);
- un solo punto solo es 0-1 (prueba 02);
- la ficha puede estar girada cualquier ángulo y reflejada (pruebas 06,
  07, 09, 10);
- las coordenadas tienen un error de 1e-4, así que se compara con una
  tolerancia muy por debajo de los 0.25 entre puntos cuando L = 1
  (prueba 08, gen2).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1509_geometry.cpp](1509_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^5) | AC | 0.015 s | 224 KB |
| [1509_geometry.go](1509_geometry.go) | Go 1.14 x64 | geometry | O(N^5) | AC | 0.031 s | 1132 KB |
| [1509_geometry.java](1509_geometry.java) | Java 1.8 | geometry | O(N^5) | AC | 0.125 s | 676 KB |
| [1509_geometry.py](1509_geometry.py) | Python 3.12 x64 | geometry | O(N^5) | AC | 0.078 s | 740 KB |
| [1509_geometry.rs](1509_geometry.rs) | Rust 1.75 x64 | geometry | O(N^5) | AC | 0.015 s | 456 KB |
