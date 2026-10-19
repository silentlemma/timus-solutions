# 1870. Zinium 2

[Timus 1870](https://acm.timus.ru/problem.aspx?space=1&num=1870) · dificultad 714 · constructive

Problema original de Igor Chevdar (preparado por Eugene Kurpilyanskiy), del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Colocar n reinas en un tablero toroidal n × n (la fila de arriba está
pegada a la de abajo y la columna izquierda a la derecha, así que las
diagonales dan la vuelta) de modo que ninguna ataque a otra, o decir
que es imposible.

## Entrada

n (4 ≤ n ≤ 10⁵).

## Salida

"Yes" y, para x = 1, …, n, la fila de la reina de la columna x; o "No".
Se acepta cualquier colocación válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
```

Salida:

```
Yes
2 4 1 3 5
```

### Ejemplo 2

Entrada:

```
8
```

Salida:

```
No
```

## Solución

Se numeran filas y columnas desde 0. En el toro dos reinas se atacan
cuando comparten x, y, x + y mod n o x − y mod n, así que cada una de
estas cantidades debe tomar cada valor una vez.

Si n es coprimo con 6, la reina de la columna i va a la fila 2i mod n.
Las filas 2i, las sumas 3i y las diferencias −i son todas distintas
porque 2 y 3 son invertibles módulo n.

Si no, no hay colocación. Si n es par, se suma x + y sobre todas las
reinas. Como las sumas toman cada resto una vez, el total es
n(n − 1)/2 ≡ n/2 (mod n). Pero también es Σx + Σy = n(n − 1) ≡ 0, una
contradicción. Si 3 divide a n (y n es impar), se suman los cuadrados.
Como (x + y)² + (x − y)² = 2x² + 2y², la suma S de los cuadrados de
todos los restos cumple S + S ≡ 2S + 2S, es decir 2S ≡ 0 (mod n). Con
S = (n − 1)n(2n − 1)/6 esto exige que 3 divida a (n − 1)(2n − 1), pero
ambos factores dan 2 módulo 3. `O(n)`.

Para el primer ejemplo las filas, contando desde 1, son 1, 3, 5, 2, 4,
otra respuesta válida.

Trampas:

- la respuesta depende de n módulo 6, no de que n sea primo: 35 tiene
  colocación, 9 y 8 no;
- el paso 2 es el menor que funciona; el paso 1 pone todas las reinas
  en una diagonal;
- la salida tiene hasta 10⁵ números, así que conviene construirla de
  una vez.

Las colocaciones pasan un comprobador para cada n de 4 a 400 y para los
n más grandes, y las respuestas "No" coinciden con una implementación
aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1870_constructive.cpp](1870_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 1520 KB |
| [1870_constructive.go](1870_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1656 KB |
| [1870_constructive.java](1870_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.109 s | 5372 KB |
| [1870_constructive.py](1870_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.125 s | 7276 KB |
| [1870_constructive.rs](1870_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 5832 KB |
