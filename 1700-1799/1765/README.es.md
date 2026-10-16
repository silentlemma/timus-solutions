# 1765. Error 404

[Timus 1765](https://acm.timus.ru/problem.aspx?space=1&num=1765) · dificultad 4004 · number_theory

Problema original de Igor Chevdar (idea de Dmitry Poletayev), del XIV Campeonato de los Urales de Programación Competitiva, 10 de abril de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una turbina tenía n álabes cuyas puntas formaban un n-ágono regular; k
de ellos se rompieron. Quitar el menor número posible de los álabes
restantes para que el centro de masas de los que quedan esté en el eje,
dejando al menos un álabe. n tiene a lo sumo dos factores primos
distintos.

## Entrada

n y k (3 ≤ n ≤ 20000, 1 ≤ k ≤ n − 1) y luego los números de los álabes
rotos en orden creciente; los álabes se numeran de 1 a n alrededor del
círculo.

## Salida

El número de álabes que se quitan y sus números en cualquier orden, o
−1 si no se puede dejar un conjunto equilibrado. Se acepta cualquier
respuesta óptima.

## Ejemplos

### Ejemplo 1

Entrada:

```
12 3
3 4 12
```

Salida:

```
2
8 9
```

### Ejemplo 2

Entrada:

```
3 1
1
```

Salida:

```
-1
```

## Solución

Las puntas son las raíces n-ésimas de la unidad, y los álabes que
quedan están equilibrados cuando la suma de sus puntas es cero. Para n
con a lo sumo dos factores primos p y q, un teorema de de Bruijn sobre
sumas nulas de raíces de la unidad dice que ese conjunto de puntas es
una unión de p-ágonos y q-ágonos regulares disjuntos. Así que hay que
conservar tantos álabes enteros como se pueda en esos polígonos.

Cada polígono queda entre los álabes con el mismo resto módulo n/(pq).
Esos pq álabes forman una cuadrícula de p por q, con el álabe t del
grupo en la fila t mod p y la columna t mod q: un q-ágono es una fila y
un p-ágono una columna. Una fila y una columna siempre se cruzan, así
que en un grupo se conservan o bien todas las filas sin álabes rotos o
bien todas esas columnas, lo que dé más; los demás álabes enteros del
grupo se quitan. Con un solo factor primo solo existen los p-ágonos, y
un grupo se conserva justo cuando ninguno de sus álabes está roto. Si
no se conserva nada, la respuesta es −1. `O(n + √n)`.

En el primer ejemplo p = 2 y q = 3. Entre los álabes impares, el 3 roto
estropea un triángulo y un diámetro; conservar los dos diámetros
enteros (1, 7 y 5, 11) gana a conservar un triángulo, así que se quita
el 9. Entre los pares, 4 y 12 estropean un triángulo y dos diámetros; el
otro triángulo, 2, 6 y 10, se queda, así que se quita el 8.

Trampas:

- con un solo factor primo, un álabe suelto no es un conjunto
  equilibrado;
- no se pueden conservar a la vez una fila y una columna, pues
  comparten un álabe;
- si ningún polígono está entero, habría que quitar todos los álabes,
  lo que no está permitido: la respuesta es −1.

Las respuestas coinciden con una búsqueda sobre todos los subconjuntos
de álabes enteros, sumando las puntas, en 250 casos aleatorios de hasta
16 álabes, y dan el mismo número de álabes que una implementación
aceptada independiente en 100 casos aleatorios de hasta 20000 álabes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1765_number_theory.cpp](1765_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n + sqrt(n)) | AC | 0.031 s | 288 KB |
| [1765_number_theory.go](1765_number_theory.go) | Go 1.14 x64 | number_theory | O(n + sqrt(n)) | AC | 0.031 s | 2020 KB |
| [1765_number_theory.java](1765_number_theory.java) | Java 1.8 | number_theory | O(n + sqrt(n)) | AC | 0.140 s | 3204 KB |
| [1765_number_theory.py](1765_number_theory.py) | Python 3.12 x64 | number_theory | O(n + sqrt(n)) | AC | 0.093 s | 3452 KB |
| [1765_number_theory.rs](1765_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n + sqrt(n)) | AC | 0.031 s | 1160 KB |
