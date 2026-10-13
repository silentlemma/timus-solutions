# 1425. Reina 2

[Timus 1425](https://acm.timus.ru/problem.aspx?space=1&num=1425) · dificultad 1680 · hashing

Problema original de Nikita Rybak, Dmitry Kovalioff e Ilya Grebnov, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El tablero es un cubo N-dimensional de S casillas por lado (1 ≤ N ≤ 5,
2 ≤ S ≤ 100). Una torre avanza cualquier número no nulo de casillas en
una coordenada; un alfil avanza el mismo número no nulo de casillas en
las N coordenadas a la vez, cada una en cualquier sentido; una reina se
mueve como cualquiera de los dos. Una reina está en un tablero vacío en
(C[1], …, C[N]). Hay que contar las casillas donde puede estar tras
exactamente dos movimientos.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

N y S, luego las N coordenadas de la reina.

## Salida

El número de casillas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
1 2 3
```

Salida:

```
27
```

En el ejemplo el primer movimiento puede ir a (2, 2, 3), (3, 2, 3),
(1, 1, 3), (1, 3, 3), (1, 2, 1) o (1, 2, 2) como torre, o a (2, 3, 2) o
(2, 1, 2) como alfil.

## Solución

El tablero puede tener 10¹⁰ casillas, pero la respuesta es pequeña:
desde el centro del tablero más grande es 858 180. Así que las casillas
se generan y se cuentan en un conjunto hash. Una reina tiene 2N
direcciones de torre y 2^N de alfil (en una dimensión coinciden). Las
casillas tras el primer movimiento son las de cada dirección desde el
inicio. Desde cada una se siguen de nuevo todas las direcciones y se
añade al conjunto cada casilla del camino; la casilla del primer
movimiento nunca se añade desde sus propios rayos, así que solo cuenta
si otro primer movimiento llega a ella.

Numerando una casilla como el número en base S cuyas cifras son
C[i] - 1, cada rayo se vuelve una progresión aritmética de números,
es decir, un rango entero. Las soluciones compiladas guardan los
números en una tabla de direccionamiento abierto de 2²¹ casillas;
Python añade rangos enteros a un conjunto. Se generan como máximo unas
4,3·10⁶ visitas a casillas.

Detalles a tener en cuenta:

- la reina puede volver a su casilla (prueba 01);
- en una línea de dos casillas solo se alcanza la inicial en dos
  movimientos (prueba 02);
- en una dimensión los movimientos de alfil y de torre son los mismos
  (pruebas 09, 13).

## Notas por lenguaje

- Python añade cada rayo al conjunto como un único `range`, así que el
  bucle por casillas corre dentro del código del conjunto. Todas las
  casillas alcanzadas junto con los rayos almacenados necesitan más de
  64 MB, así que se cuentan en ocho pasadas, cada una con las casillas
  cuya primera coordenada, contada desde cero, tiene un resto dado módulo 8:
  sigue siendo un único `range` por rayo. Las pruebas del juez tardan
  hasta 1,8 s y 33 MB.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1425_hashing.cpp](1425_hashing.cpp) | G++ 13.2 x64 | hashing | O((2N + 2^N)^2 S^2) | AC | 0.062 s | 16376 KB |
| [1425_hashing.go](1425_hashing.go) | Go 1.14 x64 | hashing | O((2N + 2^N)^2 S^2) | AC | 0.156 s | 19432 KB |
| [1425_hashing.java](1425_hashing.java) | Java 1.8 | hashing | O((2N + 2^N)^2 S^2) | AC | 0.203 s | 19128 KB |
| [1425_hashing.py](1425_hashing.py) | Python 3.12 x64 | hashing | O((2N + 2^N)^2 S^2) | AC | 1.812 s | 32572 KB |
| [1425_hashing.rs](1425_hashing.rs) | Rust 1.75 x64 | hashing | O((2N + 2^N)^2 S^2) | AC | 0.093 s | 16684 KB |
