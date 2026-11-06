# 1416. Confidencial

[Timus 1416](https://acm.timus.ru/problem.aspx?space=1&num=1416) · dificultad 385 · graphs

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

## Soluciones optimizadas

La versión compacta en C++ mantiene la recurrencia de Prim y usa entradas de 16 bits para ambas matrices. Al incorporar una arista al árbol, se marca como ausente en la matriz de pesos. Los dos extremos ya están en el árbol y el cambio no afecta a Prim. La pasada final solo examina aristas externas al árbol y puede detenerse si el coste adicional es cero.

Las implementaciones base aceptadas [1416_graphs.go](1416_graphs.go), [1416_graphs.java](1416_graphs.java), [1416_graphs.py](1416_graphs.py), [1416_graphs.rs](1416_graphs.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1416_graphs.cpp](1416_graphs.cpp) | G++ 13.2 x64 | graphs | O(n^2 + m) | AC | 0.187 s | 3448 KB | 11286111 |
| [1416_graphs.go](1416_graphs.go) \* | Go 1.14 x64 | graphs | O(n^2 + m) | AC | 0.203 s | 10568 KB | 11286112 |
| [1416_graphs.java](1416_graphs.java) | Java 1.8 | graphs | O(n^2 + m) | AC | 0.109 s | 8164 KB | 11286114 |
| [1416_graphs.py](1416_graphs.py) \* | Python 3.12 x64 | graphs | O(n^2 + m) | AC | 0.343 s | 44112 KB | 11286113 |
| [1416_graphs.rs](1416_graphs.rs) \* | Rust 1.75 x64 | graphs | O(n^2 + m) | AC | 0.015 s | 9656 KB | 11286115 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1416_graphs_optimized.cpp](1416_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(n^2 + m) | AC | 0.015 s | 1132 KB | 11310409 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
