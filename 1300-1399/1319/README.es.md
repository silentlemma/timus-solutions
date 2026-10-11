# 1319. Hotel

[Timus 1319](https://acm.timus.ru/problem.aspx?space=1&num=1319) · dificultad 39 · implementation

Problema original de Stanislav Vasiliev, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El casillero de correo de un hotel es un bloque de N × N celdas
(1 ≤ N ≤ 100), numeradas por diagonales: el número 1 está en la esquina
superior derecha, cada diagonal va de arriba abajo, y las diagonales se
suceden hacia la esquina inferior izquierda, donde está N². Hay que
imprimir la tabla numerada.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

N líneas de N números separados por espacios.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
4 2 1
7 5 3
9 8 6
```

## Solución

Las celdas de una misma diagonal tienen la misma diferencia
columna − fila. Recorriendo esa diferencia de N − 1 hasta −(N − 1), y
las filas de cada diagonal desde arriba, las celdas salen en el orden
de la numeración. `O(N²)`.

Detalles a tener en cuenta:

- la primera diagonal es la celda superior derecha sola, no la diagonal
  principal (prueba 01);
- N = 1 es una sola celda con 1 (prueba 02).

## Notas por lenguaje

- Las cinco soluciones llenan la tabla de la misma manera y la imprimen
  al final.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1319_implementation.cpp](1319_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.015 s | 244 KB |
| [1319_implementation.go](1319_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.001 s | 1188 KB |
| [1319_implementation.java](1319_implementation.java) | Java 1.8 | implementation | O(N^2) | AC | 0.093 s | 2008 KB |
| [1319_implementation.py](1319_implementation.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.046 s | 888 KB |
| [1319_implementation.rs](1319_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.001 s | 364 KB |
