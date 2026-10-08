# 1018. Conservar las ramas conexas más valiosas de un árbol binario

[Timus 1018](https://acm.timus.ru/problem.aspx?space=1&num=1018) · dificultad 280 · dp, trees

Problema original del Ural State University Internal Contest '99 #2.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un árbol tiene `N` vértices (`2 ≤ N ≤ 100`) numerados `1..N` con raíz `1`;
cada vértice tiene cero o dos hijos. Cada una de las `N - 1` aristas (ramas)
lleva entre 0 y 30 000 manzanas. Conserva exactamente `Q` ramas
(`1 ≤ Q ≤ N - 1`) de modo que sigan conectadas a la raíz —una rama quitada
se lleva todo lo que hay por encima— y el número de manzanas en las ramas
conservadas sea máximo. Imprime ese número.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `Q`, y luego `N - 1` líneas `a b c`: una rama entre los vértices `a`
y `b` (en cualquier orden) con `c` manzanas.

## Salida

El mayor número de manzanas.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 3
1 2 1
1 3 5
2 4 9
2 5 9
3 6 2
3 7 3
```

Salida:

```
19
```

### Ejemplo 2

Entrada:

```
2 1
2 1 30000
```

Salida:

```
30000
```

## Solución

Las ramas conservadas forman un subárbol que contiene la raíz. Se enraíza el
árbol en 1 (la entrada da las aristas en dirección arbitraria) y se calcula,
para cada vértice `v`, la tabla `best_v[k]`: el máximo de manzanas en `k`
ramas conservadas en el subárbol de `v` y conectadas a `v`.

**Mochila en árbol.** Se empieza con `best = [0]` (nada conservado). Para
cada hijo `c` de `v` con `w` manzanas en la arista `v–c`: conservar `j ≥ 1`
ramas de ese lado significa conservar la propia arista y `j - 1` ramas bajo
`c`, lo que vale `w + best_c[j - 1]`. Se combina con la tabla actual como en
una mochila:

`new[i + j] = max(new[i + j], best[i] + (j = 0 ? 0 : w + best_c[j - 1]))`.

La respuesta es `best_1[Q]`. Cortando cada tabla a `Q + 1` entradas, las
combinaciones cuestan en total `O(N · Q^2)`, como mucho unos `10^6` pasos;
con tablas del tamaño del subárbol es incluso `O(N^2)`.

Por qué se mantiene la conexión: una rama bajo `c` solo se cuenta junto con
la arista `v–c` (el caso `j ≥ 1`), así que ninguna rama conservada queda en
el aire.

Detalles a tener en cuenta:

- una arista puede venir como «hijo padre»: construye una lista de
  adyacencia no dirigida y enraízala con una DFS desde 1;
- elegir con voracidad la rama disponible más pesada falla: una rama ligera
  puede llevar a otras pesadas.

## Notas por lenguaje

La misma DFS recursiva en todos los lenguajes; la profundidad es como mucho
100.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1018_dp_trees.cpp](1018_dp_trees.cpp) | G++ 13.2 x64 | dp, trees | O(N · Q^2) | AC | 0.015 s | 212 KB |
| [1018_dp_trees.go](1018_dp_trees.go) | Go 1.14 x64 | dp, trees | O(N · Q^2) | AC | 0.031 s | 1152 KB |
| [1018_dp_trees.java](1018_dp_trees.java) | Java 1.8 | dp, trees | O(N · Q^2) | AC | 0.140 s | 1912 KB |
| [1018_dp_trees.py](1018_dp_trees.py) | Python 3.12 x64 | dp, trees | O(N · Q^2) | AC | 0.078 s | 596 KB |
| [1018_dp_trees.rs](1018_dp_trees.rs) | Rust 1.75 x64 | dp, trees | O(N · Q^2) | AC | 0.015 s | 260 KB |
