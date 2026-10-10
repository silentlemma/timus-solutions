# 1138. La serie más larga de trabajos con aumentos de un número entero de por ciento

[Timus 1138](https://acm.timus.ru/problem.aspx?space=1&num=1138) · dificultad 203 · dp

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El primer sueldo de un programador fue exactamente `s`, cada sueldo
siguiente es un entero positivo mayor que el anterior en un número entero
de por ciento, y el último es como mucho `n`, con `1 ≤ n, s ≤ 10000`. Halla
el mayor número posible de trabajos, contando el primero.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` y `s`.

## Salida

El mayor número de trabajos.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 2
```

Salida:

```
5
```

## Solución

Un aumento del sueldo `a` a `b > a` es de `100·(b − a) / a` por ciento, un
número entero justo cuando `a` divide a `100·(b − a)`. Con
`g = gcd(a, 100)`, eso significa que `a / g` divide a `b − a`, así que los
sueldos alcanzables desde `a` son `a + a/g, a + 2a/g, …`. Sea `jobs[a]` la
serie más larga desde `s` que termina en `a`, con `jobs[s] = 1`. Los
sueldos solo crecen, así que subiendo desde `s` y empujando `jobs[a] + 1` a
cada `b ≤ n` alcanzable se llena la tabla en orden; la respuesta es su
mayor valor. El paso `a/g` es al menos `a/100`, así que los empujes suman
como mucho unos `100·n·ln n`, y en la práctica muchos menos.

Detalles a tener en cuenta:

- el aumento debe ser positivo, así que `b > a`;
- `n = s` da un solo trabajo;
- si `s > n`, no cabe ninguna serie y la respuesta es `0`;
- trabajar con `a / gcd(a, 100)` evita probar cada porcentaje.

Las respuestas se compararon con una comprobación de todos los pares de
sueldos en todas las pruebas y en 300 entradas aleatorias de hasta 400.

## Notas por lenguaje

- Todos los lenguajes llenan la misma tabla empujando hacia delante.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1138_dp.cpp](1138_dp.cpp) | G++ 13.2 x64 | dp | O(n log n) | AC | 0.015 s | 224 KB |
| [1138_dp.go](1138_dp.go) | Go 1.14 x64 | dp | O(n log n) | AC | 0.031 s | 1144 KB |
| [1138_dp.java](1138_dp.java) | Java 1.8 | dp | O(n log n) | AC | 0.125 s | 1680 KB |
| [1138_dp.py](1138_dp.py) | Python 3.12 x64 | dp | O(n log n) | AC | 0.093 s | 508 KB |
| [1138_dp.rs](1138_dp.rs) | Rust 1.75 x64 | dp | O(n log n) | AC | 0.015 s | 256 KB |
