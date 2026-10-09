# 1068. La suma de todos los enteros entre 1 y N

[Timus 1068](https://acm.timus.ru/problem.aspx?space=1&num=1068) · dificultad 37 · math

Problema original de la ronda de prueba del concurso regional ACM ICPC del noreste de Europa 2000–2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da un entero `N` con `|N| ≤ 10000`. Imprime la suma de todos los
enteros entre 1 y `N`, ambos incluidos.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

La suma.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
-3
```

Salida:

```
-5
```

## Solución

Los números entre 1 y `N` forman un intervalo de `|N − 1| + 1` números,
esté `N` al lado que esté de 1. La suma de un intervalo es su longitud por
la media de sus extremos, `(1 + N) / 2`. El producto
`(1 + N) · (|N − 1| + 1)` siempre es par: si `N ≤ 0` sus dos factores suman
un número impar, y si no son `N + 1` y `N`, así que la división es exacta.
`O(1)`.

Detalles a tener en cuenta:

- `N` puede ser cero o negativo: entonces el intervalo va de `N` hasta 1, y
  `N(N + 1)/2` da una respuesta errónea, por ejemplo 0 en lugar de 1 para
  `N = 0`;
- la suma llega a unos `5 · 10^7` en valor absoluto, que cabe en enteros de
  32 bits; aun así las soluciones multiplican en 64 bits (Python, en sus
  enteros sin límite).

Las respuestas se comprobaron sumando los números uno a uno.

## Notas por lenguaje

- Python usa la división entera hacia abajo `//`, exacta aquí porque el
  producto es par; los demás lenguajes truncan, lo que es exacto por la
  misma razón.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1068_math.cpp](1068_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1068_math.go](1068_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1072 KB |
| [1068_math.java](1068_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1568 KB |
| [1068_math.py](1068_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 448 KB |
| [1068_math.rs](1068_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB |
