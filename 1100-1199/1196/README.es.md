# 1196. Cuántas fechas de la lista de un estudiante tiene también el profesor

[Timus 1196](https://acm.timus.ru/problem.aspx?space=1&num=1196) · dificultad 52 · binary_search, hashing

Problema original del folclore, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un profesor tiene una lista ordenada de `1 ≤ N ≤ 15000` años, y un
estudiante escribe `1 ≤ M ≤ 10⁶` años en cualquier orden; ambas listas
pueden repetir años, cada uno de 1 a `10⁹`. Hay que contar las entradas
de la lista del estudiante que también aparecen en la del profesor.

Límite de tiempo: 1.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y los años del profesor, uno por línea, y luego `M` y los del
estudiante.

## Salida

El número de entradas que coinciden.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1054
1492
4
1492
65536
1492
100
```

Salida:

```
2
```

## Solución

La lista del profesor ya viene ordenada, así que cada año del estudiante
se busca por bisección; cada coincidencia cuenta, incluidas las
repeticiones del lado del estudiante, mientras que las repeticiones del
lado del profesor no cambian nada. `O(N + M log N)`. Con un millón de números
que leer, leer rápido importa más que las búsquedas.

Detalles a tener en cuenta:

- un año que el estudiante escribe dos veces cuenta dos veces;
- la entrada tiene alrededor de un millón de líneas, así que una lectura lenta
  línea a línea puede pasarse de tiempo en algunos lenguajes.

Las respuestas se compararon con una solución escrita aparte, que usa un
conjunto hash, en todas las pruebas.

## Soluciones optimizadas

La solución optimizada en C++ analiza a mano hasta un millón de números
desde bloques de 64 KB leídos con `fread`, en lugar de llamar a `scanf`
para cada uno: 0.046 s en lugar de 0.687 s, con casi la misma memoria
(260 KB frente a 256 KB). La búsqueda binaria es la misma.

La solución optimizada en Go analiza las fechas a mano desde un lector
con búfer de 4 KB en lugar de un escáner de palabras con búfer de 1 MB,
las guarda como `int32` y las busca con su propia búsqueda binaria:
0.062 s en lugar de 0.171 s y 996 KB en lugar de 5576 KB. La solución
optimizada en Rust analiza las fechas a mano desde un búfer de 64 KB en
lugar de leer toda la entrada en una cadena y las guarda como `u32`:
320 KB en lugar de 9300 KB, con el mismo tiempo. La solución optimizada
en Python aprovecha que cada línea tiene una sola fecha: convierte cada
línea tal cual y cuenta las fechas conocidas con `map` en lugar de un
bucle de Python: 0.343 s en lugar de 0.687 s y 1324 KB en lugar de
1456 KB.

## Notas por lenguaje

- Python guarda los años del profesor en un conjunto; los demás lenguajes
  buscan por bisección en el arreglo ordenado.
- Python lee los años del estudiante línea a línea. Partir toda la
  entrada de una vez deja vivas a la vez un millón de cadenas pequeñas,
  unos 62 MB, y esa versión superó el límite de 64 MB en la prueba 8.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1196_binary_search.cpp](1196_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N + M log N) | AC | 0.687 s | 256 KB | 11283484 |
| [1196_binary_search.go](1196_binary_search.go) | Go 1.14 x64 | binary_search | O(N + M log N) | AC | 0.171 s | 5576 KB | 11283485 |
| [1196_binary_search.java](1196_binary_search.java) | Java 1.8 | binary_search | O(N + M log N) | AC | 0.328 s | 592 KB | 11303453 |
| [1196_binary_search.rs](1196_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N + M log N) | AC | 0.031 s | 9300 KB | 11283493 |
| [1196_hashing.py](1196_hashing.py) | Python 3.12 x64 | hashing | O(N + M) expected | AC | 0.687 s | 1456 KB | 11283490 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1196_binary_search_optimized.cpp](1196_binary_search_optimized.cpp) | G++ 13.2 x64 | binary_search | O(N + M log N) | AC | 0.046 s | 260 KB | 11303577 |
| [1196_binary_search_optimized.go](1196_binary_search_optimized.go) | Go 1.14 x64 | binary_search | O(N + M log N) | AC | 0.062 s | 996 KB | 11303718 |
| [1196_binary_search_optimized.rs](1196_binary_search_optimized.rs) | Rust 1.75 x64 | binary_search | O(N + M log N) | AC | 0.046 s | 320 KB | 11303720 |
| [1196_hashing_optimized.py](1196_hashing_optimized.py) | Python 3.12 x64 | hashing | O(N + M) expected | AC | 0.343 s | 1324 KB | 11303721 |
