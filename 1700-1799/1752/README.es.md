# 1752. Árbol 2

[Timus 1752](https://acm.timus.ru/problem.aspx?space=1&num=1752) · dificultad 257 · graphs

Problema original de Petr Lezhankin, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un árbol de n vértices, la distancia entre dos vértices es el número
de aristas del camino entre ellos. Para cada consulta, un vértice v y un
número d, hallar un vértice a distancia exactamente d de v.

## Entrada

n (1 ≤ n ≤ 20000) y q (1 ≤ q ≤ 50000), luego las n − 1 aristas y luego
q consultas v (1 ≤ v ≤ n) y d (0 ≤ d ≤ n).

## Salida

Para cada consulta, un vértice a distancia d de v, o 0 si no lo hay. Se
acepta cualquier vértice válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
9 10
1 8
1 5
1 4
2 7
2 5
3 6
5 9
6 9
5 4
8 1
4 3
2 4
9 3
1 1
5 2
3 5
6 4
7 3
```

Salida:

```
0
1
2
3
4
5
6
7
8
9
```

## Solución

El vértice más lejano de cualquier vértice v es siempre un extremo de un
diámetro del árbol, su camino más largo. Así que si existe un vértice a
distancia d, uno de los dos extremos, a o b, está a distancia al menos
d, y el camino de v hacia él pasa por un vértice a distancia
exactamente d.

Los extremos se hallan del modo habitual: el vértice más profundo visto
desde el vértice 1 es a, y el más profundo visto desde a es b. Al
recorrer el árbol en profundidad desde una raíz, el camino actual desde
la raíz se guarda en un arreglo por profundidad. Cuando el recorrido
llega a v a profundidad h, cada consulta en v con d ≤ h se responde con
el vértice a profundidad h − d de ese camino. Tres recorridos, desde 1,
desde a y desde b, responden todas las consultas que tienen respuesta;
el resto recibe 0. `O(n + q)`.

El programa puede imprimir vértices distintos de los del ejemplo, por
ejemplo 9 en la tercera consulta en lugar de 2; ambos están a distancia
3 del vértice 4.

Trampas:

- una consulta con d = 0 se responde con el propio v;
- un camino de 20000 vértices es demasiado profundo para la recursión en
  algunos lenguajes, así que el recorrido usa su propia pila;
- las consultas son muchas, así que se agrupan por vértice en lugar de
  hacer un recorrido para cada una.

Las respuestas coinciden con una búsqueda desde el vértice de cada
consulta en 300 árboles aleatorios de hasta 10 vértices con todas las
consultas, y una implementación aceptada independiente coincide en qué
consultas grandes no tienen respuesta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1752_graphs.cpp](1752_graphs.cpp) | G++ 13.2 x64 | graphs | O(n + q) | AC | 0.109 s | 1516 KB |
| [1752_graphs.go](1752_graphs.go) | Go 1.14 x64 | graphs | O(n + q) | AC | 0.078 s | 7244 KB |
| [1752_graphs.java](1752_graphs.java) | Java 1.8 | graphs | O(n + q) | AC | 0.125 s | 3756 KB |
| [1752_graphs.py](1752_graphs.py) | Python 3.12 x64 | graphs | O(n + q) | AC | 0.250 s | 21372 KB |
| [1752_graphs.rs](1752_graphs.rs) | Rust 1.75 x64 | graphs | O(n + q) | AC | 0.062 s | 4172 KB |
