# 1471. Distancia en el árbol

[Timus 1471](https://acm.timus.ru/problem.aspx?space=1&num=1471) · dificultad 163 · trees

Problema original de Dmitry Zhukov, del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un árbol tiene n vértices (1 ≤ n ≤ 50000), numerados de 0 a n − 1, y
n − 1 aristas con peso (de 0 a 1000). Para cada una de m preguntas
(1 ≤ m ≤ 75000) hay que escribir la longitud del camino entre dos
vértices dados.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n, luego las aristas como u v w, luego m y los pares de vértices.

## Salida

Una distancia por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 0 1
2 0 1
3
0 1
0 2
1 2
```

Salida:

```
1
1
2
```

## Solución

Se cuelga el árbol del vértice 0 y se guarda la distancia de cada
vértice a la raíz. El camino entre a y b sube hasta su ancestro común
más bajo, así que su longitud es dist(a) + dist(b) − 2·dist(lca). El
ancestro sale del recorrido de Euler: un recorrido en profundidad que
escribe un vértice al entrar en él y otra vez tras cada hijo. Entre las
primeras apariciones de a y b el recorrido pasa por su ancestro común y
no sube más, así que el ancestro es el vértice menos profundo de ese
tramo. Una tabla dispersa de mínimos sobre tramos de longitud 2^k lo
resuelve con dos consultas que se solapan. `O(n log n)` para
construirla, `O(1)` por pregunta.

Detalles a tener en cuenta:

- un camino de 50000 vértices es demasiado profundo para la recursión en
  la mayoría de los lenguajes, así que el recorrido lleva su propia pila
  (gen3);
- el vértice 0 puede ser una hoja y las aristas vienen en cualquier
  sentido (prueba 03);
- un único vértice no tiene aristas y una pregunta puede nombrar dos
  veces el mismo vértice (prueba 02).

## Soluciones optimizadas

La solución optimizada en C++ halla el ancestro con caminos pesados en
lugar del recorrido de Euler. Un recorrido en anchura desde el vértice 0
da padres, profundidades y distancias sin recursión ni pila; después los
tamaños de los subárboles se suman en orden inverso, el hijo pesado de
cada vértice es el hijo con el subárbol más grande y las aristas pesadas
forman cadenas, y cada vértice recuerda la cima de su cadena. Para una
pregunta, el vértice cuya cima de cadena es más profunda salta al padre
de esa cima hasta que ambos quedan en una misma cadena, y el menos
profundo de los dos es el ancestro. Cada salto cruza una arista ligera,
lo que al menos duplica el tamaño del subárbol, así que una pregunta
cuesta `O(log n)` saltos, y cada arreglo tiene `n` elementos en lugar de
la tabla dispersa de `O(n log n)`. Los números se analizan a mano desde
un búfer de 4 KB que se rellena con `fread`: {1471_trees_bfs.cpp}.

La solución optimizada en Go conserva el recorrido de Euler y la tabla
dispersa, pero analiza los dígitos a mano desde un lector `bufio` de
1 MB en lugar de `fmt.Fscan`, y guarda las listas de adyacencia de las
dos direcciones de cada arista en arreglos planos indexados por el
inicio de cada vértice en lugar de un slice de structs de aristas por
vértice: {1471_trees_optimized.go}.

La solución optimizada en Go con la etiqueta `bfs` halla el ancestro con
caminos pesados en lugar del recorrido de Euler. Un recorrido en anchura
desde el vértice 0 da padres, profundidades y distancias sin recursión
ni pila; después los tamaños de los subárboles se suman en orden
inverso, el hijo pesado de cada vértice es el hijo con el subárbol más
grande y las aristas pesadas forman cadenas, y cada vértice recuerda la
cima de su cadena. Para una pregunta, el vértice cuya cima de cadena es
más profunda salta al padre de esa cima hasta que ambos quedan en una
misma cadena, y el menos profundo de los dos es el ancestro. Cada salto
cruza una arista ligera, lo que al menos duplica el tamaño del subárbol,
así que una pregunta cuesta `O(log n)` saltos, y cada arreglo tiene `n`
elementos en lugar de la tabla dispersa de `O(n log n)`. Los números se
analizan a mano desde un búfer de 4 KB leído de la entrada estándar:
{1471_trees_bfs.go}.

La solución optimizada en Java con la etiqueta `bfs` halla el ancestro
con caminos pesados en lugar del recorrido de Euler. Un recorrido en
anchura desde el vértice 0 da padres, profundidades y distancias sin
recursión ni pila; después los tamaños de los subárboles se suman en
orden inverso, el hijo pesado de cada vértice es el hijo con el subárbol
más grande y las aristas pesadas forman cadenas, y cada vértice recuerda
la cima de su cadena. Para una pregunta, el vértice cuya cima de cadena
es más profunda salta al padre de esa cima hasta que ambos quedan en una
misma cadena, y el menos profundo de los dos es el ancestro. Cada salto
cruza una arista ligera, lo que al menos duplica el tamaño del subárbol,
así que una pregunta cuesta `O(log n)` saltos, y cada arreglo tiene `n`
elementos en lugar de la tabla dispersa de `O(n log n)`. Los números se
analizan a mano desde bloques de 4 KB de la entrada en lugar de
`StreamTokenizer`: {1471_trees_bfs.java}.

La solución optimizada en Python con la etiqueta `bfs` halla el ancestro
con caminos pesados en lugar del recorrido de Euler. Un recorrido en
anchura desde el vértice 0 da padres, profundidades y distancias sin
recursión ni pila; después los tamaños de los subárboles se suman en
orden inverso, el hijo pesado de cada vértice es el hijo con el subárbol
más grande y las aristas pesadas forman cadenas, y cada vértice recuerda
la cima de su cadena. Para una pregunta, el vértice cuya cima de cadena
es más profunda salta al padre de esa cima hasta que ambos quedan en una
misma cadena, y el menos profundo de los dos es el ancestro. Cada salto
cruza una arista ligera, lo que al menos duplica el tamaño del subárbol,
así que una pregunta cuesta `O(log n)` saltos, y cada lista tiene `n`
elementos en lugar de la tabla dispersa de `O(n log n)`. La entrada se
lee en trozos de 4 KB en lugar de línea a línea, las listas de
adyacencia se liberan antes de las preguntas y las respuestas se
escriben en lotes de 1024: {1471_trees_bfs.py}.

La solución optimizada en Rust halla el ancestro con caminos pesados en
lugar del recorrido de Euler. Un recorrido en anchura desde el vértice 0
da padres, profundidades y distancias sin recursión ni pila; después los
tamaños de los subárboles se suman en orden inverso, el hijo pesado de
cada vértice es el hijo con el subárbol más grande y las aristas pesadas
forman cadenas, y cada vértice recuerda la cima de su cadena. Para una
pregunta, el vértice cuya cima de cadena es más profunda salta al padre
de esa cima hasta que ambos quedan en una misma cadena, y el menos
profundo de los dos es el ancestro. Cada salto cruza una arista ligera,
lo que al menos duplica el tamaño del subárbol, así que una pregunta
cuesta `O(log n)` saltos, y cada vector tiene `n` elementos en lugar de
la tabla dispersa de `O(n log n)`. Los números se analizan a mano desde
un búfer de 4 KB en lugar de leer toda la entrada en un `String`, y las
distancias son `i32`, ya que no pasan de 49 999 · 1000 < 5 · 10⁷:
{1471_trees_bfs.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1471_trees_bfs.cpp`: reducción de tiempo +71.56%; reducción de
  memoria +54.89%; base: `1471_trees.cpp`.

- `1471_trees_bfs.go`: reducción de tiempo +68.80%; reducción de memoria
  +61.41%; base: `1471_trees.go`.

- `1471_trees_optimized.go`: reducción de tiempo +62.80%; reducción de
  memoria +13.02%; base: `1471_trees.go`.

- `1471_trees_bfs.java`: reducción de tiempo +8.56%; reducción de
  memoria +32.17%; base: `1471_trees.java`.

- `1471_trees_bfs.py`: reducción de tiempo +61.69%; reducción de memoria
  +42.82%; base: `1471_trees.py`.

- `1471_trees_bfs.rs`: reducción de tiempo +0.00%; reducción de memoria
  +61.97%; base: `1471_trees.rs`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1471_trees.cpp](1471_trees.cpp) | G++ 13.2 x64 | trees | O(n log n + m) | AC | 0.218 s | 9772 KB | 11286556 |
