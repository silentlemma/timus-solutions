# 1216. Dos peones y un rey: ¿corona el blanco?

[Timus 1216](https://acm.timus.ru/problem.aspx?space=1&num=1216) · dificultad 2043 · games

Problema original de Leonid Volkov, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un tablero de `N × N`, `6 ≤ N ≤ 26`, hay un peón blanco, un peón negro
y el rey negro, sin rey blanco. Rigen las reglas habituales del ajedrez:
el blanco mueve primero, los peones pueden avanzar dos casillas desde su
fila inicial, el peón negro puede capturar al blanco al paso, el rey
negro no puede estar donde lo ataca el peón blanco, y un peón negro que
llega a la primera fila se convierte en dama, torre, alfil o caballo a
elección del negro. El blanco gana si su peón llega a la última fila; en
cualquier otro caso, incluida una posición en la que el blanco no puede
mover, gana el negro. Hay que decidir quién gana.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego las casillas del peón blanco, del peón negro y del rey
negro, como `h5`.

## Salida

`WHITE WINS` o `BLACK WINS`.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
h5 i5 b3
```

Salida:

```
WHITE WINS
```

### Ejemplo 2

Entrada:

```
8
d5 h6 b6
```

Salida:

```
BLACK WINS
```

## Solución

Se recorre el árbol del juego con memoria. Cada jugada del blanco avanza
el peón blanco al menos una fila, así que ninguna posición se repite y la
búsqueda siempre termina; las posiciones con el blanco al turno se
guardan con su resultado.

El blanco, al mover, tiene como mucho cuatro opciones: un paso adelante,
dos desde la fila inicial o una captura a cualquiera de los lados. Una
jugada que llega a la última fila gana al instante. Un paso doble junto a
un peón negro en la misma fila se pierde por la captura al paso y se
descarta.

El negro, al mover, busca primero una captura: el rey junto al peón
blanco, el peón negro en diagonal delante de él o una pieza coronada que
lo alcanza por una línea libre. Cualquiera de ellas gana para el negro.
Si no, el negro prueba cada paso del rey a una casilla que el peón no
ataca, cada movimiento del peón (con las cuatro coronaciones en la
primera fila y el paso doble desde la fila inicial) y cada movimiento de
una pieza coronada; el blanco gana solo si gana tras todos ellos, y un
negro sin ninguna jugada gana según las reglas. En la práctica salen
decenas de miles de posiciones.

Detalles a tener en cuenta:

- ambos peones pueden avanzar dos casillas desde su fila inicial, pero
  solo el negro puede capturar al paso;
- el rey no puede pisar las dos casillas que ataca el peón blanco, pero
  sí ponerse junto al peón en otro sitio, y entonces amenaza con
  capturarlo;
- las reglas dejan al negro coronar cualquiera de las cuatro piezas, así
  que se prueba cada una en vez de suponer que la dama es la mejor;
- el blanco gana al llegar a la última fila aunque la nueva dama pueda
  ser capturada enseguida.

Las respuestas se compararon con una solución escrita aparte en 200
posiciones aleatorias de todo tipo y en todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes hacen la misma búsqueda con memoria; Python sube el
  límite de recursión, porque la búsqueda baja dos niveles por cada fila
  que sube el peón.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1216_games.cpp](1216_games.cpp) | G++ 13.2 x64 | games | O(positions) | AC | 0.031 s | 1708 KB |
| [1216_games.go](1216_games.go) | Go 1.14 x64 | games | O(positions) | AC | 0.062 s | 8184 KB |
| [1216_games.java](1216_games.java) | Java 1.8 | games | O(positions) | AC | 0.187 s | 8372 KB |
| [1216_games.py](1216_games.py) | Python 3.12 x64 | games | O(positions) | AC | 0.671 s | 6264 KB |
| [1216_games.rs](1216_games.rs) | Rust 1.75 x64 | games | O(positions) | AC | 0.046 s | 2420 KB |
