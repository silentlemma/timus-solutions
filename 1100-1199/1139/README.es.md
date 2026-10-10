# 1139. Contar las manzanas que sobrevuela un vuelo en diagonal sobre una cuadrícula de calles

[Timus 1139](https://acm.timus.ru/problem.aspx?space=1&num=1139) · dificultad 78 · number_theory

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` avenidas y `M` calles, `1 < N, M < 32000`, dividen una ciudad en
manzanas cuadradas. Un helicóptero vuela en línea recta de la esquina
suroeste a la noreste. Cuenta las manzanas que sobrevuela; una manzana es
el interior abierto de su cuadrado, así que tocar una esquina no cuenta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `M`.

## Salida

El número de manzanas.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
3 3
```

Salida:

```
2
```

## Solución

Las manzanas forman una cuadrícula de `a × b`, con `a = N − 1` y
`b = M − 1`, y el vuelo es su diagonal. Empieza dentro de la primera
manzana, y cada vez que cruza una línea de la cuadrícula entra en una
manzana nueva. Cruza las `a − 1` líneas verticales interiores y las
`b − 1` horizontales interiores, pero en una esquina interior cruza una de
cada tipo a la vez y entra en una sola manzana nueva. La diagonal pasa
por los puntos `(k·a/g, k·b/g)`, así que encuentra exactamente `g − 1`
esquinas interiores, con `g = gcd(a, b)`. En total
`1 + (a − 1) + (b − 1) − (g − 1) = a + b − gcd(a, b)`. `O(log min(a, b))`.

Detalles a tener en cuenta:

- la entrada cuenta líneas, no manzanas: hay que restar uno a cada una;
- en una cuadrícula cuadrada la diagonal pasa por todas las esquinas de
  su camino y cruza solo `a` manzanas;
- con una sola fila o columna, el vuelo cruza todas sus manzanas.

Las respuestas se compararon con un recuento columna a columna de las
manzanas bajo la diagonal, con redondeos exactos hacia abajo y hacia
arriba, para todos los `N, M ≤ 40` y en todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes aplican la misma fórmula.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1139_number_theory.cpp](1139_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 128 KB |
| [1139_number_theory.go](1139_number_theory.go) | Go 1.14 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 1060 KB |
| [1139_number_theory.java](1139_number_theory.java) | Java 1.8 | number_theory | O(log min(N, M)) | AC | 0.109 s | 1592 KB |
| [1139_number_theory.py](1139_number_theory.py) | Python 3.12 x64 | number_theory | O(log min(N, M)) | AC | 0.078 s | 400 KB |
| [1139_number_theory.rs](1139_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 248 KB |
