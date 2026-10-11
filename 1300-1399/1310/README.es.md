# 1310. Diagnóstico de la ACM

[Timus 1310](https://acm.timus.ru/problem.aspx?space=1&num=1310) · dificultad 1066 · dp

Problema original con idea de Alexander Klepinin, preparado por Alexander Klepinin y Pavel Egorov, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un estado es un vector de L ≤ 100 enteros, cada uno de 1 a M ≤ 50,
cuya suma es divisible por K ≤ 50. Se listan todos los estados en orden
lexicográfico creciente, numerados desde 0. Dado un número N de esa
lista, hay que imprimir el estado.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

L, M y K, y luego N.

## Salida

Los L valores del estado.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 10 4
213
```

Salida:

```
9 6 1
```

## Solución

Primero se cuenta, luego se eligen los valores uno a uno.

Sea ways[i][r] el número de formas de llenar i registros con valores
1..M de modo que su suma deje resto r módulo K. Entonces ways[0][0] = 1
y

ways[i][(r + v) mod K] += ways[i − 1][r] para cada v en 1..M.

Para leer el estado se recorren las posiciones guardando la suma s de
los valores ya elegidos. En una posición tras la que quedan `left`
registros, el valor v abre un bloque de ways[left][(−(s + v)) mod K]
estados. Se prueba v = 1, 2, …: mientras N no sea menor que el bloque,
se salta el bloque (N −= block); si no, se toma v y se sigue.

Las cantidades llegan a unos 50¹⁰⁰, un número de 170 cifras, así que N
y la tabla necesitan enteros grandes. La tabla tiene 101 · K entradas y
se llena con L · M · K sumas grandes. `O(L · M · K)` operaciones con
enteros grandes.

Detalles a tener en cuenta:

- el resto de un número negativo debe quedar en 0..K − 1
  ((−(s + v)) mod K);
- con K = 1 los estados son los M^L vectores, y el último es todo M
  (prueba 06);
- con un registro solo existen los valores divisibles por K (pruebas 02
  y 03).

Las respuestas se compararon con la lista directa de todos los estados
en 150 casos aleatorios pequeños.

## Notas por lenguaje

- Python, Go y Java usan sus enteros grandes incorporados; C++ y Rust
  usan un pequeño tipo numérico en base 10⁹ con solo las operaciones
  necesarias: leer, sumar, comparar y restar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1310_dp.cpp](1310_dp.cpp) | G++ 13.2 x64 | dp | O(L * M * K) | AC | 0.031 s | 800 KB |
| [1310_dp.go](1310_dp.go) | Go 1.14 x64 | dp | O(L * M * K) | AC | 0.015 s | 1752 KB |
| [1310_dp.java](1310_dp.java) | Java 1.8 | dp | O(L * M * K) | AC | 0.109 s | 6596 KB |
| [1310_dp.py](1310_dp.py) | Python 3.12 x64 | dp | O(L * M * K) | AC | 0.109 s | 884 KB |
| [1310_dp.rs](1310_dp.rs) | Rust 1.75 x64 | dp | O(L * M * K) | AC | 0.046 s | 820 KB |
