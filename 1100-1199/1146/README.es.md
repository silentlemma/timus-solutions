# 1146. El subrectángulo de mayor suma en un array cuadrado

[Timus 1146](https://acm.timus.ru/problem.aspx?space=1&num=1146) · dificultad 79 · dp

Problema original de Timus; no se indican autor ni fuente.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado un array de `N × N`, `N ≤ 100`, de enteros de −127 a 127, halla la
mayor suma de un subrectángulo, es decir, de un bloque de al menos `1 × 1`
de filas y columnas vecinas.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego los `N²` números fila a fila, separados por cualquier espacio
en blanco.

## Salida

La mayor suma.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 -2 -7 0
9 2 -6 2
-4 1 -4 1
-1 8 0 -2
```

Salida:

```
15
```

## Solución

Se fija la fila superior del rectángulo y se baja la inferior de una en
una, guardando para cada columna la suma de sus celdas entre las dos
filas. Para un par de filas fijo, el mejor rectángulo es el mejor tramo
de columnas vecinas en esa lista de sumas, que el recorrido de Kadane
encuentra en una pasada: se guarda la mejor suma de un tramo que acaba en
la columna actual, empezando de nuevo en ella cuando la suma anterior es
negativa. Las sumas de columna para la siguiente fila inferior son las
anteriores más una fila, así que cada par de filas cuesta `O(N)` y toda la
búsqueda `O(N³)`, alrededor de medio millón de pasos para `N = 100`.

Detalles a tener en cuenta:

- el rectángulo no puede estar vacío: si todos los números son negativos
  la respuesta es el mayor, no `0`, así que el mejor valor empieza en una
  celda del array;
- los números pueden repartirse en líneas de cualquier forma, así que se
  leen como un flujo de palabras;
- las sumas no superan `100² · 127`, que cabe en 32 bits.

Las respuestas se compararon con la comprobación de todos los rectángulos
mediante una tabla de sumas prefijas en 150 arrays aleatorios de hasta
`9 × 9`.

## Soluciones optimizadas

La solución optimizada en Python lee la entrada en bloques de 4 KB,
guarda cada fila en un `array` de bytes (todos los valores están entre
−127 y 127) y suma una fila a las sumas de columnas con `map` en lugar
de un bucle de Python: 632 KB en lugar de 1372 KB, con el mismo tiempo.
La solución optimizada en Rust analiza los números a mano directamente
desde `stdin().lock()`, guarda la matriz en un solo vector plano de `i8`
y reutiliza un vector de sumas de columnas: 212 KB en lugar de 372 KB,
aunque el tiempo sube de 0.015 s a 0.046 s.

## Notas por lenguaje

- Todos los lenguajes hacen el mismo recorrido.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1146_dp.cpp](1146_dp.cpp) | G++ 13.2 x64 | dp | O(N³) | AC | 0.015 s | 248 KB | 11279486 |
| [1146_dp.go](1146_dp.go) | Go 1.14 x64 | dp | O(N³) | AC | 0.031 s | 1308 KB | 11279491 |
| [1146_dp.java](1146_dp.java) | Java 1.8 | dp | O(N³) | AC | 0.078 s | 620 KB | 11279494 |
| [1146_dp.py](1146_dp.py) | Python 3.12 x64 | dp | O(N³) | AC | 0.187 s | 1372 KB | 11279492 |
| [1146_dp.rs](1146_dp.rs) | Rust 1.75 x64 | dp | O(N³) | AC | 0.015 s | 372 KB | 11279497 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1146_dp_optimized.py](1146_dp_optimized.py) \* | Python 3.12 x64 | dp | O(N³) | AC | 0.171 s | 632 KB | 11303714 |
| [1146_dp_optimized.rs](1146_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N³) | AC | 0.046 s | 212 KB | 11303715 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
