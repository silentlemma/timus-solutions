# 1044. Contar billetes equilibrados de N cifras

[Timus 1044](https://acm.timus.ru/problem.aspx?space=1&num=1044) · dificultad 122 · bruteforce

Problema original de Stanislav Vasiliev, del V Campeonato por Equipos de Programación de la Universidad Estatal de los Urales, octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número de billete tiene `N` cifras (`N` es par, `2 ≤ N ≤ 8`; se
permiten ceros a la izquierda). Está equilibrado cuando la primera mitad
de las cifras y la segunda suman lo mismo. Cuenta los billetes
equilibrados.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

El número de billetes equilibrados.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
670
```

### Ejemplo 2

Entrada:

```
2
```

Salida:

```
10
```

## Solución

Las mitades son independientes. Para cada suma `s`, se cuenta cuántos
números menores que `10^(N/2)` tienen suma de cifras `s`: hay que mirar
como mucho 10000 números. Un billete equilibrado es un par de mitades con
la misma suma, así que la respuesta es la suma de `ways[s]^2` sobre todos
los `s`. `O(10^(N/2) · N)`.

Para `N = 8` la respuesta es 4816030, que cabe en 32 bits, pero los
cuadrados se suman igualmente en enteros de 64 bits.

Detalles a tener en cuenta:

- los ceros a la izquierda cuentan: `0000` es un billete;
- cada mitad tiene `N / 2` cifras, no `N`.

El [problema 1036](../1036/README.es.md) pregunta lo mismo para hasta 100
cifras y una suma total fija; allí los recuentos salen de una DP y
necesitan enteros grandes.

## Notas por lenguaje

- Todos los lenguajes hacen el mismo recuento; Python suma las cifras de
  `str(x)`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1044_bruteforce.cpp](1044_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.015 s | 196 KB |
| [1044_bruteforce.go](1044_bruteforce.go) | Go 1.14 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.046 s | 1080 KB |
| [1044_bruteforce.java](1044_bruteforce.java) | Java 1.8 | bruteforce | O(10^(N/2) · N) | AC | 0.093 s | 1552 KB |
| [1044_bruteforce.py](1044_bruteforce.py) | Python 3.12 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.078 s | 288 KB |
| [1044_bruteforce.rs](1044_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.015 s | 216 KB |
