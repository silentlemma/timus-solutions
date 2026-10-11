# 1298. Caballo

[Timus 1298](https://acm.timus.ru/problem.aspx?space=1&num=1298) · dificultad 233 · backtracking

Problema original del folclore (preparado por Den Raskovalov), de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un tablero N × N (1 ≤ N ≤ 8) hay que encontrar un recorrido del
caballo: un camino de saltos de caballo que pasa por cada casilla
exactamente una vez. Se imprimen las casillas en orden, con una letra
para la columna y un número para la fila, o `IMPOSSIBLE` si no hay
recorrido.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

N² casillas, una por línea, o `IMPOSSIBLE`.

## Evaluación

Se acepta cualquier recorrido correcto. El verificador lee las N²
casillas y comprueba que son todas distintas, que están en el tablero y
que cada una está a un salto de caballo de la anterior. Si no existe
recorrido, la salida debe ser exactamente `IMPOSSIBLE`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
IMPOSSIBLE
```

### Ejemplo 2

Entrada:

```
5
```

Salida:

```
a1
c2
e1
d3
e5
c4
d2
e4
c5
a4
b2
d1
e3
d5
b4
a2
c1
e2
c3
b1
a3
b5
d4
b3
a5
```

## Solución

Una búsqueda en profundidad construye el camino casilla a casilla y
deshace un paso cuando se atasca, probando por turno todas las casillas
de inicio. Por sí sola podría tardar muchísimo en un tablero 8 × 8, así
que las siguientes casillas se prueban en el orden de la regla de
Warnsdorff: primero la casilla con menos casillas libres a un salto más.
Así los callejones sin salida aparecen poco y tarde.

Con este orden la búsqueda nunca tiene que retroceder para N de 5 a 8:
encuentra un recorrido desde a1 en exactamente N² llamadas. Para N = 2,
3 y 4 no hay recorrido, y la búsqueda lo demuestra probando todos los
inicios, lo que cuesta 29 976 llamadas para N = 4. N = 1 es la casilla
única a1. Como las ramas que la regla deja para después se siguen
probando, la respuesta es exacta, no una conjetura heurística.

Detalles a tener en cuenta:

- N = 1 tiene un recorrido de una casilla, a1 (prueba 03);
- el tablero 4 × 4 no tiene recorrido aunque es mayor que el 3 × 3
  (prueba 05);
- el recorrido no tiene que ser cerrado: la última casilla no necesita
  atacar a la primera.

## Notas por lenguaje

- Los cinco lenguajes deshacen los empates en el mismo orden estable,
  así que imprimen los mismos recorridos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1298_backtracking.cpp](1298_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(N^2) for N >= 5 | AC | 0.015 s | 216 KB |
| [1298_backtracking.go](1298_backtracking.go) | Go 1.14 x64 | backtracking | O(N^2) for N >= 5 | AC | 0.015 s | 4468 KB |
| [1298_backtracking.java](1298_backtracking.java) | Java 1.8 | backtracking | O(N^2) for N >= 5 | AC | 0.156 s | 7116 KB |
| [1298_backtracking.py](1298_backtracking.py) | Python 3.12 x64 | backtracking | O(N^2) for N >= 5 | AC | 0.171 s | 544 KB |
| [1298_backtracking.rs](1298_backtracking.rs) | Rust 1.75 x64 | backtracking | O(N^2) for N >= 5 | AC | 0.015 s | 244 KB |
