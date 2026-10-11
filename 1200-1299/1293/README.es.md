# 1293. Eniya

[Timus 1293](https://acm.timus.ru/problem.aspx?space=1&num=1293) · dificultad 14 · math

Problema original de Den Raskovalov, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que tratar por ambas caras N paneles rectangulares de A por B
metros, y cada metro cuadrado necesita un nanogramo de producto
(1 ≤ N, A, B ≤ 100). ¿Cuántos nanogramos hacen falta?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, A y B en una línea.

## Salida

El número de nanogramos.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 2 3
```

Salida:

```
60
```

## Solución

Cada panel tiene dos caras de A · B metros cuadrados, así que la
respuesta es 2 · N · A · B. `O(1)`.

Detalles a tener en cuenta:

- cuentan las dos caras: sin el factor 2 el ejemplo da 30 en vez de 60
  (prueba 01);
- la mayor respuesta es 2 000 000, que cabe de sobra en 32 bits
  (prueba 03).

## Notas por lenguaje

- Todos los lenguajes imprimen el mismo producto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1293_math.cpp](1293_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.001 s | 128 KB |
| [1293_math.go](1293_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1152 KB |
| [1293_math.java](1293_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1596 KB |
| [1293_math.py](1293_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 344 KB |
| [1293_math.rs](1293_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 224 KB |
