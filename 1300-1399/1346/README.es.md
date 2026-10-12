# 1346. Intervalos de monotonía

[Timus 1346](https://acm.timus.ru/problem.aspx?space=1&num=1346) · dificultad 297 · greedy

Problema original de Alexander Klepinin, del USU Championship 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una función F está dada en la rejilla entera A, A + 1, …, B, con
0 ≤ A < B ≤ 100 000 y valores de −100 000 a 100 000. Hay que partir la
rejilla en el menor número de intervalos en cada uno de los cuales F no
decrece o no crece, e imprimir cuántos son.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

A y B, luego los valores F(A), …, F(B), separados por espacios o saltos
de línea.

## Salida

El menor número de intervalos.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 10
1 2 3 4 2 1 -1 3 6 7
```

Salida:

```
3
```

## Solución

Los intervalos reparten los puntos de la rejilla, así que el paso entre
el último punto de un intervalo y el primero del siguiente es libre.
Cualquier parte de un intervalo monótono vuelve a ser monótona. Por eso
nunca estorba alargar el primer intervalo todo lo posible, y lo mismo
vale para cada siguiente: el conteo voraz es el mínimo.

Un intervalo se alarga mientras siga siendo monótono. Su sentido lo
fija su primer paso que no es plano, y los pasos planos valen para
cualquier sentido. El primer paso contra ese sentido acaba el
intervalo, y el siguiente empieza en el punto siguiente. `O(B − A)`.

Detalles a tener en cuenta:

- el paso entre dos intervalos es libre: 1 3 2 4 solo necesita 2
  intervalos, 1 3 y 2 4 (prueba 02);
- los pasos planos pertenecen al intervalo vaya en el sentido que vaya,
  y una función constante es un solo intervalo (pruebas 03, 05 y 06);
- los valores pueden venir en varias líneas.

Los conteos se compararon con una programación dinámica sobre todos los
repartos en 500 funciones aleatorias de hasta 12 puntos.

## Notas por lenguaje

- Las cinco soluciones hacen la misma pasada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1346_greedy.cpp](1346_greedy.cpp) | G++ 13.2 x64 | greedy | O(B - A) | AC | 0.062 s | 588 KB |
| [1346_greedy.go](1346_greedy.go) | Go 1.14 x64 | greedy | O(B - A) | AC | 0.031 s | 2512 KB |
| [1346_greedy.java](1346_greedy.java) | Java 1.8 | greedy | O(B - A) | AC | 0.109 s | 900 KB |
| [1346_greedy.py](1346_greedy.py) | Python 3.12 x64 | greedy | O(B - A) | AC | 0.140 s | 11140 KB |
| [1346_greedy.rs](1346_greedy.rs) | Rust 1.75 x64 | greedy | O(B - A) | AC | 0.015 s | 2632 KB |
