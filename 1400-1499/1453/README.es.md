# 1453. Dama

[Timus 1453](https://acm.timus.ru/problem.aspx?space=1&num=1453) · dificultad 1200 · math

Problema original de Dmitry Kovalioff, Ilya Grebnov y Nikita Rybak, de Timus Top Coders: Second Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tablero de ajedrez de N dimensiones es un cubo de S × S × ... × S
casillas (1 ≤ N ≤ 10000, 2 ≤ S ≤ 100000). La torre avanza cualquier
número no nulo de casillas por una coordenada; el alfil avanza por las N
coordenadas a la vez la misma cantidad no nula; la dama se mueve como
cualquiera de los dos. Una dama está en (C[1], ..., C[N]) en un tablero
vacío. Hay que contar las casillas a las que puede moverse.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y S, y luego las N coordenadas.

## Salida

El número de casillas, que puede tener miles de cifras.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
1 2 3
```

Salida:

```
8
```

Los movimientos de torre llegan a (2, 2, 3), (3, 2, 3), (1, 1, 3),
(1, 3, 3), (1, 2, 1) y (1, 2, 2), y los de alfil a (2, 3, 2) y
(2, 1, 2).

## Solución

Los movimientos de torre dan N (S − 1) casillas. En una dimensión el
alfil se mueve igual que la torre, así que esa es toda la respuesta.
Con N ≥ 2 un movimiento de alfil cambia todas las coordenadas y uno de
torre solo una, así que los dos conjuntos no se solapan.

Un movimiento de alfil de longitud t elige un lado en cada coordenada, y
el lado ± en la coordenada i es posible cuando el margen de ese lado,
S − C[i] o C[i] − 1, es al menos t. Una coordenada con margen t en
ambos lados ofrece 2 opciones, con margen en un solo lado 1, y sin
margen la longitud t es imposible. Así que para longitudes t hasta el
menor de los max(S − C[i], C[i] − 1) hay 2^k(t) movimientos, donde k(t)
cuenta las coordenadas con min(S − C[i], C[i] − 1) ≥ t. Un histograma de
esos mínimos da todos los k(t) en una pasada, y la respuesta
N (S − 1) + Σ 2^k(t) tiene hasta unas 3000 cifras: se cuenta cuántos t
comparten cada k y se construye la suma duplicando desde el mayor k
hacia abajo, en bloques decimales de nueve cifras. `O(N + S + N · D)`
con D bloques.

Detalles a tener en cuenta:

- una dimensión, donde alfil y torre alcanzan las mismas casillas
  (prueba 02);
- la respuesta no cabe en ningún tipo entero nativo (pruebas 06, gen1 a
  gen3);
- una coordenada en el borde deja un solo lado (pruebas 03, 07, 08).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1453_math.cpp](1453_math.cpp) | G++ 13.2 x64 | math | O(N + S + N D) | AC | 0.031 s | 612 KB |
| [1453_math.go](1453_math.go) | Go 1.14 x64 | math | O(N + S + N D) | AC | 0.031 s | 2152 KB |
| [1453_math.java](1453_math.java) | Java 1.8 | math | O(N + S + N D) | AC | 0.109 s | 5828 KB |
| [1453_math.py](1453_math.py) | Python 3.12 x64 | math | O(N + S + N D) | AC | 0.109 s | 2376 KB |
| [1453_math.rs](1453_math.rs) | Rust 1.75 x64 | math | O(N + S + N D) | AC | 0.015 s | 1240 KB |
