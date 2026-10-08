# 1008. Conversión entre dos codificaciones de una figura conexa de píxeles

[Timus 1008](https://acm.timus.ru/problem.aspx?space=1&num=1008) · dificultad 367 · bfs

Problema original del Third Open USTU Collegiate Programming Contest (PhysTech Cup), 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una figura es un conjunto no vacío de píxeles negros con coordenadas
`1 ≤ x, y ≤ 10` que es 4-conexo (los píxeles que comparten un lado son
vecinos). Se puede escribir de dos formas:

1. **Lista**: el número de píxeles y luego una línea `x y` por píxel,
   ordenadas por `x` y después por `y`.
2. **Descripción**: la línea `x y` del píxel *inicial* —el de menor `x` y,
   entre esos, menor `y`— seguida de una línea por píxel en orden de
   búsqueda en anchura desde el inicial. La línea de un píxel enumera, en el
   orden `R` (x+1), `T` (y+1), `L` (x-1), `B` (y-1), aquellos vecinos que aún
   no se han mencionado; se añaden a la cola en ese mismo orden. Cada línea
   salvo la última termina en `,`, la última en `.`.

Dada una codificación, imprime la otra.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Una de las dos codificaciones. Las líneas no tienen espacios al principio ni
al final; `x` e `y` van separados por un espacio.

## Salida

La otra codificación.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
2 5
3 3
3 4
3 5
4 3
5 3
5 4
```

Salida:

```
2 5
R,
B,
B,
R,
R,
T,
.
```

### Ejemplo 2

Entrada:

```
2 5
R,
B,
B,
R,
R,
T,
.
```

Salida:

```
7
2 5
3 3
3 4
3 5
4 3
5 3
5 4
```

## Solución

La descripción *es* una búsqueda en anchura, así que ambas direcciones son la
misma búsqueda.

- **Lista → descripción**: se marcan los píxeles en una cuadrícula, se busca
  el inicial y se ejecuta BFS; para cada píxel extraído se prueban las cuatro
  direcciones en el orden `R T L B`, y cada vecino negro aún no visto se
  marca, se encola y se escribe.
- **Descripción → lista**: se reproduce la búsqueda. La cola empieza con el
  píxel inicial; la línea `i` pertenece al `i`-ésimo píxel de la cola y cada
  letra añade el vecino en esa dirección. Al final la cola contiene todos los
  píxeles; se ordenan por `(x, y)`.

Qué codificación llega: solo la descripción termina en `.`, así que basta con
mirar el último token. Leer tokens separados por espacios en blanco también
resuelve la línea vacía `,` (es un token) y los finales de línea CRLF.

Hay como mucho 100 píxeles, así que todo es `O(100)`; una cuadrícula con un
borde de celdas vacías (índices `0..11`) evita comprobar los límites.

Detalles a tener en cuenta:

- un solo píxel se describe con sus coordenadas y una línea con solo `.`;
- el inicial es el más bajo entre los píxeles *más a la izquierda*, no el más
  bajo de todos;
- un vecino se escribe una sola vez, por el píxel que lo descubre primero.

## Notas por lenguaje

El mismo BFS en todos los lenguajes. La versión en Java, al reproducir la
descripción, rellena una cuadrícula y la imprime columna a columna, lo que da
el orden correcto sin ordenar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1008_bfs.cpp](1008_bfs.cpp) | G++ 13.2 x64 | bfs | O(P log P), P ≤ 100 pixels | AC | 0.015 s | 380 KB |
| [1008_bfs.go](1008_bfs.go) | Go 1.14 x64 | bfs | O(P log P), P ≤ 100 pixels | AC | 0.015 s | 1112 KB |
| [1008_bfs.java](1008_bfs.java) | Java 1.8 | bfs | O(P + W·H) | AC | 0.093 s | 536 KB |
| [1008_bfs.py](1008_bfs.py) | Python 3.12 x64 | bfs | O(P log P), P ≤ 100 pixels | AC | 0.078 s | 624 KB |
| [1008_bfs.rs](1008_bfs.rs) | Rust 1.75 x64 | bfs | O(P log P), P ≤ 100 pixels | AC | 0.046 s | 252 KB |
