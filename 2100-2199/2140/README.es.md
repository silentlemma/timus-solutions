# 2140. Menos pasos, saltos, caídas y subidas por un mapa de vóxeles

[Timus 2140](https://acm.timus.ru/problem.aspx?space=1&num=2140) · dificultad 1161 · bfs

Problema original de Vadim Barinov, del Concurso Escolar de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un mapa de A × B × H cubos unitarios tiene casillas libres y ocupadas.
Un personaje está en una casilla libre sobre un suelo (en la capa más
baja o encima de una casilla ocupada) y se mueve en cuatro direcciones
horizontales con cuatro tipos de movimiento: andar a la vecina, saltar
dos casillas por encima de una casilla intermedia libre con una casilla
libre debajo, bajar a la vecina de una capa inferior y trepar a la
vecina de una capa superior, cada uno con sus reglas sobre qué casillas
deben estar libres. Hallar una sucesión más corta de movimientos del
inicio a la meta, o indicar NO. Se acepta cualquier sucesión más corta.
Los límites son 3 segundos y 256 MB.

## Entrada

A, B y H, cada uno a lo sumo 50, el mapa como H bloques de A líneas de B
caracteres de la capa inferior hacia arriba, y luego el inicio y la meta.

## Salida

NO, o YES, el número de movimientos y los movimientos como "tipo
dirección".

## Evaluación

Un comprobador reproduce los movimientos y compara su número con la
respuesta guardada.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2 1
..
1 1 1
1 2 1
```

Salida:

```
YES
1
walk east
```

### Ejemplo 2

Entrada:

```
3 4 2
.#..
....
.#..
....
....
....
1 1 1
3 4 1
```

Salida:

```
YES
4
climb east
jump south
drop east
walk east
```

## Solución

Todos los movimientos tardan lo mismo, así que es una búsqueda en
anchura sobre las a lo sumo 125 000 casillas donde el personaje puede
estar, con hasta 16 movimientos desde cada una: cuatro tipos en cuatro
direcciones. Cada movimiento comprueba sus casillas exactamente como
dice el enunciado:

- andar: la vecina es una casilla donde se puede estar;
- saltar: la vecina y la casilla bajo ella están libres y la casilla a
  dos pasos es una casilla donde se puede estar;
- bajar: la vecina está libre y la casilla bajo ella es una casilla
  donde se puede estar;
- trepar: la casilla sobre el personaje está libre y su vecina es una
  casilla donde se puede estar.

Un marco de casillas ocupadas alrededor del mapa elimina todas las
comprobaciones de límites, y una casilla está sobre un suelo cuando está
libre y la de debajo está ocupada, contando como ocupado el marco bajo
la capa inferior. La búsqueda recuerda el movimiento que alcanzó primero
cada casilla, y la ruta se lee hacia atrás desde la meta. El trabajo es
O(A B H).

En el segundo ejemplo el personaje trepa al muro, salta sobre la
casilla intermedia libre, baja de nuevo y anda hasta la meta en cuatro
movimientos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2140_bfs.cpp](2140_bfs.cpp) | G++ 13.2 x64 | bfs | O(A B H) | AC | 0.031 s | 1612 KB |
| [2140_bfs.go](2140_bfs.go) | Go 1.14 x64 | bfs | O(A B H) | AC | 0.046 s | 4656 KB |
| [2140_bfs.java](2140_bfs.java) | Java 1.8 | bfs | O(A B H) | AC | 0.125 s | 4964 KB |
| [2140_bfs.py](2140_bfs.py) | Python 3.12 x64 | bfs | O(A B H) | AC | 0.265 s | 9140 KB |
| [2140_bfs.rs](2140_bfs.rs) | Rust 1.75 x64 | bfs | O(A B H) | AC | 0.046 s | 3184 KB |
