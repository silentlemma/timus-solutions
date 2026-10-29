# 1110. Todos los restos cuya potencia N-ésima da resto Y

[Timus 1110](https://acm.timus.ru/problem.aspx?space=1&num=1110) · dificultad 53 · bruteforce

Problema original de la Olimpiada Nacional Búlgara de Informática, primer día.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados `N`, `M` e `Y` (`0 < N < 999`, `1 < M < 999`, `0 < Y < 999`), halla
todos los enteros `X` de `[0, M − 1]` con `X^N mod M = Y`.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N M Y` en una línea.

## Salida

Todos esos `X` en orden creciente, separados por espacios, o `-1` si no
hay ninguno.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 6 4
```

Salida:

```
2 4
```

## Solución

Hay menos de mil candidatos, así que se prueba cada `X` y se calcula
`X^N mod M` por exponenciación rápida, reduciendo módulo `M` tras cada
multiplicación. `O(M log N)`.

Detalles a tener en cuenta:

- `Y` puede ser `M` o mayor; un resto nunca lo es, y entonces la
  respuesta es `-1`;
- `X^N` es enorme: se reduce en cada paso, y los productos quedan por
  debajo de `M²`, que cabe en 32 bits;
- con `N = 1` la respuesta es solo `Y` siempre que `Y < M`.

Las respuestas se comprobaron con la multiplicación repetida simple, `N`
multiplicaciones para cada `X`.

## Soluciones optimizadas

La solución optimizada en C++ imprime cada raíz en cuanto la encuentra en
lugar de juntar las raíces en un vector: 128 KB en lugar de 196 KB, con
el mismo tiempo. La solución optimizada en Java lee los tres números
byte a byte de `System.in` en lugar de crear un `Scanner`, que por sí
solo ocupa más de un megabyte: 412 KB en lugar de 1568 KB, con el mismo
tiempo.

## Notas por lenguaje

- Python usa el `pow` de tres argumentos incorporado; los demás lenguajes
  llevan una pequeña función de potencia.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1110_bruteforce.cpp](1110_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(M log N) | AC | 0.015 s | 196 KB | 11279202 |
| [1110_bruteforce.go](1110_bruteforce.go) | Go 1.14 x64 | bruteforce | O(M log N) | AC | 0.015 s | 1104 KB | 11279203 |
| [1110_bruteforce.java](1110_bruteforce.java) | Java 1.8 | bruteforce | O(M log N) | AC | 0.109 s | 1568 KB | 11279205 |
| [1110_bruteforce.py](1110_bruteforce.py) | Python 3.12 x64 | bruteforce | O(M log N) | AC | 0.078 s | 352 KB | 11279204 |
| [1110_bruteforce.rs](1110_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(M log N) | AC | 0.015 s | 212 KB | 11279206 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1110_bruteforce_optimized.cpp](1110_bruteforce_optimized.cpp) | G++ 13.2 x64 | bruteforce | O(M log N) | AC | 0.015 s | 128 KB | 11303557 |
| [1110_bruteforce_optimized.java](1110_bruteforce_optimized.java) | Java 1.8 | bruteforce | O(M log N) | AC | 0.109 s | 412 KB | 11303558 |
