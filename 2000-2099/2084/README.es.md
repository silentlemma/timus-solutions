# 2084. Ordenar tareas que pagan una deuda

[Timus 2084](https://acm.timus.ru/problem.aspx?space=1&num=2084) · dificultad 3112 · dp, sorting

Problema original de Nikita Burlakov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una deuda empieza en X. Cada una de N tareas primero baja la deuda en aᵢ
(sin bajar de cero) y luego gana max(0, bᵢ − D), donde D es la deuda en
ese momento. Hallar el orden de las tareas con el mayor total e
imprimirlo. Los límites son 2 segundos y 256 MB.

## Entrada

X y N, 0 ≤ X ≤ 100, 1 ≤ N ≤ 200, y después a₁ … a_N (de 0 a 100) y
b₁ … b_N (de 0 a 10⁶).

## Salida

El mayor total y después un orden de las tareas que lo consigue. Se
acepta cualquier orden así.

## Evaluación

Un comprobador compara el total y reproduce el orden impreso.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
0 1 5
5 1 0
```

Salida:

```
6
3 2 1
```

### Ejemplo 2

Entrada:

```
4 4
3 0 1 2
7 8 2 3
```

Salida:

```
19
1 4 3 2
```

## Solución

La deuda nunca supera X, así que una tarea con b > X siempre gana b − X
más que la misma tarea con b = X; esa parte se suma al final, y desde
entonces todo b es a lo sumo X. Sea rᵢ la reparación total hecha hasta
la tarea i incluida. Entonces la deuda es X − min(X, rᵢ), y la tarea
gana max(0, min(X, rᵢ) − (X − bᵢ)).

Se toma un orden óptimo y se llaman abandonadas las tareas que no ganan
nada. Moverlas al principio solo aumenta la reparación que ven las
demás, así que las abandonadas pueden ir primero. Cada una de las demás
gana entonces min(X, rᵢ) − (X − bᵢ), y la suma de las segundas partes no
depende del orden. Las primeras partes son las sumas de prefijos de las
reparaciones, que son máximas en cada posición cuando las tareas van por
a decreciente. A la inversa, para cualquier conjunto de abandonadas ese
orden gana al menos la fórmula, porque una tarea real nunca gana menos de
cero. Así que la respuesta es el mejor valor de la fórmula sobre todos
los conjuntos de abandonadas.

Se ordenan las tareas por a creciente. Con las conservadas en orden
decreciente tras las abandonadas, la tarea k ve las abandonadas
anteriores a ella en la lista ordenada más todas las tareas desde k. Así
que una DP sobre la lista ordenada guarda s, la reparación de las
abandonadas hasta ahora (con tope X, pues valores mayores no cambian
nada): una tarea conservada gana min(X, s + suffix_k) − (X − b_k), una
abandonada suma su a a s. Las elecciones guardadas dan el orden: primero
las abandonadas y luego las conservadas por a decreciente. Es O(N · X).

En el primer ejemplo la tercera tarea repara primero las 5 unidades, y
luego la segunda y la primera ganan 1 y 5: 6 en total.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2084_dp.cpp](2084_dp.cpp) | G++ 13.2 x64 | dp | O(N X) | AC | 0.015 s | 268 KB |
| [2084_dp.go](2084_dp.go) | Go 1.14 x64 | dp | O(N X) | AC | 0.031 s | 1740 KB |
| [2084_dp.java](2084_dp.java) | Java 1.8 | dp | O(N X) | AC | 0.156 s | 4360 KB |
| [2084_dp.py](2084_dp.py) | Python 3.12 x64 | dp | O(N X) | AC | 0.125 s | 1988 KB |
| [2084_dp.rs](2084_dp.rs) | Rust 1.75 x64 | dp | O(N X) | AC | 0.046 s | 480 KB |