| [1471_trees.go](1471_trees.go) | Go 1.14 x64 | trees | O(n log n + m) | AC | 0.250 s | 24328 KB | 11307211 |
| [1471_trees.java](1471_trees.java) | Java 1.8 | trees | O(n log n + m) | AC | 0.187 s | 18492 KB | 11307212 |
| [1471_trees.py](1471_trees.py) | Python 3.12 x64 | trees | O(n log n + m) | AC | 0.937 s | 44300 KB | 11307213 |
| [1471_trees.rs](1471_trees.rs) | Rust 1.75 x64 | trees | O(n log n + m) | AC | 0.046 s | 22180 KB | 11286571 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1471_trees_bfs.cpp](1471_trees_bfs.cpp) | G++ 13.2 x64 | trees, bfs | O(n + m log n) | AC | 0.062 s | 4408 KB | 11307214 |
| [1471_trees_bfs.go](1471_trees_bfs.go) | Go 1.14 x64 | trees, bfs | O(n + m log n) | AC | 0.078 s | 9388 KB | 11307215 |
| [1471_trees_optimized.go](1471_trees_optimized.go) | Go 1.14 x64 | trees | O(n log n + m) | AC | 0.093 s | 21160 KB | 11307220 |
| [1471_trees_bfs.java](1471_trees_bfs.java) | Java 1.8 | trees, bfs | O(n + m log n) | AC | 0.171 s | 12544 KB | 11307216 |
| [1471_trees_bfs.py](1471_trees_bfs.py) | Python 3.12 x64 | trees, bfs | O(n + m log n) | AC | 0.359 s | 25332 KB | 11307218 |
| [1471_trees_bfs.rs](1471_trees_bfs.rs) | Rust 1.75 x64 | trees, bfs | O(n + m log n) | AC | 0.046 s | 8436 KB | 11307219 |
