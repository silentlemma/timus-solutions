# 1002. Escribir un número con la menor cantidad de palabras

[Timus 1002](https://acm.timus.ru/problem.aspx?space=1&num=1002) · dificultad 225 · dp, hashing, strings

Problema original de la Olimpiada Centroeuropea de Informática 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada letra latina minúscula representa una cifra según la tabla. Para una cadena de hasta 100 cifras y un diccionario de hasta 50000 palabras de 1–50 letras, concatena palabras reutilizables que formen la cadena con el mínimo número de palabras. Hay varios casos y como máximo 300 KB de entrada total. Conserva los ceros iniciales. Tiempo: 2 segundos. Memoria: 64 MB.

| Dígito | Letras |
|---|---|
| 0 | o q z |
| 1 | i j |
| 2 | a b c |
| 3 | d e f |
| 4 | g h |
| 5 | k l |
| 6 | m n |
| 7 | p r s |
| 8 | t u v |
| 9 | w x y |

## Entrada

Por caso: la cadena de cifras, el número de palabras y una palabra por línea. Una línea `-1` termina la entrada.

## Salida

Para cada caso, una secuencia mínima separada por espacios simples, o exactamente `No solution.` si no existe.

## Evaluación

Se acepta cualquier secuencia más corta: el verificador comprueba que las
palabras estén en el diccionario, que escriban el número y que no exista una
secuencia más corta.

## Ejemplos

### Ejemplo 1

Entrada:

```
8733
3
use
e
tree
12
2
ab
cd
-1
```

Salida:

```
tree
No solution.
```

### Ejemplo 2

Entrada:

```
22
4
ac
ba
b
c
-1
```

Salida:

```
ac
```

## Solución

Sea `best[i]` el mínimo de palabras que forman las primeras `i` cifras;
al inicio solo `best[0] = 0` es alcanzable. Desde cada posición alcanzable,
cualquier codificación de palabra que coincida con la subcadena siguiente
crea una arista de coste uno hasta su final. Las posiciones crecen:
recorrer prefijos calcula caminos mínimos en este DAG. Guardar la última
palabra permite reconstruir hacia atrás. Cualquier óptimo empatado sirve.

Las versiones sencillas guardan un mapa hash de codificación a una palabra
representativa; para codificaciones iguales basta cualquier representante.
Se consultan subcadenas de longitudes 1 a `W = 50`. Con longitud del número
`P` y total de letras del diccionario `T`, el tiempo esperado es
`O(T + P W²)` contando construcción y hashing de subcadenas; la memoria
depende del diccionario. Las cinco fuentes Accepted se conservan intactas.

## Soluciones optimizadas

Antes de leer el diccionario, construye un trie de las subcadenas del
propio NÚMERO de longitud hasta `W`, con como máximo `1 + P W` nodos.
Recorre cada codificación de palabra por él; si falta una arista,
descártala. Guarda un representante en cada terminal alcanzado. Las
palabras inútiles no crean nodos ni entradas persistentes: resulta útil
con diccionarios grandes que apenas coinciden con un número corto.

Durante la DP, sigue las cifras por el trie sin asignar ni hashear
subcadenas. Toda palabra utilizable está presente porque su codificación
es una subcadena del número, y todo terminal retenido corresponde a una
palabra real. Se conservan las aristas y el óptimo de la DP. La longitud
de la palabra elegida determina la posición anterior al reconstruir.

Con diez cifras fijas, tiempo `O(T + P W)` y memoria de trabajo
`O(P W + R)`, siendo `R` el texto de representantes guardados, más los
búferes. C++ usa un pool estático acotado y limpia los nodos del caso
anterior; ese coste se suma entre casos. Go y Rust leen palabras en flujo;
Java reutiliza el búfer de tokens, pero acumula líneas de salida. Python
usa transiciones enteras planas. Es otro algoritmo, con etiquetas
`dp, strings`, sin el sufijo `_optimized`.

Las cinco versiones cumplen por reducción medida de memoria frente al
hashing original del mismo lenguaje. Las diferencias cercanas a un tick
del temporizador no se consideran prueba fiable de aceleración.

Reducción medida de memoria: C++ 83.1%, Go 57.0%, Java 89.9%, Python 82.5%, Rust 76.7%. Cada fuente tiene su propio Accepted con ID en la tabla.

## Notas por lenguaje

Python se comprobó en 1802 casos con un BFS independiente de posiciones
que prueba cada palabra completa. Se verifican pertenencia al diccionario,
codificación y número mínimo, permitiendo empates. Hay colisiones de
codificación, reutilización, imposibilidad, ceros iniciales, palabras de
50 letras, diccionarios grandes irrelevantes y alternancia de casos grandes
y pequeños. El flujo fuzz concatenado supera intencionadamente el límite
total normal: es una prueba adicional de reinicio y semántica, no una
entrada declarada válida de 300 KB. Los cinco programas reales también
superaron 14 entradas del repositorio en Docker.

La tabla muestra la instantánea filtrada del 2 de noviembre de 2026.
Un asterisco indica objetivo de clasificación pendiente pese a una mejora
real. Una muestra vacía no demuestra superioridad competitiva.

| Lenguaje | Puesto en tiempo | Puesto en memoria | Registros de otros autores (tiempo / memoria) |
|---|---|---|---|
| C++ | 1 | 3 | 198 / 198 |
| Go | 1 | 1 | 4 / 4 |
| Java | 2 | 1 | 8 / 8 |
| Python | 1 | 1 | 49 / 49 |
| Rust | 4 | 1 | 3 / 3 |

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1002_dp_hashing.cpp](1002_dp_hashing.cpp) | G++ 13.2 x64 | dp, hashing | O(T + P W^2) expected | AC | 0.015 s | 2764 KB | 11277423 |
| [1002_dp_hashing.go](1002_dp_hashing.go) | Go 1.14 x64 | dp, hashing | O(T + P W^2) expected | AC | 0.031 s | 3016 KB | 11277424 |
| [1002_dp_hashing.java](1002_dp_hashing.java) | Java 1.8 | dp, hashing | O(T + P W^2) expected | AC | 0.109 s | 7032 KB | 11277426 |
| [1002_dp_hashing.py](1002_dp_hashing.py) | Python 3.12 x64 | dp, hashing | O(T + P W^2) expected | AC | 0.093 s | 5424 KB | 11277425 |
| [1002_dp_hashing.rs](1002_dp_hashing.rs) | Rust 1.75 x64 | dp, hashing | O(T + P W^2) expected | AC | 0.031 s | 2540 KB | 11277427 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1002_dp_strings.cpp](1002_dp_strings.cpp) | G++ 13.2 x64 | dp, strings | O(T + P W) | AC | 0.015 s | 468 KB | 11308088 |
| [1002_dp_strings.go](1002_dp_strings.go) | Go 1.14 x64 | dp, strings | O(T + P W) | AC | 0.031 s | 1296 KB | 11308089 |
| [1002_dp_strings.java](1002_dp_strings.java) \* | Java 1.8 | dp, strings | O(T + P W) | AC | 0.093 s | 712 KB | 11308092 |
| [1002_dp_strings.py](1002_dp_strings.py) | Python 3.12 x64 | dp, strings | O(T + P W) | AC | 0.078 s | 948 KB | 11308086 |
| [1002_dp_strings.rs](1002_dp_strings.rs) \* | Rust 1.75 x64 | dp, strings | O(T + P W) | AC | 0.031 s | 592 KB | 11308095 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
