# 1109. El menor número de aristas que tocan todos los vértices de un grafo bipartito

[Timus 1109](https://acm.timus.ru/problem.aspx?space=1&num=1109) · dificultad 250 · matching

Problema original de la Olimpiada Nacional Búlgara de Informática, primer día.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo bipartito tiene `M` vértices a la izquierda y `N` a la derecha
(`M, N ≤ 1000`) y `K` aristas, cada una entre un vértice izquierdo y uno
derecho; todo vértice tiene al menos una arista. Halla el menor número de
aristas tal que todo vértice sea extremo de al menos una arista elegida.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`M N K` y luego `K` líneas `a b`: una arista entre el vértice izquierdo
`a` y el vértice derecho `b`. Las aristas pueden repetirse.

## Salida

El menor número de aristas.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2 4
1 1
2 1
3 1
3 2
```

Salida:

```
3
```

## Solución

Es un recubrimiento mínimo por aristas, y su tamaño es `M + N − ν`, donde
`ν` es el tamaño de un emparejamiento máximo. Dado un emparejamiento
máximo, se añade para cada vértice no emparejado una arista cualquiera
suya: `ν + (M + N − 2ν)` aristas. En sentido contrario, en un
recubrimiento mínimo cada arista tiene un extremo cubierto solo por ella,
así que el recubrimiento es un conjunto de estrellas; tomando una arista
de cada estrella sale un emparejamiento de `M + N − |recubrimiento|`
aristas, de modo que ningún recubrimiento puede ser menor.

El emparejamiento máximo se halla con Hopcroft–Karp: un BFS desde todos
los vértices izquierdos libres divide el grafo en capas, después un DFS a
lo largo de las capas aumenta por caminos mínimos disjuntos en vértices,
y las fases se repiten mientras exista un camino de aumento.
`O(K √(M + N))`.

Detalles a tener en cuenta:

- el emparejamiento no es la respuesta por sí solo: los vértices no
  emparejados aún necesitan una arista cada uno;
- un emparejamiento voraz, que toma la primera pareja libre, puede quedar
  corto, como en las pruebas en escalera;
- con hasta un millón de aristas y medio segundo, buscar un camino de
  aumento simple desde cada vértice puede ser demasiado lento, y también
  una lectura lenta.

Las respuestas se comprobaron con una fuerza bruta sobre todos los
subconjuntos de aristas en cientos de grafos pequeños y con el
emparejamiento simple de Kuhn por caminos de aumento en los grandes.

## Notas por lenguaje

- C++, Java y Rust buscan los caminos de aumento de forma recursiva;
  Python los recorre con una pila explícita.
- Go y Java leen los números con sus propios lectores de bytes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1109_matching.cpp](1109_matching.cpp) | G++ 13.2 x64 | matching | O(K √(M + N)) | AC | 0.062 s | 468 KB |
| [1109_matching.go](1109_matching.go) | Go 1.14 x64 | matching | O(K √(M + N)) | AC | 0.015 s | 2512 KB |
| [1109_matching.java](1109_matching.java) | Java 1.8 | matching | O(K √(M + N)) | AC | 0.125 s | 1264 KB |
| [1109_matching.py](1109_matching.py) | Python 3.12 x64 | matching | O(K √(M + N)) | AC | 0.093 s | 8516 KB |
| [1109_matching.rs](1109_matching.rs) | Rust 1.75 x64 | matching | O(K √(M + N)) | AC | 0.015 s | 1820 KB |
