# 1402. Cócteles

[Timus 1402](https://acm.timus.ru/problem.aspx?space=1&num=1402) · dificultad 130 · combinatorics

Problema original de Sergey Pupyrev, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cóctel mezcla dos o más de N ≤ 21 bebidas, cada una a lo sumo una
vez, y el orden de las bebidas importa. Hay que contar los cócteles
distintos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

El número de cócteles.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
12
```

## Solución

Un cóctel de k bebidas es una elección ordenada de k bebidas distintas,
y hay N·(N − 1)·…·(N − k + 1) de ellas. Se suman para k de 2 a N,
obteniendo cada producto a partir del anterior. `O(N)`.

Detalles a tener en cuenta:

- con una sola bebida no hay ningún cóctel (prueba 02);
- para N = 21 la respuesta es de unos 1,4·10²⁰, más de 64 bits, así que
  las soluciones usan enteros de 128 bits o enteros grandes (prueba 07).

Las pruebas se juzgan por comparación exacta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1402_combinatorics.cpp](1402_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N) | AC | 0.015 s | 188 KB |
| [1402_combinatorics.go](1402_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N) | AC | 0.031 s | 1176 KB |
| [1402_combinatorics.java](1402_combinatorics.java) | Java 1.8 | combinatorics | O(N) | AC | 0.109 s | 1688 KB |
| [1402_combinatorics.py](1402_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N) | AC | 0.078 s | 388 KB |
| [1402_combinatorics.rs](1402_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N) | AC | 0.031 s | 232 KB |
