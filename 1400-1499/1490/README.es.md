# 1490. Círculo de fuego

[Timus 1490](https://acm.timus.ru/problem.aspx?space=1&num=1490) · dificultad 196 · math

Problema original de Alexander Ipatov, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El suelo está cubierto de baldosas de 1 × 1. Un círculo de fuego de
radio entero R (R ≤ 10⁵) tiene el centro en un punto donde se juntan
cuatro baldosas. Una baldosa se estropea si tiene al menos dos puntos en
común con el círculo. Hay que contar las baldosas estropeadas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

R.

## Salida

El número de baldosas estropeadas.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
16
```

### Ejemplo 2

Entrada:

```
4
```

Salida:

```
60
```

## Solución

Los ejemplos muestran que cuenta todo el disco, no solo su borde. Una
baldosa comparte más de un punto con el disco justo cuando su esquina
más cercana al centro está estrictamente dentro; una baldosa cuya
esquina más cercana está en la circunferencia solo la toca en ese punto.

Por simetría se cuenta un cuarto y se multiplica por 4. Ahí la baldosa
con esquina inferior izquierda (i, j) cuenta cuando i² + j² < R², así
que la columna i tiene ⌊√(R² − i² − 1)⌋ + 1 baldosas, con i de 0 a
R − 1. Una raíz cuadrada entera lo mantiene exacto. La respuesta llega
a unos π·10¹⁰ y necesita 64 bits. `O(R)`.

Detalles a tener en cuenta:

- una baldosa que solo toca el disco en una esquina, como la que hay
  tras (3, 4) para R = 5, no cuenta (pruebas 04, 05, 06);
- la respuesta para R = 10⁵ es 31 416 325 412, más de 32 bits
  (prueba 07);
- una raíz en coma flotante debe corregirse hasta la raíz entera exacta
  (pruebas 06, 07).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1490_math.cpp](1490_math.cpp) | G++ 13.2 x64 | math | O(R) | AC | 0.015 s | 128 KB |
| [1490_math.go](1490_math.go) | Go 1.14 x64 | math | O(R) | AC | 0.031 s | 1088 KB |
| [1490_math.java](1490_math.java) | Java 1.8 | math | O(R) | AC | 0.109 s | 1612 KB |
| [1490_math.py](1490_math.py) | Python 3.12 x64 | math | O(R) | AC | 0.078 s | 472 KB |
| [1490_math.rs](1490_math.rs) | Rust 1.75 x64 | math | O(R) | AC | 0.031 s | 232 KB |
