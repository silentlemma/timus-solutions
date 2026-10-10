# 1115. Repartir longitudes en filas de longitud total dada

[Timus 1115](https://acm.timus.ru/problem.aspx?space=1&num=1115) · dificultad 415 · backtracking

Problema original de la primera competición de selección del equipo búlgaro para la IOI.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N < 100` objetos con longitudes enteras de 1 a 100 y `M` filas
(`1 < M < 10`) de longitudes dadas. Reparte todos los objetos en las filas
de modo que las longitudes de cada fila sumen exactamente la longitud de
la fila; cada fila recibe al menos un objeto. Se sabe que existe un
reparto. Imprime uno.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N M`, luego `N` líneas con las longitudes de los objetos y luego `M`
líneas con las longitudes de las filas.

## Salida

Para cada fila, en el orden de la entrada, dos líneas: el número de
objetos que tiene y sus longitudes.

## Evaluación

Se acepta cualquier reparto válido. El comprobador verifica que cada fila
suma su longitud y que los objetos usados son exactamente los dados.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 2
4
10
2
5
3
11
13
```

Salida:

```
3
5 4 2
2
10 3
```

## Solución

Es una partición exacta en varias partes, un problema difícil en general,
así que las soluciones buscan con poda fuerte. Las filas se llenan de una
en una, empezando por la más corta, porque las filas cortas tienen menos
formas de llenarse; la última fila toma todo lo que queda. Dentro de una
fila, los objetos se prueban por longitud decreciente, y cada longitud
igual se prueba una sola vez en cada posición, ya que objetos iguales son
intercambiables.

La poda clave es una tabla de sumas de subconjuntos. Antes de llenar una
fila, un conjunto de bits `reach[k]` guarda las sumas que pueden formar
los objetos libres desde la posición `k` (se construye desde el final con
`reach[k] = reach[k+1] | reach[k+1] << len`). Un objeto solo se toma si el
resto de la fila aún puede completarse con los objetos posteriores, así
que una fila nunca lleva a un callejón sin salida; solo la interacción
entre filas puede obligar a retroceder. Con flotas aleatorias, y con
longitudes casi iguales donde hay muchos llenados parciales, cada caso
termina muy por debajo del límite de tiempo.

Detalles a tener en cuenta:

- probar objetos iguales en todos los órdenes hace explotar la búsqueda
  cuando hay muchas longitudes repetidas;
- sin la comprobación de sumas, una fila se explora aunque su resto ya no
  se pueda alcanzar;
- las filas deben imprimirse en el orden de la entrada, aunque se llenan
  en otro.

Las respuestas se comprobaron con el comprobador en todas las pruebas y en
120 flotas aleatorias de hasta 99 objetos en hasta 9 filas, con
longitudes casi iguales y en su mayoría iguales.

## Notas por lenguaje

- C++ usa `std::bitset`; Go, Java y Rust guardan las sumas en arreglos de
  palabras de 64 bits con un desplazamiento con «o» escrito a mano; Python
  usa enteros grandes como conjuntos de bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1115_backtracking.cpp](1115_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(2^N) worst case | AC | 0.015 s | 440 KB |
| [1115_backtracking.go](1115_backtracking.go) | Go 1.14 x64 | backtracking | O(2^N) worst case | AC | 0.015 s | 1872 KB |
| [1115_backtracking.java](1115_backtracking.java) | Java 1.8 | backtracking | O(2^N) worst case | AC | 0.140 s | 4508 KB |
| [1115_backtracking.py](1115_backtracking.py) | Python 3.12 x64 | backtracking | O(2^N) worst case | AC | 0.078 s | 684 KB |
| [1115_backtracking.rs](1115_backtracking.rs) | Rust 1.75 x64 | backtracking | O(2^N) worst case | AC | 0.015 s | 748 KB |
