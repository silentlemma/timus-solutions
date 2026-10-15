# 1691. Complejidad del algoritmo

[Timus 1691](https://acm.timus.ru/problem.aspx?space=1&num=1691) · dificultad 2997 · graphs

Problema original de Ivan Burmistrov, del Ural SU Contest en el campus de invierno de Petrozavodsk, febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un grafo dirigido sin arcos múltiples (con lazos permitidos), sea
F(N) el número de caminos de longitud N de s a t. Hallar el menor
k ≥ 0 tal que F(N) ≤ C · Nᵏ para alguna constante C y todo N ≥ 1, o −1
si F crece más deprisa que cualquier polinomio.

## Entrada

n, m, s, t (1 ≤ n, m ≤ 100000), y luego los m arcos.

## Salida

k, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3 1 2
1 1
1 2
2 2
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
3 6 1 2
1 2
2 1
1 3
3 1
2 3
3 2
```

Salida:

```
-1
```

## Solución

Solo importan los vértices que están en algún camino de s a t: los
alcanzables desde s que además alcanzan t. Si t es inalcanzable, F es
cero y k = 0. Estos vértices forman componentes fuertemente conexas
enteras, porque todo lo que está en un ciclo con uno de ellos también
queda entre s y t.

Una componente con más arcos que vértices contiene dos ciclos distintos
por un vértice común. Entonces un camino puede recorrerlos en
exponencialmente muchos órdenes, y la respuesta es −1. Si no, cada
componente es un solo vértice, quizá con lazo, o un ciclo simple, con
tantos arcos como vértices. Un camino que pasa por c ciclos simples
reparte su longitud sobrante entre ellos de unas N^(c − 1) maneras.
Así que F(N) ≤ C · N^(c − 1), y en una progresión aritmética adecuada
de N alcanza ese orden. Por tanto k = max(0, c − 1), donde c es el
mayor número de componentes cíclicas en un camino de s a t.

El algoritmo de Kosaraju numera las componentes de modo que los arcos
entre ellas van de números menores a mayores. Una pasada en ese orden
calcula c como camino más largo, con peso 1 en cada componente cíclica.
Todos los recorridos usan una pila explícita. `O(n + m)`.

Trampas:

- una componente con dos ciclos que no alcanza t (o no es alcanzable
  desde s) no importa (test 07);
- un solo ciclo en el camino deja F acotada, así que k = 0, no 1
  (test 08);
- un lazo es un ciclo de longitud 1, y s = t está permitido (test 04);
- la profundidad de recursión llegaría a 10⁵, así que los recorridos
  usan su propia pila.

Las respuestas coinciden con una implementación aceptada independiente.
En 121 grafos diminutos también coinciden con el crecimiento de F(N),
calculado exactamente hasta N = 3000.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1691_graphs.cpp](1691_graphs.cpp) | G++ 13.2 x64 | graphs | O(n + m) | AC | 0.171 s | 9792 KB |
| [1691_graphs.go](1691_graphs.go) | Go 1.14 x64 | graphs | O(n + m) | AC | 0.187 s | 18576 KB |
| [1691_graphs.java](1691_graphs.java) | Java 1.8 | graphs | O(n + m) | AC | 0.296 s | 37820 KB |
| [1691_graphs.py](1691_graphs.py) | Python 3.12 x64 | graphs | O(n + m) | AC | 0.515 s | 55192 KB |
| [1691_graphs.rs](1691_graphs.rs) | Rust 1.75 x64 | graphs | O(n + m) | AC | 0.093 s | 20620 KB |
