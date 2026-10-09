# 1035. El menor número de hilos para un bordado de dos caras

[Timus 1035](https://acm.timus.ru/problem.aspx?space=1&num=1035) · dificultad 1370 · graphs, dsu

Problema original de Pavel Zaletsky, del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tela tiene una cuadrícula de `N × M` celdas cuadradas
(`1 ≤ N, M ≤ 200`). Una puntada cubre una diagonal de una celda y está en
una cara de la tela, el derecho o el revés; cada diagonal de cada celda
lleva como mucho una puntada por cara. Un hilo hace una sucesión de
puntadas unidas en vértices de la cuadrícula, y dos puntadas consecutivas
de un hilo siempre están en caras opuestas (la aguja atraviesa la tela en
el vértice común). Dadas las puntadas de ambas caras, halla el menor
número de hilos con los que se hace todo el bordado.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `M` (filas y columnas) y luego `2N` líneas de `M` caracteres: las
primeras `N` líneas describen el derecho y las `N` siguientes el revés,
visto con la misma orientación que el derecho. Un carácter es `.` (sin
puntada), `/` o `\` (una diagonal) o `X` (ambas diagonales).

## Salida

El número mínimo de hilos.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 5
.....
.\...
..\..
.....
.....
....\
.\X..
.....
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
3 3
\..
.\.
..\
...
.\.
...
```

Salida:

```
2
```

## Solución

Los vértices de la cuadrícula son los vértices de un grafo y las puntadas
son aristas coloreadas según la cara. Un hilo es un recorrido cuyas
aristas alternan de color, y hay que repartir todas las aristas en el
menor número de esos recorridos.

Se mira un grupo conexo de puntadas y, en cada vértice `v`, los `f(v)`
extremos de puntadas del derecho y los `b(v)` del revés. Dentro de un
recorrido, un vértice se atraviesa con una puntada del derecho y otra del
revés, así que en `v` hay al menos `|f(v) − b(v)|` extremos de
recorridos. Cada recorrido tiene dos extremos, lo que da la cota inferior
`S / 2`, donde `S` es la suma de `|f(v) − b(v)|` en el grupo, y un grupo
con puntadas siempre necesita al menos un hilo. Ambas cotas se alcanzan:
si `S = 0`, todos los vértices están equilibrados y un grafo conexo con
colores equilibrados tiene un recorrido cerrado alternante por todas sus
aristas (teorema de Kotzig). Si no, se emparejan los extremos que faltan
con `S / 2` conexiones extra, lo que equilibra el grupo; el recorrido
cerrado, cortado en esas conexiones, da exactamente `S / 2` hilos.

Así que la respuesta es la suma sobre los grupos de `max(1, S / 2)`. Una
estructura union-find sobre los `(N + 1)(M + 1)` vértices encuentra los
grupos, y un arreglo guarda `f(v) − b(v)`. `O(N · M · α)`.

Detalles a tener en cuenta:

- el revés se da con la misma orientación que el derecho: una `\` en el
  revés une los mismos vértices que una `\` en el derecho;
- las puntadas de una misma cara nunca se unen directamente: una línea de
  puntadas del derecho necesita un hilo por puntada;
- un grupo con todos los vértices equilibrados necesita igualmente un
  hilo; los vértices vacíos no forman grupos, y un bordado sin puntadas
  necesita 0 hilos.

## Notas por lenguaje

- Todos los lenguajes usan la misma union-find con reducción de caminos;
  Java lee las filas con `BufferedReader`, porque `StreamTokenizer`
  tomaría `/` por el comienzo de un comentario.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1035_dsu.cpp](1035_dsu.cpp) | G++ 13.2 x64 | dsu | O(N·M·α) | AC | 0.015 s | 844 KB |
| [1035_dsu.go](1035_dsu.go) | Go 1.14 x64 | dsu | O(N·M·α) | AC | 0.031 s | 2276 KB |
| [1035_dsu.java](1035_dsu.java) | Java 1.8 | dsu | O(N·M·α) | AC | 0.109 s | 5076 KB |
| [1035_dsu.py](1035_dsu.py) | Python 3.12 x64 | dsu | O(N·M·α) | AC | 0.203 s | 2916 KB |
| [1035_dsu.rs](1035_dsu.rs) | Rust 1.75 x64 | dsu | O(N·M·α) | AC | 0.031 s | 1440 KB |
