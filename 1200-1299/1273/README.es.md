# 1273. Traviesas

[Timus 1273](https://acm.timus.ru/problem.aspx?space=1&num=1273) · dificultad 464 · dp

Problema original de Magaz Asanov (preparado por Leonid Volkov), del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los dos rieles son las rectas x = 0 y x = 1. Cada una de las K ≤ 100
traviesas une (0, Y1) con (1, Y2) en puntos enteros, |Y1|, |Y2| ≤ 1000;
no hay dos traviesas con el mismo extremo izquierdo ni con el mismo
extremo derecho. Hay que quitar las menos traviesas posibles para que
no se crucen dos de las que quedan.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

K y luego K pares Y1 Y2.

## Salida

El menor número de traviesas que hay que quitar.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 1
3 0
1 2
```

Salida:

```
1
```

## Solución

Como los extremos nunca coinciden, dos traviesas se cruzan justo cuando
sus extremos izquierdos y derechos van en orden opuesto. Ordenando las
traviesas por el extremo izquierdo, un conjunto sin cruces es uno con
extremos derechos crecientes, y lo más que se puede conservar es la
subsecuencia creciente más larga de los extremos derechos. La respuesta
es K menos su longitud, hallada con la DP cuadrática sobre la última
traviesa conservada. `O(K²)`.

Detalles a tener en cuenta:

- la entrada no está ordenada por ningún extremo (prueba 06);
- K puede ser 0 (prueba 02);
- las coordenadas pueden ser negativas.

Las respuestas se compararon con probar todos los subconjuntos de
traviesas en 119 casos aleatorios de hasta 12 traviesas.

## Soluciones optimizadas

La versión con ordenación y búsqueda binaria conserva la reducción a una subsecuencia estrictamente creciente de extremos derechos tras ordenar por los izquierdos. En lugar de la DP cuadrática, tails[i] guarda el menor extremo final posible de una subsecuencia de longitud i+1. Se sustituye el primer extremo no menor que la coordenada nueva, o se amplía el arreglo si no existe. Un extremo menor conserva todas las continuaciones posibles; por ello, la longitud ocupada es óptima. La respuesta es K menos esa longitud. Ordenar y buscar cuesta O(K log K), con O(K) de espacio; para K = 0 se obtiene 0.

El envío aceptado en Rust 1.75 x64 tarda 0.031 s frente a 0.015 s de la base y usa 56 KB frente a 232 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1273_dp_binary_search_optimized.py`. Se busca la posición de cada cola con bisect_left; se mantienen el invariante de subsecuencia estrictamente creciente y el tiempo O(n log n). El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328532 (Python 3.12 x64): **0.078 s / 712 KB**. Comparación archivada: `1273_dp.py` (Python 3.12 x64) — 0.093 s / 392 KB (#11284283).

## Notas por lenguaje

Las versiones sencillas conservan la DP cuadrática en todos los lenguajes. Go y Java empaquetan las dos coordenadas desplazadas en un entero: cada una está entre 0 y 2000 y cabe en 11 bits. Ordenar esos enteros ordena los extremos izquierdos, y una máscara recupera el derecho. C++ y Rust usan arreglos para K ≤ 100; Python usa bisect_left. Go emplea manejadores estándar y Rust E/S acotada del C runtime con entrada C.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1273_dp.cpp](1273_dp.cpp) | G++ 13.2 x64 | dp | O(K²) | AC | 0.015 s | 192 KB | 11284277 |
| [1273_dp.go](1273_dp.go) | Go 1.14 x64 | dp | O(K²) | AC | 0.015 s | 1140 KB | 11284281 |
| [1273_dp.java](1273_dp.java) | Java 1.8 | dp | O(K²) | AC | 0.140 s | 2780 KB | 11284285 |
| [1273_dp.py](1273_dp.py) | Python 3.12 x64 | dp | O(K²) | AC | 0.093 s | 392 KB | 11284283 |
| [1273_dp.rs](1273_dp.rs) | Rust 1.75 x64 | dp | O(K²) | AC | 0.015 s | 232 KB | 11284290 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1273_binary_search_sorting.cpp](1273_binary_search_sorting.cpp) | G++ 13.2 x64 | binary_search, sorting | O(K log K) | AC | 0.001 s | 116 KB | 11314674 |
| [1273_binary_search_sorting.go](1273_binary_search_sorting.go) \* | Go 1.14 x64 | binary_search, sorting | O(K log K) | AC | 0.015 s | 260 KB | 11314678 |
| [1273_binary_search_sorting.java](1273_binary_search_sorting.java) | Java 1.8 | binary_search, sorting | O(K log K) | AC | 0.109 s | 392 KB | 11314681 |
| [1273_binary_search_sorting.py](1273_binary_search_sorting.py) | Python 3.12 x64 | binary_search, sorting | O(K log K) | AC | 0.093 s | 384 KB | 11314686 |
| [1273_binary_search_sorting.rs](1273_binary_search_sorting.rs) | Rust 1.75 x64 | binary_search, sorting | O(K log K) | AC | 0.031 s | 56 KB | 11314875 |
| [1273_dp_binary_search_optimized.py](1273_dp_binary_search_optimized.py) | Python 3.12 x64 | dp, binary_search | O(K log K) time; O(K) space | AC | 0.078 s | 712 KB | 11328532 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
