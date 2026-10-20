# 2132. Repartir las aristas de un grafo en pares adyacentes

[Timus 2132](https://acm.timus.ru/problem.aspx?space=1&num=2132) · dificultad 1528 · graphs, constructive

Problema original de Alexander Petrov, preparado por Alexander Ipatov, del concurso «Más vale tarde que nunca».

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da como lista de aristas un grafo simple con un número par de
aristas. Repartir todas las aristas en pares de aristas que comparten un
vértice, o indicar que es imposible. Se acepta cualquier reparto válido.
Los límites son 1 segundo y 128 MB.

## Entrada

Pares de números de vértices, un par por arista: un número par de
aristas entre 2 y 10⁵, con vértices de 1 a 10⁵.

## Salida

El número de pares m y m ternas a b c para las aristas {a, b} y {b, c},
o −1.

## Evaluación

Un comprobador verifica que las ternas usan cada arista exactamente una
vez.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2
2 3
3 1
1 10
```

Salida:

```
2
1 2 3
3 1 10
```

### Ejemplo 2

Entrada:

```
1 2
2 3
3 1
4 10
```

Salida:

```
-1
```

## Solución

Las aristas de componentes conexas distintas no pueden emparejarse, así
que una componente con un número impar de aristas hace que la respuesta
sea −1. Un grafo conexo con un número par de aristas siempre puede
repartirse, y la construcción lo muestra.

Se construye un árbol generador de cada componente con una búsqueda y
se procesan los vértices de modo que cada uno vaya después de todos sus
descendientes. Cada arista fuera del árbol se asigna a uno de sus
extremos, el que se procesa antes. En un vértice v se reúnen las aristas
a sus hijos que siguen libres y las aristas fuera del árbol asignadas a
v, y se emparejan a través de v. Si sobra una, se empareja con la arista
de v a su padre, que queda usada; si no, la arista al padre queda libre
para el padre. Si a la raíz de una componente le sobra una arista, la
componente tenía un número impar de aristas. La búsqueda es iterativa y
todo cuesta O(V + E).

En el segundo ejemplo el triángulo 1 – 2 – 3 tiene tres aristas y la
arista 4 – 10 está sola, así que no hay reparto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2132_graphs_constructive.cpp](2132_graphs_constructive.cpp) | G++ 13.2 x64 | graphs, constructive | O(V + E) | AC | 0.109 s | 7376 KB |
| [2132_graphs_constructive.go](2132_graphs_constructive.go) | Go 1.14 x64 | graphs, constructive | O(V + E) | AC | 0.078 s | 21920 KB |
| [2132_graphs_constructive.java](2132_graphs_constructive.java) | Java 1.8 | graphs, constructive | O(V + E) | AC | 0.156 s | 8900 KB |
| [2132_graphs_constructive.py](2132_graphs_constructive.py) | Python 3.12 x64 | graphs, constructive | O(V + E) | AC | 0.359 s | 30520 KB |
| [2132_graphs_constructive.rs](2132_graphs_constructive.rs) | Rust 1.75 x64 | graphs, constructive | O(V + E) | AC | 0.046 s | 12784 KB |
