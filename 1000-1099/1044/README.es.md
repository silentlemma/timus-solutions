# 1044. Contar billetes equilibrados de N cifras

[Timus 1044](https://acm.timus.ru/problem.aspx?space=1&num=1044) · dificultad 123 · bruteforce

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

Para `N = 8` la respuesta es 4816030, que cabe en 32 bits, pero fuera de
Python los cuadrados se suman igualmente en enteros de 64 bits.

Detalles a tener en cuenta:

- los ceros a la izquierda cuentan: `0000` es un billete;
- cada mitad tiene `N / 2` cifras, no `N`.

El [problema 1036](../1036/README.es.md) pregunta lo mismo para hasta
100 cifras y una suma total fija; allí los recuentos salen de una DP y
necesitan enteros grandes.

## Soluciones optimizadas

La solución optimizada en C++ guarda los recuentos en un arreglo fijo de
37 elementos en la pila en lugar de un `std::vector`: como `N ≤ 8`, una
mitad tiene como mucho cuatro cifras y su suma de cifras no pasa de 36.
Así el programa no necesita ninguna biblioteca de contenedores:
{1044_bruteforce_optimized.cpp}.

La solución optimizada en Java lee `N` byte a byte de `System.in` en
lugar de crear un `Scanner`, cuyas expresiones regulares y datos de
configuración regional cuestan más que el propio recuento; el recuento
es el mismo: {1044_bruteforce_optimized.java}.

La versión rápida de Go usa programación dinámica sobre la suma de los dígitos en vez de enumerar las mitades. Añadir un dígito convoluciona los conteos con diez unos; una suma deslizante calcula cada nuevo conteo en tiempo constante. Tras `N/2` pasos, se suman sus cuadrados. Tiempo `O(N²)` y memoria auxiliar `O(N)`. La enumeración se conserva como versión básica.

{1044_dp.go}.

Ejecuciones Accepted correspondientes al código: versión básica 0.046 s / 1080 KB; esta versión 0.015 s / 804 KB (envío 11307438). Cumple el objetivo de clasificación en la instantánea del 2026-10-31.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1044_bruteforce_optimized.cpp`: reducción de tiempo +0.00%; reducción
  de memoria +36.73%; base: `1044_bruteforce.cpp`.

- `1044_dp.go`: reducción de tiempo +67.39%; reducción de memoria
  +25.56%; base: `1044_bruteforce.go`.

- `1044_bruteforce_optimized.java`: reducción de tiempo +16.13%;
  reducción de memoria +79.64%; base: `1044_bruteforce.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1044_bruteforce.rs](1044_bruteforce.rs).

- Todos los lenguajes hacen el mismo recuento; Python suma las cifras de
  `str(x)`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1044_bruteforce.cpp](1044_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.015 s | 196 KB | 11278614 |
| [1044_bruteforce.go](1044_bruteforce.go) | Go 1.14 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.046 s | 1080 KB | 11278618 |
| [1044_bruteforce.java](1044_bruteforce.java) | Java 1.8 | bruteforce | O(10^(N/2) · N) | AC | 0.093 s | 1552 KB | 11278622 |
| [1044_bruteforce.py](1044_bruteforce.py) | Python 3.12 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.078 s | 288 KB | 11278621 |
| [1044_bruteforce.rs](1044_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.015 s | 216 KB | 11278623 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1044_bruteforce_optimized.cpp](1044_bruteforce_optimized.cpp) | G++ 13.2 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.001 s | 124 KB | 11304375 |
| [1044_dp.go](1044_dp.go) | Go 1.14 x64 | dp | O(N²) | AC | 0.015 s | 804 KB | 11307438 |
| [1044_bruteforce_optimized.java](1044_bruteforce_optimized.java) \* | Java 1.8 | bruteforce | O(10^(N/2) · N) | AC | 0.078 s | 316 KB | 11304376 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
