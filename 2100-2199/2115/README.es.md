# 2115. Ordenar una fila con a lo sumo un intercambio

[Timus 2115](https://acm.timus.ru/problem.aspx?space=1&num=2115) · dificultad 228 · sorting

Problema original de Ivan Smirnov, de la Olimpiada Académica Universitaria Escolar de Informática 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n alumnos forman una fila con alturas aᵢ. La fila está bien si está
ordenada de forma creciente o decreciente. Decir si ya lo está, si un
intercambio de dos alumnos puede conseguirlo (y cuál), o ninguna de las
dos cosas. Se acepta cualquier intercambio que la arregle. Los límites
son 1 segundo y 256 MB.

## Entrada

n ≤ 10⁵ y después las alturas, hasta 10⁹.

## Salida

`Nothing to do here`; o `Yes` y las dos posiciones; o `No hope`.

## Evaluación

Un comprobador compara el veredicto y, para `Yes`, intercambia los dos
alumnos impresos y comprueba el orden.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
150 160 170
```

Salida:

```
Nothing to do here
```

### Ejemplo 2

Entrada:

```
4
140 160 150 170
```

Salida:

```
Yes
2 3
```

## Solución

Se ordenan las alturas; el objetivo es esa fila ordenada o su inversa.
Un intercambio solo cambia dos lugares, así que solo puede convertir la
fila en un objetivo si difiere de él en exactamente dos lugares i y j, y
entonces funciona justo cuando aᵢ y aⱼ son el valor objetivo del otro.
Se prueban ambos objetivos, lo que cuesta O(n log n) por la ordenación.

En el segundo ejemplo 140 160 150 170 difiere del orden creciente en los
lugares 2 y 3, y cambiarlos ordena la fila (cambiar 1 y 4 da en cambio
el orden decreciente).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2115_sorting.cpp](2115_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.109 s | 2556 KB |
| [2115_sorting.go](2115_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.140 s | 5696 KB |
| [2115_sorting.java](2115_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.156 s | 3676 KB |
| [2115_sorting.py](2115_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.140 s | 15740 KB |
| [2115_sorting.rs](2115_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.046 s | 3524 KB |
