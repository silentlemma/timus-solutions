# 1622. Final de partida

[Timus 1622](https://acm.timus.ru/problem.aspx?space=1&num=1622) · dificultad 3122 · backtracking

Problema original del SPbSU ITMO Contest en el campus de Petrozavodsk, invierno de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Solitario de clavijas en el tablero en cruz de 33 casillas (un cuadrado
de 7 × 7 sin sus esquinas de 2 × 2, columnas A–G, filas 1–7): 32 fichas
ocupan todas las casillas salvo el centro D4. Un movimiento hace saltar
una ficha en horizontal o vertical sobre una ficha vecina hasta una
casilla vacía, y la ficha saltada se retira. Dada una casilla, imprime
31 movimientos que dejen una sola ficha exactamente allí, o
`Impossible`.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

La casilla de la última ficha.

## Salida

31 movimientos `from-to`, uno por línea, o `Impossible`.

## Ejemplos

### Ejemplo 1

Entrada:

```
D4
```

Salida:

```
D2-D4
B3-D3
C1-C3
E1-C1
D3-B3
A3-C3
E3-E1
G3-E3
C4-C2
C1-C3
A4-C4
C4-C2
E4-C4
G4-E4
E4-E2
E1-E3
C5-C3
C2-C4
A5-C5
D5-B5
E6-E4
G5-E5
C7-C5
C4-C6
E7-C7
C7-C5
B5-D5
D5-F5
E3-E5
F5-D5
D6-D4
```

### Ejemplo 2

Entrada:

```
D3
```

Salida:

```
Impossible
```

## Solución

Qué casillas son posibles se deduce de un invariante. Dividimos las
casillas en tres clases según (r + c) mod 3. Un salto involucra tres
casillas consecutivas de una línea, una de cada clase, y cambia en uno la
cantidad de fichas de cada clase, así que las tres paridades se invierten.
Lo mismo vale para las clases de (r − c) mod 3. Tras 31 saltos las
paridades están fijadas, lo que fija ambos restos de la última ficha, y
con ellos r y c módulo 3: deben coincidir con el centro, que es
alcanzable. En el tablero solo quedan D4, D1, D7, A4 y G4; cualquier otra
casilla es `Impossible`.

Los movimientos salen de una búsqueda en profundidad sobre el tablero
como máscara de 33 bits, que recuerda las posiciones ya halladas sin
salida. Buscar D4 o D7 lleva una fracción de segundo, mientras que D1
directamente tarda mucho más; pero la posición inicial es simétrica, así
que A4, D1 y G4 son D7 girada por cuartos de vuelta: se busca D7 y se
gira cada movimiento de la respuesta.

Detalles a tener en cuenta:

- los movimientos del ejemplo son solo una respuesta; un verificador
  reproduce los movimientos;
- una casilla junto al centro (D3) ya es imposible.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1622_backtracking.cpp](1622_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(S) | AC | 0.015 s | 420 KB |
| [1622_backtracking.go](1622_backtracking.go) | Go 1.14 x64 | backtracking | O(S) | AC | 0.031 s | 1244 KB |
| [1622_backtracking.java](1622_backtracking.java) | Java 1.8 | backtracking | O(S) | AC | 0.109 s | 1952 KB |
| [1622_backtracking.py](1622_backtracking.py) | Python 3.12 x64 | backtracking | O(S) | AC | 0.093 s | 804 KB |
| [1622_backtracking.rs](1622_backtracking.rs) | Rust 1.75 x64 | backtracking | O(S) | AC | 0.046 s | 460 KB |
