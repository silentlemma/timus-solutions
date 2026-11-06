# 1873. Crónicas de GOV

[Timus 1873](https://acm.timus.ru/problem.aspx?space=1&num=1873) · dificultad 365 · implementation

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

## Soluciones optimizadas

Go y Python conservan la misma tabla de catorce cantidades de concursos. Go lee el identificador directamente con un búfer fijo y lo reutiliza para la respuesta. Go usa syscall.Read y syscall.Write con los descriptores estándar y maneja interrupciones y escrituras parciales. La versión para PyPy lee el identificador y escribe la respuesta precodificada con flujos binarios sin búfer, sin formatear texto.

El envío aceptado en PyPy 3.10 x64 tarda 0.14 s frente a 0.078 s de la base y usa 208 KB frente a 388 KB.

Las implementaciones base aceptadas [1873_implementation.cpp](1873_implementation.cpp), [1873_implementation.java](1873_implementation.java), [1873_implementation.rs](1873_implementation.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1873_implementation.cpp](1873_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 128 KB | 11290960 |
| [1873_implementation.go](1873_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1072 KB | 11290961 |
| [1873_implementation.java](1873_implementation.java) \* | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1584 KB | 11290964 |
| [1873_implementation.py](1873_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 388 KB | 11290962 |
| [1873_implementation.rs](1873_implementation.rs) \* | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 240 KB | 11290966 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1873_implementation_optimized.go](1873_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(1) | AC | 0.015 s | 288 KB | 11311200 |
| [1873_implementation_optimized.py](1873_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(1) | AC | 0.14 s | 208 KB | 11311240 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
