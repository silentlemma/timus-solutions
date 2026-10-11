# 1282. Árbol de juego

[Timus 1282](https://acm.timus.ru/problem.aspx?space=1&num=1282) · dificultad 337 · games

Problema original de Sergey Volchenkov, Vladimir Pinaev y Michael Kopachev, del cuarto de final de la región central de Rusia del ACM ICPC 2003–2004, Rybinsk, 15–16 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un juego para dos se da con su árbol de N ≤ 1000 nodos con raíz en el
nodo 1. Se mueve por turnos, empezando en la raíz quien juega primero,
bajando a un hijo. Cada hoja guarda el resultado: +1 si gana quien
juega primero, −1 si gana quien juega segundo, 0 si hay empate. ¿Qué
resultado se alcanza con el mejor juego de ambos?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego, para los nodos 2 a N, `N padre` para un nodo interior o
`L padre resultado` para una hoja.

## Salida

`+1`, `-1` o `0`.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
N 1
N 1
L 2 -1
L 2 +1
L 3 +1
L 3 +1
```

Salida:

```
+1
```

### Ejemplo 2

Entrada:

```
7
N 1
N 1
L 2 -1
L 2 +1
L 3 +1
L 3 0
```

Salida:

```
0
```

### Ejemplo 3

Entrada:

```
18
N 1
N 1
N 2
L 2 +1
N 3
L 3 +1
L 3 +1
L 4 -1
L 4 +1
N 4
N 6
L 6 -1
L 6 -1
L 11 -1
L 11 +1
L 12 +1
L 12 -1
```

Salida:

```
+1
```

## Solución

Es minimax. Quien juega primero mueve en los nodos de profundidad par y
toma el mayor valor de los hijos; quien juega segundo, en los de
profundidad impar, y toma el menor. Un nodo puede aparecer antes que su
padre, así que los valores no se calculan en el orden de la entrada: un
recorrido en anchura desde la raíz da todas las profundidades, y
recorrer ese orden al revés visita a todos los hijos antes que al padre.
`O(N)`.

Detalles a tener en cuenta:

- un padre puede aparecer después de su hijo (prueba 05);
- una cadena de 1000 nodos haría profunda una recursión ingenua
  (prueba 06);
- los resultados se escriben `+1`, con signo más, en la entrada y en la
  salida.

Las respuestas se compararon con un minimax recursivo sencillo en 149
árboles generados.

## Notas por lenguaje

- Todos los lenguajes recorren al revés el mismo orden en anchura.
- Java quita el signo más antes de leer un resultado.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1282_games.cpp](1282_games.cpp) | G++ 13.2 x64 | games | O(N) | AC | 0.015 s | 240 KB |
| [1282_games.go](1282_games.go) | Go 1.14 x64 | games | O(N) | AC | 0.031 s | 1208 KB |
| [1282_games.java](1282_games.java) | Java 1.8 | games | O(N) | AC | 0.140 s | 1656 KB |
| [1282_games.py](1282_games.py) | Python 3.12 x64 | games | O(N) | AC | 0.093 s | 780 KB |
| [1282_games.rs](1282_games.rs) | Rust 1.75 x64 | games | O(N) | AC | 0.015 s | 284 KB |
