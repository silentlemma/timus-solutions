# 1197. Cuántas casillas ataca un caballo solitario

[Timus 1197](https://acm.timus.ru/problem.aspx?space=1&num=1197) · dificultad 28 · implementation

Problema original del folclore, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un caballo está solo en un tablero de ajedrez. Para cada una de las
`N ≤ 64` casillas dadas, hay que contar cuántas casillas del tablero
ataca el caballo desde ahí.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` casillas en notación de ajedrez: una letra de la `a` a la
`h` para la columna y una cifra del `1` al `8` para la fila.

## Salida

Para cada casilla, el número de casillas atacadas en su propia línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
a1
d4
g6
```

Salida:

```
2
8
6
```

## Solución

El caballo tiene ocho saltos posibles: dos casillas en una dirección y
una en la perpendicular. Se prueban los ocho y se cuentan los que caen
dentro del tablero. `O(N)`.

Detalles a tener en cuenta:

- cerca de un borde o de una esquina solo algunos saltos quedan dentro
  del tablero, así que hay que comprobar las dos coordenadas de cada
  salto;
- la letra es la columna y la cifra la fila, pero el tablero es
  simétrico, así que confundirlas no cambia la respuesta.

Las respuestas se compararon con una solución escrita aparte en las 64
casillas.

## Notas por lenguaje

- Todos los lenguajes guardan los ocho saltos en una tabla y la recorren.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1197_implementation.cpp](1197_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.001 s | 396 KB |
| [1197_implementation.go](1197_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1072 KB |
| [1197_implementation.java](1197_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 1576 KB |
| [1197_implementation.py](1197_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.046 s | 328 KB |
| [1197_implementation.rs](1197_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 216 KB |
