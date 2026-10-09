# 1087. Un juego de quitar piedras en el que tomar la última pierde

[Timus 1087](https://acm.timus.ru/problem.aspx?space=1&num=1087) · dificultad 277 · games

Problema original de Anton Botov, de la Tercera Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 4 de marzo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un montón tiene `n` piedras (`1 ≤ n ≤ 10000`). Dos jugadores quitan por
turnos `k₁`, `k₂`, … o `kₘ` piedras (`1 ≤ m ≤ 50`, `1 ≤ kᵢ ≤ n`); siempre
es posible mover. Quien toma la última piedra pierde. Imprime 1 si el
primer jugador gana con juego perfecto, y 2 si no.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` y `m`, y luego `k₁ … kₘ`.

## Salida

1 o 2.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
17 3
1 3 4
```

Salida:

```
2
```

## Solución

Sea `win[x]` si gana el jugador que mueve con `x` piedras restantes. Con
0 piedras, el otro jugador acaba de tomar la última, así que `win[0]` es
verdadero. Para `x ≥ 1`, el jugador gana si algún movimiento permitido
`k ≤ x` lleva a una posición perdedora:
`win[x] = O sobre k de no win[x − k]`. La tabla se llena de 1 a `n`.
`O(n·m)`.

Detalles a tener en cuenta:

- es la regla «misère»: vaciar el montón es perder, así que un movimiento
  que toma todas las piedras que quedan nunca es ganador, y `win[0]` es
  verdadero, no falso como en el juego habitual;
- los tamaños de movimiento pueden repetirse, y un movimiento mayor que
  el montón no está permitido.

Las respuestas se comprobaron con una búsqueda memorizada en el juego,
guiada por una pila explícita desde `n` hacia abajo.

## Notas por lenguaje

- Python quita los tamaños repetidos con `set` antes del bucle.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1087_games.cpp](1087_games.cpp) | G++ 13.2 x64 | games | O(n·m) | AC | 0.015 s | 204 KB |
| [1087_games.go](1087_games.go) | Go 1.14 x64 | games | O(n·m) | AC | 0.031 s | 1092 KB |
| [1087_games.java](1087_games.java) | Java 1.8 | games | O(n·m) | AC | 0.109 s | 1652 KB |
| [1087_games.py](1087_games.py) | Python 3.12 x64 | games | O(n·m) | AC | 0.093 s | 568 KB |
| [1087_games.rs](1087_games.rs) | Rust 1.75 x64 | games | O(n·m) | AC | 0.015 s | 228 KB |
