# 2203. Contar viajes a la tienda cuando dos ingredientes se acaban a su propio ritmo

[Timus 2203](https://acm.timus.ru/problem.aspx?space=1&num=2203) · dificultad 1097 · math, number_theory

Problema original de Valentin Zuev, de la Olimpiada Académica Universitaria Escolar de Informática 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un bocadillo necesita A gramos de pan y B gramos de salchichón, que se
venden en barras de X gramos y piezas de Y gramos. Cuando las
existencias no alcanzan para el siguiente bocadillo, un viaje compra el
menor número de barras y piezas que lo permite. Empezando sin nada y
haciendo N bocadillos, ¿cuántos viajes hay? Los límites son 1 segundo y
256 MB.

## Entrada

A, B, X, Y y N, 1 ≤ A, B ≤ 100, 1 ≤ X, Y, N ≤ 10⁹.

## Salida

El número de viajes.

## Ejemplos

### Ejemplo 1

Entrada:

```
30 20 90 30 4
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
5 6 7 72 100
```

Salida:

```
74
```

### Ejemplo 3

Entrada:

```
99 100 37 47 1000000000
```

Salida:

```
1000000000
```

## Solución

Si X ≤ A, lo que sobra es menos de una barra y por tanto menos de lo que
pide un bocadillo, así que cada bocadillo necesita un viaje; lo mismo
con Y ≤ B. Entonces la respuesta es N.

Si no, cada viaje compra a lo sumo una barra. Numerando los bocadillos
desde 0, la barra j (desde 0) se compra antes del bocadillo k
exactamente cuando por primera vez (k + 1)A > jX, es decir,
k = ⌊jX / A⌋. Con g = gcd(A, X), P = X / g y E = A / g, los viajes por
pan son ⌊jP / E⌋, un patrón de E viajes que se repite cada P bocadillos,
y por debajo de N hay ⌈NA / X⌉. Los viajes por salchichón funcionan
igual con sus propios P' y E'.

Un viaje compra ambas cosas cuando un índice de bocadillo está en los
dos patrones, y la respuesta es los viajes por pan más los viajes por
salchichón menos esos compartidos. Para cada uno de los E · E' ≤ 10⁴
pares de restos r = ⌊iP / E⌋ y r' = ⌊jP' / E'⌋, los índices
r + sP = r' + tP' forman, por el teorema chino del resto, o bien nada
(cuando gcd(P, P') no divide r' − r) o bien una progresión aritmética de
paso lcm(P, P'), cuyos términos menores que N se cuentan directamente.

En el primer ejemplo los viajes por pan son 0 y 3 y los de salchichón
0, 1 y 3, así que los compartidos son 0 y 3 y la respuesta es
2 + 3 − 2 = 3.

Esto cuesta O(AB + log XY).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2203_math_number_theory.cpp](2203_math_number_theory.cpp) | G++ 13.2 x64 | math, number_theory | O(AB + log XY) | AC | 0.015 s | 184 KB |
| [2203_math_number_theory.go](2203_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(AB + log XY) | AC | 0.031 s | 912 KB |
| [2203_math_number_theory.java](2203_math_number_theory.java) | Java 1.8 | math, number_theory | O(AB + log XY) | AC | 0.093 s | 172 KB |
| [2203_math_number_theory.py](2203_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(AB + log XY) | AC | 0.093 s | 324 KB |
| [2203_math_number_theory.rs](2203_math_number_theory.rs) | Rust 1.75 x64 | math, number_theory | O(AB + log XY) | AC | 0.031 s | 20 KB |
