# 1005. Repartir pesos en dos montones

[Timus 1005](https://acm.timus.ru/problem.aspx?space=1&num=1005) · dificultad 78 · dp, bitmask, bruteforce, meet_in_middle

Problema original del Campeonato de la Universidad Estatal de los Urales 1997.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados `n` enteros positivos `w1, ..., wn` (`1 ≤ n ≤ 20`, `1 ≤ wi ≤ 100 000`),
repártelos en dos grupos de modo que la diferencia entre las sumas de los
grupos sea la menor posible. Imprime esa diferencia. Un grupo puede quedar
vacío.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número `n` y luego los `n` pesos, separados por espacios en blanco.

## Salida

Un entero: la menor diferencia posible.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
5 8 13 27 14
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
1
100000
```

Salida:

```
100000
```

## Solución

Si un grupo pesa `s`, el otro pesa `total - s` y la diferencia es
`|total - 2s|`. Así que hay que encontrar la suma de un subconjunto
`s ≤ total / 2` más cercana a `total / 2`.

**Sumas de subconjuntos (dp).** `reach[s]` indica si algunos pesos suman
exactamente `s`; se empieza con `reach[0]` y se agregan los pesos uno a uno,
recorriendo `s` de mayor a menor para que cada peso se use como mucho una vez.
Solo importan las sumas hasta `total / 2 ≤ 1 000 000`, así que son como mucho
`20 · 10^6` pasos y memoria `O(total)`. La respuesta sale del mayor `s`
alcanzable con `s ≤ total / 2`.

**Bitset (dp, bitmask).** La misma tabla cabe en un único entero cuyo bit `s`
es `reach[s]`: agregar un peso `x` es `reach |= reach << x`. En Python, con sus
enteros de precisión arbitraria, esto trabaja con palabras de máquina enteras
a la vez y es mucho más rápido que un bucle sobre `s`.

Detalles a tener en cuenta:

- el total llega a `2 · 10^6`: `int` alcanza, pero una tabla de todas las sumas
  hasta `total` desperdicia memoria; basta con `total / 2`;
- `n = 1`: la respuesta es el único peso.

## Soluciones optimizadas

**Todos los subconjuntos** (C++). Con `n ≤ 20` se pueden recorrer los
`2^20` subconjuntos. En orden de código Gray cada subconjunto difiere del
anterior en un solo peso, así que la suma se actualiza en `O(1)`; el último
peso puede quedarse en el segundo grupo, lo que reduce el trabajo a la
mitad. Tiempo `O(2^(n-1))` y ninguna tabla, así que necesita mucha menos
memoria que la DP: 200 KB en lugar de 1124 KB, con el mismo tiempo.

**Encuentro en el medio** (Go, Java, Rust). Se dividen los pesos en dos
mitades de a lo sumo 10 y se listan, ordenadas, las sumas de todos los
subconjuntos de cada mitad, a lo sumo 1024. Un montón es un subconjunto de
una mitad más un subconjunto de la otra, así que se recorren las sumas de la
mitad izquierda hacia arriba y las de la derecha hacia abajo, moviendo el
lado que acerca el montón a `total / 2`; cada par que se salta así no es
mejor que uno ya visto. El recorrido termina antes cuando la diferencia
llega a `total mod 2`, que ninguna división puede mejorar. Tiempo
`O(n·2^(n/2))` y unos pocos kilobytes de memoria en lugar de una tabla de
`total / 2` entradas. Go y Java además analizan la entrada a mano desde un
búfer pequeño. Con el mismo tiempo, Go usa 920 KB en lugar de 2000 KB,
Java 472 KB en lugar de 1388 KB y Rust 244 KB en lugar de 1144 KB.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: las soluciones sencillas llenan
  la tabla booleana de sumas, unos `2 · 10^7` pasos simples.
- **Python**: el bitset sobre un entero grande; un doble bucle simple sobre
  pesos y sumas sería demasiado lento.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1005_dp.cpp](1005_dp.cpp) | G++ 13.2 x64 | dp | O(n·S) | AC | 0.015 s | 1124 KB | 11277610 |
| [1005_dp.go](1005_dp.go) | Go 1.14 x64 | dp | O(n·S) | AC | 0.062 s | 2000 KB | 11277623 |
| [1005_dp.java](1005_dp.java) | Java 1.8 | dp | O(n·S) | AC | 0.109 s | 1388 KB | 11303450 |
| [1005_dp.rs](1005_dp.rs) | Rust 1.75 x64 | dp | O(n·S) | AC | 0.031 s | 1144 KB | 11277646 |
| [1005_dp_bitmask.py](1005_dp_bitmask.py) | Python 3.12 x64 | dp, bitmask | O(n·S/64) | AC | 0.093 s | 920 KB | 11277630 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1005_bruteforce_bitmask.cpp](1005_bruteforce_bitmask.cpp) | G++ 13.2 x64 | bruteforce, bitmask | O(2^(n-1)) | AC | 0.015 s | 200 KB | 11277615 |
| [1005_meet_in_middle.go](1005_meet_in_middle.go) | Go 1.14 x64 | meet_in_middle | O(n·2^(n/2)) | AC | 0.046 s | 920 KB | 11303539 |
| [1005_meet_in_middle.java](1005_meet_in_middle.java) | Java 1.8 | meet_in_middle | O(n·2^(n/2)) | AC | 0.109 s | 472 KB | 11303540 |
| [1005_meet_in_middle.rs](1005_meet_in_middle.rs) | Rust 1.75 x64 | meet_in_middle | O(n·2^(n/2)) | AC | 0.031 s | 244 KB | 11303541 |
