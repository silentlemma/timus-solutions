# 1099. Emparejar vigilantes nocturnos: emparejamiento máximo en un grafo general

[Timus 1099](https://acm.timus.ru/problem.aspx?space=1&num=1099) · dificultad 1144 · matching, graphs

Problema original de Jivko Ganev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N ≤ 222` vigilantes y una lista de parejas de vigilantes que pueden
trabajar juntos (hasta el final de la entrada). Cada vigilante trabaja
con como mucho un compañero, y nadie trabaja solo. Programa tantos
vigilantes como sea posible: imprime cuántos son y las parejas.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego parejas `i j` hasta el final de la entrada.

## Salida

El número de vigilantes programados `C` y luego `C/2` parejas.

## Evaluación

Se acepta cualquier conjunto máximo de parejas. El comprobador verifica
que el número es el máximo y que cada pareja está permitida y usa a cada
vigilante como mucho una vez.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 2
2 3
1 3
```

Salida:

```
2
1 2
```

## Solución

Es un emparejamiento máximo en un grafo general, que, a diferencia de uno
bipartito, tiene ciclos impares, así que los caminos de aumento simples
no bastan. El algoritmo de flores de Edmonds se ocupa de ellos. Se empieza
con un emparejamiento voraz. Después, desde cada vigilante libre, se hace
crecer un árbol alternante por búsqueda en anchura: desde un vértice
exterior `v`, un vecino libre `to` termina un camino de aumento, y un
vecino emparejado entra en el árbol junto con su pareja. Cuando `v`
encuentra otro vértice exterior, los dos caminos del árbol y la arista
entre ellos forman un ciclo impar (una flor). Sus vértices reciben la base
de la flor (el ancestro común más bajo), pasan a ser exteriores y entran
en la cola, y los enlaces a los padres alrededor del ciclo se fijan para
que un camino a través de la flor se pueda seguir. Al encontrar un camino
de aumento, intercambiar las aristas emparejadas y libres a lo largo de
él aumenta el emparejamiento en uno. `O(N³)`.

Detalles a tener en cuenta:

- el número de parejas no se da, así que se leen hasta el final de la
  entrada;
- una pareja puede repetirse o venir en los dos órdenes, y un vigilante
  emparejado consigo mismo no puede trabajar, así que esas líneas se
  ignoran;
- un grafo sin parejas da `0` y nada más.

El comprobador se apoya en la cantidad esperada; las cantidades se
comprobaron con el rango de una matriz de Tutte aleatoria módulo un primo
grande, que es el doble del tamaño de un emparejamiento máximo, en todas
las pruebas y en cientos de grafos pequeños aleatorios.

## Notas por lenguaje

- Rust guarda los arreglos de la búsqueda en una estructura `Matcher`,
  ya que las funciones auxiliares los modifican.
- Java y C++ construyen listas de adyacencia ordenadas a partir de
  conjuntos, lo que elimina las parejas repetidas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1099_matching.cpp](1099_matching.cpp) | G++ 13.2 x64 | matching | O(N^3) | AC | 0.046 s | 2364 KB |
| [1099_matching.go](1099_matching.go) | Go 1.14 x64 | matching | O(N^3) | AC | 0.046 s | 5768 KB |
| [1099_matching.java](1099_matching.java) | Java 1.8 | matching | O(N^3) | AC | 0.156 s | 5940 KB |
| [1099_matching.py](1099_matching.py) | Python 3.12 x64 | matching | O(N^3) | AC | 0.093 s | 5612 KB |
| [1099_matching.rs](1099_matching.rs) | Rust 1.75 x64 | matching | O(N^3) | AC | 0.015 s | 2044 KB |
