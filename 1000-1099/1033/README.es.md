# 1033. El área visible de las paredes de un laberinto

[Timus 1033](https://acm.timus.ru/problem.aspx?space=1&num=1033) · dificultad 237 · bfs, dfs

Problema original de Vladimir Pinaev, del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un laberinto es una cuadrícula `N × N` (`3 ≤ N ≤ 33`) de celdas de 3 × 3
metros: `.` es vacía y `#` es un bloque macizo. El laberinto está rodeado
por un muro exterior, salvo en las celdas superior izquierda e inferior
derecha, que son las dos entradas (siempre vacías). Las paredes miden 3
metros de alto. Un visitante camina entre celdas vacías que comparten un
lado; los bloques que se tocan por una esquina no dejan hueco. Halla el área
total de las superficies de pared que un visitante puede ver desde las
partes del laberinto alcanzables desde las entradas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas de `N` caracteres `.` y `#`.

## Salida

El área de pared visible en metros cuadrados.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
....
.##.
.#..
....
```

Salida:

```
180
```

### Ejemplo 2

Entrada:

```
3
...
...
...
```

Salida:

```
72
```

## Solución

Una superficie de pared se ve exactamente cuando es un lado de una celda
vacía alcanzable que da a un bloque o al muro exterior. Cada uno de esos
lados es un cuadrado de 3 × 3, así que la respuesta es `9 ·` (el número de
esos lados).

Se hace un BFS (o DFS) sobre las celdas vacías, pasando por lados comunes,
empezando desde **ambas** entradas a la vez: pueden llevar a partes
distintas del laberinto. Para cada celda visitada se miran sus cuatro lados:
un lado hacia `#` o más allá del borde es pared visible, un lado hacia una
celda vacía se sigue. Al final se restan los 4 lados que son aberturas:
arriba y a la izquierda de la celda superior izquierda, abajo y a la derecha
de la inferior derecha. `O(N^2)`.

Detalles a tener en cuenta:

- solo cuentan las celdas alcanzables desde una entrada; las salas
  cerradas no se ven;
- empieza desde ambas entradas: el laberinto puede estar partido en dos;
- los vecinos en diagonal no están conectados.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: BFS con una cola.
- **Python**: la misma búsqueda con una pila (DFS); el orden no importa.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1033_bfs.cpp](1033_bfs.cpp) | G++ 13.2 x64 | bfs | O(N^2) | AC | 0.001 s | 416 KB |
| [1033_bfs.go](1033_bfs.go) | Go 1.14 x64 | bfs | O(N^2) | AC | 0.015 s | 1124 KB |
| [1033_bfs.java](1033_bfs.java) | Java 1.8 | bfs | O(N^2) | AC | 0.125 s | 1644 KB |
| [1033_bfs.rs](1033_bfs.rs) | Rust 1.75 x64 | bfs | O(N^2) | AC | 0.015 s | 228 KB |
| [1033_dfs.py](1033_dfs.py) | Python 3.12 x64 | dfs | O(N^2) | AC | 0.078 s | 452 KB |
