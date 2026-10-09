# 1076. Clasificar la basura en contenedores moviendo lo mínimo

[Timus 1076](https://acm.timus.ru/problem.aspx?space=1&num=1076) · dificultad 713 · matching

Problema original de Jivko Ganev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` contenedores (`1 ≤ N ≤ 150`), y el contenedor `i` tiene `a[i][j]`
unidades (`0 ≤ a[i][j] ≤ 100`) de cada uno de los `N` tipos de basura `j`.
Hay que clasificar la basura para que cada tipo quede solo en su propio
contenedor. Mover una unidad entre dos contenedores distintos cuesta 1.
Halla el menor coste total.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas con `N` cantidades cada una: la línea `i` describe
el contenedor `i`.

## Salida

El menor coste total.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
62 41 86 94
73 58 11 12
69 93 89 88
81 40 69 13
```

Salida:

```
650
```

## Solución

Al final cada tipo tiene su propio contenedor, así que el estado final es
una asignación uno a uno de tipos a contenedores. Si el tipo `j` va al
contenedor `i`, las `a[i][j]` unidades que ya están allí se quedan y todas
las demás unidades del tipo `j` se mueven una vez. Así que el coste es la
cantidad total menos la suma de `a[i][j]` sobre los pares asignados, y la
tarea es un emparejamiento perfecto de peso máximo entre contenedores y
tipos: el problema de asignación.

El algoritmo húngaro lo resuelve en `O(N^3)`. Esta es la versión con
potenciales `u` para las filas y `v` para las columnas: las filas se
añaden una a una, y para cada una se hace crecer, columna a columna, un
camino de aumento más corto en costes reducidos, moviendo los potenciales
en cada paso según la menor holgura `delta`. Con costes `−a[i][j]` el
mínimo es `−v[0]`, y la respuesta es el total más ese mínimo.

Detalles a tener en cuenta:

- tomar primero la mayor cantidad es incorrecto: con las filas `10 9 0`,
  `9 0 0` y `0 0 1` la elección voraz deja en su sitio 11 unidades, y la
  mejor asignación 19;
- probar todas las permutaciones es impensable con `N = 150`, y un flujo
  de coste mínimo general es más lento de lo necesario en Python.

Las respuestas se comprobaron con un flujo de coste mínimo con caminos más
cortos por SPFA, y para `N ≤ 7` con todas las asignaciones.

## Notas por lenguaje

- Los cinco lenguajes implementan el mismo algoritmo húngaro, con
  potenciales numerados desde 1 y los arreglos `owner` y `way`.
- Java lee la matriz con `StreamTokenizer`, mucho más rápido que
  `Scanner` para 22 500 números.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1076_matching.cpp](1076_matching.cpp) | G++ 13.2 x64 | matching | O(N^3) | AC | 0.031 s | 252 KB |
| [1076_matching.go](1076_matching.go) | Go 1.14 x64 | matching | O(N^3) | AC | 0.031 s | 1612 KB |
| [1076_matching.java](1076_matching.java) | Java 1.8 | matching | O(N^3) | AC | 0.125 s | 804 KB |
| [1076_matching.py](1076_matching.py) | Python 3.12 x64 | matching | O(N^3) | AC | 0.515 s | 2460 KB |
| [1076_matching.rs](1076_matching.rs) | Rust 1.75 x64 | matching | O(N^3) | AC | 0.046 s | 796 KB |
