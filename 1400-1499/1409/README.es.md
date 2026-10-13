# 1409. Dos bandidos

[Timus 1409](https://acm.timus.ru/problem.aspx?space=1&num=1409) · dificultad 15 · math

Problema original de Den Raskovalov, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay como mucho 10 latas en fila. Harry dispara a ellas una a una desde
la izquierda, Larry desde la derecha, y ambos aciertan a la vez la
última lata. Dado cuántas latas derribó cada uno, hay que hallar
cuántas latas no derribó Harry y cuántas no derribó Larry.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Los números de latas derribadas por Harry y por Larry.

## Salida

Los números de latas no derribadas por Harry y por Larry.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 7
```

Salida:

```
6 3
```

## Solución

La lata compartida cuenta en los dos números, así que había H + L − 1
latas. Harry no derribó las otras L − 1 latas de Larry y Larry no
derribó H − 1, de modo que la respuesta es L − 1 y H − 1. `O(1)`.

Detalles a tener en cuenta:

- la respuesta para Harry sale del número de Larry y al revés, así que
  es fácil invertir el orden (prueba 03);
- una sola lata da 0 0 (prueba 02).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1409_math.cpp](1409_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 400 KB |
| [1409_math.go](1409_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1080 KB |
| [1409_math.java](1409_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1560 KB |
| [1409_math.py](1409_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.046 s | 360 KB |
| [1409_math.rs](1409_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 212 KB |
