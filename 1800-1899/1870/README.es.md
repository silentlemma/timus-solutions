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
- la salida tiene hasta 10⁵ números. Un búfer permite escribirlos
  por bloques.

Las colocaciones pasan un comprobador para cada n de 4 a 400 y para los
n más grandes, y las respuestas "No" coinciden con una implementación
aceptada independiente.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321969 · Java 1.8 №11321970 · Go 1.14 x64 №11322301 · Python 3.12 x64 №11322302 · Rust 1.75 x64 №11322303.

## Soluciones optimizadas

Las versiones optimizadas imprimen los números de fila impares y luego los pares mediante un búfer pequeño. Es el orden de 2i módulo n con numeración desde uno y no requiere guardar toda la disposición.

Rust 1.75 x64, envío 11322002. Tiempo 0,031 → 0,015 s, memoria 5812 → 200 KB.

Python 3.12 x64, envío 11322003. Tiempo 0,093 → 0,109 s, memoria 6424 → 824 KB.

Go 1.14 x64, envío 11322004. Tiempo 0,031 → 0,031 s, memoria 1632 → 924 KB.

Java 1.8, envío 11322005. Tiempo 0,109 → 0,093 s, memoria 5368 → 504 KB.

G++ 13.2 x64, envío 11322006. Tiempo 0,015 → 0,015 s, memoria 1504 → 112 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1870_constructive.cpp](1870_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 1504 KB | 11321969 |
| [1870_constructive.go](1870_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1632 KB | 11322301 |
| [1870_constructive.java](1870_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.109 s | 5368 KB | 11321970 |
| [1870_constructive.py](1870_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.093 s | 6424 KB | 11322302 |
| [1870_constructive.rs](1870_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 5812 KB | 11322303 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1870_constructive_optimized.rs](1870_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.015 s | 200 KB | 11322002 |
| [1870_constructive_optimized.py](1870_constructive_optimized.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.109 s | 824 KB | 11322003 |
| [1870_constructive_optimized.go](1870_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 924 KB | 11322004 |
| [1870_constructive_optimized.java](1870_constructive_optimized.java) | Java 1.8 | constructive | O(n) | AC | 0.093 s | 504 KB | 11322005 |
| [1870_constructive_optimized.cpp](1870_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 112 KB | 11322006 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
