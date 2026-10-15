# 1641. Guardias

[Timus 1641](https://acm.timus.ru/problem.aspx?space=1&num=1641) · dificultad 511 · constructive

Problema original de Pavel Atnashev, del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de los n alumnos se encarga de una de las k aulas, y toda aula
necesita a alguien. Cada uno de los m días hacen guardia dos alumnos a
cargo de aulas distintas. Ningún par puede repetir guardia, y todo alumno
debe hacer guardia al menos una vez. Hay que dar un plan así; se sabe que
existe.

## Entrada

n, k y m (2 ≤ k ≤ n ≤ 100).

## Salida

n líneas con el aula de cada alumno y luego m líneas con el par de
guardia de cada día. Se acepta cualquier plan válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3 4
```

Salida:

```
1
2
1
2
3
1 2
3 4
3 5
4 5
```

### Ejemplo 2

Entrada:

```
4 2 4
```

Salida:

```
1
2
1
2
1 2
3 4
1 4
2 3
```

## Solución

En términos de grafos: repartir los alumnos en k grupos no vacíos y
elegir m aristas distintas entre grupos distintos que cubran a todos.
Para cubrir n alumnos hacen falta al menos ⌈n/2⌉ aristas, y como mucho
hay tantas como en el grafo k-partito completo. Ese número es máximo con
grupos lo más parejos posible, así que repartir las aulas por turno, al
alumno i el aula i mod k, nunca es peor que otro reparto; como el plan
existe, m cabe.

Con el reparto por turno, los alumnos i e i + 1 siempre tienen aulas
distintas, así que los pares (0, 1), (2, 3), … cubren a todos en ⌈n/2⌉
días; si n es impar, el último alumno va con el 0, o con el 1 si el 0
comparte su aula. Los días restantes toman en orden cualquier par no
usado de aulas distintas. `O(n² log n)` en C++; `O(n²)` en los demás.

Detalles a tener en cuenta:

- importa cubrir primero a todos: llenar los días simplemente en orden
  podría gastarlos todos en los primeros alumnos (prueba 07);
- con k = n cada aula tiene un alumno y se permiten todos los pares
  (prueba 06).

Un verificador acepta cualquier plan válido; los planes del programa lo
pasan en las 1866 entradas factibles con n ≤ 12.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1641_constructive.cpp](1641_constructive.cpp) | G++ 13.2 x64 | constructive | O(n² log n) | AC | 0.031 s | 300 KB |
| [1641_constructive.go](1641_constructive.go) | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1576 KB |
| [1641_constructive.java](1641_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.125 s | 2048 KB |
| [1641_constructive.py](1641_constructive.py) | Python 3.12 x64 | constructive | O(n²) | AC | 0.078 s | 1312 KB |
| [1641_constructive.rs](1641_constructive.rs) | Rust 1.75 x64 | constructive | O(n²) | AC | 0.031 s | 644 KB |
