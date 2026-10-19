# 1832. Espectáculo Arirang

[Timus 1832](https://acm.timus.ru/problem.aspx?space=1&num=1832) · dificultad 953 · constructive

Problema original de Victor Kamashev (preparado por Daniil Aizenshtein), del XV Campeonato Abierto de los Urales de Programación Competitiva, abril de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n artistas en fila se reparten en d corros, con d un divisor propio
desconocido de n: el corro j-ésimo lo forman en círculo los artistas j,
j + d, j + 2d, … Elegir colores de camisa entre 26 de modo que los
vecinos de cada corro difieran sea cual sea d, o decir que es
imposible.

## Entrada

n (2 ≤ n ≤ 300000).

## Salida

n letras minúsculas, los colores de los artistas, o "Impossible". Se
acepta cualquier coloración válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
```

Salida:

```
acacbdb
```

## Solución

Se numeran los artistas desde 0. Dos artistas son vecinos para algún d
exactamente cuando distan d o n − d, con d divisor propio de n.

Sea m el menor número que no divide a n. Entonces m no divide a ningún
divisor propio, así que colorear por x mod m separa a cualquier par de
artistas a distancia d. Como mcm(1, …, 13) = 360360 supera 300000, m
es como mucho 13.

Quedan los pares que cruzan el cierre del círculo, a distancia n − d.
Con p el menor factor primo de n, todo divisor propio es como mucho
n/p, así que esas distancias son al menos n − n/p. Se parte la fila en
los primeros n − n/p artistas y los últimos n/p: dentro de cada parte
no hay distancias tan largas, porque n/p ≤ n − n/p. Ambas partes se
colorean por x mod m, la segunda con sus propias m letras. Así los
pares dentro de una parte están bien y los pares entre partes nunca
comparten color. Se usan como mucho 2m ≤ 26 letras, así que la
respuesta nunca es "Impossible". `O(n)`.

Para n = 7, m = 2 y p = 7: los seis primeros artistas alternan a y b y
el último recibe c, lo que da abababc; la respuesta del ejemplo es otra
coloración válida.

Trampas:

- los corros se cierran, así que los artistas a distancia n − d también
  son vecinos;
- con d = n/2 un corro tiene solo dos artistas, que siguen siendo
  vecinos;
- colorear solo por x mod m falla en el cierre: para n = 7 da el mismo
  color a los artistas 0 y 6.

Todos los n de 2 a 3000 y muchos grandes, incluidos los que usan
las 26 letras, se comprobaron contra cada divisor propio.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1832_constructive.cpp](1832_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 476 KB |
| [1832_constructive.go](1832_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 2192 KB |
| [1832_constructive.java](1832_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 2708 KB |
| [1832_constructive.py](1832_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.140 s | 5448 KB |
| [1832_constructive.rs](1832_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 492 KB |
