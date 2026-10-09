# 1036. Billetes equilibrados con una suma de cifras dada

[Timus 1036](https://acm.timus.ru/problem.aspx?space=1&num=1036) · dificultad 304 · dp

Problema original del archivo de Timus Online Judge; no se indican el autor ni el origen.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número de billete es una cadena de `2N` cifras decimales
(`1 ≤ N ≤ 50`); se permiten ceros a la izquierda. Un billete está
equilibrado cuando sus primeras `N` cifras y sus últimas `N` cifras suman
lo mismo. Dado `S` (`0 ≤ S ≤ 1000`), cuenta los billetes equilibrados cuyas
cifras suman `S`.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `S` en una línea.

## Salida

El número de esos billetes (puede tener unas cien cifras).

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
3 6
```

Salida:

```
100
```

## Solución

Las dos mitades de un billete equilibrado con suma de cifras `S` suman
`S / 2`, así que la respuesta es `0` cuando `S` es impar y, si no, `W^2`,
donde `W` es el número de cadenas de `N` cifras que suman `S / 2`: las dos
mitades se eligen de forma independiente.

`W` sale de una DP sobre las cifras: `ways[k][t]` es el número de cadenas
de `k` cifras con suma `t`, y `ways[k + 1][t]` es la suma de
`ways[k][t − d]` para las cifras `d = 0..9`. Solo hacen falta las sumas
hasta `S / 2`, y `S / 2 > 9N` da `0` de inmediato. Son `O(N · S)` sumas.

Los números no caben en 64 bits: `W` llega a unos `10^48` y la respuesta a
unos `10^97`, así que la DP y el cuadrado final usan enteros grandes.

Detalles a tener en cuenta:

- una suma impar no tiene billetes equilibrados;
- la suma puede superar la máxima posible de un billete (hasta 1000 frente
  a `18N ≤ 900`);
- los ceros a la izquierda cuentan: `0101` es un billete de cuatro cifras.

Una alternativa es la fórmula cerrada por inclusión–exclusión,
`W = Σ (−1)^k C(N, k) C(S/2 − 10k + N − 1, N − 1)`; las pruebas se
comprobaron con ella.

## Notas por lenguaje

- **C++**, **Rust**: un pequeño tipo de enteros grandes en base `10^9` con
  suma y multiplicación.
- **Go**: `math/big`; **Java**: `BigInteger`; **Python**: enteros
  integrados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1036_dp.cpp](1036_dp.cpp) | G++ 13.2 x64 | dp | O(N·S) big additions | AC | 0.031 s | 280 KB |
| [1036_dp.go](1036_dp.go) | Go 1.14 x64 | dp | O(N·S) big additions | AC | 0.015 s | 2728 KB |
| [1036_dp.java](1036_dp.java) | Java 1.8 | dp | O(N·S) big additions | AC | 0.140 s | 5728 KB |
| [1036_dp.py](1036_dp.py) | Python 3.12 x64 | dp | O(N·S) big additions | AC | 0.093 s | 512 KB |
| [1036_dp.rs](1036_dp.rs) | Rust 1.75 x64 | dp | O(N·S) big additions | AC | 0.015 s | 336 KB |
