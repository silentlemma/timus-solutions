# 1056. Los centros de un árbol

[Timus 1056](https://acm.timus.ru/problem.aspx?space=1&num=1056) · dificultad 552 · bfs, trees

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
todos los vértices en medio diámetro redondeado hacia arriba; si no, habría
un camino más largo.

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

## Soluciones optimizadas

Se procesan los vértices por número decreciente, ya que el padre siempre tiene un número menor. Para cada vértice se guardan la longitud de su rama descendente más larga y su extremo. Al procesar un hijo, se une su rama con la más larga ya procesada a través del padre. La mayor longitud obtenida es el diámetro. Desde el extremo de la rama más larga se sube la mitad del diámetro hasta el centro. Si el diámetro es impar, su padre es el segundo centro. Tiempo y espacio O(N).

Los dos brazos de cualquier camino se encuentran en su vértice más alto. Al procesar el segundo brazo, el algoritmo lo combina con el brazo anterior más largo de ese vértice. El centro del diámetro está en el brazo más largo o en la bifurcación, así que basta con ascender por los padres desde el extremo de ese brazo.

## Notas por lenguaje

Las cinco versiones BFS usan un arreglo como cola. La versión Python de árbol guarda padres y ramas en vez de listas de adyacencia. El envío 11316948 usó 1.532 KB frente a los 3.040 KB de BFS y tardó 0,093 s frente a 0,062 s.

Go guarda los padres, la longitud de la rama descendente más larga y su extremo en arreglos de 16 bits. El envío 11317158 tardó 0,031 s y usó 1196 KB frente a 0,015 s y 2972 KB en BFS.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321750 · Java 1.8 №11321752 · Rust 1.75 x64 №11321755 · Go 1.14 x64 №11322056 · Python 3.12 x64 №11322057.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1056_bfs.cpp](1056_bfs.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.001 s | 580 KB | 11321750 |
| [1056_bfs.go](1056_bfs.go) | Go 1.14 x64 | bfs | O(N) | AC | 0.015 s | 2972 KB | 11322056 |
| [1056_bfs.java](1056_bfs.java) | Java 1.8 | bfs | O(N) | AC | 0.078 s | 2548 KB | 11321752 |
| [1056_bfs.py](1056_bfs.py) | Python 3.12 x64 | bfs | O(N) | AC | 0.062 s | 3040 KB | 11322057 |
| [1056_bfs.rs](1056_bfs.rs) | Rust 1.75 x64 | bfs | O(N) | AC | 0.015 s | 1376 KB | 11321755 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1056_trees.py](1056_trees.py) \* | Python 3.12 x64 | trees | O(N) | AC | 0.093 s | 1532 KB | 11316948 |
| [1056_trees.go](1056_trees.go) | Go 1.14 x64 | trees | O(N) | AC | 0.031 s | 1196 KB | 11317158 |

\* Aceptado; aún no se alcanza la meta de clasificación de Python. El corte de clasificación no contiene envíos comparables en Go de otros autores.
