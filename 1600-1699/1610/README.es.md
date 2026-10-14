# 1610. Ahora están de moda los cactus

[Timus 1610](https://acm.timus.ru/problem.aspx?space=1&num=1610) · dificultad 2024 · games

Problema original de Alexander Ipatov y Vladimir Yakovlev, del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cactus es un grafo conexo en el que cada arista está como mucho en un
ciclo simple; un vértice es la raíz. Dos jugadores cortan por turnos una
arista; lo que deja de estar unido a la raíz se cae. Gana quien corta la
última arista todavía unida a la raíz. ¿Quién gana con juego óptimo? El
cactus tiene como mucho 50000 vértices y se da como caminos disjuntos
en aristas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n, m y la raíz r, luego m caminos, cada uno con su longitud y sus
vértices.

## Salida

`First` o `Second`.

## Ejemplos

### Ejemplo 1

Entrada:

```
17 2 1
15 3 4 5 6 7 8 3 2 9 10 11 12 13 14 9
6 2 1 15 16 17 15
```

Salida:

```
First
```

### Ejemplo 2

Entrada:

```
16 2 1
15 3 4 5 6 7 8 3 2 9 10 11 12 13 14 9
5 2 1 15 16 1
```

Salida:

```
Second
```

## Solución

Es Hackenbush verde, y quien mueve gana exactamente cuando el valor de
Grundy del grafo con raíz no es 0. Dos reglas clásicas dan el valor de
un cactus. Por el principio de los dos puntos, una rama colgada de un
vértice por una sola arista vale g + 1, donde g es el valor de lo que
cuelga bajo esa arista. Por el principio de fusión, los vértices de un
ciclo pueden fundirse en uno sin cambiar el valor: el ciclo se convierte
en tantos lazos como aristas tiene, cada lazo vale 1, así que el propio
ciclo vale su longitud módulo 2, y lo que colgaba de sus vértices pasa a
colgar del vértice fundido.

Una búsqueda en profundidad desde la raíz, sin recursión, hace que cada
arista fuera del árbol una un vértice con uno de sus antecesores; cada
arista así cierra un ciclo, que se anota en su vértice más alto. Después
se procesan los vértices de abajo arriba: un vértice hace XOR de g + 1
sobre sus hijos en el árbol que no están en un ciclo con él, y para
cada ciclo que encabeza, de la paridad del ciclo y de los valores de sus
otros vértices. `O(n + m)` en total, porque cada arista está como mucho
en un ciclo.

Los resultados se contrastaron con una búsqueda exhaustiva del juego en
250 cactus pequeños aleatorios de hasta 12 aristas.

Detalles a tener en cuenta:

- un ciclo par en la raíz vale 0, así que un cuadrado solo pierde para
  quien mueve, mientras que un triángulo gana (pruebas 05 y 06);
- la raíz puede ser cualquier vértice, incluso uno en medio de un camino
  (prueba 09);
- una recursión de 50000 niveles desborda la pila en varios lenguajes,
  así que la búsqueda lleva su propia pila.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1610_games.cpp](1610_games.cpp) | G++ 13.2 x64 | games | O(n + m) | AC | 0.093 s | 5800 KB |
| [1610_games.go](1610_games.go) | Go 1.14 x64 | games | O(n + m) | AC | 0.125 s | 13364 KB |
| [1610_games.java](1610_games.java) | Java 1.8 | games | O(n + m) | AC | 0.203 s | 14784 KB |
| [1610_games.py](1610_games.py) | Python 3.12 x64 | games | O(n + m) | AC | 0.343 s | 24436 KB |
| [1610_games.rs](1610_games.rs) | Rust 1.75 x64 | games | O(n + m) | AC | 0.062 s | 11688 KB |
