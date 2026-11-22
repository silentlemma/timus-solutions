# 1332. Bombardeo con genios

[Timus 1332](https://acm.timus.ru/problem.aspx?space=1&num=1332) · dificultad 612 · geometry

Problema original de Alexander Bikbaev, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 100 ciudades son discos del mismo radio r con centros enteros
distintos, |x|, |y| ≤ 10 000. Una bomba destruye todo a distancia R del
punto donde cae, y una ciudad solo se destruye si queda entera dentro
de ese disco. Hay que hallar cuántas ciudades puede destruir como mucho
una bomba; 1 ≤ R, r ≤ 10 000.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas con los centros, luego R y r.

## Salida

El mayor número de ciudades destruidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 0
0 4
4 0
3 1
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
5
0 0
0 1
0 2
0 3
0 4
1 1
```

Salida:

```
1
```

## Solución

Una ciudad queda entera dentro de la explosión exactamente cuando su
centro está a D = R − r o menos de la bomba. Si D < 0 no se puede
destruir ninguna ciudad, y si no, la tarea es cubrir tantos centros
como se pueda con un disco de radio D.

Se toma un disco óptimo y se empuja mientras conserve todos sus
centros. Se puede mover hasta que un centro quede en su borde, y luego
girar alrededor de ese centro hasta que un segundo llegue también al
borde, salvo que contenga un solo centro. Así que basta probar los
discos centrados en el centro de una ciudad y los discos de radio D que
pasan por dos centros a distancia 2D como mucho. Hay hasta dos para cada par,
con el centro a distancia √(D² − (d/2)²) a cada lado del punto medio del
par. Se comprueban como máximo N + N(N − 1) lugares contra todos los
centros, con una pequeña tolerancia para los centros justo en el
borde. `O(N³)`.

Detalles a tener en cuenta:

- la ciudad tiene que caber entera, así que el alcance es R − r, y con
  R < r la respuesta es 0 (prueba 03);
- con R = r el alcance es 0 y se destruye una ciudad cada vez
  (pruebas 02 y 04);
- los centros justo en el borde cuentan; con puntos enteros como (3, 4)
  en una circunferencia de radio 5 el código usa una tolerancia
  (pruebas 06 y gen3).

Las respuestas se compararon con un barrido angular alrededor de cada
centro en 400 casos pequeños aleatorios.

## Notas por lenguaje

- Las cinco soluciones sencillas sencillas sencillas sencillas sencillas prueban los mismos lugares y comparan distancias
  al cuadrado.

## Soluciones optimizadas

Fijamos una ciudad en el borde del disco. Cada otra ciudad a una distancia de hasta 2D determina un intervalo cerrado de ángulos en los que el disco la cubre. Al ordenar los extremos se obtiene el máximo solapamiento. Los intervalos que cruzan el ángulo cero se cuentan al inicio y, para ángulos iguales, los inicios se procesan primero.

Python usa este barrido. El envío 11318349 tardó 0,093 s y usó 676 KB.

Go usa este barrido. El envío 11328272 tardó 0,031 s y usó 1004 KB.

Java usa este barrido. El envío 11318354 tardó 0,125 s y usó 456 KB.

Rust usa este barrido. El envío 11318359 tardó 0,046 s y usó 220 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321855 · Go 1.14 x64 №11322297 · Java 1.8 №11322298 · Python 3.12 x64 №11322299 · Rust 1.75 x64 №11322300.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1332_geometry.cpp](1332_geometry.cpp) | G++ 13.2 x64 | geometry | O(N³) | AC | 0.015 s | 340 KB | 11321855 |
| [1332_geometry.go](1332_geometry.go) | Go 1.14 x64 | geometry | O(N³) | AC | 0.031 s | 1328 KB | 11322297 |
| [1332_geometry.java](1332_geometry.java) | Java 1.8 | geometry | O(N³) | AC | 0.156 s | 1972 KB | 11322298 |
| [1332_geometry.py](1332_geometry.py) | Python 3.12 x64 | geometry | O(N³) | AC | 0.234 s | 1044 KB | 11322299 |
| [1332_geometry.rs](1332_geometry.rs) | Rust 1.75 x64 | geometry | O(N³) | AC | 0.046 s | 384 KB | 11322300 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1332_geometry_sorting.py](1332_geometry_sorting.py) | Python 3.12 x64 | geometry, sorting | O(N² log N) | AC | 0.093 s | 676 KB | 11318349 |
| [1332_geometry_sorting.go](1332_geometry_sorting.go) \* | Go 1.14 x64 | geometry, sorting | O(N² log N) | AC | 0.031 s | 1004 KB | 11328272 |
| [1332_geometry_sorting.java](1332_geometry_sorting.java) \* | Java 1.8 | geometry, sorting | O(N² log N) | AC | 0.125 s | 456 KB | 11318354 |
| [1332_geometry_sorting.rs](1332_geometry_sorting.rs) \* | Rust 1.75 x64 | geometry, sorting | O(N² log N) | AC | 0.046 s | 220 KB | 11318359 |

\* El objetivo de clasificación de Go sigue pendiente. El objetivo de clasificación de Java sigue pendiente. El objetivo de clasificación de Rust sigue pendiente.
