# 1024. El orden de una permutación

[Timus 1024](https://acm.timus.ru/problem.aspx?space=1&num=1024) · dificultad 321 · math

Problema original de Nikita Shamgunov, de la Segunda Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 7 de octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una permutación `P` de `1..N` (`1 ≤ N ≤ 1000`) viene dada por
`P(1), ..., P(N)`. Sus potencias son `P^1 = P` y `P^k(n) = P(P^(k-1)(n))`.
Encuentra el menor `k ≥ 1` para el que `P^k` es la identidad. La respuesta
no supera `10^9`.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego los `N` números `P(1), ..., P(N)`.

## Salida

El menor tal `k`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
2 3 1 5 4
```

Salida:

```
6
```

### Ejemplo 2

Entrada:

```
1
1
```

Salida:

```
1
```

## Solución

Toda permutación se descompone en **ciclos** disjuntos: se empieza en un
elemento y se aplica `P` hasta volver. En un ciclo de longitud `c` la
permutación es una rotación, así que `P^k` es la identidad en él exactamente
cuando `c` divide a `k`. `P^k` es la identidad en todas partes cuando esto
vale para cada ciclo, y el menor tal `k` es el **mínimo común múltiplo** de
las longitudes de los ciclos.

Se recorren los ciclos con un arreglo `seen` (cada elemento se visita una
vez, `O(N)`) y se acumulan las longitudes con
`lcm(a, b) = a / gcd(a, b) · b`; dividir primero mantiene pequeño el valor
intermedio.

Detalles a tener en cuenta:

- el producto de las longitudes no es la respuesta: longitudes 4 y 6 dan
  12, no 24;
- calcular las potencias de `P` una a una puede llevar hasta `10^9` pasos;
- el mcm cabe en `10^9` según el enunciado, pero `a · b` antes de dividir
  puede no caber en 32 bits: usa enteros de 64 bits.

## Notas por lenguaje

El mismo recorrido de ciclos en todos los lenguajes; C++ (`std::lcm`) y
Python (`math.lcm`) tienen el mcm en la biblioteca estándar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1024_math.cpp](1024_math.cpp) | G++ 13.2 x64 | math | O(N log N) | AC | 0.015 s | 200 KB |
| [1024_math.go](1024_math.go) | Go 1.14 x64 | math | O(N log N) | AC | 0.015 s | 1100 KB |
| [1024_math.java](1024_math.java) | Java 1.8 | math | O(N log N) | AC | 0.140 s | 2400 KB |
| [1024_math.py](1024_math.py) | Python 3.12 x64 | math | O(N log N) | AC | 0.078 s | 524 KB |
| [1024_math.rs](1024_math.rs) | Rust 1.75 x64 | math | O(N log N) | AC | 0.046 s | 224 KB |
