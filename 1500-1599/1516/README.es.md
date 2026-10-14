# 1516. Nostalgia

[Timus 1516](https://acm.timus.ru/problem.aspx?space=1&num=1516) · dificultad 1767 · backtracking

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tablero de damas de 8 × 8 tiene de 1 a 12 fichas blancas y de 1 a
12 negras, todas en casillas de un mismo color. Una ficha captura en
diagonal, en cualquier sentido, una ficha enemiga contigua si esta no
está en el borde y la casilla justo detrás está libre: salta allí, y la
ficha capturada sale del tablero en el acto. Un movimiento puede
encadenar cualquier número de capturas. Hay que hallar el menor número
de fichas de cualquier color que retirar para que luego alguna ficha
blanca capture todas las negras restantes en un solo movimiento. No hay
damas, ni siquiera en las filas de coronación.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las 8 filas del tablero desde arriba: 'W' blanca, 'B' negra, '.' vacía.

## Salida

El menor número de fichas que retirar.

## Ejemplos

### Ejemplo 1

Entrada:

```
W.......
.W......
..B...B.
.....W..
..B.B...
........
........
........
```

Salida:

```
1
```

## Solución

Retirar todas las fichas negras siempre funciona, así que la respuesta
es como mucho su número. Si no, alguna ficha blanca hace una cadena de
capturas; se prueban todas con una búsqueda en profundidad desde cada
ficha blanca. La ficha que captura deja libre su casilla. En la cadena,
una ficha blanca en una casilla de aterrizaje hay que retirarla y
cuesta uno, y una ficha negra en una casilla de aterrizaje también hay
que retirarla, con lo que queda sin capturar. Toda ficha negra que la
cadena no captura hay que retirarla, así que cada punto de la búsqueda
da el coste (blancas retiradas) + (negras) − (negras capturadas). Cada
salto captura una negra distinta, así que las cadenas tienen como mucho
12 saltos, y en la práctica la búsqueda es mínima. El tablero se guarda
en máscaras de 64 bits.

Detalles a tener en cuenta:

- las negras del borde no se pueden capturar, así que hay que
  retirarlas; si están todas allí, la respuesta es su número (prueba 02,
  gen4);
- una ficha de cualquier color en una casilla de aterrizaje hay que
  retirarla (pruebas 04, 05);
- las capturadas salen en el acto y la casilla de salida queda libre,
  así que una cadena puede dar la vuelta y volver adonde empezó
  (prueba 06);
- las fichas pueden estar en las casillas claras (prueba 07);
- hay que probar cada ficha blanca (prueba 08).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1516_backtracking.cpp](1516_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(W * 4^B) | AC | 0.015 s | 380 KB |
| [1516_backtracking.go](1516_backtracking.go) | Go 1.14 x64 | backtracking | O(W * 4^B) | AC | 0.031 s | 1072 KB |
| [1516_backtracking.java](1516_backtracking.java) | Java 1.8 | backtracking | O(W * 4^B) | AC | 0.109 s | 496 KB |
| [1516_backtracking.py](1516_backtracking.py) | Python 3.12 x64 | backtracking | O(W * 4^B) | AC | 0.093 s | 784 KB |
| [1516_backtracking.rs](1516_backtracking.rs) | Rust 1.75 x64 | backtracking | O(W * 4^B) | AC | 0.015 s | 224 KB |
