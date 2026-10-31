# 1272. Un metro que no es el de Ekaterimburgo

[Timus 1272](https://acm.timus.ru/problem.aspx?space=1&num=1272) · dificultad 144 · dsu

Problema original de Magaz Asanov (preparado por Igor Goldberg), del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad está sobre 1 ≤ N ≤ 10 000 islas unidas por 0 ≤ K ≤ 12 000
túneles y 0 ≤ M ≤ 12 000 puentes, y entre todos conectan todas las
islas. Un metro debe conectar todas las islas usando algunos de estos
enlaces, con el menor número posible de puentes. ¿Cuántos puentes
necesita?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, K y M, luego K túneles y M puentes, cada uno como dos números de
isla entre 1 y N.

## Salida

El menor número de puentes.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 3 4
1 2
2 3
4 5
1 3
3 4
4 6
5 6
```

Salida:

```
2
```

## Solución

Los túneles no cuestan nada, así que se toman todos: dividen las islas
en grupos ya conectados. Cada puente puede unir como mucho dos grupos en
uno y, como toda la red es conexa, siempre se pueden elegir puentes que
unan los grupos de uno en uno. La respuesta es el número de grupos por
túneles menos uno, contado con una estructura de unión-búsqueda sobre
los túneles; se ignoran los extremos de los puentes.
`O((N + K) log N)`.

Detalles a tener en cuenta:

- los puentes no importan, solo que conectan los grupos, cosa que el
  enunciado garantiza;
- los túneles pueden repetirse o unir una isla consigo misma
  (prueba 05);
- con una sola isla, o si los túneles ya lo conectan todo, la respuesta
  es 0 (pruebas 02, 04).

## Soluciones optimizadas

La solución optimizada en C++ analiza los números a mano desde un búfer
de 4 KB en lugar de `scanf` y guarda los padres en un arreglo global
fijo de 10 001 celdas, suficiente para `N ≤ 10 000`, en lugar de un
`std::vector`. Además lee los puentes hasta el final, cosa que la
solución sencilla no hace: {1272_dsu_optimized.cpp}.

La solución optimizada en Go analiza los números byte a byte desde el
`bufio.Reader` en lugar de `fmt.Fscan` y guarda los padres como
`uint16`, que admite números de isla hasta 10 000, en lugar de `int`.
Además lee los puentes hasta el final, cosa que la solución sencilla no
hace: {1272_dsu_optimized.go}.

La solución optimizada en Python lee la entrada en trozos de 8 KB y
convierte los tokens trozo a trozo, saltando los puentes según llegan,
en lugar de partir toda la entrada en una lista de una vez:
{1272_dsu_optimized.py}.

La solución optimizada en Rust analiza los números a mano desde un búfer
de 4 KB que se rellena desde la entrada estándar, en lugar de leer toda
la entrada en un `String`, así que en memoria quedan solo los padres y
el búfer: {1272_dsu_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1272_dsu_optimized.cpp`: reducción de tiempo +51.61%; reducción de
  memoria +49.12%; base: `1272_dsu.cpp`.

- `1272_dsu_optimized.go`: reducción de tiempo -106.67%; reducción de
  memoria +35.85%; base: `1272_dsu.go`.

- `1272_dsu_optimized.py`: reducción de tiempo -17.20%; reducción de
  memoria +67.67%; base: `1272_dsu.py`.

- `1272_dsu_optimized.rs`: reducción de tiempo +0.00%; reducción de
  memoria +63.93%; base: `1272_dsu.rs`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1272_dsu.java](1272_dsu.java).

- Todos los lenguajes usan la misma unión-búsqueda con reducción de
  caminos a la mitad. Python y Rust leen toda la entrada, añadiendo `O(M)` de tiempo.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1272_dsu.cpp](1272_dsu.cpp) | G++ 13.2 x64 | dsu | O((N + K) log N) | AC | 0.031 s | 228 KB | 11284262 |
| [1272_dsu.go](1272_dsu.go) | Go 1.14 x64 | dsu | O((N + K) log N) | AC | 0.015 s | 1428 KB | 11284264 |
| [1272_dsu.java](1272_dsu.java) | Java 1.8 | dsu | O((N + K) log N) | AC | 0.140 s | 488 KB | 11284270 |
| [1272_dsu.py](1272_dsu.py) | Python 3.12 x64 | dsu | O((N + K) log N + M) | AC | 0.093 s | 3328 KB | 11284266 |
| [1272_dsu.rs](1272_dsu.rs) | Rust 1.75 x64 | dsu | O((N + K) log N + M) | AC | 0.046 s | 732 KB | 11284276 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1272_dsu_optimized.cpp](1272_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O((N + K) log N + M) | AC | 0.015 s | 116 KB | 11304487 |
| [1272_dsu_optimized.go](1272_dsu_optimized.go) | Go 1.14 x64 | dsu | O((N + K) log N + M) | AC | 0.031 s | 916 KB | 11304488 |
| [1272_dsu_optimized.py](1272_dsu_optimized.py) \* | Python 3.12 x64 | dsu | O((N + K) log N + M) | AC | 0.109 s | 1076 KB | 11304489 |
| [1272_dsu_optimized.rs](1272_dsu_optimized.rs) | Rust 1.75 x64 | dsu | O((N + K) log N + M) | AC | 0.046 s | 264 KB | 11304490 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
