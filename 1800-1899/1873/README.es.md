# 1873. Crónicas de GOV

[Timus 1873](https://acm.timus.ru/problem.aspx?space=1&num=1873) · dificultad 366 · implementation

Problema original de Mikhail Rubinchik, del Concurso Regional Escolar de Programación de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El enunciado cuenta la larga historia del equipo Alarm, luego
Team.GOV, concurso a concurso, con cada cambio de alineación. Los
jugadores están numerados de 0 a 13. Dado el número de un jugador, hay
que escribir en cuántos concursos jugó con el equipo. La ronda de
calentamiento del último campeonato de los Urales no cuenta.

## Entrada

Un número de jugador de 0 a 13.

## Salida

El número de concursos que el jugador jugó con el equipo.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
21
```

### Ejemplo 2

Entrada:

```
11
```

Salida:

```
0
```

## Solución

Todo el trabajo está en leer la historia con cuidado; el programa solo
consulta una tabla. Los concursos y sus alineaciones, en orden:

| Concursos | Jugadores |
| --- | --- |
| Alarm: universidad, cuartos de final, semifinal, Urales, Tartaristán | 0, 1, 2 |
| universidad, otoño de 2008 | 1, 2 |
| cuartos de final | 1, 2, 3 |
| semifinal | 1, 2, 4 |
| selección para el campeonato de los Urales | 1, 2, 5 |
| campeonato de los Urales | 1, 5 |
| cuartos de final, universidad, semifinal | 1, 2, 6 |
| Batalla de generaciones | 1, 6, 7 |
| selección para el campeonato de los Urales | 5, 6 |
| campeonato de los Urales | 1, 5, 6 |
| universidad, cuartos de final, olimpiada de toda Siberia, semifinal | 1, 8, 9 |
| el último campeonato de los Urales | 1, 3, 10 |
| SWERC | 1, 12, 13 |

Al sumar salen 5, 21, 12, 2, 1, 4, 6, 1, 4, 4, 1, 0, 1, 1 concursos
para los jugadores 0 a 13. `O(1)`.

Trampas:

- el jugador 11 solo participó en la ronda de calentamiento, así que la
  respuesta es 0;
- algunos concursos los jugaron dos personas: el campeonato
  universitario de 2008 sin el jugador 3, un campeonato de los Urales
  sin el jugador 2 y una selección sin el jugador 1;
- el SWERC del final de la historia también cuenta.

La tabla coincide con una implementación aceptada independiente para
los catorce jugadores.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1873_implementation.cpp](1873_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 128 KB |
| [1873_implementation.go](1873_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1072 KB |
| [1873_implementation.java](1873_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1584 KB |
| [1873_implementation.py](1873_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 388 KB |
| [1873_implementation.rs](1873_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 240 KB |
