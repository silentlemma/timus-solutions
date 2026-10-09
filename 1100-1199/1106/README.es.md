# 1106. Dividir un grafo de modo que cada vértice tenga un vecino al otro lado

[Timus 1106](https://acm.timus.ru/problem.aspx?space=1&num=1106) · dificultad 74 · bfs

Problema original de Dmitry Filimonenkov, del Tetrahedron Team Contest, mayo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo no dirigido tiene `N ≤ 100` vértices, y cada vértice tiene al
menos un vecino. Divide los vértices en dos grupos de modo que cada
vértice tenga un vecino en el otro grupo. Imprime `0` si es imposible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas: la línea `i` enumera los vecinos del vértice `i`
y termina en `0`. Las listas son simétricas.

## Salida

El tamaño del primer grupo y, en la segunda línea, sus vértices
separados por espacios simples.

## Evaluación

Se acepta cualquier división válida. El comprobador verifica que los
vértices listados son distintos y coinciden con el tamaño, y que cada
vértice, esté o no en el primer grupo, tiene un vecino al otro lado.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
2 3 0
3 1 0
1 2 4 5 0
3 0
3 0
7 0
6 0
```

Salida:

```
4
1 4 5 6
```

## Solución

Siempre existe una división, así que nunca se imprime `0`. Se lanza un
BFS desde cada vértice aún no alcanzado y cada vértice va al grupo que da
la paridad de su profundidad en el árbol del BFS. Un vértice que no es
raíz queda al otro lado de su padre; una raíz tiene al menos un vecino, y
ese vecino es su hijo en el árbol, a profundidad 1. Solo importan las
aristas del árbol, así que los ciclos impares no molestan. `O(N + M)`
para `M` amistades.

Detalles a tener en cuenta:

- no es una comprobación de bipartición: un triángulo no se puede
  colorear bien con dos colores, pero se divide sin problema como un
  vértice contra dos;
- el grafo puede tener varias componentes, y cada una necesita su propia
  raíz de BFS.

Las respuestas se comprobaron con el comprobador en todas las pruebas y
en cientos de grafos aleatorios de las cuatro formas del generador.

## Notas por lenguaje

- Rust toma cada lista con `take_while` sobre un iterador de tokens
  compartido.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1106_bfs.cpp](1106_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + M) | AC | 0.015 s | 272 KB |
| [1106_bfs.go](1106_bfs.go) | Go 1.14 x64 | bfs | O(N + M) | AC | 0.031 s | 1480 KB |
| [1106_bfs.java](1106_bfs.java) | Java 1.8 | bfs | O(N + M) | AC | 0.125 s | 748 KB |
| [1106_bfs.py](1106_bfs.py) | Python 3.12 x64 | bfs | O(N + M) | AC | 0.093 s | 964 KB |
| [1106_bfs.rs](1106_bfs.rs) | Rust 1.75 x64 | bfs | O(N + M) | AC | 0.031 s | 296 KB |
