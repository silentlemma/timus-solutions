# 1196. Cuántas fechas de la lista de un estudiante tiene también el profesor

[Timus 1196](https://acm.timus.ru/problem.aspx?space=1&num=1196) · dificultad 53 · binary_search

Problema original del folclore, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un profesor tiene una lista ordenada de `N ≤ 15000` años, y un estudiante
escribe `M ≤ 10⁶` años en cualquier orden; ambas listas pueden repetir
años, todos hasta `10⁹`. Hay que contar las entradas de la lista del
estudiante que también aparecen en la del profesor.

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
lado del profesor no cambian nada. `O(M log N)`. Con un millón de números
que leer, leer rápido importa más que las búsquedas.

Detalles a tener en cuenta:

- un año que el estudiante escribe dos veces cuenta dos veces;
- la entrada tiene hasta un millón de líneas, así que una lectura lenta
  línea a línea puede pasarse de tiempo en algunos lenguajes.

Las respuestas se compararon con una solución escrita aparte, que usa un
conjunto hash, en todas las pruebas.

## Notas por lenguaje

- Python guarda los años del profesor en un conjunto; los demás lenguajes
  buscan por bisección en el arreglo ordenado. Java lee la entrada con un
  lector de bytes escrito a mano.
- Python lee los años del estudiante línea a línea. Partir toda la
  entrada de una vez deja vivas a la vez un millón de cadenas pequeñas,
  unos 62 MB, y esa versión superó el límite de 64 MB en la prueba 8.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1196_binary_search.cpp](1196_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(M log N) | AC | 0.687 s | 256 KB |
| [1196_binary_search.go](1196_binary_search.go) | Go 1.14 x64 | binary_search | O(M log N) | AC | 0.171 s | 5576 KB |
| [1196_binary_search.java](1196_binary_search.java) | Java 1.8 | binary_search | O(M log N) | AC | 0.312 s | 616 KB |
| [1196_binary_search.py](1196_binary_search.py) | Python 3.12 x64 | binary_search | O(M log N) | AC | 0.687 s | 1456 KB |
| [1196_binary_search.rs](1196_binary_search.rs) | Rust 1.75 x64 | binary_search | O(M log N) | AC | 0.031 s | 9300 KB |
