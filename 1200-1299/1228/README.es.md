# 1228. Los límites de un arreglo a partir de sus multiplicadores de índice

[Timus 1228](https://acm.timus.ru/problem.aspx?space=1&num=1228) · dificultad 108 · math

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arreglo de `n` dimensiones `array[0..k1, 0..k2, …, 0..kn]`, `n ≤ 20`,
se dispone con el último índice cambiando más rápido, así que el elemento
`X[i1, …, in]` tiene número `1 + D1·i1 + … + Dn·in` para ciertos
multiplicadores `Di`. Dados los multiplicadores y el número total de
elementos `s`, hay que hallar los límites superiores `k1, …, kn`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` y `s`, y luego `D1, …, Dn`.

## Salida

`k1, …, kn` separados por espacios o saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 24
8
4
1
```

Salida:

```
2 1 3
```

## Solución

Aumentar en uno el índice `i` salta un bloque entero de las dimensiones
siguientes, así que `D(i−1) = Di · (ki + 1)`, y el arreglo entero es un
bloque de la primera dimensión: `s = D1 · (k1 + 1)`. Leyendo los
multiplicadores con `s` delante, cada límite es uno menos que el
cociente de dos vecinos: `k1 = s/D1 − 1` y `ki = D(i−1)/Di − 1`. `O(n)`.

Detalles a tener en cuenta:

- el último multiplicador es siempre 1, y el primer límite sale de `s`,
  no de un multiplicador;
- los productos llegan casi a `2³¹`, así que no conviene hacer las cuentas
  intermedias con enteros de 32 bits con signo.

Los límites se comprobaron multiplicándolos de vuelta hasta `s` en 59
arreglos generados, y se compararon con una solución escrita aparte en
todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes ponen `s` delante de los multiplicadores y dividen
  vecinos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1228_math.cpp](1228_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 200 KB |
| [1228_math.go](1228_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.001 s | 1136 KB |
| [1228_math.java](1228_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1616 KB |
| [1228_math.py](1228_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 424 KB |
| [1228_math.rs](1228_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 216 KB |
