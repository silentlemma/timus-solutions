# 2149. Girar palomas ASCII hasta un patrón ordenado

[Timus 2149](https://acm.timus.ru/problem.aspx?space=1&num=2149) · dificultad 148 · implementation

Problema original de Kirill Borozdin, del Concurso de Programación por Equipos de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n palomas están en fila, con n par, cada una mirando a la izquierda o a
la derecha, dibujadas en ASCII. La fila está ordenada cuando la mitad
izquierda mira hacia un lado y la derecha hacia el otro, o cuando las
palomas en posiciones pares miran hacia un lado y las de posiciones
impares hacia el otro. Hallar el menor número de palomas que hay que
girar. Los límites son 0.5 segundos y 256 MB.

## Entrada

n, 2 ≤ n ≤ 100, y luego tres líneas de 5n − 1 caracteres con las
palomas: `<@..`, `.OO=`, `./\.` para una paloma que mira a la izquierda
y `..@>`, `=OO.`, `./\.` para una que mira a la derecha, separadas por
columnas de puntos.

## Salida

El menor número de giros.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
..@>.<@...<@.....@>...@>...@>.<@...<@..
=OO...OO=..OO=.=OO..=OO..=OO...OO=..OO=
./\.../\.../\.../\.../\.../\.../\.../\.
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
4
..@>...@>.<@.....@>
=OO..=OO...OO=.=OO.
./\.../\.../\.../\.
```

Salida:

```
1
```

## Solución

Solo hace falta la primera línea: con índices desde cero, la paloma i
mira a la izquierda exactamente cuando el carácter de la posición 5i es
`<`. Se prueban cuatro patrones candidatos, en dos pares de opuestos. Se
cuentan las palomas que difieren de "la mitad izquierda mira a la
izquierda y la derecha a la derecha"; su patrón opuesto difiere justo en
las demás palomas, así que necesita n menos esa cuenta. Lo mismo vale
para "las posiciones pares miran a la izquierda y las impares a la
derecha". La respuesta es el menor de los cuatro números, hallado en
O(n).

En el segundo ejemplo solo la primera paloma rompe la alternancia, así
que basta un giro.

## Soluciones optimizadas

La solución optimizada en C++ lee con `scanf` en un único búfer fijo de
`char` de 500 bytes en lugar de `std::cin` en un `std::string`, así que
el programa prescinde de la biblioteca `iostream`; una línea tiene como
mucho 5 · 100 − 1 = 499 caracteres, porque `n ≤ 100`:
{2149_implementation_optimized.cpp}.

La solución optimizada en Java lee los bytes desde un búfer de 4 KB en
lugar de `Scanner` y cuenta las palomas directamente sobre los bytes de
la primera línea, cada cinco columnas, sin crear un `String` con ella;
las otras dos líneas se leen y se descartan:
{2149_implementation_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `2149_implementation_optimized.cpp`: reducción de tiempo +0.00%;
  reducción de memoria +73.47%; base: `2149_implementation.cpp`.

- `2149_implementation_optimized.java`: reducción de tiempo -12.00%;
  reducción de memoria +75.13%; base: `2149_implementation.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [2149_implementation.rs](2149_implementation.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2149_implementation.cpp](2149_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 392 KB | 11304075 |
| [2149_implementation.go](2149_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1100 KB | 11295005 |
| [2149_implementation.java](2149_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1576 KB | 11304076 |
| [2149_implementation.py](2149_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 412 KB | 11295006 |
| [2149_implementation.rs](2149_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 240 KB | 11295008 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2149_implementation_optimized.cpp](2149_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 104 KB | 11304538 |
| [2149_implementation_optimized.java](2149_implementation_optimized.java) \* | Java 1.8 | implementation | O(n) | AC | 0.140 s | 392 KB | 11304539 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
