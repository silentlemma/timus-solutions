# 2122. Distancia de Hamming total entre subsecuencias de cada longitud

[Timus 2122](https://acm.timus.ru/problem.aspx?space=1&num=2122) · dificultad 3528 · math, combinatorics

Problema original de Alexey Danilyuk y Oleg Merkurev, del concurso t.me/umnik_team, campamento de Petrozavodsk, verano de 2018.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para una cadena binaria s de longitud n y cada k de 1 a n, tomar todas
las subsecuencias de longitud k (elegidas por posiciones) y sumar las
distancias de Hamming de todos sus pares no ordenados. Imprimir las n
sumas módulo 40 961. Los límites son 4 segundos y 256 MB.

## Entrada

La cadena s, 1 ≤ n ≤ 4000.

## Salida

n números, las sumas para k = 1 … n módulo 40 961.

## Ejemplos

### Ejemplo 1

Entrada:

```
11000110111001
```

Salida:

```
48 4056 15326 31033 20654 29362 32472 13700 21357 12217 20411 12456 212 0
```

### Ejemplo 2

Entrada:

```
000
```

Salida:

```
0 0 0
```

## Solución

Se fija k y una posición j de las subsecuencias. Si c_j de las C(n, k)
subsecuencias tienen un 1 en la posición j, esa posición aporta
c_j · (C(n, k) − c_j) pares distintos. Sumando sobre j,

answer(k) = C(n, k) · Σ c_j − Σ c_j².

Σ c_j cuenta los unos dentro de todas las subsecuencias, y cada 1 de s
está en C(n − 1, k − 1) de ellas, así que
Σ c_j = (número de unos) · C(n − 1, k − 1). Solo Σ c_j²
requiere trabajo.

En lugar de elegir posiciones, se borran n − k de ellas una a una.
Entonces cada subsecuencia aparece (n − k)! veces, una por orden de
borrado, y r_k(j) = c_j · (n − k)! cuenta los órdenes de borrado. Al
pasar de longitud k + 1 a k (posiciones desde 0), el elemento de la
posición j se queda cuando se borra uno de los k − j elementos
posteriores, y el de la posición j + 1 pasa a j cuando se borra uno de
los j + 1 primeros:

r_k(j) = (k − j) · r_{k+1}(j) + (j + 1) · r_{k+1}(j + 1).

Empezando por r_n = s, cada longitud cuesta O(k), O(n²) en total. Los
demás términos se escalan igual, y al final toda la expresión se divide
entre ((n − k)!)². El módulo 40 961 es un primo mayor que 4000, así que
esos factoriales son invertibles.

En el segundo ejemplo todas las subsecuencias son iguales, así que cada
suma es 0.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2122_math_combinatorics.cpp](2122_math_combinatorics.cpp) | G++ 13.2 x64 | math, combinatorics | O(n^2) | AC | 0.031 s | 464 KB |
| [2122_math_combinatorics.go](2122_math_combinatorics.go) | Go 1.14 x64 | math, combinatorics | O(n^2) | AC | 0.046 s | 1272 KB |
| [2122_math_combinatorics.java](2122_math_combinatorics.java) | Java 1.8 | math, combinatorics | O(n^2) | AC | 0.156 s | 740 KB |
| [2122_math_combinatorics.py](2122_math_combinatorics.py) | Python 3.12 x64 | math, combinatorics | O(n^2) | AC | 3.453 s | 1228 KB |
| [2122_math_combinatorics.rs](2122_math_combinatorics.rs) | Rust 1.75 x64 | math, combinatorics | O(n^2) | AC | 0.015 s | 308 KB |
