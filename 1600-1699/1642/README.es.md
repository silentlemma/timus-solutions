# 1642. Laberinto unidimensional

[Timus 1642](https://acm.timus.ru/problem.aspx?space=1&num=1642) · dificultad 96 · implementation

Problema original de Daniil Ayzenshteyn, del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una persona está en el 0 de una recta con obstáculos y una salida en x.
Camina en la dirección elegida, sale en cuanto llega a la salida y da la
vuelta en cada obstáculo. Para las dos direcciones iniciales, hacia
delante (creciente) y hacia atrás, hay que hallar la distancia recorrida
antes de salir, o decir que la salida es inalcanzable.

## Entrada

n y x (0 ≤ n ≤ 100), y luego n coordenadas distintas de obstáculos.
Todas las coordenadas son no nulas, de valor absoluto hasta 1000, y no
hay obstáculo en la salida. En cualquier dirección el camino encuentra
la salida o un obstáculo.

## Salida

Dos distancias, primero hacia delante, o `Impossible`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 -2
-10 -4 2
```

Salida:

```
6 2
```

### Ejemplo 2

Entrada:

```
3 -2
10 -1 2
```

Salida:

```
Impossible
```

## Solución

Solo importan los obstáculos más cercanos: left, el mayor por debajo de
0 (o −∞ si no existe), y right, el menor por encima de 0 (o +∞ si no existe).
La salida es alcanzable exactamente cuando
left < x < right; si no, `Impossible`. En las dos direcciones el camino
es entonces directo o con un rodeo:

- x > 0: hacia delante x; hacia atrás hasta left y vuelta,
  2 · |left| + x;
- x < 0: hacia delante hasta right y vuelta, 2 · right + |x|; hacia
  atrás |x|.

El obstáculo necesario para el rodeo existe por la promesa del
enunciado. `O(n)`.

Detalles a tener en cuenta:

- un obstáculo entre el inicio y la salida bloquea las dos direcciones,
  así que una sola respuesta vale para ambas (el segundo ejemplo, la
  prueba 06);
- puede no haber ningún obstáculo del lado de la salida.

Las respuestas coinciden con una implementación aceptada independiente
en 300 rectas aleatorias.

## Soluciones optimizadas

La solución optimizada en Java analiza los números, con su signo, a
mano desde un búfer pequeño en lugar de usar `Scanner`: 436 KB en lugar
de 1688 KB, con el mismo tiempo. Lo demás es igual.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1642_implementation.cpp](1642_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.031 s | 124 KB | 11303497 |
| [1642_implementation.go](1642_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1076 KB | 11288477 |
| [1642_implementation.java](1642_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1688 KB | 11288479 |
| [1642_implementation.py](1642_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 504 KB | 11288478 |
| [1642_implementation.rs](1642_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 228 KB | 11303498 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1642_implementation_optimized.java](1642_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 436 KB | 11303629 |
