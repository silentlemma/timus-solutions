# 1025. Los menos partidarios para ganar una votación por mayoría en dos niveles

[Timus 1025](https://acm.timus.ru/problem.aspx?space=1&num=1025) · dificultad 67 · greedy, sorting

Problema original de la Segunda Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 7 de octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los votantes están repartidos en `K` grupos (`K` impar, `1 ≤ K ≤ 101`),
cada uno de tamaño impar; en total como mucho 9999. Un grupo dice «sí»
cuando más de la mitad de sus miembros vota sí, y una decisión se aprueba
cuando más de la mitad de los grupos dice «sí». Encuentra el menor número de
partidarios que, colocados en los grupos adecuados, aprueban cualquier
decisión.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`K` y luego los `K` tamaños de los grupos.

## Salida

El menor número de partidarios.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
9 3 11 1 7
```

Salida:

```
7
```

### Ejemplo 2

Entrada:

```
1
9999
```

Salida:

```
5000
```

## Solución

Para aprobar una decisión los partidarios deben ganar `K / 2 + 1` grupos
(división entera, `K` es impar), y ganar un grupo de `s` votantes (`s`
impar) requiere `s / 2 + 1` partidarios; los que sobren en ese grupo se
desperdician, igual que los partidarios en grupos perdidos.

Así que hay que elegir `K / 2 + 1` grupos con el menor coste total
`s / 2 + 1`. El coste crece con el tamaño, así que los mejores grupos son
simplemente los más pequeños: se ordenan los tamaños y se suman los costes
de los primeros `K / 2 + 1`. `O(K log K)`.

Detalles a tener en cuenta:

- la mayoría de grupos es `K / 2 + 1`, y la mayoría en un grupo de `s` es
  `s / 2 + 1`, no `s / 2`;
- los tamaños no vienen ordenados en la entrada.

## Soluciones optimizadas

La solución optimizada en Java lee la entrada en bloques de 1 KB y la
analiza a mano en lugar de usar `Scanner`: 384 KB en lugar de 1724 KB,
con el mismo tiempo.

## Notas por lenguaje

La misma ordenación y suma en todos los lenguajes.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1025_greedy_sorting.cpp](1025_greedy_sorting.cpp) | G++ 13.2 x64 | greedy, sorting | O(K log K) | AC | 0.001 s | 188 KB | 11303273 |
| [1025_greedy_sorting.go](1025_greedy_sorting.go) | Go 1.14 x64 | greedy, sorting | O(K log K) | AC | 0.031 s | 1076 KB | 11278301 |
| [1025_greedy_sorting.java](1025_greedy_sorting.java) | Java 1.8 | greedy, sorting | O(K log K) | AC | 0.109 s | 1724 KB | 11278306 |
| [1025_greedy_sorting.py](1025_greedy_sorting.py) | Python 3.12 x64 | greedy, sorting | O(K log K) | AC | 0.093 s | 372 KB | 11278304 |
| [1025_greedy_sorting.rs](1025_greedy_sorting.rs) | Rust 1.75 x64 | greedy, sorting | O(K log K) | AC | 0.031 s | 220 KB | 11278307 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1025_greedy_sorting_optimized.java](1025_greedy_sorting_optimized.java) \* | Java 1.8 | greedy, sorting | O(K log K) | AC | 0.125 s | 384 KB | 11303704 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
