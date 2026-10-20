# 2206. Puntos de red con coordenadas coprimas dentro de un polígono convexo

[Timus 2206](https://acm.timus.ru/problem.aspx?space=1&num=2206) · dificultad 1875 · geometry, number_theory

Problema original de Vadim Barinov, de la Olimpiada Académica Universitaria Escolar de Informática 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da un polígono convexo de N vértices con coordenadas de exactamente
tres decimales. Contar los puntos (x, y) de coordenadas enteras
positivas coprimas dentro de él o en su borde. Los límites son 4.5
segundos y 512 MB.

## Entrada

N, 3 ≤ N ≤ 2 · 10⁵, y luego los vértices en sentido antihorario, cada
coordenada entre 1 y 2 · 10⁶.

## Salida

El número de puntos coprimos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1.000 1.000
3.000 1.000
1.000 3.000
```

Salida:

```
5
```

## Solución

Se multiplican todas las coordenadas por 1000 para que sean enteras.
Para cada columna entera x el polígono cubre un segmento de y entre sus
cadenas inferior y superior. Recorriendo cada arista por las columnas
enteras que abarca, la división entera exacta da upper(x) = ⌊arriba⌋ y
lower(x) = ⌈abajo⌉ − 1, así que la columna contiene upper(x) − lower(x)
puntos enteros; una arista vertical no añade nada nuevo.

Entre ellos, los puntos con gcd(x, y) = 1 se cuentan por inversión de
Möbius sobre el divisor común d:

Σ sobre d de μ(d) · Σ sobre las columnas x divisibles por d de
(⌊upper(x) / d⌋ − ⌊lower(x) / d⌋).

Para cada d la suma interior visita W / d columnas, donde W es el ancho
del polígono, así que el total es O(W log W) con W ≤ 2 · 10⁶. Un divisor
mayor que la mitad de la columna más a la derecha solo puede ser la
propia columna, que se trata con un único término. μ sale de una criba.

En el ejemplo el triángulo contiene (1, 1), (1, 2), (1, 3), (2, 1),
(2, 2) y (3, 1), y solo (2, 2) no es coprimo, así que la respuesta es 5.

Esto cuesta O(N + W log W).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2206_geometry_number_theory.cpp](2206_geometry_number_theory.cpp) | G++ 13.2 x64 | geometry, number_theory | O(N + W log W) | AC | 0.359 s | 26576 KB |
| [2206_geometry_number_theory.go](2206_geometry_number_theory.go) | Go 1.14 x64 | geometry, number_theory | O(N + W log W) | AC | 1.421 s | 67156 KB |
| [2206_geometry_number_theory.java](2206_geometry_number_theory.java) | Java 1.8 | geometry, number_theory | O(N + W log W) | AC | 0.781 s | 28460 KB |
| [2206_geometry_number_theory.py](2206_geometry_number_theory.py) | PyPy 3.10 x64 | geometry, number_theory | O(N + W log W) | AC | 1.968 s | 122932 KB |
| [2206_geometry_number_theory.rs](2206_geometry_number_theory.rs) | Rust 1.75 x64 | geometry, number_theory | O(N + W log W) | AC | 0.875 s | 61056 KB |
