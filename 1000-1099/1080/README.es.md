# 1080. Colorear un mapa con dos colores

[Timus 1080](https://acm.timus.ru/problem.aspx?space=1&num=1080) · dificultad 190 · bfs, graphs

Problema original de Emil Kelevedzhiev, del Torneo de Informática del Festival Matemático de Invierno, Varna 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un mapa tiene `N` países (`0 < N < 99`); desde cualquier país se llega a
cualquier otro cruzando fronteras. Colorea los países de rojo (0) y azul
(1) de modo que los vecinos siempre difieran, con el país 1 en rojo.
Imprime los colores como una cadena de cifras, o `-1` si no se puede.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas: la línea `i` lista los vecinos del país `i` con
números mayores y termina en 0.

## Salida

La cadena de colores, o `-1`.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
2 0
3 0
0
```

Salida:

```
010
```

## Solución

Un mapa se puede colorear así exactamente cuando su grafo de fronteras es
bipartito. Se lanza una búsqueda en anchura desde el país 1 con color 0 y
cada país nuevo alcanzado recibe el color opuesto al del país desde el
que se llegó. Si alguna frontera une dos países del mismo color, hay un
ciclo impar y la respuesta es `-1`. Como el mapa es conexo, el color del
país 1 fija todos los demás, así que la respuesta es única. `O(N + M)`.

Detalles a tener en cuenta:

- cada línea solo lista los vecinos con números mayores, así que cada
  frontera se añade en los dos sentidos;
- un país sin vecinos de número mayor tiene una línea con solo un 0;
- las cifras se imprimen sin separadores.

Las respuestas se comprobaron con conjuntos disjuntos que guardan la
paridad del camino a la raíz, un método que no recorre el mapa.

## Notas por lenguaje

- Todos los lenguajes leen los vecinos token a token hasta el 0 que
  cierra cada línea.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1080_bfs.cpp](1080_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + M) | AC | 0.001 s | 284 KB |
| [1080_bfs.go](1080_bfs.go) | Go 1.14 x64 | bfs | O(N + M) | AC | 0.031 s | 1364 KB |
| [1080_bfs.java](1080_bfs.java) | Java 1.8 | bfs | O(N + M) | AC | 0.125 s | 5556 KB |
| [1080_bfs.py](1080_bfs.py) | Python 3.12 x64 | bfs | O(N + M) | AC | 0.078 s | 816 KB |
| [1080_bfs.rs](1080_bfs.rs) | Rust 1.75 x64 | bfs | O(N + M) | AC | 0.031 s | 296 KB |
