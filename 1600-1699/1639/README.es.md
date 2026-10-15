# 1639. Chocolate 2

[Timus 1639](https://acm.timus.ru/problem.aspx?space=1&num=1639) · dificultad 32 · games

Problema original de Alexander Pronchenkov (preparado por Ivan Burmistrov), del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos jugadores parten por turnos una tableta de chocolate de m × n: cada
movimiento toma cualquier trozo y lo parte en dos por las ranuras. Pierde
quien no puede mover porque solo quedan trozos de 1 × 1. ¿Debe Karlsson
mover primero o segundo para ganar con seguridad?

## Entrada

Dos enteros m y n (1 ≤ m, n ≤ 50).

## Salida

`[:=[first]` si gana quien mueve primero, y `[second]=:]` en otro caso.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 4
```

Salida:

```
[:=[first]
```

### Ejemplo 2

Entrada:

```
1 3
```

Salida:

```
[second]=:]
```

## Solución

Cada movimiento convierte un trozo en dos, así que aumenta el número de
trozos exactamente en uno. El juego empieza con un trozo y termina con
m · n, de modo que siempre dura m · n − 1 movimientos, hagan lo que
hagan los jugadores. El primer jugador hace el último movimiento, y
gana, exactamente cuando m · n − 1 es impar, es decir, cuando m · n es
par. `O(1)`.

Detalles a tener en cuenta:

- la estrategia no importa, así que no hay nada que buscar;
- una tableta de 1 × 1 no admite ningún movimiento, y el primer jugador
  pierde enseguida (prueba 03).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1639_games.cpp](1639_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 120 KB |
| [1639_games.go](1639_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.031 s | 1132 KB |
| [1639_games.java](1639_games.java) | Java 1.8 | games | O(1) | AC | 0.125 s | 1608 KB |
| [1639_games.py](1639_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.078 s | 412 KB |
| [1639_games.rs](1639_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.062 s | 228 KB |
