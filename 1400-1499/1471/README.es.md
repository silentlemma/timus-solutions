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

## Notas por lenguaje

- Python guarda todos los números de la entrada y las filas de la tabla
  dispersa en `array` planos y libera las palabras de la entrada antes de
  construir las tablas: con listas de enteros de Python superaba el
  límite de 64 MB en la prueba 14 del juez. Ahora tarda 0,67 s y 44 MB.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1471_trees.cpp](1471_trees.cpp) | G++ 13.2 x64 | trees | O(n log n + m) | AC | 0.218 s | 9772 KB |
| [1471_trees.go](1471_trees.go) | Go 1.14 x64 | trees | O(n log n + m) | AC | 0.078 s | 21144 KB |
| [1471_trees.java](1471_trees.java) | Java 1.8 | trees | O(n log n + m) | AC | 0.140 s | 13228 KB |
| [1471_trees.py](1471_trees.py) | Python 3.12 x64 | trees | O(n log n + m) | AC | 0.671 s | 43868 KB |
| [1471_trees.rs](1471_trees.rs) | Rust 1.75 x64 | trees | O(n log n + m) | AC | 0.046 s | 22180 KB |
