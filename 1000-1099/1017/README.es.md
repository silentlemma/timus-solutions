# 1017. Contar escaleras: particiones en partes distintas

[Timus 1017](https://acm.timus.ru/problem.aspx?space=1&num=1017) · dificultad 157 · dp

Problema original del Ural State University Internal Contest '99 #2.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una escalera hecha con `N` cubos iguales (`5 ≤ N ≤ 500`) es una secuencia de
al menos dos columnas (escalones) de alturas estrictamente crecientes, cada
una de al menos 1, que usa los `N` cubos. Cuenta las escaleras distintas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

El número de escaleras.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
11
```

Salida:

```
11
```

## Solución

Una escalera queda determinada por el conjunto de alturas de sus escalones:
son distintas y su orden está fijado (creciente). Así que la respuesta es el
número de formas de escribir `N` como suma de enteros positivos
**distintos**, menos uno: la «escalera» de un solo escalón de `N` cubos no
vale.

**Conteo con mochila 0/1.** `ways[s]` es el número de conjuntos de tamaños
distintos con suma `s`. Se empieza con `ways[0] = 1` y se añaden los
tamaños `1, 2, ..., N` uno a uno: para un tamaño `k`, `ways[s] += ways[s - k]`
con `s` bajando de `N` a `k`, para que cada tamaño se use como mucho una vez
(subiendo se permitirían repeticiones). Tras todos los tamaños, la respuesta
es `ways[N] - 1`.

Son `O(N^2) = 250 000` pasos. Los números crecen deprisa: para `N = 500` la
respuesta ronda `7.3 · 10^14`, así que hacen falta enteros de 64 bits.

Otra vía: `f(n, k)`, las particiones de `n` en partes distintas no menores
que `k`, cumple `f(n, k) = f(n, k + 1) + f(n - k, k + 1)`, lo que con
memoización da los mismos números.

Detalles a tener en cuenta:

- recorrer `s` hacia arriba cuenta particiones con partes repetidas;
- olvidar restar la partición de una sola parte;
- los enteros de 32 bits con signo se desbordan desde `N = 226`.

## Notas por lenguaje

La misma DP en todos los lenguajes con enteros de 64 bits; los enteros de
Python no tienen límite.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1017_dp.cpp](1017_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 196 KB |
| [1017_dp.go](1017_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.031 s | 1088 KB |
| [1017_dp.java](1017_dp.java) | Java 1.8 | dp | O(N^2) | AC | 0.109 s | 1580 KB |
| [1017_dp.py](1017_dp.py) | Python 3.12 x64 | dp | O(N^2) | AC | 0.093 s | 420 KB |
| [1017_dp.rs](1017_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.015 s | 236 KB |
