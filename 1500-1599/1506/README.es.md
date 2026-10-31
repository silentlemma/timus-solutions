# 1506. Columnas de números

[Timus 1506](https://acm.timus.ru/problem.aspx?space=1&num=1506) · dificultad 134 · implementation

Problema original de Stanislav Vasiliev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que imprimir N números de 0 a 999 (1 ≤ N ≤ 100) en K columnas
(1 ≤ K ≤ N) con el menor número de filas. Todas las columnas tienen la
misma altura salvo la última, que puede ser más corta. Los números
llenan la primera columna de arriba abajo, luego la segunda, y así
sucesivamente. Cada número va alineado a la derecha en un campo de
4 caracteres, y ninguna línea tiene espacios finales.
Se garantiza que existe una tabla con exactamente K columnas no vacías.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y K, y luego los N números.

## Salida

La tabla.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 3
1 2 30 40 50 600 700
```

Salida:

```
   1  40 700
   2  50
  30 600
```

## Solución

El menor número de filas es H = ⌈N / K⌉. Toda altura válida h cumple
h ≥ H y (K − 1)·h < N. La garantía de existencia implica entonces
(K − 1)·H < N, así que con altura H la última columna no queda vacía.
La columna c tiene los números
de índices c·H a c·H + H − 1, así que la fila r está formada por los
números c·H + r que existen, para c = 0, 1, …; se acaban en la primera
columna agotada, que solo puede ser la última. Cada uno se imprime en
un campo de 4 y ahí termina la fila. `O(N)`.

Detalles a tener en cuenta:

- los números bajan por las columnas, no van a lo largo de las filas
  (prueba 01);
- cada número ocupa 4 caracteres, también el primero, así que cada
  línea empieza con espacios (prueba 01);
- cuando la última columna es más corta, las filas de abajo terminan un
  número antes, sin espacios finales (prueba 06);
- la garantía de existencia es esencial: la última columna debe tener
  al menos un número (prueba 06); no todo par con 1 ≤ K ≤ N es viable;
- K = N da una sola fila y K = 1 una sola columna (pruebas 03, 04).

## Soluciones optimizadas

La solución optimizada en C++ guarda los números en un arreglo fijo de
100 `int` en la pila en lugar de un `std::vector`, ya que N ≤ 100, así
que el programa no reserva nada en el montón:
{1506_implementation_optimized.cpp}.

La solución optimizada en Java rellena cada celda por su cuenta:
convierte el número con `Integer.toString` y pone espacios delante hasta
4 caracteres, en lugar de llamar a `String.format`, que crea un
formateador nuevo y analiza el patrón en cada celda. Un número de hasta
999 tiene como mucho tres cifras, así que cada celda lleva al menos un
espacio delante: {1506_implementation_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1506_implementation_optimized.cpp`: reducción de tiempo +0.00%;
  reducción de memoria +48.98%; base: `1506_implementation.cpp`.

- `1506_implementation_optimized.java`: reducción de tiempo +14.68%;
  reducción de memoria +56.56%; base: `1506_implementation.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1506_implementation.go](1506_implementation.go).
- [1506_implementation.rs](1506_implementation.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1506_implementation.cpp](1506_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11287283 |
| [1506_implementation.go](1506_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1108 KB | 11287284 |
| [1506_implementation.java](1506_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 976 KB | 11287286 |
| [1506_implementation.py](1506_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.093 s | 460 KB | 11287285 |
| [1506_implementation.rs](1506_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 252 KB | 11287287 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1506_implementation_optimized.cpp](1506_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 100 KB | 11304437 |
| [1506_implementation_optimized.java](1506_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 424 KB | 11304438 |
