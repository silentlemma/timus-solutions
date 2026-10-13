# 1358. Cables

[Timus 1358](https://acm.timus.ru/problem.aspx?space=1&num=1358) · dificultad 540 · graphs

Problema original de Den Raskovalov (enunciado de Aleksandr Bikbaev), del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 1000 ordenadores están unidos por N − 1 cables en una red conexa,
es decir, un árbol. Hay que colocar los ordenadores como puntos del
plano, con coordenadas de valor absoluto a lo sumo 1000, de modo que los
cables, dibujados como segmentos rectos, no se crucen, y que cada dos
ordenadores estén a distancia mayor que 1.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego N − 1 líneas con los extremos a, b de cada cable.

## Salida

N líneas con las coordenadas de los ordenadores 1 a N. Se acepta
cualquier colocación válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 2
2 3
```

Salida:

```
0 0
10 0
0 10
```

## Solución

Se enraíza el árbol en el ordenador 1 y se recorre en profundidad. Cada
ordenador va a la columna que indica su lugar en ese recorrido,
x = 2 · índice − 999, y a la fila que indica su profundidad,
y = profundidad. Cada ordenador tiene su propia columna, a dos unidades
de la siguiente, así que todas las distancias son al menos 2, y todas
las coordenadas quedan en [−999, 999].

Los cables nunca se cruzan. Cada cable une un ordenador de una fila con
un hijo en la fila siguiente, así que dos cables solo pueden cruzarse
si están en la misma franja entre dos filas. El recorrido en
profundidad visita cada subárbol como un bloque de columnas
consecutivas, y los ordenadores de una misma fila tienen subárboles
disjuntos; por eso los cables que salen de dos ordenadores distintos de
una fila quedan en dos rangos de columnas disjuntos, y los que salen del
mismo ordenador solo comparten ese extremo. `O(N)`.

Detalles a tener en cuenta:

- un camino de 1000 ordenadores con raíz en un extremo alcanza una
  profundidad de 999 y cabe en los límites (prueba generada 8);
- con N = 1 no hay ningún cable (prueba 02);
- el recorrido debe ser iterativo o tener pila suficiente para una
  profundidad de 999.

Las pruebas se juzgan con un verificador que comprueba los límites, cada
par de puntos y cada par de cables, incluidos los cables que comparten
un extremo y se solapan.

## Notas por lenguaje

- Todos los lenguajes visitan los hijos en el orden de entrada y dan la
  misma colocación; el verificador también acepta otras respuestas válidas.
- Java guarda las listas de adyacencia en arreglos planos para caber en
  el corto límite de tiempo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1358_graphs.cpp](1358_graphs.cpp) | G++ 13.2 x64 | graphs | O(N) | AC | 0.015 s | 260 KB |
| [1358_graphs.go](1358_graphs.go) | Go 1.14 x64 | graphs | O(N) | AC | 0.031 s | 1208 KB |
| [1358_graphs.java](1358_graphs.java) | Java 1.8 | graphs | O(N) | AC | 0.140 s | 624 KB |
| [1358_graphs.py](1358_graphs.py) | Python 3.12 x64 | graphs | O(N) | AC | 0.093 s | 820 KB |
| [1358_graphs.rs](1358_graphs.rs) | Rust 1.75 x64 | graphs | O(N) | AC | 0.046 s | 308 KB |
