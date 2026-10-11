# 1264. Días de trabajo

[Timus 1264](https://acm.timus.ru/problem.aspx?space=1&num=1264) · dificultad 21 · math

Problema original de Den Raskovalov, de la Competición Abierta por Equipos de Programación para Escolares de la Región de Sverdlovsk, 11 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una función cuenta cuántas veces aparece cada valor de 0 a M en un
arreglo de N elementos, escrita con una línea `if` por cada elemento y
cada valor (0 ≤ N, M ≤ 40 000). Escribir una línea lleva un segundo.
¿Cuántos segundos lleva toda la función?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M.

## Salida

El número de segundos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 1
```

Salida:

```
6
```

## Solución

Hay N elementos y M + 1 valores, así que la respuesta es N · (M + 1).
`O(1)`.

Detalles a tener en cuenta:

- los valores van de 0 a M, así que son M + 1, no M;
- la respuesta llega a 40 000 · 40 001 = 1 600 040 000, cerca del
  límite de 32 bits con signo; las soluciones usan 64 bits (prueba 05);
- con N = 0 la respuesta es 0 sea cual sea M (pruebas 02, 03).

## Notas por lenguaje

- Todos los lenguajes imprimen el mismo producto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1264_math.cpp](1264_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1264_math.go](1264_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB |
| [1264_math.java](1264_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1552 KB |
| [1264_math.py](1264_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 320 KB |
| [1264_math.rs](1264_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 232 KB |
