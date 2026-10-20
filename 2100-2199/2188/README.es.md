# 2188. El adelantamiento más temprano que ya no se pierde

[Timus 2188](https://acm.timus.ru/problem.aspx?space=1&num=2188) · dificultad 1769 · prefix_sums, binary_search

Problema original de Artyom Kutuzov, del Concurso Escolar de Programación de los Urales 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un bote pirata sale D pies por delante y avanza bᵢ pies en el segundo
i; el bote de Jim puede avanzar en ese segundo cualquier número entero
de pies entre 0 y aᵢ. Jim quiere que el primer segundo t al final del
cual va estrictamente por delante sea lo menor posible, con la regla de
que luego siga estrictamente por delante hasta el final del segundo n.
Para cada una de q suposiciones de D, hallar ese t, o −1. Los límites
son 1 segundo y 256 MB.

## Entrada

n y q, 1 ≤ n, q ≤ 10⁵, luego a₁ … a_n y b₁ … b_n con valores de 0 a
10⁹, y luego d₁ … d_q con 1 ≤ dⱼ ≤ 10⁹.

## Salida

La respuesta para cada suposición.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 10
7 4 7 0 5 6 4 4 5 4
5 3 5 1 2 3 3 7 2 0
1 2 3 4 5 6 7 8 14 15
```

Salida:

```
1
2
3
5
5
5
6
10
10
-1
```

### Ejemplo 2

Entrada:

```
1 4
4
1
1 2 3 4
```

Salida:

```
1
1
-1
-1
```

## Solución

Sea x(i) lo recorrido por Jim menos lo recorrido por los piratas, de
modo que Jim va delante al final del segundo i cuando x(i) > D, y sea
G(i) la suma de prefijo de aᵢ − bᵢ, es decir, x a toda velocidad. Ambos
botes se mueven uniformemente dentro de un segundo, así que ir delante
en los dos extremos de un segundo significa ir delante durante todo él.

Antes de t Jim no debe ir delante, así que lo mejor que puede hacer es
ir a toda velocidad sin pasar de D. Ese camino recortado termina en
x = G(i) − max(0, Mᵢ − D), donde Mᵢ es el mayor de 0, G(1), …, G(i).
Desde el segundo t Jim va a toda velocidad, así que con M el máximo
antes de t y S el menor G(i) para i ≥ t, sigue delante exactamente
cuando

S − max(0, M − D) > D, es decir, S > max(D, M).

Así que un segundo t solo puede servir si S > M, y entonces sirve para
todo D < S. Los mínimos de sufijo S crecen con t, así que los segundos
útiles tienen umbrales S crecientes, y cada consulta es una búsqueda
binaria del primer umbral mayor que D.

En el segundo ejemplo G(1) = 3, así que con D = 1 y D = 2 adelanta en
el primer segundo, mientras que con D = 3 y D = 4 nunca se pone delante.

Las sumas de prefijo y los mínimos de sufijo cuestan O(n), y las
consultas O(q log n).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2188_prefix_sums_binary_search.cpp](2188_prefix_sums_binary_search.cpp) | G++ 13.2 x64 | prefix_sums, binary_search | O(n + q log n) | AC | 0.078 s | 2732 KB |
| [2188_prefix_sums_binary_search.go](2188_prefix_sums_binary_search.go) | Go 1.14 x64 | prefix_sums, binary_search | O(n + q log n) | AC | 0.062 s | 12984 KB |
| [2188_prefix_sums_binary_search.java](2188_prefix_sums_binary_search.java) | Java 1.8 | prefix_sums, binary_search | O(n + q log n) | AC | 0.156 s | 5764 KB |
| [2188_prefix_sums_binary_search.py](2188_prefix_sums_binary_search.py) | Python 3.12 x64 | prefix_sums, binary_search | O(n + q log n) | AC | 0.281 s | 32712 KB |
| [2188_prefix_sums_binary_search.rs](2188_prefix_sums_binary_search.rs) | Rust 1.75 x64 | prefix_sums, binary_search | O(n + q log n) | AC | 0.046 s | 7212 KB |
