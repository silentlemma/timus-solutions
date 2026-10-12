# 1336. El problema de Ben Betsalel

[Timus 1336](https://acm.timus.ru/problem.aspx?space=1&num=1336) · dificultad 123 · math

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que escribir un número entero n, 1 ≤ n ≤ 10⁹, como cociente de un
cuadrado entre un cubo: hallar enteros m y k de 1 a 10¹⁰⁰ con
m² = k³ · n. Se acepta cualquier par así.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número n.

## Salida

m en la primera línea y k en la segunda.

## Comprobación

El comprobador acepta cualesquiera m y k de 1 a 10¹⁰⁰ con m² = k³ · n.

## Ejemplos

### Ejemplo 1

Entrada:

```
18
```

Salida:

```
12
2
```

### Ejemplo 2

Entrada:

```
1
```

Salida:

```
1
1
```

## Solución

Se toma k = n y m = n². Entonces m² = n⁴ = n³ · n. Así que siempre
existe un par, y por eso el problema siempre tiene solución. `O(1)`.

Detalles a tener en cuenta:

- m llega a 10¹⁸, lo que necesita un entero de 64 bits (prueba 03);
- los ejemplos muestran pares más pequeños; se acepta cualquiera
  correcto.

## Notas por lenguaje

- Las cinco soluciones imprimen n² y n.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1336_math.cpp](1336_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1336_math.go](1336_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB |
| [1336_math.java](1336_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1564 KB |
| [1336_math.py](1336_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 352 KB |
| [1336_math.rs](1336_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB |
