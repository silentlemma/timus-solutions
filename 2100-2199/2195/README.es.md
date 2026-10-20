# 2195. Convertir un árbol binario en otro pasando por un camino

[Timus 2195](https://acm.timus.ru/problem.aspx?space=1&num=2195) · dificultad 1537 · constructive

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos árboles binarios de N vértices tienen raíz 0. Un movimiento toma un
vértice v que no es la raíz con su subárbol y lo cuelga de un vértice u
fuera de ese subárbol, y el árbol debe seguir siendo binario. Dar a lo
sumo N movimientos que hagan el primer árbol isomorfo al segundo. Los
límites son 1 segundo y 256 MB.

## Entrada

N, 2 ≤ N ≤ 1000, y luego los padres de los vértices 1 … N − 1 en el
primer árbol y en el segundo.

## Salida

El número de movimientos M ≤ N, y luego M líneas v u.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0 1
0 1 2
```

Salida:

```
1
2 3
```

### Ejemplo 2

Entrada:

```
4
2 0 0
0 3 0
```

Salida:

```
2
3 1
1 0
```

## Solución

Todo árbol binario se puede estirar en un camino. Se listan los vértices
en preorden; cuando el siguiente vértice no es hijo del anterior, se
cuelga del anterior. Avanzando en preorden, los vértices ya vistos
forman un camino, y el vértice anterior era una hoja, porque en preorden
un vértice con hijos va seguido de su primer hijo. Así recibe su único
hijo, el árbol sigue siendo binario y el vértice anterior no está dentro
del subárbol movido. Al final el árbol es el camino del preorden.

Solo hay movimiento cuando el vértice anterior es una hoja que no es la
última, así que un árbol con ℓ hojas necesita ℓ − 1 movimientos, y un
árbol binario de N vértices tiene a lo sumo (N + 1) / 2 hojas.

El segundo árbol se estira en su propio camino de la misma forma, y cada
movimiento se puede deshacer colgando el subárbol donde estaba, lo que
mantiene el árbol binario porque restaura un estado anterior. Así la
respuesta son los movimientos del primer árbol, seguidos de los del
segundo en orden inverso, con cada vértice del segundo árbol renombrado
al vértice del primero en el mismo lugar del camino. El total es a lo
sumo N − 1.

En el segundo ejemplo el primer árbol se estira con un movimiento en el
camino 0 → 2 → 1 → 3, y un movimiento deshecho del segundo árbol le da
la forma buscada.

Esto cuesta O(N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2195_constructive.cpp](2195_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 296 KB |
| [2195_constructive.go](2195_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.046 s | 1052 KB |
| [2195_constructive.java](2195_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.109 s | 416 KB |
| [2195_constructive.py](2195_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.125 s | 808 KB |
| [2195_constructive.rs](2195_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 136 KB |
