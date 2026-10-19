# 1865. La isla de Märket

[Timus 1865](https://acm.timus.ru/problem.aspx?space=1&num=1865) · dificultad 3334 · constructive

Problema original de Eugene Kurpilyanskiy (idea de Leonid Volkov), del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La isla es el rectángulo de (0, 0) a (w, h), y el faro es un cuadrado
d × d con la esquina suroeste en (x, y), estrictamente dentro. Hay que
trazar una frontera de la costa norte a la costa sur: una poligonal de
vértices enteros cuyos segmentos son alternadamente verticales y
horizontales, el primero y el último verticales, todos de longitud no
nula. No debe tocarse a sí misma ni a las costas oeste y este, debe
tocar la costa norte y la sur una vez cada una y dividir la isla en dos
mitades iguales con todo el faro en la oriental (finlandesa). La
frontera puede tocar el faro, pero no cruzarlo. Se permiten como mucho
1000 vértices.

## Entrada

w y h (3 ≤ w, h ≤ 10⁶, w·h par), luego x, y y d (d > 0, 0 < x < w − d,
0 < y < h − d).

## Salida

El número de vértices y los vértices de norte a sur, o "Impossible". Se
acepta cualquier frontera válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 3
1 1 1
```

Salida:

```
6
4 3
4 2
1 2
1 1
4 1
4 0
```

### Ejemplo 2

Entrada:

```
10 10
1 1 8
```

Salida:

```
Impossible
```

## Solución

Con vértices enteros ambas partes están hechas de celdas unitarias, y la
mitad son w·h/2 celdas. Algunas celdas son finlandesas sea cual sea la
frontera. La frontera no puede llegar a la costa este, así que la
columna de h celdas junto a ella es de Finlandia. El faro añade d²
celdas. Finlandia es conexa, así que alguna fila contiene además las
w − 1 − x − d celdas entre el faro y esa columna. Si
h + d² + (w − 1 − x − d) supera la mitad, la respuesta es "Impossible".
Si no, sirve una de dos formas.

Si h + d(w − 1 − x) ≤ la mitad, cada fila de Finlandia va de alguna
columna hasta la costa: las filas del faro desde la columna x, las
demás desde la columna w − 1. Las celdas que faltan se toman de arriba
abajo, moviendo filas hacia el oeste pero nunca más allá de la
columna 1. En cada una de las tres franjas de filas (encima, al lado y debajo
del faro) unas filas llegan a la columna 1, una fila se queda a medio
camino y el resto conserva su columna. La frontera baja por estas
columnas, así que nunca se toca a sí misma, y tiene menos de 20
vértices.

Si no, las filas enteras del faro dan demasiado a Finlandia, y la
frontera rodea el faro. Baja por la columna w − 1 hasta la parte
superior del faro, sigue sus lados superior, oeste y sur, y sube por el
lado este. Luego Finlandia toma de arriba abajo filas enteras del
pasillo al este del faro y parte de una fila más. Lo que falta es menor
que (d − 1) veces el ancho del pasillo, así que todo queda al lado del
faro. La frontera vuelve a la columna w − 1 y baja recta hasta la costa
sur. Ambas formas cuestan `O(1)`.

La respuesta al primer ejemplo es distinta pero igual de válida: filas
de 3, 5 y 1 celdas desde arriba dan a Finlandia 9 celdas, la mitad de
18.

Trampas:

- w·h llega a 10¹², así que hacen falta enteros de 64 bits;
- tocar el faro está permitido, así que la frontera puede ir por sus
  lados;
- las filas movidas al oeste se detienen en la columna 1, o la frontera
  tocaría la costa oeste;
- los trozos de frontera en una misma columna deben unirse, o habría un
  segmento de longitud cero;
- cuando el faro está junto a la columna de la costa el pasillo está
  vacío, y siempre sirve la primera forma.

Las fronteras pasan un comprobador en las 2354 islas con lados de hasta
10 y en islas grandes aleatorias, y las respuestas "Impossible"
coinciden con una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1865_constructive.cpp](1865_constructive.cpp) | G++ 13.2 x64 | constructive | O(1) | AC | 0.015 s | 196 KB |
| [1865_constructive.go](1865_constructive.go) | Go 1.14 x64 | constructive | O(1) | AC | 0.046 s | 1156 KB |
| [1865_constructive.java](1865_constructive.java) | Java 1.8 | constructive | O(1) | AC | 0.125 s | 552 KB |
| [1865_constructive.py](1865_constructive.py) | Python 3.12 x64 | constructive | O(1) | AC | 0.109 s | 820 KB |
| [1865_constructive.rs](1865_constructive.rs) | Rust 1.75 x64 | constructive | O(1) | AC | 0.031 s | 252 KB |
