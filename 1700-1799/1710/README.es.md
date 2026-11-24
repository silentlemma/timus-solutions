# 1710. ¡Borís, te equivocas!

[Timus 1710](https://acm.timus.ru/problem.aspx?space=1&num=1710) · dificultad 649 · geometry

Problema original de Alexander Ipatov (preparado por Vladimir Yakovlev), del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Borís afirma que dos triángulos son congruentes si coinciden AB, BC y
el ángulo en A, es decir, dos lados y el ángulo opuesto a uno de ellos.
Dado un triángulo ABC, imprimir YES si todo triángulo que coincide con
él de esa forma le es congruente. Si no, imprimir NO y un triángulo
A₂B₂C₂ así que no le sea congruente.

## Entrada

Los puntos A, B y C, uno por línea: coordenadas enteras de valor
absoluto hasta 100, no alineados.

## Salida

YES, o NO y los tres puntos de un contraejemplo con la mayor precisión.
Sus coordenadas deben quedar dentro de 1000 y no puede ser degenerado.
Se acepta cualquier contraejemplo.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 0
-1 4
4 0
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
0 0
4 3
6 0
```

Salida:

```
NO
0.0000000000 0.0000000000
-3.0000000000 4.0000000000
0.0000000000 2.0000000000
```

## Solución

Se mantienen A, B y la dirección del rayo de A hacia C. Todo triángulo
que coincide puede moverse a esa posición, con C₂ sobre el rayo a
distancia |BC| de B. Un punto a distancia t sobre el rayo sirve cuando
t² − 2t·(AB·u) + |AB|² − |BC|² = 0, con u el vector unitario a lo
largo de AC. Una raíz es |AC|. La otra es t′ = 2(AB·AC)/|AC| − |AC|,
pues las raíces suman 2(AB·u).

Existe un triángulo distinto justo cuando t′ > 0 y t′ ≠ |AC|. En
enteros: 2(AB·AC) > |AC|² y AB·AC ≠ |AC|². Entonces
C₂ = A + (C − A)·(2(AB·AC) − |AC|²)/|AC|². Queda sobre el rayo a menos
de 2|AB| de A, muy dentro de 1000, y el triángulo ABC₂ tiene los mismos
AB, BC y ángulo A pero otro lado AC. `O(1)`.

Trampas:

- cuando AB·AC = |AC|² la circunferencia alrededor de B toca el rayo,
  así que la otra raíz es el propio C y la respuesta es YES (test 07).
  Una prueba en coma flotante imprime fácilmente C otra vez como punto
  «distinto»;
- un ángulo obtuso o recto en A da t′ ≤ 0: YES (ejemplo 1, test 04);
- Java debe imprimir con una configuración regional fija, porque
  algunas imprimen una coma decimal.

Un comprobador acepta cualquier contraejemplo. Revisa los dos lados y
el ángulo en A, un tercer lado distinto, un área no nula y la cota de
1000. Los veredictos coinciden con una implementación aceptada
independiente en 900 triángulos aleatorios, salvo en los de tangencia,
donde aquella imprime C otra vez.

## Soluciones optimizadas

Las versiones optimizadas leen coordenadas enteras e imprimen A y B directamente como enteros. Solo el punto reflejado requiere decimales.

Python 3.12 x64, envío 11319471. Tiempo 0,078 → 0,109 s, memoria 456 → 436 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322295 · Go 1.14 x64 №11321873 · Java 1.8 №11321949 · Rust 1.75 x64 №11321952 · Python 3.12 x64 №11322296.

Java 1.8, envío 11321999. Tiempo 0,125 → 0,093 s, memoria 1780 → 480 KB.

G++ 13.2 x64, envío 11322000. Tiempo 0,031 → 0,015 s, memoria 124 → 124 KB.

Rust obtiene las coordenadas con numeradores y denominadores enteros y formatea el resultado en un búfer fijo. Rust 1.75 x64, envío 11323313. Tiempo 0,046 → 0,046 s, memoria 260 → 60 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1710_geometry.cpp](1710_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 124 KB | 11322295 |
| [1710_geometry.go](1710_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1084 KB | 11321873 |
| [1710_geometry.java](1710_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1780 KB | 11321949 |
| [1710_geometry.py](1710_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 456 KB | 11322296 |
| [1710_geometry.rs](1710_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 260 KB | 11321952 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1710_geometry_optimized.py](1710_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 436 KB | 11319471 |
| [1710_geometry_optimized.java](1710_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 480 KB | 11321999 |
| [1710_geometry_optimized.cpp](1710_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 124 KB | 11322000 |
| [1710_geometry_optimized.rs](1710_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 60 KB | 11323313 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
