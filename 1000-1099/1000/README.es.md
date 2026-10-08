# 1000. Suma de dos enteros

[Timus 1000](https://acm.timus.ru/problem.aspx?space=1&num=1000) · dificultad 16 · math

Problema original de Pavel Atnashev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan dos enteros `a` y `b`. Imprime su suma `a + b`.

El problema original no indica cotas para `a` y `b`; las soluciones usan
enteros de 64 bits, así que se procesa cualquier par de valores cuya suma quepa
en un entero con signo de 64 bits.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Dos enteros `a` y `b`, separados por espacios en blanco (un espacio o un salto
de línea).

## Salida

Un entero: `a + b`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
```

Salida:

```
5
```

### Ejemplo 2

Entrada:

```
2000000000 2000000000
```

Salida:

```
4000000000
```

## Solución

Leer los dos números e imprimir su suma. Tiempo y memoria `O(1)`.

Detalles a tener en cuenta:

- la suma de dos valores que caben en 32 bits puede no caber en 32 bits, por eso
  se usa un tipo de 64 bits para los operandos y el resultado;
- los números se leen como tokens separados por espacios en blanco, así que da
  igual si están en una línea o en dos.

## Notas por lenguaje

- **C++**: `long long` y `scanf("%lld %lld")`.
- **Go**: `int64` con `fmt.Scan`, que omite cualquier espacio en blanco.
- **Python**: los enteros tienen precisión arbitraria; leer todos los tokens con
  `sys.stdin.read().split()` funciona con cualquier distribución en líneas.
- **Java**: `long` y `Scanner`; para una entrada tan pequeña `Scanner` es
  suficientemente rápido.
- **Rust**: leer toda la entrada en un `String`, dividirla por espacios en blanco
  y convertir a `i64`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1000_math.cpp](1000_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.001 s | 128 KB |
| [1000_math.go](1000_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1060 KB |
| [1000_math.java](1000_math.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 1548 KB |
| [1000_math.py](1000_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 132 KB |
| [1000_math.rs](1000_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.001 s | 228 KB |
