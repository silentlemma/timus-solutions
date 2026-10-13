# 1381. Cucarachas en el edificio

[Timus 1381](https://acm.timus.ru/problem.aspx?space=1&num=1381) · dificultad 3310 · graphs

Problema original de Andrew Rumyantsev, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un edificio infinito hacia arriba y hacia abajo tiene un piso por planta,
cada uno con 0 a N cucarachas, 0 ≤ N ≤ 30. Cada mes el número de un piso
pasa a ser una función dada de los números de ese piso y de los de abajo
y arriba el mes anterior; un piso vacío entre pisos vacíos sigue vacío.
¿Puede bajar el total de cucarachas en un mes, partiendo de alguna
disposición finita?
¿Puede subir? Hay que imprimir `=` si ninguna de las dos, `<` si solo
puede bajar, `>` si solo puede subir y `<>` si ambas.

Límite de tiempo: 1,5 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego N + 1 bloques de N + 1 líneas de N + 1 números: en la línea i
del bloque j, el número k-ésimo es el valor siguiente de un piso con j
cucarachas, i abajo y k arriba.

## Salida

`=`, `<`, `>` o `<>`.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
0 1
0 1

0 0
1 1
```

Salida:

```
=
```

### Ejemplo 2

Entrada:

```
2
0 0 0
0 0 0
0 0 0

1 1 1
1 1 1
1 1 1

2 2 2
2 2 2
2 2 0
```

Salida:

```
<
```

## Solución

Se leen las plantas de abajo arriba como una sucesión c, vacía fuera de
una parte finita. El total cambia en Σ (f(c₋, c, c₊) − c) sobre todas
las plantas, un término por planta. Cada par de plantas vecinas (a, b)
es un nodo de un grafo, y cada planta siguiente c un paso
(a, b) → (b, c) de peso f(a, b, c) − b. Una disposición finita es
entonces un camino cerrado por el nodo (0, 0), el par vacío, y su peso
es el cambio del total. Un piso vacío entre vacíos suma 0, así que las
partes vacías infinitas no cuentan.

Así que el total puede bajar justo cuando algún camino cerrado por
(0, 0) tiene peso negativo. Ese camino se parte en ciclos simples de la
parte del grafo a la que se llega desde (0, 0) y desde la que se vuelve.
Esa parte tiene un camino cerrado negativo justo cuando tiene un ciclo
negativo, que puede recorrerse tantas veces como haga falta. Se deja
solo esa parte y se busca un ciclo negativo con Bellman–Ford, empezando
con todos los nodos a distancia 0. El total puede subir justo cuando hay
un ciclo positivo: la misma búsqueda con los pesos cambiados de signo.
Hay (N + 1)² ≤ 961 nodos y (N + 1)³ ≤ 29 791 pasos. `O(N⁵)`.

Detalles a tener en cuenta:

- la tabla se indexa primero por el propio piso, luego por el de abajo
  y luego por el de arriba;
- un ciclo lejos de (0, 0) sí cuenta: cualquier par es alcanzable
  desde (0, 0) y puede volver;
- un desplazamiento, en el que cada piso copia al de arriba, conserva el
  total (prueba 08).

Las respuestas se compararon con probar todas las disposiciones de hasta
10 plantas para 500 reglas aleatorias con N = 1 o 2.

## Notas por lenguaje

- Python corta Bellman–Ford antes mirando cada ocho pasadas si hay un
  ciclo entre las últimas mejoras, que siempre es negativo; los demás
  lenguajes hacen hasta 961 pasadas normales.
- Python se ejecuta con PyPy: CPython excede el límite de 1,5 s en la
  prueba 7 del juez, y PyPy tarda unos 0,53 s en total.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1381_graphs.cpp](1381_graphs.cpp) | G++ 13.2 x64 | graphs | O(N⁵) | AC | 0.171 s | 1404 KB |
| [1381_graphs.go](1381_graphs.go) | Go 1.14 x64 | graphs | O(N⁵) | AC | 0.171 s | 8084 KB |
| [1381_graphs.java](1381_graphs.java) | Java 1.8 | graphs | O(N⁵) | AC | 0.421 s | 2776 KB |
| [1381_graphs.py](1381_graphs.py) | PyPy 3.10 x64 | graphs | O(N⁵) | AC | 0.531 s | 11224 KB |
| [1381_graphs.rs](1381_graphs.rs) | Rust 1.75 x64 | graphs | O(N⁵) | AC | 0.140 s | 2384 KB |
