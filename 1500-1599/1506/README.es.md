# 1506. Columnas de números

[Timus 1506](https://acm.timus.ru/problem.aspx?space=1&num=1506) · dificultad 134 · implementation

Problema original de Stanislav Vasiliev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que imprimir N números de 0 a 999 (1 ≤ N ≤ 100) en K columnas
(1 ≤ K ≤ N) con el menor número de filas. Todas las columnas tienen la
misma altura salvo la última, que puede ser más corta. Los números
llenan la primera columna de arriba abajo, luego la segunda, y así
sucesivamente. Cada número va alineado a la derecha en un campo de 4
caracteres, y ninguna línea tiene espacios finales.
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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1506_implementation.cpp](1506_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB |
| [1506_implementation.go](1506_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1108 KB |
| [1506_implementation.java](1506_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 976 KB |
| [1506_implementation.py](1506_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.093 s | 460 KB |
| [1506_implementation.rs](1506_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 252 KB |
