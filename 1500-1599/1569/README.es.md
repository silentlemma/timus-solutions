# 1569. Redes en la Iset

[Timus 1569](https://acm.timus.ru/problem.aspx?space=1&num=1569) · dificultad 886 · bfs

Problema original de Sergey Pupyrev, del XII Campeonato de Programación de la Universidad Estatal de los Urales, 6 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un plan conexo une N ≤ 100 nodos con M canales, como mucho uno por par.
Hay que elegir N − 1 de los canales planeados que sigan conectando todos
los nodos de modo que la mayor distancia entre dos nodos sea lo menor
posible, e imprimirlos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, y luego los dos nodos de cada canal planeado.

## Salida

Los canales elegidos, un par de nodos por línea. Se acepta cualquier
red óptima.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
1 2
2 3
2 4
3 4
```

Salida:

```
1 2
2 3
2 4
```

## Solución

Es un árbol generador de diámetro mínimo. El centro de cualquier árbol
es un nodo, cuando el diámetro es par, o el punto medio de un canal,
cuando es impar. Si el mejor árbol tiene diámetro 2r y centro en el
nodo c, todo nodo está a distancia como mucho r de c en ese árbol y por
tanto en el plan, y el árbol de caminos mínimos desde c tiene diámetro
como mucho 2r. Del mismo modo, para diámetro 2r + 1 con el centro en el
canal (a, b), todo nodo está a como mucho r de a o de b, y el árbol de
caminos mínimos que crece desde ambos extremos a la vez, más el propio
canal, tiene diámetro como mucho 2r + 1.

Así que una búsqueda en anchura desde cada nodo da todas las distancias;
cada nodo c puntúa 2·max dist(c, ·), cada canal (a, b) puntúa
2·max min(dist(a, ·), dist(b, ·)) + 1, y el árbol de caminos mínimos
desde el mejor centro es la respuesta. Esto tarda O(N·(N + M)). Los
resultados se contrastaron con probar todos los árboles generadores en
300 planes pequeños aleatorios.

Detalles a tener en cuenta:

- el centro del mejor árbol puede ser un canal, lo que da un diámetro
  impar que ningún centro en un nodo alcanza (prueba 05);
- con el centro en un canal, ese canal debe quedarse en el árbol;
- hay varias redes óptimas, así que un verificador compara la mayor
  distancia y comprueba que cada canal esté en el plan.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1569_bfs.cpp](1569_bfs.cpp) | G++ 13.2 x64 | bfs | O(N (N + M)) | AC | 0.015 s | 424 KB |
| [1569_bfs.go](1569_bfs.go) | Go 1.14 x64 | bfs | O(N (N + M)) | AC | 0.031 s | 2144 KB |
| [1569_bfs.java](1569_bfs.java) | Java 1.8 | bfs | O(N (N + M)) | AC | 0.171 s | 3664 KB |
| [1569_bfs.py](1569_bfs.py) | Python 3.12 x64 | bfs | O(N (N + M)) | AC | 0.218 s | 1576 KB |
| [1569_bfs.rs](1569_bfs.rs) | Rust 1.75 x64 | bfs | O(N (N + M)) | AC | 0.031 s | 584 KB |
