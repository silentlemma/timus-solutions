# 1695. Trabajo para robots

[Timus 1695](https://acm.timus.ru/problem.aspx?space=1&num=1695) · dificultad 2913 · backtracking

Problema original de Mikhail Kolodyazhniy, preparado por Alex Samsonov, del Ural SU Contest en el campus de invierno de Petrozavodsk, febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada día va a trabajar un grupo no vacío de robots que son todos amigos
entre sí, y ningún grupo puede repetirse. Dado el grafo de amistad de
n robots, hallar el primer día en que no queda ningún grupo nuevo.

## Entrada

n (1 ≤ n ≤ 50) y luego la matriz de amistad n × n de ceros y unos,
simétrica y con ceros en la diagonal.

## Salida

El número de ese día.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
011100
101100
110100
111000
000001
000010
```

Salida:

```
19
```

## Solución

Un grupo de trabajo es una clique del grafo de amistad, es decir, un
conjunto independiente del grafo de no amigos. Cada grupo no vacío
ocupa un día, así que la respuesta es el número de cliques no vacías
más uno, que es el número de conjuntos independientes del grafo de no
amigos contando el vacío.

Los conjuntos independientes de un conjunto de vértices M se cuentan
recursivamente:

- si M se separa en varias partes conexas, se multiplican sus
  cantidades;
- si todo par de vértices de M son enemigos, los conjuntos son el vacío
  y los |M| vértices sueltos: |M| + 1;
- si ningún vértice tiene más de dos enemigos, M es un camino o un
  ciclo, con cantidades de tipo Fibonacci: P(s) = P(s − 1) + P(s − 2)
  para un camino y P(s − 1) + P(s − 3) para un ciclo;
- si no, se toma un vértice v con más enemigos, al menos tres:
  count(M) = count(M − v) + count(M − v − enemigos de v).

Ramificar solo en vértices de grado tres o más mantiene pequeña la
recursión, y una memoria por la máscara de vértices elimina los
subproblemas repetidos. La respuesta llega a 2⁵⁰ cuando todos los
robots son amigos y cabe en 64 bits.

Trampas:

- el grupo vacío no es un día de trabajo, pero el día de oxidarse es
  uno más que el número de grupos, así que contar el vacío da la
  respuesta directamente;
- todos amigos da 2⁵⁰ (test 03), ningún amigo da n + 1 (test 04);
- un ciclo de enemigos necesita su propia fórmula (test 07).

Las respuestas coinciden con un recuento sobre todos los subconjuntos
en grafos pequeños y con una implementación aceptada independiente en
grafos aleatorios, dispersos y regulares de 50 robots.

Complejidad: `O(1.38^n·n)`: ramificar en un vértice con al menos tres
enemigos da T(n) = T(n − 1) + T(n − 4).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1695_backtracking.cpp](1695_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(1.38^n·n) | AC | 0.031 s | 956 KB |
| [1695_backtracking.go](1695_backtracking.go) | Go 1.14 x64 | backtracking | O(1.38^n·n) | AC | 0.031 s | 2632 KB |
| [1695_backtracking.java](1695_backtracking.java) | Java 1.8 | backtracking | O(1.38^n·n) | AC | 0.140 s | 4824 KB |
| [1695_backtracking.py](1695_backtracking.py) | Python 3.12 x64 | backtracking | O(1.38^n·n) | AC | 0.265 s | 3316 KB |
| [1695_backtracking.rs](1695_backtracking.rs) | Rust 1.75 x64 | backtracking | O(1.38^n·n) | AC | 0.046 s | 1488 KB |
