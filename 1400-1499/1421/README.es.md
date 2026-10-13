# 1421. Operaciones de crédito

[Timus 1421](https://acm.timus.ru/problem.aspx?space=1&num=1421) · dificultad 544 · greedy

Problema original de Ilya Grebnov, Dmitry Kovalioff y Nikita Rybak, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Llenar una matriz N × N (2 ≤ N ≤ 100) con enteros de 0 a 100 de modo que
la fila i sume SR[i] y la columna j sume SC[j] (cada suma de 0 a
32 000, con totales iguales). Hay que imprimir «YES» y una matriz así, o
«NO» si no existe.

Límite de tiempo: 0.25 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego las N sumas de filas, luego las N sumas de columnas.

## Salida

«NO», o «YES» y la matriz.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
267 157 188 259
193 320 346 12
```

Salida:

```
YES
100 55 100 12
0 70 87 0
0 95 93 0
93 100 66 0
```

## Solución

Se llenan las filas una a una, tomando cada vez los créditos de las
columnas que aún necesitan más. Para una fila que necesita r, se bajan
las necesidades de todas las columnas hacia un nivel común L: la
columna j da min(100, max(0, SC[j] − L)). Lo que se da disminuye al
crecer L, así que una búsqueda binaria halla el menor L que da como
mucho r, y las pocas unidades que faltan salen, una por columna, de las
columnas que están justo en el nivel L. Si ni siquiera L = 0 da r, la
respuesta es «NO».

Por qué esto nunca estropea una solución: supongamos que existe una
matriz, pero su primera fila deja a la columna j al menos 2 más que a la
columna k, aunque la fila podría tomar una unidad más de j y toma algo
de k. Entonces el resto de la columna j suma más que el de la columna
k, y alguna fila de abajo tiene más en j que en k. Pasar una unidad de k
a j en la primera fila, y al revés en esa otra fila, conserva todas las
sumas y los límites y deja las necesidades restantes estrictamente más
igualadas. Repitiéndolo se llega a la fila equilibrada que construye el
voraz, y el problema restante solo depende del multiconjunto de
necesidades de las columnas, así que el voraz conserva una solución
siempre que exista. `O(N² log S)`.

Detalles a tener en cuenta:

- cada fila y cada columna pueden caber por separado mientras que dos
  filas juntas no, así que no basta con comprobar líneas sueltas
  (prueba 06);
- se acepta cualquier matriz válida, así que las pruebas usan un
  verificador (prueba 01);
- una fila que necesita más de 100 por columna es imposible de entrada
  (pruebas 03, 08).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1421_greedy.cpp](1421_greedy.cpp) | G++ 13.2 x64 | greedy | O(N^2 log S) | AC | 0.015 s | 268 KB |
| [1421_greedy.go](1421_greedy.go) | Go 1.14 x64 | greedy | O(N^2 log S) | AC | 0.031 s | 1188 KB |
| [1421_greedy.java](1421_greedy.java) | Java 1.8 | greedy | O(N^2 log S) | AC | 0.093 s | 832 KB |
| [1421_greedy.py](1421_greedy.py) | Python 3.12 x64 | greedy | O(N^2 log S) | AC | 0.171 s | 760 KB |
| [1421_greedy.rs](1421_greedy.rs) | Rust 1.75 x64 | greedy | O(N^2 log S) | AC | 0.031 s | 336 KB |
