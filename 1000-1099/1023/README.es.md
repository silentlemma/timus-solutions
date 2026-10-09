# 1023. Elegir el límite de jugada que hace ganar al segundo jugador

[Timus 1023](https://acm.timus.ru/problem.aspx?space=1&num=1023) · dificultad 217 · games, number_theory

Problema original de la Segunda Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 7 de octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos jugadores retiran por turnos de 1 a `L` botones de un montón de `K`
botones; gana quien toma el último. El primer jugador ha elegido `K`
(`3 ≤ K ≤ 10^8`); ahora el segundo elige `L` con `2 ≤ L < K`. Encuentra el
menor `L` con el que el segundo jugador gana contra cualquier juego del
primero, o imprime 0 si no existe.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`K`.

## Salida

El menor `L` ganador, o 0.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
35
```

Salida:

```
4
```

## Solución

**El juego.** Con jugadas de 1 a `L` botones, las posiciones en que pierde
quien mueve son exactamente los múltiplos de `L + 1`: desde un montón así
cualquier jugada deja un no múltiplo, y desde un no múltiplo la jugada que
quita `n mod (L + 1)` botones deja un múltiplo. Así que el segundo jugador
gana exactamente cuando `L + 1` divide a `K`.

**La elección de L.** Se busca el menor `L ≥ 2` con `L + 1 | K`, es decir,
el menor divisor `d ≥ 3` de `K`, y `L = d - 1`; la condición `L < K` es
`d ≤ K`. Como `d = K` siempre sirve (`K ≥ 3`), la respuesta nunca es 0.

**Encontrar d rápido.** Se prueba `d = 3, 4, ...` mientras `d^2 ≤ K`. Si
ninguno divide a `K`, el menor divisor por encima de `sqrt(K)` es `K / j`
para el mayor divisor `j ≤ sqrt(K)`, y los únicos divisores hasta `sqrt(K)`
que quedan son 1 y 2. Así que `d = K / 2` si `K` es par y `K / 2 ≥ 3`, y si
no `d = K`. Como mucho `sqrt(10^8) = 10^4` pasos.

Detalles a tener en cuenta:

- `K = 4`: el divisor 2 es pequeño y `K / 2 = 2` también, así que `d = 4`,
  `L = 3`;
- `K = 2p` con `p` primo: el divisor `p` está por encima de `sqrt(K)` y no
  hay que perderlo;
- probar todos los `L` hasta `K` son `10^8` pasos: bien en C++, demasiado
  lento en Python.

## Notas por lenguaje

La misma búsqueda de divisores en todos los lenguajes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1023_games_number_theory.cpp](1023_games_number_theory.cpp) | G++ 13.2 x64 | games, number_theory | O(sqrt(K)) | AC | 0.015 s | 128 KB |
| [1023_games_number_theory.go](1023_games_number_theory.go) | Go 1.14 x64 | games, number_theory | O(sqrt(K)) | AC | 0.031 s | 1072 KB |
| [1023_games_number_theory.java](1023_games_number_theory.java) | Java 1.8 | games, number_theory | O(sqrt(K)) | AC | 0.109 s | 1576 KB |
| [1023_games_number_theory.py](1023_games_number_theory.py) | Python 3.12 x64 | games, number_theory | O(sqrt(K)) | AC | 0.078 s | 400 KB |
| [1023_games_number_theory.rs](1023_games_number_theory.rs) | Rust 1.75 x64 | games, number_theory | O(sqrt(K)) | AC | 0.015 s | 220 KB |
