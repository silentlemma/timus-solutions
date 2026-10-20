# 2205. El ancestro común más bajo en el árbol de mayores divisores propios

[Timus 2205](https://acm.timus.ru/problem.aspx?space=1&num=2205) · dificultad 818 · number_theory

Problema original de Vadim Barinov, de la Olimpiada Académica Universitaria Escolar de Informática 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos números naturales distintos están unidos cuando uno es el mayor
divisor propio del otro. Un camino es una sucesión de números distintos
con los consecutivos unidos, y su precio es su menor número. Para cada
uno de N pares (a, b), imprimir el mayor precio de un camino de a a b, o
−1 si no hay ninguno. Los límites son 2 segundos y 256 MB.

## Entrada

N, 1 ≤ N ≤ 5 · 10⁵, y luego N pares con 1 ≤ a, b ≤ 10⁷.

## Salida

La respuesta para cada par.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
4 4
4 5
4 6
```

Salida:

```
4
1
1
```

## Solución

El mayor divisor propio de n > 1 es n / p para su menor factor primo p,
así que todo número mayor que 1 tiene exactamente un vecino menor: las
uniones forman un árbol con raíz 1, y cada par tiene exactamente un
camino. Los valores solo bajan hacia la raíz, así que el menor número
del camino es el ancestro común más bajo, y −1 nunca ocurre.

Se escriben los factores primos de a en orden decreciente. Sus
ancestros quitan los factores menores de uno en uno, así que son
exactamente los productos de los primeros factores de esa lista. El
ancestro común es entonces el producto del comienzo común más largo de
las dos listas decrecientes.

Ese producto sale de g = gcd(a, b). Sea t el mayor factor primo de a / g
o de b / g. Todo primo mayor que t tiene el mismo exponente en a y en b,
y el propio t aparece en g con el menor de sus dos exponentes, que es
donde las listas empiezan a diferir. Por debajo de t las listas ya se
han separado. Así que la respuesta es g sin todos sus factores primos
menores que t; si a = b es el propio a, y si g = 1 es 1.

Una criba de menores factores primos impares hasta 10⁷, guardada solo
para los impares, da cualquier factorización, y las potencias de 2 se
quitan con un truco de bits.

En el ejemplo 4 = 2 · 2 y 6 = 3 · 2 difieren ya en el mayor factor, así
que su ancestro común es 1.

La criba cuesta O(V log log V) con V = 10⁷, y cada consulta O(log V).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2205_number_theory.cpp](2205_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(V log log V + N log V) | AC | 0.343 s | 13416 KB |
| [2205_number_theory.go](2205_number_theory.go) | Go 1.14 x64 | number_theory | O(V log log V + N log V) | AC | 0.312 s | 54196 KB |
| [2205_number_theory.java](2205_number_theory.java) | Java 1.8 | number_theory | O(V log log V + N log V) | AC | 0.390 s | 19488 KB |
| [2205_number_theory.py](2205_number_theory.py) | PyPy 3.10 x64 | number_theory | O(V log log V + N log V) | AC | 1.921 s | 109108 KB |
| [2205_number_theory.rs](2205_number_theory.rs) | Rust 1.75 x64 | number_theory | O(V log log V + N log V) | AC | 0.234 s | 36432 KB |
