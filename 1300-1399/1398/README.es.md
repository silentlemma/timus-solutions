# 1398. Alfil y peón

[Timus 1398](https://acm.timus.ru/problem.aspx?space=1&num=1398) · dificultad 860 · games

Problema original de Magaz Asanov, de la ronda de prueba del Campeonato de los Urales de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un alfil blanco y un peón negro en una fila de la 2 a la 7 están en un
tablero de ajedrez y se mueven con las reglas habituales, empezando las
blancas. Las negras ganan si el peón se convierte en una dama que el
alfil no puede capturar en la jugada inmediata. Hay tablas si mueven
las negras y el peón no puede moverse. En los demás casos ganan las
blancas. Hay que imprimir el resultado con el mejor juego.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La casilla del alfil y luego la del peón, en notación de ajedrez.

## Salida

WHITE, DRAW o BLACK.

## Ejemplos

### Ejemplo 1

Entrada:

```
a1
c2
```

Salida:

```
WHITE
```

## Solución

El peón avanza en cada turno de las negras, así que una partida dura a
lo sumo una docena de jugadas, y un minimax sobre (alfil, peón, turno)
con memoria cubre los 64·64·2 estados. Las blancas prueban cada jugada
del alfil por las cuatro diagonales hasta el borde o el peón, y capturar
el peón gana al momento. Las negras eligen el peor resultado para las
blancas entre:

- un paso adelante, o dos desde la fila 7, a casillas vacías;
- llegar a la fila 1: las blancas ganan solo si el alfil ve a la dama;
- capturar el alfil en diagonal, tras lo cual nada detiene al peón.

Sin ninguna jugada, el peón está bloqueado y hay tablas. `O(1)`, con a
lo sumo 8 192 estados.

Detalles a tener en cuenta:

- el peón baja por el tablero, hacia la fila 1;
- de las 3 024 posiciones iniciales solo cuatro son tablas: a2 b2, b1 a3,
  g1 h3 y h2 g2 (pruebas 02 a 05);
- las negras solo ganan desde la fila 2, cuando la dama aparece en una
  casilla del otro color o fuera de alcance (pruebas 06 y 07);
- el paso doble y la duda de si capturar el alfil cuenta como derrota de
  las blancas nunca cambian un resultado, porque las blancas nunca
  necesitan entregar el alfil.

Dos de las soluciones se compararon en las 3 024 posiciones iniciales, y
las cuatro tablas coinciden con el número dado en el foro.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1398_games.cpp](1398_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 152 KB |
| [1398_games.go](1398_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.031 s | 1148 KB |
| [1398_games.java](1398_games.java) | Java 1.8 | games | O(1) | AC | 0.125 s | 1632 KB |
| [1398_games.py](1398_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.109 s | 684 KB |
| [1398_games.rs](1398_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 432 KB |
