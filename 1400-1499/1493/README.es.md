# 1493. A un paso de la felicidad

[Timus 1493](https://acm.timus.ru/problem.aspx?space=1&num=1493) · dificultad 47 · implementation

Problema original de Vladimir Yakovlev, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un billete tiene un número de seis cifras, contando los ceros iniciales;
es afortunado si sus tres primeras cifras y sus tres últimas suman lo
mismo. Las dos sumas del billete dado difieren exactamente en uno. Hay
que escribir «Yes» si el billete anterior o el siguiente es afortunado,
y «No» en otro caso.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las seis cifras del billete.

## Salida

«Yes» o «No».

## Ejemplos

### Ejemplo 1

Entrada:

```
715068
```

Salida:

```
Yes
```

### Ejemplo 2

Entrada:

```
445219
```

Salida:

```
No
```

### Ejemplo 3

Entrada:

```
012200
```

Salida:

```
Yes
```

## Solución

Se comprueban directamente los dos vecinos: el número menos uno y más
uno, escritos con seis cifras, comparando las sumas de las mitades. Las
sumas del billete dado difieren, así que no es 000000 ni 999999, y los
dos vecinos son billetes reales. Los acarreos pueden cambiar varias
cifras a la vez, por eso los vecinos se recalculan enteros en lugar de
tocar una sola cifra. `O(1)`.

Detalles a tener en cuenta:

- el número puede empezar por ceros, y también son cifras (prueba 03);
  una lectura que toma un 0 inicial como prefijo octal falla;
- un acarreo o un préstamo a través del centro cambia las dos mitades,
  como de 100000 a 099999 (pruebas 06, 08, 09);
- los vecinos 000000 y 999999 también son billetes afortunados
  (pruebas 04, 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1493_implementation.cpp](1493_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 124 KB |
| [1493_implementation.go](1493_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB |
| [1493_implementation.java](1493_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.140 s | 1596 KB |
| [1493_implementation.py](1493_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.062 s | 376 KB |
| [1493_implementation.rs](1493_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.062 s | 224 KB |
