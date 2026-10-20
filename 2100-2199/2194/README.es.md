# 2194. Menos turnos en un tablero de serpientes donde un seis vuelve a tirar

[Timus 2194](https://acm.timus.ru/problem.aspx?space=1&num=2194) · dificultad 838 · bfs

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ficha empieza en la casilla 1 de un tablero de N casillas. Una
tirada de k la lleva a min(i + k, N); caer en N gana, y caer en una
serpiente de longitud pᵢ la manda a i − pᵢ, quizá sobre otra serpiente.
Un seis permite volver a tirar en el mismo turno. Hallar el menor número
de turnos para ganar si el dado colabora, o −1. Los límites son 1
segundo y 256 MB.

## Entrada

N, 2 ≤ N ≤ 2 · 10⁵, y luego p₂ … p_{N−1} con 0 ≤ pᵢ < i.

## Salida

El menor número de turnos, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
0 1 1 1 1 1 1 0
```

Salida:

```
-1
```

### Ejemplo 2

Entrada:

```
10
1 2 1 2 0 1 1 1
```

Salida:

```
1
```

### Ejemplo 3

Entrada:

```
10
1 1 2 2 0 6 7 8
```

Salida:

```
2
```

## Solución

Las serpientes solo mandan la ficha a la izquierda, así que la casilla
donde termina tras llegar a i se calcula una vez de izquierda a derecha:
land(i) = land(i − pᵢ), o i si no hay serpiente.

Un estado es la casilla donde la ficha está a punto de tirar, con el
número de turnos empezados. Una tirada de uno a cinco acaba el turno, una
arista de peso 1, y un seis lo continúa, una arista de peso 0. Al inicio
hay un turno empezado, y la primera tirada que llega a N da la respuesta
con el número de turnos actual. Una búsqueda en anchura 0-1 con cola
doble trata los dos pesos en O(6N).

En el segundo ejemplo un seis desde la casilla 1 cae en la 7, baja a la
6, y un cuatro desde allí llega a la 10 en el mismo turno.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2194_bfs.cpp](2194_bfs.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.156 s | 2552 KB |
| [2194_bfs.go](2194_bfs.go) | Go 1.14 x64 | bfs | O(N) | AC | 0.156 s | 8952 KB |
| [2194_bfs.java](2194_bfs.java) | Java 1.8 | bfs | O(N) | AC | 0.140 s | 6640 KB |
| [2194_bfs.py](2194_bfs.py) | Python 3.12 x64 | bfs | O(N) | AC | 0.312 s | 21612 KB |
| [2194_bfs.rs](2194_bfs.rs) | Rust 1.75 x64 | bfs | O(N) | AC | 0.046 s | 7656 KB |
