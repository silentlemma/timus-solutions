# 1195. Quién gana una partida inacabada de tres en raya

[Timus 1195](https://acm.timus.ru/problem.aspx?space=1&num=1195) · dificultad 260 · games

Problema original de Leonid Volkov y Oleg Kats, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tablero de tres en raya de 3×3 tiene exactamente tres cruces y tres
círculos y todavía ninguna línea completa; las cruces empezaron, así que
ahora les toca a ellas. Hay que hallar el resultado con juego perfecto de
ambos bandos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Tres líneas de `X`, `O` y `#` para una casilla vacía.

## Salida

`Crosses win`, `Ouths win` o `Draw`.

## Ejemplos

### Ejemplo 1

Entrada:

```
XXO
#X#
#OO
```

Salida:

```
Ouths win
```

### Ejemplo 2

Entrada:

```
O#O
#X#
XOX
```

Salida:

```
Draw
```

### Ejemplo 3

Entrada:

```
XX#
XOO
#O#
```

Salida:

```
Crosses win
```

## Solución

Solo quedan tres casillas vacías, así que todo el árbol de juego tiene a
lo sumo `3·2·1` partidas. Lo resuelve un minimax sencillo: el bando que
juega prueba cada casilla vacía; una jugada que completa una línea gana,
y si no, el resultado es el contrario del mejor resultado del rival desde
ahí; un tablero lleno es tablas. `O(1)`.

Detalles a tener en cuenta:

- siempre juegan las cruces, porque ambos bandos han hecho tres jugadas;
- la comprobación de línea completa debe mirar la marca recién puesta, no
  las dos;
- la respuesta para los círculos se escribe `Ouths win`.

Las respuestas se compararon con una solución escrita aparte en los 1372
tableros con tres cruces, tres círculos y ninguna línea completa.

## Notas por lenguaje

- Todos los lenguajes hacen la misma búsqueda recursiva sobre un arreglo
  de 9 casillas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1195_games.cpp](1195_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 352 KB |
| [1195_games.go](1195_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.015 s | 1084 KB |
| [1195_games.java](1195_games.java) | Java 1.8 | games | O(1) | AC | 0.109 s | 1544 KB |
| [1195_games.py](1195_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.078 s | 528 KB |
| [1195_games.rs](1195_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 212 KB |
