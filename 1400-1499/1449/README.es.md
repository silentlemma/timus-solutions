# 1449. Operaciones de crédito 2

[Timus 1449](https://acm.timus.ru/problem.aspx?space=1&num=1449) · dificultad 1464 · matching

Problema original de Ilya Grebnov, Nikita Rybak y Dmitry Kovalioff, de Timus Top Coders: Second Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N empresas (2 ≤ N ≤ 100) tomaron créditos de N bancos; A[i, j] es el
crédito de la empresa i en el banco j (0 ≤ A[i, j] ≤ 10⁶). Hay que
elegir sobornos enteros no negativos BR[i] para las empresas y BC[j]
para los bancos de modo que cada crédito cumpla A[i, j] ≤ BR[i] + BC[j]
y el total de sobornos sea el menor posible. Se imprime cualquier
elección óptima.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego la matriz de créditos N × N.

## Salida

BR en la primera línea y BC en la segunda.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
5 8 4 3
3 6 2 1
4 6 4 1
4 3 5 4
```

Salida:

```
2 0 1 2
3 6 3 2
```

## Solución

Es el dual en programación lineal del problema de asignación. Para
cualquier permutación σ los sobornos cubren los créditos A[i, σ(i)], así
que el total es al menos el peso del emparejamiento perfecto más pesado;
el método húngaro produce potenciales que alcanzan justo ese peso. Se
ejecuta sobre los costes −A: al terminar, u[i] + v[j] ≤ −A[i, j] con
igualdad en el emparejamiento que encuentra, así que BR = −u y BC = −v
cubren todos los créditos y suman el peso del emparejamiento más
pesado, y los potenciales siguen siendo enteros.

Los potenciales pueden ser negativos, pero sumar t a todos los BR y
restarlo de todos los BC no cambia ni el total ni ninguna suma
BR[i] + BC[j]. Se desplaza hasta que el menor BR sea 0. Entonces ningún
BC es negativo: si BC[j] lo fuera, todos los BR[i] ≥ A[i, j] − BC[j]
serían positivos, incluido el que vale 0. `O(N³)`.

Detalles a tener en cuenta:

- una matriz de ceros también necesita respuesta, toda ceros (prueba
  02);
- si un solo banco dio todos los créditos, basta con que pague ese banco
  (prueba 07);
- los potenciales no son los sobornos: se cambia su signo antes de
  aplicar el desplazamiento.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1449_matching.cpp](1449_matching.cpp) | G++ 13.2 x64 | matching | O(N^3) | AC | 0.015 s | 284 KB |
| [1449_matching.go](1449_matching.go) | Go 1.14 x64 | matching | O(N^3) | AC | 0.031 s | 1368 KB |
| [1449_matching.java](1449_matching.java) | Java 1.8 | matching | O(N^3) | AC | 0.093 s | 780 KB |
| [1449_matching.py](1449_matching.py) | Python 3.12 x64 | matching | O(N^3) | AC | 0.171 s | 1520 KB |
| [1449_matching.rs](1449_matching.rs) | Rust 1.75 x64 | matching | O(N^3) | AC | 0.031 s | 424 KB |
