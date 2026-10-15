# 1715. Another Ball Killer

[Timus 1715](https://acm.timus.ru/problem.aspx?space=1&num=1715) · dificultad 1010 · simulation

Problema original del folclore, preparado por Eugene Krokhalev, de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tablero de n × m está lleno de bolas de cinco colores. Una jugada
quita una figura, un grupo conexo (por lados) de dos o más bolas de un
color, y suma k(k − 1) puntos por k bolas. Las bolas de arriba caen, y
una columna vacía hace que las columnas a su derecha se desplacen a la
izquierda. Un jugador perezoso elige un color principal y repite:
mientras haya alguna figura de otro color, quita la mayor de ellas;
luego quita la mayor figura del color principal, si la hay. En caso de
empate se elige la figura con la bola más baja y, después, la más a la
izquierda de las más bajas. Para cada color presente en el tablero,
imprimir los puntos que obtiene el jugador con ese color principal.

## Entrada

n y m (1 ≤ n, m ≤ 50) y luego n filas de arriba abajo con las letras
B, G, R, W e Y.

## Salida

Para cada color presente, en el orden B, G, R, W, Y, una línea
«color: puntos».

## Ejemplos

### Ejemplo 1

Entrada:

```
3 6
WWWGBG
WBGGGB
GGGGBB
```

Salida:

```
B: 74
G: 92
W: 74
```

## Solución

Se juega tal como se describe. Una búsqueda halla todas las figuras del
tipo pedido (del color principal o no) por recorrido en anchura. Para
cada figura guarda su tamaño y su bola más baja, la más a la izquierda
de la fila más baja, y elige la mejor por tamaño, luego por la fila de
esa bola y luego por su columna. Quitar una figura vacía sus casillas.
Después cada columna se compacta hacia abajo, y las columnas no vacías
hacia la izquierda.

Cada jugada quita al menos dos bolas, así que una partida tiene a lo
sumo nm / 2 jugadas. Cada jugada cuesta una o dos búsquedas por el
tablero, así que una partida lleva `O((nm)²)`, unos pocos millones de
visitas a casillas para 50 × 50, y se juegan hasta cinco partidas.

Trampas:

- el desempate trata de una sola bola: entre las mayores figuras se
  toma la bola más baja de todas y, si una fila tiene varias, la más a
  la izquierda. No es la figura cuya bola más a la izquierda está más
  abajo;
- tras cada eliminación se prueban de nuevo los colores no principales
  antes de la siguiente jugada principal, pues las bolas que caen pueden
  formar figuras nuevas;
- un tablero sin figuras imprime igualmente 0 para cada color presente
  (tests 02 y 03);
- la solución en Python se envía a PyPy: CPython necesita unos 2,5 s en
  un tablero aleatorio de 50 × 50.

Las puntuaciones coinciden con una implementación aceptada
independiente en 300 tableros pequeños aleatorios y en tableros grandes
con dos y cinco colores.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1715_simulation.cpp](1715_simulation.cpp) | G++ 13.2 x64 | simulation | O((nm)²) per colour | AC | 0.531 s | 560 KB |
| [1715_simulation.go](1715_simulation.go) | Go 1.14 x64 | simulation | O((nm)²) per colour | AC | 0.468 s | 7032 KB |
| [1715_simulation.java](1715_simulation.java) | Java 1.8 | simulation | O((nm)²) per colour | AC | 0.453 s | 5256 KB |
| [1715_simulation.py](1715_simulation.py) | PyPy 3.10 x64 | simulation | O((nm)²) per colour | AC | 1.812 s | 9088 KB |
| [1715_simulation.rs](1715_simulation.rs) | Rust 1.75 x64 | simulation | O((nm)²) per colour | AC | 0.906 s | 368 KB |
