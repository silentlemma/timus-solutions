# 2202. Unir pares de puntos con curvas sin cruces alrededor del contorno de un rectángulo

[Timus 2202](https://acm.timus.ru/problem.aspx?space=1&num=2202) · dificultad 2009 · graphs, segment_tree

Problema original de Valentin Zuev, de la Olimpiada Académica Universitaria Escolar de Informática 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N pares de puntos distintos deben unirse de uno en uno con curvas que
no se cruzan entre sí ni tocan el contorno del rectángulo
(0, 0)–(W, H), salvo que una curva puede empezar o terminar en un punto
del contorno. Decir si se pueden unir todos los pares. Los límites son
3 segundos y 256 MB.

## Entrada

N, W y H, 1 ≤ N ≤ 10⁵, 1 ≤ W, H ≤ 10⁸, y luego N pares de puntos con
coordenadas de valor absoluto hasta 10⁸.

## Salida

YES o NO.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2 2
-1 1 3 1
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
3 4 4
0 0 3 3
4 0 1 3
2 4 2 0
```

Salida:

```
YES
```

### Ejemplo 3

Entrada:

```
3 4 4
0 0 4 4
4 0 0 4
2 4 2 0
```

Salida:

```
NO
```

## Solución

El contorno es una curva cerrada, así que un par con un punto
estrictamente dentro y el otro estrictamente fuera nunca se puede unir:
la respuesta es NO.

Un par con al menos un punto estrictamente dentro o estrictamente fuera
traza una curva que toca el contorno en a lo sumo un punto, y una curva
así no separa nada. Dibujando primero estos pares y los demás
rodeándolos, se pueden ignorar.

Quedan los pares con ambos puntos en el contorno. Cada una de sus curvas
es una cuerda que va entera por dentro o entera por fuera del
rectángulo, porque no puede cruzar el contorno. Se numeran los puntos
por su posición a lo largo del contorno; dos cuerdas del mismo lado se
cruzan exactamente cuando sus extremos se alternan. Así la respuesta es
YES exactamente cuando el grafo de alternancia de esas cuerdas es
bipartito, un lado dentro y otro fuera.

Ese grafo puede tener Θ(N²) aristas, así que la coloración solo
construye un bosque generador. Un árbol de segmentos sobre las
posiciones del contorno guarda, para cada extremo no visitado, la
posición de su pareja, con el mínimo y el máximo por nodo. Una cuerda
[l, r] cruza otra exactamente cuando algún extremo estrictamente entre l
y r tiene su pareja fuera de [l, r], así que una consulta halla una
cuerda que cruza y no tiene color, que recibe el color opuesto y se
borra del árbol. Cada cuerda se encuentra una vez.

Al final cada clase de color se comprueba con un recorrido con pila a
lo largo del contorno: las cuerdas de una clase deben anidarse bien, o
el grafo no es bipartito.

En el tercer ejemplo las tres cuerdas unen (0, 0)–(4, 4), (4, 0)–(0, 4)
y (2, 4)–(2, 0); cada dos de ellas se alternan, así que forman un
triángulo y la respuesta es NO.

La ordenación y las consultas al árbol cuestan O(N log N).

## Notas por lenguaje

- Python se ejecuta con PyPy: con CPython 3.12 supera el límite de tiempo
  en el test 73 (3.015 s), mientras que con PyPy 3.10 se acepta en 1.453 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2202_graphs_segment_tree.cpp](2202_graphs_segment_tree.cpp) | G++ 13.2 x64 | graphs, segment_tree | O(N log N) | AC | 0.125 s | 9188 KB |
| [2202_graphs_segment_tree.go](2202_graphs_segment_tree.go) | Go 1.14 x64 | graphs, segment_tree | O(N log N) | AC | 0.171 s | 22444 KB |
| [2202_graphs_segment_tree.java](2202_graphs_segment_tree.java) | Java 1.8 | graphs, segment_tree | O(N log N) | AC | 0.312 s | 16340 KB |
| [2202_graphs_segment_tree.py](2202_graphs_segment_tree.py) | PyPy 3.10 x64 | graphs, segment_tree | O(N log N) | AC | 1.453 s | 33364 KB |
| [2202_graphs_segment_tree.rs](2202_graphs_segment_tree.rs) | Rust 1.75 x64 | graphs, segment_tree | O(N log N) | AC | 0.078 s | 18172 KB |
