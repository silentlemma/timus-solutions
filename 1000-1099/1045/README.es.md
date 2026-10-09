# 1045. Un juego con una ficha en un árbol de vértices que se queman

[Timus 1045](https://acm.timus.ru/problem.aspx?space=1&num=1045) · dificultad 522 · games, trees

Problema original de Dmitry Filimonenkov, del concurso universitario de programación de la Universidad Estatal de los Urales, 25 de marzo de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un árbol tiene `n` vértices (`n ≤ 1000`, cada vértice tiene como mucho
20 vecinos). Una ficha empieza en el vértice `k`. Dos jugadores mueven por
turnos: un movimiento lleva la ficha por una arista a un vecino, y el
vértice que deja queda destruido para siempre. Pierde quien no puede
mover. Determina quién gana con juego perfecto; si gana el primer jugador,
da el primer movimiento ganador, el vértice menor si hay varios.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` y `k`, y luego `n − 1` líneas con las aristas.

## Salida

`First player wins flying to airport L` con el vértice `L` del primer
movimiento, o `First player loses`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
3 2
3 1
1 4
```

Salida:

```
First player wins flying to airport 2
```

### Ejemplo 2

Entrada:

```
3 1
1 2
2 3
```

Salida:

```
First player loses
```

## Solución

Todos los vértices destruidos están en el camino de `k` a la ficha, así
que el único vecino al que la ficha no puede ir es aquel del que vino.
Cada partida es un descenso por el árbol con raíz en `k`, y la posición
solo depende del vértice actual.

Así que es el análisis clásico de posiciones ganadoras y perdedoras: un
vértice es ganador para quien mueve cuando al menos un hijo es perdedor;
una hoja es perdedora. El primer jugador gana si `k` tiene un hijo
perdedor, y la respuesta es el menor de esos hijos.

El árbol puede ser un camino de 1000 vértices, así que las soluciones
evitan la recursión profunda: un orden en anchura desde `k` pone a los
padres antes que a los hijos, y al recorrerlo al revés se marca a un padre
como ganador en cuanto aparece un hijo perdedor. `O(n)`.

Detalles a tener en cuenta:

- se pide el menor movimiento ganador, no el primero de la entrada;
- `n = 1`: no hay aristas ni movimiento, el primer jugador pierde;
- el primer jugador solo gana moviendo a un hijo *perdedor*; un hijo
  ganador para el siguiente jugador es un mal movimiento.

## Notas por lenguaje

- Todos los lenguajes usan el mismo orden en anchura en lugar de
  recursión.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1045_games.cpp](1045_games.cpp) | G++ 13.2 x64 | games | O(n) | AC | 0.015 s | 252 KB |
| [1045_games.go](1045_games.go) | Go 1.14 x64 | games | O(n) | AC | 0.031 s | 1216 KB |
| [1045_games.java](1045_games.java) | Java 1.8 | games | O(n) | AC | 0.109 s | 716 KB |
| [1045_games.py](1045_games.py) | Python 3.12 x64 | games | O(n) | AC | 0.078 s | 624 KB |
| [1045_games.rs](1045_games.rs) | Rust 1.75 x64 | games | O(n) | AC | 0.015 s | 284 KB |
