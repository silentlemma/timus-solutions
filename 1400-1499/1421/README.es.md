# 1421. Operaciones de crédito

[Timus 1421](https://acm.timus.ru/problem.aspx?space=1&num=1421) · dificultad 539 · greedy

Problema original de Ilya Grebnov, Dmitry Kovalioff y Nikita Rybak, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Llenar una matriz N × N (2 ≤ N ≤ 100) con enteros de 0 a 100 de modo que
la fila i sume SR[i] y la columna j sume SC[j] (cada suma de 0 a
32 000, con totales iguales). Hay que imprimir «YES» y una matriz así, o
«NO» si no existe.

Límite de tiempo: 0.25 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego las N sumas de filas, luego las N sumas de columnas.

## Salida

«NO», o «YES» y la matriz.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
267 157 188 259
193 320 346 12
```

Salida:

```
YES
100 55 100 12
0 70 87 0
0 95 93 0
93 100 66 0
```

## Solución

Se llenan las filas una a una, tomando cada vez los créditos de las
columnas que aún necesitan más. Para una fila que necesita r, se bajan
las necesidades de todas las columnas hacia un nivel común L: la
columna j da min(100, max(0, SC[j] − L)). Lo que se da disminuye al
crecer L, así que una búsqueda binaria halla el menor L que da como
mucho r, y las pocas unidades que faltan salen, una por columna, de las
columnas que están justo en el nivel L. Si ni siquiera L = 0 da r, la
respuesta es «NO».

Por qué esto nunca estropea una solución: supongamos que existe una
matriz, pero su primera fila deja a la columna j al menos 2 más que a la
columna k, aunque la fila podría tomar una unidad más de j y toma algo
de k. Entonces el resto de la columna j suma más que el de la columna
k, y alguna fila de abajo tiene más en j que en k. Pasar una unidad de k
a j en la primera fila, y al revés en esa otra fila, conserva todas las
sumas y los límites y deja las necesidades restantes estrictamente más
igualadas. Repitiéndolo se llega a la fila equilibrada que construye el
voraz, y el problema restante solo depende del multiconjunto de
necesidades de las columnas, así que el voraz conserva una solución
siempre que exista. `O(N² log S)`.

Detalles a tener en cuenta:

- cada fila y cada columna pueden caber por separado mientras que dos
  filas juntas no, así que no basta con comprobar líneas sueltas
  (prueba 06);
- se acepta cualquier matriz válida, así que las pruebas usan un
  verificador (prueba 01);
- una fila que necesita más de 100 por columna es imposible de entrada
  (pruebas 03, 08).

## Soluciones optimizadas

Rust conserva greedy por nivel y prueba de intercambio. Sumas≤32000 usan16 bits, créditos≤100 un byte. N≤100 permite matriz fija10000 bytes y márgenes400, sin vectores por fila ni cadenas por número. Rechazar margen>100N es necesario pero no suficiente; conservar las demás comprobaciones y omitir filas cero. Buscar nivel hasta el máximo residual actual, repartir contribuciones/resto empatado y restar columnas inmediatamente. Si L > 0, al bajar a L − 1 cada columna elegible aporta una unidad más. La minimalidad de L garantiza que bastan. Con L = 0 la suma de la fila ya es exacta.

Compárese el objetivo con los residuos tras esta fila en una matriz factible. Un exceso respecto al objetivo implica un residuo de al menos L, y un defecto uno de como máximo L − 1, porque cada objetivo ajusta L o L − 1 al intervalo de su columna. Alguna fila posterior tiene más en la columna con exceso que en la deficitaria. Intercambiar una unidad entre ambas columnas en las dos filas, en sentidos opuestos, mantiene sumas y cotas y acerca los residuos a sus objetivos. Repetir hasta alcanzar el vector exacto.

Exigir residuos cero antes de YES, sin matriz parcial al fallar. E/S C de caracteres y entrada C imprimen enteros directos. Tiempo O(N² log S), S=max(2,máximo inicial), memoria O(N²) con límites fijos. Se conservan bases; C++/Go/Java/Python reutilizan las admitidas.

El envío aceptado en Rust 1.75 x64 tarda 0.062 s frente a 0.031 s de la base y usa 84 KB frente a 336 KB.

Las implementaciones base aceptadas [1421_greedy.cpp](1421_greedy.cpp), [1421_greedy.go](1421_greedy.go), [1421_greedy.java](1421_greedy.java), [1421_greedy.py](1421_greedy.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1421_greedy.cpp](1421_greedy.cpp) | G++ 13.2 x64 | greedy | O(N^2 log S) | AC | 0.015 s | 268 KB | 11286140 |
| [1421_greedy.go](1421_greedy.go) | Go 1.14 x64 | greedy | O(N^2 log S) | AC | 0.031 s | 1188 KB | 11286141 |
| [1421_greedy.java](1421_greedy.java) | Java 1.8 | greedy | O(N^2 log S) | AC | 0.093 s | 832 KB | 11286146 |
| [1421_greedy.py](1421_greedy.py) \* | Python 3.12 x64 | greedy | O(N^2 log S) | AC | 0.171 s | 760 KB | 11286142 |
| [1421_greedy.rs](1421_greedy.rs) | Rust 1.75 x64 | greedy | O(N^2 log S) | AC | 0.031 s | 336 KB | 11286147 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1421_greedy_optimized.rs](1421_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N² log S) | AC | 0.062 s | 84 KB | 11315704 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
