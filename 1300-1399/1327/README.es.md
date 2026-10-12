# 1327. Fusibles

[Timus 1327](https://acm.timus.ru/problem.aspx?space=1&num=1327) · dificultad 47 · math

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un ordenador pierde un fusible cada día laborable impar: el día 1,
luego el día 3, el día 5 y así sucesivamente. Hay que contar los
fusibles perdidos del día A al día B, ambos incluidos,
1 ≤ A ≤ B ≤ 10 000.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

A en la primera línea y B en la segunda.

## Salida

El número de fusibles.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
5
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
100
200
```

Salida:

```
50
```

## Solución

Los días 1 a x contienen ⌊(x + 1) / 2⌋ días impares. Los días impares
de A a B son los que hay hasta B menos los que hay hasta A − 1, lo que
da ⌊(B + 1) / 2⌋ − ⌊A / 2⌋. `O(1)`.

Detalles a tener en cuenta:

- un intervalo de un solo día da 1 si el día es impar y 0 si es par
  (pruebas 03 y 04);
- los dos extremos cuentan cuando son impares (pruebas 01 y 07).

## Notas por lenguaje

- Las cinco soluciones usan la misma fórmula.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1327_math.cpp](1327_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1327_math.go](1327_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB |
| [1327_math.java](1327_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1624 KB |
| [1327_math.py](1327_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 404 KB |
| [1327_math.rs](1327_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 236 KB |
