# 1311. Una construcción estable

[Timus 1311](https://acm.timus.ru/problem.aspx?space=1&num=1311) · dificultad 1432 · implementation

Problema original de Alexey Lakhtin, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un muro está hecho de ladrillos de igual altura, grosor y densidad pero
de distintas longitudes, en H ≤ 10 000 capas de hasta 1000 ladrillos
cada una, como mucho 100 000 en total. Un ladrillo ocupa [L, R] con
extremos enteros de 0 a 10 000, y ningún ladrillo descansa sobre dos o
más ladrillos de la capa de abajo. Sin argamasa, ¿se sostiene el muro?
Algo se cae si un ladrillo, junto con todo lo que descansa sobre él,
tiene su centro de masas en el borde de su apoyo o fuera de él.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

H; luego, para cada capa desde arriba: el número de ladrillos K y K
líneas `L R` en orden creciente.

## Salida

`Yes` si el muro se sostiene; si no, `No`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1
10 20
3
1 7
13 17
100 200
2
0 20
60 160
```

Salida:

```
Yes
```

## Solución

Todo ladrillo por encima de la capa inferior descansa exactamente sobre
un ladrillo de debajo, el que solapa (con longitud positiva), así que
los ladrillos forman árboles apoyados en la capa inferior. El apoyo de
un ladrillo es su solape con ese ladrillo, y la carga es el propio
ladrillo más todo lo que descansa sobre él, directa o indirectamente.

La masa de un ladrillo es proporcional a su longitud, y su momento
respecto a 0 es (R² − L²) / 2. Así, la carga de un ladrillo tiene
W = Σ (R − L) y M = Σ (R² − L²) / 2 sobre su subárbol, y su centro es
M / W. Guardando 2M en lugar de M, la condición lo < M / W < hi pasa a
ser

2 · lo · W < 2M < 2 · hi · W,

todo en enteros exactos (2M queda por debajo de 2 · 10¹³).

Las capas llegan desde arriba, que es justo el orden en que las cargas
quedan completas. Para cada capa nueva se recorren a la vez la capa de
arriba y la nueva con dos punteros: cada ladrillo de arriba encuentra
el ladrillo de abajo que solapa, se comprueba con ese solape y le suma
su W y su 2M. Un ladrillo sin nada debajo, o que solo toca a otro en una
esquina, se cae. La capa inferior está sobre el suelo.
`O(total de ladrillos)`.

Detalles a tener en cuenta:

- un centro justo en el borde cuenta como caída (prueba 03 frente a la
  prueba 04);
- los ladrillos que solo se tocan en un extremo no sostienen nada
  (prueba 05), y una capa vacía deja colgando los ladrillos de encima
  (prueba 06);
- un peso añadido arriba puede salvar un ladrillo en voladizo: aquí
  bastan nueve ladrillos pequeños y ocho no (pruebas 09 y 10).

Las respuestas se compararon con una comprobación independiente con
fracciones exactas, que construye explícitamente el árbol de apoyos, en
600 muros aleatorios.

## Notas por lenguaje

- Python corta la entrada en capas enteras y trabaja con listas
  simples, unos 0,1 s para 100 000 ladrillos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1311_implementation.cpp](1311_implementation.cpp) | G++ 13.2 x64 | implementation | O(total bricks) | AC | 0.109 s | 204 KB |
| [1311_implementation.go](1311_implementation.go) | Go 1.14 x64 | implementation | O(total bricks) | AC | 0.031 s | 5572 KB |
| [1311_implementation.java](1311_implementation.java) | Java 1.8 | implementation | O(total bricks) | AC | 0.109 s | 4440 KB |
| [1311_implementation.py](1311_implementation.py) | Python 3.12 x64 | implementation | O(total bricks) | AC | 0.281 s | 21796 KB |
| [1311_implementation.rs](1311_implementation.rs) | Rust 1.75 x64 | implementation | O(total bricks) | AC | 0.015 s | 3152 KB |
