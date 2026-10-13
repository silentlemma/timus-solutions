# 1380. El ajedrez de Ostap

[Timus 1380](https://acm.timus.ru/problem.aspx?space=1&num=1380) · dificultad 3976 · implementation

Problema original de Ivan Popelyshev, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una posición de ajedrez, que no tiene por qué tener sentido, el
bando que mueve y hasta 60 jugadas, hay que comprobar cada jugada. Las
piezas se mueven como en el ajedrez, pero no hay enroque, ni captura al
paso, ni coronación. Una jugada es legal si mueve una pieza del bando
que mueve como esa pieza puede moverse y no deja atacado a ningún rey
de ese bando. Tras cada jugada hay que imprimir `Incorrect` si es
ilegal, y si no `Mate`, `Draw` (ahogado), `Check` o `Correct` para el
bando que mueve a continuación. Se para tras una jugada ilegal, un mate
o unas tablas, y entonces se imprime una línea vacía y el tablero. No
se comprueba la posición inicial antes de la primera jugada.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

64 números separados por espacios o saltos de línea, empezando por la
fila 8: 0 para una casilla vacía, 1 a 6 para peón, caballo, alfil,
torre, dama o rey blancos, negativos para las negras. Luego el número
de jugadas P (1 ≤ P ≤ 60), `White` o `Black` para el bando que mueve, y
P jugadas como `e2-e4`. Las columnas van de `a` a `h` de izquierda a
derecha, y las filas de `1` a `8` de abajo arriba.

## Salida

Una palabra por jugada procesada, luego una línea vacía y el tablero
en el formato de la entrada. Una jugada ilegal no se realiza; se
ignoran las jugadas posteriores a `Incorrect`, `Mate` o `Draw`.

## Ejemplos

### Ejemplo 1

Entrada:

```
-4 -2 -3 -5 -6 -3 -2 -4
-1 -1 -1 -1 -1 -1 -1 -1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
4 2 3 5 6 3 2 4
2
White
e2-e4
e7-e4
```

Salida:

```
Correct
Incorrect

-4 -2 -3 -5 -6 -3 -2 -4
-1 -1 -1 -1 -1 -1 -1 -1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 0 1 1 1
4 2 3 5 6 3 2 4
```

### Ejemplo 2

Entrada:

```
-4 -2 -3 -5 -6 -3 -2 -4
-1 -1 -1 -1 -1 -1 -1 -1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
4 2 3 5 6 3 2 4
8
White
e2-e4
e7-e5
d1-f3
h7-h6
f1-c4
g7-g6
f3-f7
e8-f7
```

Salida:

```
Correct
Correct
Correct
Correct
Correct
Correct
Mate

-4 -2 -3 -5 -6 -3 -2 -4
-1 -1 -1 -1 0 5 0 0
0 0 0 0 0 0 -1 -1
0 0 0 0 -1 0 0 0
0 0 3 0 1 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 0 1 1 1
4 2 3 0 6 0 2 4
```

### Ejemplo 3

Entrada:

```
0 0 0 0 0 6 0 -6
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1
White
h6-a6
```

Salida:

```
Correct

0 0 0 0 0 6 0 -6
0 0 0 0 0 0 0 0
5 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
```

## Solución

Se simula la partida en una matriz de 8 × 8:

- una pieza alcanza una casilla si en ella no hay una pieza de su color
  y el movimiento encaja: la L del caballo, un paso del rey, la línea de
  una pieza de largo alcance con las casillas intermedias vacías, un
  paso del peón hacia delante a una casilla vacía, dos pasos desde su
  segunda fila por encima de una casilla vacía hasta otra vacía, o un
  paso diagonal hacia delante sobre una pieza rival;
- un bando está en jaque si alguna pieza rival alcanza alguno de sus
  reyes;
- una jugada es legal si la pieza es del bando que mueve, alcanza la
  casilla de destino y tras hacerla ningún rey de ese bando está en
  jaque; si no, se deshace;
- tras una jugada legal se mira al otro bando: tiene jugada si alguna de
  sus piezas tiene una jugada legal a alguna casilla. Sin jugada y en
  jaque es mate; sin jugada en otro caso, tablas. Si hay una jugada
  legal, se imprime `Check` si hay jaque y `Correct` en caso contrario.

Por posición se prueban a lo sumo 64 · 64 jugadas, y cada una se coteja
con a lo sumo 64 atacantes por cada uno de hasta 64 reyes. Las líneas
de las piezas de largo alcance tienen como máximo seis casillas
intermedias. Una cota holgada es `O(P · 64⁴)`, o `O(P)` para el tablero
fijo de 8 × 8.

El enunciado deja casos abiertos; las pruebas del juez siguen estas
reglas, según se vio en el foro del problema:

- el tablero se imprime tras la última jugada aunque todas sean
  correctas (ejemplo 3);
- un peón avanza dos casillas desde su segunda fila venga de donde
  venga, pero no desde la primera (pruebas 04 y 05);
- se puede capturar al rey; un bando sin rey nunca está en jaque, y sin
  otras piezas no tiene jugada: tablas (prueba 06);
- un bando puede tener varios reyes, y una jugada debe dejarlos a todos
  a salvo (pruebas 10 a 12).

## Notas por lenguaje

- Las cinco soluciones prueban las jugadas sobre el propio tablero y
  las deshacen.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1380_implementation.cpp](1380_implementation.cpp) | G++ 13.2 x64 | implementation | O(P·64⁴) | AC | 0.031 s | 396 KB |
| [1380_implementation.go](1380_implementation.go) | Go 1.14 x64 | implementation | O(P·64⁴) | AC | 0.015 s | 1128 KB |
| [1380_implementation.java](1380_implementation.java) | Java 1.8 | implementation | O(P·64⁴) | AC | 0.125 s | 1736 KB |
| [1380_implementation.py](1380_implementation.py) | Python 3.12 x64 | implementation | O(P·64⁴) | AC | 0.078 s | 1092 KB |
| [1380_implementation.rs](1380_implementation.rs) | Rust 1.75 x64 | implementation | O(P·64⁴) | AC | 0.046 s | 240 KB |
