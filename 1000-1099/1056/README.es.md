# 1056. Los centros de un árbol

[Timus 1056](https://acm.timus.ru/problem.aspx?space=1&num=1056) · dificultad 551 · bfs, trees

Problema original de la Academia Estatal de Aviación de Rybinsk.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un árbol de `N` vértices (`2 ≤ N ≤ 10000`) se construye añadiendo vértices
uno a uno: el vértice `i` (para `i = 2 … N`) se une a un vértice anterior
`p_i`. Un centro es un vértice cuya mayor distancia (en aristas) a los
demás vértices es la menor. Imprime todos los centros en orden creciente.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `p_2 … p_N`, uno por línea.

## Salida

Los centros en orden creciente.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1
1
2
2
```

Salida:

```
1 2
```

### Ejemplo 2

Entrada:

```
6
1
2
3
4
5
```

Salida:

```
3 4
```

## Solución

Un árbol tiene uno o dos centros, y son el centro de cualquier camino más
largo (un diámetro): la mayor distancia desde un vértice es al menos la
distancia al extremo más lejano del diámetro, y el vértice central llega a
todos los vértices en medio diámetro; si no, habría un camino más largo.

Un diámetro se obtiene con dos búsquedas en anchura: el vértice `u` más
lejano desde cualquier inicio (el vértice 1) es un extremo de algún camino
más largo, y el vértice `v` más lejano desde `u` es el otro extremo. Al
volver desde `v` por los predecesores de la búsqueda se obtiene el camino
de longitud `D`; sus vértices número `D / 2` y `(D + 1) / 2` contando
desde `v` son los centros: un vértice si `D` es par, dos vecinos si es
impar. `O(N)`.

Detalles a tener en cuenta:

- si hay dos centros, se imprimen ambos, en orden creciente;
- `N = 2`: los dos vértices son centros;
- el árbol puede ser un camino de 10000 vértices, así que una búsqueda
  recursiva puede ser demasiado profunda; la búsqueda en anchura no usa
  recursión.

Otra forma es quitar todas las hojas capa a capa hasta que queden uno o
dos vértices; las pruebas se comprobaron así y, para árboles pequeños, con
las distancias desde cada vértice.

## Notas por lenguaje

- Todos los lenguajes hacen las mismas dos búsquedas en anchura con un
  arreglo como cola.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1056_bfs.cpp](1056_bfs.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.015 s | 596 KB |
| [1056_bfs.go](1056_bfs.go) | Go 1.14 x64 | bfs | O(N) | AC | 0.015 s | 2964 KB |
| [1056_bfs.java](1056_bfs.java) | Java 1.8 | bfs | O(N) | AC | 0.093 s | 2536 KB |
| [1056_bfs.py](1056_bfs.py) | Python 3.12 x64 | bfs | O(N) | AC | 0.078 s | 3088 KB |
| [1056_bfs.rs](1056_bfs.rs) | Rust 1.75 x64 | bfs | O(N) | AC | 0.015 s | 1380 KB |
