# 1335. La Tesis Blanca

[Timus 1335](https://acm.timus.ru/problem.aspx?space=1&num=1335) · dificultad 182 · math

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado N, 2 ≤ N ≤ 30 000, hay que hallar tres números enteros distintos A,
B y C entre N² y (N + 1)², ambos incluidos, tales que A² + B² sea
divisible por C, o imprimir `No solution` si no los hay. Se acepta
cualquier terna así.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

A, B y C, o `No solution`.

## Comprobación

El comprobador acepta tres números distintos cualesquiera del rango con
A² + B² divisible por C. Siempre existe una terna, así que `No solution`
nunca se acepta.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
8 6 4
```

### Ejemplo 2

Entrada:

```
1000
```

Salida:

```
1000000 1000756 1000976
```

## Solución

Se toma C = N² + 1, A = N² y B = N² + N + 1. Módulo C el primer número
es −1 y el segundo es N, así que A² + B² ≡ 1 + N², que es el propio C,
y la suma es divisible por C. Los tres están entre N² y (N + 1)², ya que
N² + N + 1 < N² + 2N + 1, y son distintos para todo N ≥ 1. Por tanto la
respuesta existe siempre y `No solution` nunca ocurre. `O(1)`.

La terna se encontró listando todas las soluciones con A = N² para N
pequeños y viendo que (N² + N + 1, N² + 1) aparecía siempre.

Detalles a tener en cuenta:

- los números llegan a unos 9 · 10⁸, y sus cuadrados, que solo necesita
  el comprobador, a 8 · 10¹⁷, más de lo que caben en 32 bits;
- los ejemplos muestran otras ternas; se acepta cualquiera correcta.

## Notas por lenguaje

- Las cinco soluciones imprimen la misma terna.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1335_math.cpp](1335_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1335_math.go](1335_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1064 KB |
| [1335_math.java](1335_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1612 KB |
| [1335_math.py](1335_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 392 KB |
| [1335_math.rs](1335_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 244 KB |
