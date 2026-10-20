# 2219. Menos vasos cuyas longitudes de paseo sumen hasta cada aula

[Timus 2219](https://acm.timus.ru/problem.aspx?space=1&num=2219) · dificultad 1468 · bfs, greedy

Problema original de Ivan Moskovchenko, de la clasificatoria del Campeonato Regional de los Urales ICPC 2025.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo simple conexo tiene N aulas y M pasillos. El vaso i permite
recorrer exactamente aᵢ pasillos, con repeticiones. Para cada aula v,
hallar el menor número de vasos cuyas longitudes sumen la longitud de
algún recorrido del aula 1 a v, o −1. Los límites son 2.5 segundos y
256 MB.

## Entrada

N, M y K, 2 ≤ N ≤ 10⁵, N − 1 ≤ M ≤ 2 · 10⁵, 1 ≤ K ≤ 10⁵, luego los
pasillos, y luego a₁ … a_K con 1 ≤ aᵢ ≤ 10⁹.

## Salida

Las respuestas de las aulas 1 … N.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 4 4
1 2
2 3
3 4
4 5
1 2 3 4
```

Salida:

```
0 1 1 1 1
```

### Ejemplo 2

Entrada:

```
5 4 2
1 2
2 3
3 4
4 5
1 2
```

Salida:

```
0 1 1 2 -1
```

### Ejemplo 3

Entrada:

```
2 1 1
1 2
999
```

Salida:

```
0 1
```

## Solución

Un recorrido siempre se puede alargar en 2 yendo y volviendo, así que
existe uno de longitud L de 1 a v exactamente cuando L es al menos el
recorrido más corto hasta v con la misma paridad que L. Esos dos
recorridos más cortos por aula salen de una búsqueda en anchura sobre
estados (aula, paridad).

Así basta saber, para cada número x y cada paridad p, la mayor suma de
x vasos con paridad p. Con los vasos ordenados de mayor a menor, la
mayor suma en general son los x primeros, y la mejor suma de la otra
paridad cambia un vaso: quita el menor vaso elegido de alguna paridad y
añade el mayor no elegido de la otra, probando ambas opciones. Es el
argumento de intercambio habitual para una suma máxima con restricción
de paridad.

Recorriendo x = 1, 2, …, dos punteros por paridad registran, para cada
longitud L menor que 2N, el primer número de vasos cuya mejor suma de la
paridad de L llega a L. Un aula toma el menor número entre sus dos
distancias de paridad distinta, y el aula 1 no necesita vasos.

En el segundo ejemplo el aula 5 está a 4 pasillos, mientras que los
vasos dan a lo sumo 1 + 2 = 3, así que la respuesta es −1.

La búsqueda cuesta O(N + M), y los vasos O(K log K) por la ordenación.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2219_bfs_greedy.cpp](2219_bfs_greedy.cpp) | G++ 13.2 x64 | bfs, greedy | O(N + M + K log K) | AC | 0.187 s | 11000 KB |
| [2219_bfs_greedy.go](2219_bfs_greedy.go) | Go 1.14 x64 | bfs, greedy | O(N + M + K log K) | AC | 0.156 s | 21080 KB |
| [2219_bfs_greedy.java](2219_bfs_greedy.java) | Java 1.8 | bfs, greedy | O(N + M + K log K) | AC | 0.265 s | 10852 KB |
| [2219_bfs_greedy.py](2219_bfs_greedy.py) | Python 3.12 x64 | bfs, greedy | O(N + M + K log K) | AC | 1.234 s | 57712 KB |
| [2219_bfs_greedy.rs](2219_bfs_greedy.rs) | Rust 1.75 x64 | bfs, greedy | O(N + M + K log K) | AC | 0.062 s | 15152 KB |
