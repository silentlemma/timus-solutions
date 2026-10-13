# 1379. Transporte de tazas

[Timus 1379](https://acm.timus.ru/problem.aspx?space=1&num=1379) · dificultad 581 · graphs

Problema original de Pavel Egorov, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un camión de 3000 kg debe llevar tantas tazas como pueda, de 100 g cada
una y no más de los 10 000 000 encargadas, del cruce 1 al cruce N,
N ≤ 500, en 24 horas. Cada carretera de doble sentido tiene un tiempo de
recorrido en minutos y un peso máximo permitido del camión en gramos.
Hay que imprimir el mayor número de tazas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, luego M líneas: los extremos de una carretera, su tiempo y su
límite de peso.

## Salida

El número de tazas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
1 2 10 3000220
2 3 20 3000201
1 3 1 3000099
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
1 0
```

Salida:

```
10000000
```

## Solución

Un camión más pesado puede usar menos carreteras, así que llegar a
tiempo solo empeora al crecer la carga. El peso máximo de una ruta es el
límite de alguna de sus carreteras, así que se hace una búsqueda binaria
entre los límites de carretera de al menos 3 000 000 g. Para
cada uno, el algoritmo de Dijkstra usa solo las carreteras que aguantan
ese peso y nunca guarda tiempos de más de 1440 minutos. Con el mayor
peso W que llega a tiempo, la respuesta es
min(10 000 000, ⌊(W − 3 000 000) / 100⌋). `O((N + M log M) · log M)`.

Detalles a tener en cuenta:

- con N = 1 las tazas ya están en la sede: las 10 000 000 (ejemplo 2);
- exactamente 24 horas, 1440 minutos, aún es a tiempo (prueba 03);
- el camino más rápido puede aguantar menos que uno más lento
  (prueba 05);
- una carretera que aguanta justo el camión vacío no permite ninguna
  taza (prueba 06);
- hay carreteras que no llevan tiempo (prueba 07).

Las respuestas se compararon con probar todos los caminos simples en
400 grafos aleatorios de hasta 6 cruces.

## Notas por lenguaje

- Python necesita PyPy: una cadena de carreteras cortas dentro de un
  grafo completo de carreteras de un día obliga a las búsquedas a
  recorrer muchas carreteras, unos 0,5 s con CPython y 0,25 s con
  PyPy.
- Java guarda su montículo en un arreglo de long simples, con el tiempo
  y el vértice empaquetados en un número: una cola de prioridad de
  arreglos pequeños excedía el límite de tiempo en la prueba 46 del juez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1379_graphs.cpp](1379_graphs.cpp) | G++ 13.2 x64 | graphs | O((N + M log M) · log M) | AC | 0.265 s | 7532 KB |
| [1379_graphs.go](1379_graphs.go) | Go 1.14 x64 | graphs | O((N + M log M) · log M) | AC | 0.515 s | 23772 KB |
| [1379_graphs.java](1379_graphs.java) | Java 1.8 | graphs | O((N + M log M) · log M) | AC | 0.500 s | 11512 KB |
| [1379_graphs.py](1379_graphs.py) | PyPy 3.10 x64 | graphs | O((N + M log M) · log M) | AC | 0.500 s | 58564 KB |
| [1379_graphs.rs](1379_graphs.rs) | Rust 1.75 x64 | graphs | O((N + M log M) · log M) | AC | 0.046 s | 15788 KB |
