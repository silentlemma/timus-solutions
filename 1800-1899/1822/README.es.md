# 1822. La guerra de Hugo II

[Timus 1822](https://acm.timus.ru/problem.aspx?space=1&num=1822) · dificultad 686 · binary_search

Problema original de Kirill Butin, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los nobles de un reino forman un árbol bajo el rey, el noble 1. Una
orden con un número x baja desde el rey. Un noble sin vasallos reúne
sus tropas enseguida, en tᵢ días. Un noble con vasallos espera a que
estén listos al menos el x% de sus vasallos directos y luego reúne
tropas en tᵢ días. El rey parte en cuanto está listo al menos el x% de
sus vasallos directos. Hallar el mayor x con el que el rey parte en no
más de t días.

## Entrada

n y t (1 ≤ n ≤ 10⁴, 0 ≤ t ≤ 10⁶), luego, para los nobles 2, …, n, el
señor pᵢ y los días tᵢ (0 ≤ tᵢ ≤ 100).

## Salida

El mayor x, con error absoluto de como mucho 10⁻⁴.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 3
1 2
2 2
2 1
1 2
1 4
```

Salida:

```
50.00000000
```

## Solución

Con x fijo, un noble con c vasallos espera a ⌈x·c/100⌉ de ellos, es
decir, al ⌈x·c/100⌉-ésimo menor de sus días de preparación, y queda
listo tᵢ días después; una pasada de las hojas hacia arriba da el día
del rey. Un x mayor nunca acelera a nadie, así que los x factibles
forman un intervalo [0, X].

Dentro de él solo importan los valores ⌈x·c/100⌉, que cambian solo en
fracciones m/c, con c un número de vasallos directos. Así que el propio
X es 100·m/c para alguna de esas fracciones. Se reúnen las fracciones de
cada c distinto, se ordenan y se busca en binario la última que el rey
alcanza, comprobando cada una con enteros exactos. C++, Go, Java y Rust
ordenan por producto cruzado; Python, por el valor m/c en coma flotante.
Las fracciones distintas difieren al menos en 1/9999², por lo que esa
ordenación es segura con estas restricciones. Se redondea 100·m/c a ocho
decimales con aritmética entera, hacia arriba en caso de empate, y se
imprimen la parte entera y la fraccionaria rellenada con ceros, separadas
por un punto. Los cinco lenguajes dan la misma salida, con error de como
mucho 5·10⁻⁹.
Con a lo sumo 2n fracciones, `O(n log² n)`.

En el ejemplo, con x = 50 el noble 2 espera a uno de los vasallos 3 y
4, listo el día 1, y queda listo el día 3. Los vasallos del rey están
listos los días 3, 2 y 4, así que el segundo llega el día 3, a tiempo.
Cualquier x mayor que 50 obliga al noble 2 a esperar a ambos. El rey
espera a dos de 4, 2, 4 cuando x ≤ 200/3, y a los tres en caso contrario
(por ejemplo, al 75%). En ambos casos parte el día 4, demasiado tarde.

Trampas:

- x es una proporción de vasallos directos redondeada hacia arriba: con
  3 vasallos, un 34% ya exige dos;
- un señor puede tener un número mayor que sus vasallos, así que el
  orden de proceso sale de un recorrido desde el rey;
- el rey no gasta días en reunir tropas;
- la salida debe usar punto decimal independientemente de la configuración
  regional: el test 10 revela la coma decimal predeterminada de Java con
  una configuración rusa, por lo que se usa explícitamente `Locale.US`;
- sin vasallos el rey parte enseguida y la respuesta es 100.

## Soluciones optimizadas

La programación dinámica en el árbol acumula primero el tiempo de cada camino desde el rey. Luego recorre el árbol desde las hojas y ordena los límites de los vasallos directos. Para una posición r, la proporción está limitada por el r-ésimo valor y por r dividido entre el número de vasallos.

Python 3.12 x64, envío 11318642. Tiempo 0,125 → 0,109 s, memoria 4116 → 3356 KB.

Rust 1.75 x64, envío 11318846. Tiempo 0,015 → 0,062 s, memoria 1368 → 552 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321968 · Java 1.8 №11321961 · Rust 1.75 x64 №11321962 · Go 1.14 x64 №11322431 · Python 3.12 x64 №11322432.

Go 1.14 x64, envío 11321995. Tiempo 0,031 → 0,031 s, memoria 3820 → 1608 KB.

Java 1.8, envío 11321996. Tiempo 0,156 → 0,093 s, memoria 6636 → 808 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1822_binary_search.cpp](1822_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n log^2 n) | AC | 0.031 s | 552 KB | 11321968 |
| [1822_binary_search.go](1822_binary_search.go) | Go 1.14 x64 | binary_search | O(n log^2 n) | AC | 0.031 s | 3820 KB | 11322431 |
| [1822_binary_search.java](1822_binary_search.java) | Java 1.8 | binary_search | O(n log^2 n) | AC | 0.156 s | 6636 KB | 11321961 |
| [1822_binary_search.py](1822_binary_search.py) | Python 3.12 x64 | binary_search | O(n log^2 n) | AC | 0.125 s | 4116 KB | 11322432 |
| [1822_binary_search.rs](1822_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n log^2 n) | AC | 0.015 s | 1368 KB | 11321962 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1822_trees_dp.py](1822_trees_dp.py) | Python 3.12 x64 | trees, dp | O(n log n) | AC | 0.109 s | 3356 KB | 11318642 |
| [1822_trees_dp.rs](1822_trees_dp.rs) | Rust 1.75 x64 | trees, dp | O(n log n) | AC | 0.062 s | 552 KB | 11318846 |
| [1822_trees_dp.go](1822_trees_dp.go) \* | Go 1.14 x64 | trees, dp | O(n log n) | AC | 0.031 s | 1608 KB | 11321995 |
| [1822_trees_dp.java](1822_trees_dp.java) | Java 1.8 | trees, dp | O(n log n) | AC | 0.093 s | 808 KB | 11321996 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
