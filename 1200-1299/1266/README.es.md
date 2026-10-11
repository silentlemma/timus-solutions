# 1266. Ley de Kirchhoff

[Timus 1266](https://acm.timus.ru/problem.aspx?space=1&num=1266) · dificultad 1421 · math

Problema original de Alexander Klepinin (preparado por Stanislav Vasilyev), del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un circuito tiene N nodos (2 ≤ N ≤ 20) y M resistencias
(1 ≤ M < 1000), cada una une dos nodos con un valor entero de 1 a 1000;
un par de nodos puede estar unido por muchas resistencias. Hay que
hallar la resistencia total entre los nodos 1 y N, redondeada a dos
cifras tras el punto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, luego M líneas `A B R`.

## Salida

La resistencia.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 5
1 2 15
2 4 5
1 3 10
3 4 10
2 3 1
```

Salida:

```
9.40
```

## Solución

Se sigue la receta del enunciado. Se suman las conductancias 1/R de
todas las resistencias entre cada par de nodos. Se fija el potencial
del nodo 1 en 1 y el del nodo N en 0; en cada otro nodo las corrientes
suman cero:

```text
sum over v of g(u, v) · (V(u) − V(v)) = 0
```

Es un sistema lineal de como mucho 18 incógnitas, que se resuelve por
eliminación gaussiana con pivoteo parcial. La corriente que sale del
nodo 1 es I = Σ g(1, v) · (1 − V(v)), y la resistencia es 1 / I.

Los nodos a los que no se llega desde el nodo 1 no llevan corriente,
pero las ecuaciones no fijan sus potenciales, así que antes se descartan con
una búsqueda desde el nodo 1. Cada nodo restante toca el nodo 1 o el
nodo N a través de su parte del circuito, y el sistema tiene solución
única. `O(M + N³)`.

Detalles a tener en cuenta:

- los nodos aislados y las partes separadas de ambos extremos hacen el
  sistema singular si se mantienen (pruebas 05, 06);
- las resistencias en paralelo entre los mismos nodos se suman como
  conductancias (prueba 03);
- con N = 2 no hay ninguna incógnita (pruebas 02, 03).

Las respuestas se compararon en 120 circuitos aleatorios con la fórmula
del teorema de Kirchhoff de los árboles, el cociente de dos menores del
laplaciano calculados en fracciones exactas.

## Notas por lenguaje

- Todos los lenguajes hacen la misma eliminación en doubles.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1266_math.cpp](1266_math.cpp) | G++ 13.2 x64 | math | O(M + N³) | AC | 0.001 s | 236 KB |
| [1266_math.go](1266_math.go) | Go 1.14 x64 | math | O(M + N³) | AC | 0.031 s | 1140 KB |
| [1266_math.java](1266_math.java) | Java 1.8 | math | O(M + N³) | AC | 0.078 s | 1484 KB |
| [1266_math.py](1266_math.py) | Python 3.12 x64 | math | O(M + N³) | AC | 0.078 s | 792 KB |
| [1266_math.rs](1266_math.rs) | Rust 1.75 x64 | math | O(M + N³) | AC | 0.031 s | 256 KB |
