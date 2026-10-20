# 2127. Determinante de la matriz de adyacencia de un casi árbol

[Timus 2127](https://acm.timus.ru/problem.aspx?space=1&num=2127) · dificultad 3079 · graphs, matrix

Problema original de Alexey Danilyuk, del concurso t.me/umnik_team, campamento de Petrozavodsk, verano de 2018.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo simple conexo tiene n vértices y a lo sumo n + 50 aristas.
Imprimir el determinante de su matriz de adyacencia módulo 998 244 353.
Los límites son 2 segundos y 128 MB.

## Entrada

n y m, 1 ≤ n ≤ 2 · 10⁵, n − 1 ≤ m ≤ n + 50, y luego las m aristas.

## Salida

El determinante módulo 998 244 353.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
1 2
2 3
3 4
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
```

Salida:

```
4
```

### Ejemplo 3

Entrada:

```
1 0
```

Salida:

```
0
```

### Ejemplo 4

Entrada:

```
2 1
2 1
```

Salida:

```
998244352
```

## Solución

La matriz es enorme, así que primero se reduce el grafo con pasos que
cambian el determinante de forma conocida.

- Una hoja u con vecino v: la fila u tiene su único elemento no nulo en
  la columna v, y la columna u solo en la fila v, así que desarrollar por
  ambas da det A = −det A′ sin u ni v. Se repite mientras haya hojas (el
  grafo puede partirse en trozos), y un vértice sin vecinos hace que el
  determinante sea 0.
- Un camino por dos vértices de grado 2, a y b, x – a – b – y, se elimina
  con un complemento de Schur sobre {a, b}: el bloque [[0, 1], [1, 0]]
  tiene determinante −1, y eliminarlo añade una arista de peso −1 entre
  x e y. Así, cada par de vértices del camino cuesta un factor −1 y
  cambia el signo de la arista que lo sustituye. Un camino con un número
  par de vértices interiores se convierte en una arista con peso, y con
  un número impar queda un vértice interior.
- Un trozo que es solo un ciclo de longitud L tiene determinante 2 si L
  es impar, 0 si L es múltiplo de 4 y −4 en otro caso.

Quitadas las hojas, todo vértice tiene grado al menos 2, y como
m − n ≤ 50 hay como mucho unos cien vértices de grado mayor que 2. La
matriz comprimida contiene esos vértices y un vértice restante por cada
camino impar. Las filas de los vértices restantes solo tienen entradas
en las columnas de los vértices de ramificación, así que si hay más de
ellos que vértices de ramificación son linealmente dependientes y el
determinante es 0. El resto es una eliminación gaussiana módulo el primo
sobre unas 200 filas como mucho. El tiempo total es O(n + m + k³), con k
el tamaño de la matriz pequeña.

En el primer ejemplo el camino 1 – 2 – 3 – 4 pierde los pares (1, 2) y
(3, 4) como hojas, lo que da (−1)² = 1. En el cuarto una sola arista da
−1.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2127_graphs_matrix.cpp](2127_graphs_matrix.cpp) | G++ 13.2 x64 | graphs, matrix | O(n + m + k^3), k <= 200 | AC | 0.125 s | 9508 KB |
| [2127_graphs_matrix.go](2127_graphs_matrix.go) | Go 1.14 x64 | graphs, matrix | O(n + m + k^3), k <= 200 | AC | 0.062 s | 19976 KB |
| [2127_graphs_matrix.java](2127_graphs_matrix.java) | Java 1.8 | graphs, matrix | O(n + m + k^3), k <= 200 | AC | 0.109 s | 7904 KB |
| [2127_graphs_matrix.py](2127_graphs_matrix.py) | Python 3.12 x64 | graphs, matrix | O(n + m + k^3), k <= 200 | AC | 0.546 s | 56440 KB |
| [2127_graphs_matrix.rs](2127_graphs_matrix.rs) | Rust 1.75 x64 | graphs, matrix | O(n + m + k^3), k <= 200 | AC | 0.062 s | 21988 KB |
