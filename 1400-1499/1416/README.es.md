# 1416. Confidencial

[Timus 1416](https://acm.timus.ru/problem.aspx?space=1&num=1416) · dificultad 394 · graphs

Problema original de Den Raskovalov, del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo conexo tiene n vértices (2 ≤ n ≤ 500) y m aristas con costes
de 0 a 1000, con como mucho una arista entre dos vértices. Hay que
imprimir el coste de un árbol generador mínimo y el coste del siguiente
árbol generador por coste (que puede ser igual al primero), o −1 si no
hay otro árbol generador.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

n y m, luego m líneas a b w.

## Salida

«Cost: » y el primer coste, luego «Cost: » y el segundo.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 6
1 2 2
2 3 2
3 4 2
4 1 2
1 3 1
2 4 1
```

Salida:

```
Cost: 4
Cost: 4
```

### Ejemplo 2

Entrada:

```
3 2
1 2 2
2 3 2
```

Salida:

```
Cost: 4
Cost: -1
```

## Solución

Un segundo mejor árbol generador difiere de algún árbol mínimo en
exactamente una arista: entra una arista de fuera del árbol y sale la
arista más pesada del camino del árbol entre sus extremos. Así que el
segundo coste es el mínimo más el menor valor de w − (arista más pesada
del camino) entre las aristas de fuera del árbol, y −1 si todas las
aristas están en el árbol.

Con hasta 500 vértices, el algoritmo de Prim sobre la matriz de costes
cuesta O(n²). La arista más pesada de cada camino del árbol sale de
paso: cuando el vértice v entra por el padre p con una arista de coste
c, para cada vértice u ya en el árbol
heaviest(u, v) = max(heaviest(u, p), c). `O(n² + m)`.

Detalles a tener en cuenta:

- el segundo árbol puede costar lo mismo que el primero (prueba 01);
- un grafo que ya es un árbol no tiene segundo árbol (pruebas 02, 03,
  gen2);
- los costes pueden ser 0 (pruebas 04, 06).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1416_graphs.cpp](1416_graphs.cpp) | G++ 13.2 x64 | graphs | O(n^2 + m) | AC | 0.187 s | 3448 KB |
| [1416_graphs.go](1416_graphs.go) | Go 1.14 x64 | graphs | O(n^2 + m) | AC | 0.203 s | 10568 KB |
| [1416_graphs.java](1416_graphs.java) | Java 1.8 | graphs | O(n^2 + m) | AC | 0.109 s | 8164 KB |
| [1416_graphs.py](1416_graphs.py) | Python 3.12 x64 | graphs | O(n^2 + m) | AC | 0.343 s | 44112 KB |
| [1416_graphs.rs](1416_graphs.rs) | Rust 1.75 x64 | graphs | O(n^2 + m) | AC | 0.015 s | 9656 KB |
