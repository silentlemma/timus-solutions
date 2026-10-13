# 1419. Mapas de los mundos de islas

[Timus 1419](https://acm.timus.ru/problem.aspx?space=1&num=1419) · dificultad 1212 · graphs

Problema original de Alexander Klepinin, del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una imagen de M × N caracteres (ambos impares, de 1 a 99) tiene `O` en
cada posición de fila y columna impares (contando desde 1) y `-`, `|`,
`/`, `\` o un espacio en las demás. Es un mapa real de un mundo de
islas si los símbolos son puentes entre islas vecinas, cada isla tiene
exactamente tres puentes y las islas siguen conectadas tras destruir
cualquier puente. Hay que imprimir «Island world» o «Just a picture».

Es la comprobación que hay detrás del [problema 1411](../1411/README.es.md).

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

M y N, luego N líneas de M caracteres.

## Salida

«Island world» o «Just a picture».

## Ejemplos

### Ejemplo 1

Entrada:

```
15 9
O-O-O-O-O-O O-O
|\| |  \|/|/|/|
O-O O-O O O O O
 \ / /|  /  |/|
O-O O-O-O-O O-O
|\  |    / \  |
O-O O O-O-O O-O
|/ /| |\  |\ \|
O-O-O-O-O-O-O-O
```

Salida:

```
Island world
```

### Ejemplo 2

Entrada:

```
5 3
O-O-O
|   |
O-O-O
```

Salida:

```
Just a picture
```

## Solución

Las líneas se leen tal cual, porque pueden empezar con espacios. Cada
símbolo debe encajar en su hueco: `-` entre dos islas de una fila, `|`
entre dos islas de una columna, `\` o `/` en medio de cuatro islas;
cualquier otro símbolo hace que no sea un mapa. Cada símbolo añade una
arista entre las dos islas que une. Luego cada isla debe tener grado
tres, y una búsqueda en profundidad calcula los tiempos de entrada y los
valores low: el grafo es conexo si la búsqueda llega a todas las islas,
y no tiene puentes de corte si ninguna arista del árbol hacia un vértice
v cumple low(v) > tin(padre). La búsqueda lleva su propia pila, porque
un camino de 2500 islas es demasiado profundo para la pila de llamadas
de algunos lenguajes. `O(MN)`.

Detalles a tener en cuenta:

- un símbolo en un hueco equivocado, como un `-` donde solo cabe `|`, no
  es un puente (prueba 06);
- un mapa con todas las islas de grado tres aún puede partirse en dos o
  colgar de un único puente (pruebas 03, 07);
- una sola isla no tiene ningún puente (prueba 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1419_graphs.cpp](1419_graphs.cpp) | G++ 13.2 x64 | graphs | O(MN) | AC | 0.015 s | 572 KB |
| [1419_graphs.go](1419_graphs.go) | Go 1.14 x64 | graphs | O(MN) | AC | 0.031 s | 1796 KB |
| [1419_graphs.java](1419_graphs.java) | Java 1.8 | graphs | O(MN) | AC | 0.093 s | 1280 KB |
| [1419_graphs.py](1419_graphs.py) | Python 3.12 x64 | graphs | O(MN) | AC | 0.109 s | 1696 KB |
| [1419_graphs.rs](1419_graphs.rs) | Rust 1.75 x64 | graphs | O(MN) | AC | 0.031 s | 588 KB |
