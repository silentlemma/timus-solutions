# 1499. Tricornios

[Timus 1499](https://acm.timus.ru/problem.aspx?space=1&num=1499) · dificultad 1474 · constructive

Problema original de Alex Samsonov, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un polígono regular con vértices 1 … N (3 ≤ N ≤ 50000) ya tiene K cortes
por diagonales que no se cruzan (0 ≤ K ≤ N − 3). Hay que añadir cortes
por diagonales, sin cruzar ninguno de los demás, hasta dividir el
polígono en triángulos, y escribirlos.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N, K y luego K líneas con los dos vértices de un corte.

## Salida

El número de cortes nuevos y luego los cortes como pares de vértices.
Se acepta cualquier triangulación.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1
1 4
```

Salida:

```
1
3 1
```

## Solución

Toda triangulación de un N-ágono tiene N − 3 diagonales, así que faltan
exactamente N − 3 − K cortes. Los cortes dados dividen el polígono en
caras convexas, y cualquier cara se triangula con un abanico de
diagonales desde uno de sus vértices.

Las caras se hallan con una pila recorriendo los vértices 1 … N en
orden. Se apila cada vértice v; luego, para cada corte dado u–v con
u < v, del u más cercano al más lejano, los vértices apilados encima de
u, junto con u y v, forman una cara: se desapilan, se triangula la cara
en abanico desde u y se vuelve a apilar v. Tras el recorrido la pila
guarda la cara que contiene el lado N–1, que también se triangula. Cada
vértice se apila y desapila un número acotado de veces, así que el
recorrido es lineal salvo la ordenación de los cortes en cada vértice.
`O(N log N)`.

Detalles a tener en cuenta:

- un corte puede darse con el vértice mayor primero (prueba 06);
- varios cortes pueden acabar en un mismo vértice y sus caras deben
  cerrarse de dentro hacia fuera (prueba 05, gen4);
- si se dan los N − 3 cortes, o N = 3, la respuesta es 0 (pruebas 02,
  03, gen3).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1499_constructive.cpp](1499_constructive.cpp) | G++ 13.2 x64 | constructive | O(N log N) | AC | 0.078 s | 2108 KB |
| [1499_constructive.go](1499_constructive.go) | Go 1.14 x64 | constructive | O(N log N) | AC | 0.093 s | 9344 KB |
| [1499_constructive.java](1499_constructive.java) | Java 1.8 | constructive | O(N log N) | AC | 0.171 s | 10440 KB |
| [1499_constructive.py](1499_constructive.py) | Python 3.12 x64 | constructive | O(N log N) | AC | 0.187 s | 14896 KB |
| [1499_constructive.rs](1499_constructive.rs) | Rust 1.75 x64 | constructive | O(N log N) | AC | 0.031 s | 4108 KB |
