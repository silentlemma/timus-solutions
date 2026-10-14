# 1609. Las baldosas del tranvía

[Timus 1609](https://acm.timus.ru/problem.aspx?space=1&num=1609) · dificultad 2995 · constructive

Problema original de Sergey Pupyrev, del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que cubrir una zona n × m (n, m ≤ 10, nm par) con baldosas 1 × 2.
El capataz coloca primero unas pocas para que el resto pueda terminarse
de una sola manera. Hay que hallar el menor número de baldosas
necesario y mostrar una colocación: las casillas que cubren como `1` y
las demás como `0`. Vale cualquier colocación óptima.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

n y m.

## Salida

El número de baldosas y luego n filas de m caracteres.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
```

Salida:

```
2
1100
0110
0000
0000
```

### Ejemplo 2

Entrada:

```
2 5
```

Salida:

```
2
11110
00000
```

## Solución

Es el número de forzamiento mínimo de los embaldosados con dominós de
una cuadrícula. Solo hay 75 tableros, así que las respuestas se hallan
una vez por búsqueda y se guardan en el programa: 40 patrones, uno para
cada n ≤ m, girado de lado cuando n > m.

La búsqueda se apoya en una prueba rápida. Un grafo bipartito con un
único emparejamiento perfecto siempre tiene un vértice de grado 1
(teorema de Kotzig), así que las casillas libres tienen un único
embaldosado exactamente cuando cubrir una y otra vez una casilla con un
solo vecino libre las agota todas. Para k = 0, 1, 2, … se prueban todos
los conjuntos de k baldosas sin solapes con esa prueba, y el primer k
que funciona es la respuesta: el fallo exhaustivo en k − 1 demuestra que
menos baldosas no bastan. El tablero más grande, 10 × 10, necesita 5
baldosas, lo que lleva un minuto; cualquier otro tablero, un segundo.

Los patrones guardados hacen además que las casillas colocadas se
embaldosen de una sola manera, así que el dibujo de `1` y `0` fija todo
el embaldosado con cualquier lectura. Las respuestas para cuadrados
coinciden con el teorema de Pachter y Kim: un tablero 2k × 2k necesita k
baldosas.

Las pruebas usan un verificador que comprueba el número de baldosas, que
las casillas marcadas se cubren con esas baldosas y que las casillas
libres tienen exactamente un embaldosado.

Detalles a tener en cuenta:

- una tira 1 × m ya tiene un solo embaldosado, así que la respuesta es 0
  y la cuadrícula es toda de ceros (pruebas 03, 05 y 06);
- los tableros estrechos son más difíciles: 2 × 8 necesita 3 baldosas y
  3 × 8 solo 2 (pruebas 07 y 09);
- la salida no muestra cómo están las baldosas, solo las casillas que
  cubren; con patrones cuyas casillas cubiertas se embaldosan de una sola
  manera no queda duda.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1609_constructive.cpp](1609_constructive.cpp) | G++ 13.2 x64 | constructive | O(nm) | AC | 0.015 s | 196 KB |
| [1609_constructive.go](1609_constructive.go) | Go 1.14 x64 | constructive | O(nm) | AC | 0.031 s | 1120 KB |
| [1609_constructive.java](1609_constructive.java) | Java 1.8 | constructive | O(nm) | AC | 0.140 s | 1684 KB |
| [1609_constructive.py](1609_constructive.py) | Python 3.12 x64 | constructive | O(nm) | AC | 0.093 s | 724 KB |
| [1609_constructive.rs](1609_constructive.rs) | Rust 1.75 x64 | constructive | O(nm) | AC | 0.062 s | 224 KB |
