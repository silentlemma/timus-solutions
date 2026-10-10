# 1208. El mayor número de equipos legendarios sin miembros en común

[Timus 1208](https://acm.timus.ru/problem.aspx?space=1&num=1208) · dificultad 214 · bitmask

Problema original de Leonid Volkov, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `K ≤ 18` equipos legendarios de tres programadores cada uno, y
algunos programadores han estado en más de uno. Un programador solo puede
jugar en un equipo, así que hay que hallar el mayor número de equipos que
pueden participar a la vez, es decir, sin un programador en dos de ellos.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`K` y luego los tres nombres de cada equipo, de hasta 20 letras
minúsculas.

## Salida

El mayor número de equipos que pueden participar.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
gerostratos scorpio shamgshamg
zaitsev silverberg cousteau
zaitsev petersen shamgshamg
clipper petersen shamgshamg
clipper bakirelli vasiliadi
silverberg atn dolly
knuth dijkstra bellman
```

Salida:

```
4
```

## Solución

Dos equipos chocan si comparten un miembro, y la respuesta es el mayor
conjunto de equipos sin choques entre ellos. Para cada equipo se guarda
una máscara de bits con los equipos con los que choca, él incluido. Para
un conjunto de equipos dado como máscara, se mira su equipo más bajo: o
se queda en casa, y queda el conjunto sin él, o juega, y queda el
conjunto sin él y sin todos los equipos con los que choca. Así

`best(S) = max(best(S sin i), 1 + best(S menos clash(i)))`, con `i` el
equipo más bajo de `S`.

Ambos conjuntos menores son números menores, así que la tabla se puede
rellenar para las `2^K` máscaras en orden creciente. `O(2^K + K²)`.

Detalles a tener en cuenta:

- un equipo choca consigo mismo, lo que lo quita cuando se elige;
- el mismo programador puede estar en muchos equipos, así que los choques
  no son solo entre vecinos de la lista.

Las respuestas se compararon con una solución escrita aparte en 200
entradas aleatorias y en equipos sacados de grupos de 3 a 1000
programadores.

## Notas por lenguaje

- Python evalúa la misma recursión de forma perezosa con
  `functools.lru_cache`, que solo visita los conjuntos que realmente
  aparecen; los demás lenguajes rellenan toda la tabla.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1208_bitmask.cpp](1208_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^K + K²) | AC | 0.015 s | 976 KB |
| [1208_bitmask.go](1208_bitmask.go) | Go 1.14 x64 | bitmask | O(2^K + K²) | AC | 0.062 s | 3204 KB |
| [1208_bitmask.java](1208_bitmask.java) | Java 1.8 | bitmask | O(2^K + K²) | AC | 0.109 s | 2688 KB |
| [1208_bitmask.py](1208_bitmask.py) | Python 3.12 x64 | bitmask | O(2^K + K²) | AC | 0.078 s | 456 KB |
| [1208_bitmask.rs](1208_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^K + K²) | AC | 0.046 s | 684 KB |
