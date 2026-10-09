# 1040. Numerar las aristas para que cada vértice vea números coprimos

[Timus 1040](https://acm.timus.ru/problem.aspx?space=1&num=1040) · dificultad 1001 · dfs, constructive

Problema original de Dmitry Filimonenkov, del V Campeonato por Equipos de Programación de la Universidad Estatal de los Urales, octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo no dirigido conexo tiene `N` vértices (`2 ≤ N ≤ 50`) y `M`
aristas (`1 ≤ M ≤ N(N − 1)/2`), sin lazos ni aristas múltiples. Numera las
aristas con `1..M`, cada número una vez, de modo que en cada vértice con
dos o más aristas el máximo común divisor de sus números sea 1. Imprime
`NO` si es imposible.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `M`, y luego `M` líneas con los dos extremos de cada arista.

## Salida

`YES` y, en la línea siguiente, los números de las aristas en el orden de
la entrada; o `NO`.

## Evaluación

Se acepta cualquier numeración válida. El comprobador verifica que la
respuesta sea `YES`, que los números sean una permutación de `1..M` y que
el mcd en cada vértice con al menos dos aristas sea 1.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 6
1 2
2 3
2 4
4 3
5 6
4 5
```

Salida:

```
YES
1 2 4 3 6 5
```

### Ejemplo 2

Entrada:

```
2 1
2 1
```

Salida:

```
YES
1
```

## Solución

La respuesta siempre es `YES`, porque dos números consecutivos son
coprimos. Se hace una búsqueda en profundidad desde cualquier vértice y se
da a cada arista el siguiente número de un contador la primera vez que la
búsqueda la mira, lleve a un vértice nuevo o a uno ya visitado:

```text
dfs(v):
    marcar v
    para cada arista e = (v, w):
        si e no tiene número:
            number[e] = ++counter
            si w no está marcado: dfs(w)
```

Sea `w` un vértice al que se entra por la arista número `k`. Ninguna otra
de sus aristas tiene número todavía: una arista desde un vértice anterior
hacia `w` ya habría llevado la búsqueda a `w`. Entre asignar `k` y llamar a
`dfs(w)` no se numera nada, así que la primera otra arista de `w` recibe
`k + 1`, y `gcd(k, k + 1)` es 1. El vértice inicial recibe el número 1 en
su primera arista. Un vértice con una sola arista no necesita nada.
`O(N + M)`.

Detalles a tener en cuenta:

- las aristas hacia vértices visitados deben numerarse en la misma
  pasada; numerar primero solo las aristas del árbol y el resto después
  rompe el argumento;
- `NO` nunca es la respuesta: el grafo es conexo;
- la respuesta da los números en el orden de las aristas de la entrada.

## Notas por lenguaje

- Todos los lenguajes usan un DFS recursivo; la profundidad es como mucho
  50.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1040_dfs.cpp](1040_dfs.cpp) | G++ 13.2 x64 | dfs | O(N + M) | AC | 0.015 s | 252 KB |
| [1040_dfs.go](1040_dfs.go) | Go 1.14 x64 | dfs | O(N + M) | AC | 0.031 s | 1208 KB |
| [1040_dfs.java](1040_dfs.java) | Java 1.8 | dfs | O(N + M) | AC | 0.093 s | 688 KB |
| [1040_dfs.py](1040_dfs.py) | Python 3.12 x64 | dfs | O(N + M) | AC | 0.078 s | 672 KB |
| [1040_dfs.rs](1040_dfs.rs) | Rust 1.75 x64 | dfs | O(N + M) | AC | 0.031 s | 372 KB |
