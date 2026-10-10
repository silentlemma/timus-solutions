# 1119. El camino más corto por una cuadrícula con algunos atajos en diagonal

[Timus 1119](https://acm.timus.ru/problem.aspx?space=1&num=1119) · dificultad 70 · dp

Problema original de Leonid Volkov, del USU Open Collegiate Programming Contest, octubre de 2001, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cuadrícula tiene `N × M` manzanas cuadradas (`0 < N, M ≤ 1000`) de 100
metros de lado. Un camino va de la esquina suroeste de la manzana `(1, 1)`
a la esquina noreste de la manzana `(N, M)` por las calles, solo hacia el
norte o el este; `K ≤ 100` manzanas dadas pueden cruzarse además por su
diagonal de suroeste a noreste. Halla la longitud del camino más corto,
redondeada al metro.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N M`, luego `K` y luego `K` líneas `x y` con las manzanas que se pueden
cruzar.

## Salida

La menor longitud en metros, redondeada.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2
3
1 1
3 2
1 2
```

Salida:

```
383
```

## Solución

Un camino solo va al norte y al este, así que las diagonales que usa
forman una cadena de manzanas estrictamente creciente en ambas
coordenadas, y toda cadena así puede recorrerse. Cada diagonal cambia dos
lados (200 m) por `100√2` m, así que el mejor camino usa la cadena más
larga. Se ordenan las manzanas y se halla la cadena más larga con la
programación dinámica cuadrática de la subsecuencia creciente más larga;
con `L` diagonales la longitud es `100·(N + M − 2L) + 100√2·L`. `O(K²)`.

Detalles a tener en cuenta:

- dos manzanas en la misma fila o columna no pueden usarse ambas: la
  cadena debe crecer estrictamente en ambas coordenadas;
- las manzanas pueden repetirse en la entrada;
- la longitud nunca queda exactamente a medio camino entre enteros, porque
  `100√2·L` es irracional para `L > 0`, así que el redondeo normal es
  seguro.

Las respuestas se comprobaron con una programación dinámica sobre los
`(N + 1)(M + 1)` cruces de la cuadrícula, a los que se llega desde el
oeste, desde el sur o por una diagonal, en todas las pruebas y 60
cuadrículas aleatorias.

## Notas por lenguaje

- Todos los lenguajes hacen la misma programación dinámica cuadrática.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1119_dp.cpp](1119_dp.cpp) | G++ 13.2 x64 | dp | O(K²) | AC | 0.031 s | 212 KB |
| [1119_dp.go](1119_dp.go) | Go 1.14 x64 | dp | O(K²) | AC | 0.031 s | 1136 KB |
| [1119_dp.java](1119_dp.java) | Java 1.8 | dp | O(K²) | AC | 0.187 s | 3928 KB |
| [1119_dp.py](1119_dp.py) | Python 3.12 x64 | dp | O(K²) | AC | 0.078 s | 504 KB |
| [1119_dp.rs](1119_dp.rs) | Rust 1.75 x64 | dp | O(K²) | AC | 0.031 s | 232 KB |
