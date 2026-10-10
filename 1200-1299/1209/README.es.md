# 1209. Las cifras de 1, 10, 100, 1000 escritos seguidos

[Timus 1209](https://acm.timus.ru/problem.aspx?space=1&num=1209) · dificultad 34 · math

Problema original de Alexey Lakhtin, del USU Open Collegiate Programming Contest, octubre de 2002, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se escriben las potencias de diez una tras otra: `110100100010000…`.
Para hasta 65535 posiciones `1 ≤ K < 2³¹`, hay que imprimir la cifra de
cada posición.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego las `N` posiciones.

## Salida

Las `N` cifras separadas por espacios.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3
14
7
6
```

Salida:

```
0 0 1 0
```

## Solución

La `m`-ésima potencia escrita es `10^(m−1)`, que ocupa `m` cifras, así
que empieza en la posición `1 + (1 + 2 + … + (m − 1)) = 1 + m(m − 1)/2`,
y ahí está su único 1. La posición `K` tiene un 1 exactamente cuando
`K − 1 = m(m − 1)/2` para algún `m`, es decir, cuando
`8(K − 1) + 1 = (2m − 1)²` es un cuadrado perfecto. `O(1)` por posición.

Detalles a tener en cuenta:

- `8(K − 1) + 1` llega a unos `1.7·10¹⁰`, más de 32 bits;
- una raíz cuadrada en coma flotante puede fallar por uno cerca de
  cuadrados grandes, así que hay que corregirla con comprobaciones
  enteras exactas.

Las respuestas se compararon con una solución escrita aparte en todas
las posiciones de 1 a 65535, en posiciones aleatorias y en posiciones
junto a los unos.

## Notas por lenguaje

- Python usa `math.isqrt`, que es exacta; los demás lenguajes corrigen
  la raíz en coma flotante con comparaciones enteras.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1209_math.cpp](1209_math.cpp) | G++ 13.2 x64 | math | O(1) per position | AC | 0.062 s | 388 KB |
| [1209_math.go](1209_math.go) | Go 1.14 x64 | math | O(1) per position | AC | 0.062 s | 2664 KB |
| [1209_math.java](1209_math.java) | Java 1.8 | math | O(1) per position | AC | 0.062 s | 1372 KB |
| [1209_math.py](1209_math.py) | Python 3.12 x64 | math | O(1) per position | AC | 0.125 s | 6556 KB |
| [1209_math.rs](1209_math.rs) | Rust 1.75 x64 | math | O(1) per position | AC | 0.015 s | 3160 KB |
