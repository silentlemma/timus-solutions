# 2143. Sentar a un grupo sin que dos miembros queden juntos

[Timus 2143](https://acm.timus.ru/problem.aspx?space=1&num=2143) · dificultad 665 · dp, bitmask

Problema original de Alexey Kungurtsev, del Concurso de Programación por Equipos de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un avión tiene n filas de asientos A B C | D E F con un pasillo en medio,
y algunos asientos están ocupados. Dos asientos son vecinos si están al
mismo lado del pasillo y tanto sus filas como sus letras difieren a lo
sumo en uno. Sentar a un grupo de k personas en asientos libres de modo
que no haya dos vecinos, o indicar que es imposible. Se acepta cualquier
reparto válido. Los límites son 0.5 segundos y 256 MB.

## Entrada

n y k, 1 ≤ n ≤ 100, 1 ≤ k ≤ 6n, y luego n filas como ".**|_|**." con
"." para un asiento libre y "*" para uno ocupado. Hay al menos k
asientos libres.

## Salida

"PORAZHENIE", o "POBEDA" y k asientos como 1A.

## Evaluación

Un comprobador verifica el veredicto y que los asientos estén libres,
sean distintos y no sean vecinos dos a dos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2
.**|_|**.
**.|_|***
```

Salida:

```
POBEDA
1A
2C
```

### Ejemplo 2

Entrada:

```
2 3
...|_|***
***|_|***
```

Salida:

```
PORAZHENIE
```

## Solución

Los dos lados del pasillo nunca se tocan, así que cada lado es una
cuadrícula n × 3 aparte donde la vecindad es el movimiento del rey.
Cualquier subconjunto de un reparto válido es válido, así que basta con
hallar el mayor reparto válido de cada lado y comprobar que juntos
tienen al menos k asientos.

En un lado, los asientos de una fila forman una máscara de 3 bits. Una
máscara se permite en una fila si solo usa asientos libres y no tiene
dos bits vecinos, y dos máscaras encajan en filas consecutivas si ningún
bit de una está en la misma columna o en una vecina de un bit de la
otra: (m | m << 1 | m >> 1) & m′ = 0. Una DP sobre las filas y la máscara
de la última fila guarda el mayor número de personas y la máscara
anterior, así que el mejor reparto se reconstruye desde la última fila.
Hay 8 máscaras, así que el trabajo es O(64 n).

En el segundo ejemplo los tres asientos libres 1A, 1B y 1C admiten a lo
sumo dos personas, 1A y 1C, así que no se puede sentar a tres.

## Soluciones optimizadas

Las versiones optimizadas guardan las puntuaciones de una sola fila. Cada lado admite cinco máscaras y se usa un byte por máscara y fila para reconstruir la asignación.

El envío 11317658 en C++ tardó 0.015 s y usó 120 KB. La versión sencilla tardó 0.015 s y usó 396 KB.

El envío 11317670 en Python tardó 0.078 s y usó 716 KB. La versión sencilla tardó 0.078 s y usó 808 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321394 · Java 1.8 №11321629 · Python 3.12 x64 №11321450 · Rust 1.75 x64 №11321543 · Go 1.14 x64 №11322325.

El envío 11322363 en Java tardó 0.125 s y usó 520 KB. La versión sencilla tardó 0.125 s y usó 1752 KB.

El envío 11322373 en Go tardó 0.031 s y usó 316 KB. La versión sencilla tardó 0.031 s y usó 1168 KB.

Rust 1.75 x64, envío 11317691. Tiempo 0,046 → 0,015 s, memoria 252 → 232 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2143_dp_bitmask.cpp](2143_dp_bitmask.cpp) | G++ 13.2 x64 | dp, bitmask | O(n) | AC | 0.015 s | 396 KB | 11321394 |
| [2143_dp_bitmask.go](2143_dp_bitmask.go) | Go 1.14 x64 | dp, bitmask | O(n) | AC | 0.031 s | 1168 KB | 11322325 |
| [2143_dp_bitmask.java](2143_dp_bitmask.java) | Java 1.8 | dp, bitmask | O(n) | AC | 0.125 s | 1752 KB | 11321629 |
| [2143_dp_bitmask.py](2143_dp_bitmask.py) | Python 3.12 x64 | dp, bitmask | O(n) | AC | 0.078 s | 808 KB | 11321450 |
| [2143_dp_bitmask.rs](2143_dp_bitmask.rs) | Rust 1.75 x64 | dp, bitmask | O(n) | AC | 0.046 s | 252 KB | 11321543 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2143_dp_bitmask_optimized.cpp](2143_dp_bitmask_optimized.cpp) | G++ 13.2 x64 | dp, bitmask | O(n) | AC | 0.015 s | 120 KB | 11317658 |
| [2143_dp_bitmask_optimized.py](2143_dp_bitmask_optimized.py) | Python 3.12 x64 | dp, bitmask | O(n) | AC | 0.078 s | 716 KB | 11317670 |
| [2143_dp_bitmask_optimized.java](2143_dp_bitmask_optimized.java) | Java 1.8 | dp, bitmask | O(n) | AC | 0.125 s | 520 KB | 11322363 |
| [2143_dp_bitmask_optimized.go](2143_dp_bitmask_optimized.go) \* | Go 1.14 x64 | dp, bitmask | O(n) | AC | 0.031 s | 316 KB | 11322373 |
| [2143_dp_bitmask_optimized.rs](2143_dp_bitmask_optimized.rs) \* | Rust 1.75 x64 | dp, bitmask | O(n) | AC | 0.015 s | 232 KB | 11317691 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
