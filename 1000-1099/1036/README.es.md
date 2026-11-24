# 1036. Billetes equilibrados con una suma de cifras dada

[Timus 1036](https://acm.timus.ru/problem.aspx?space=1&num=1036) · dificultad 305 · dp

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

## Soluciones optimizadas

Las tres variantes complementan cada dígito a nueve y trabajan con la menor de las dos sumas complementarias. C++ y Rust conservan dos filas de programación dinámica con seis bloques en base 10⁹ por entrada. Una ventana deslizante suma el término nuevo y resta el que sale, así que cada entrada requiere una suma y como máximo una resta. Go usa la fórmula de inclusión y exclusión indicada arriba y reutiliza enteros grandes. Al final se eleva al cuadrado el recuento de una mitad. Los envíos aceptados usaron 116 KB en C++, 1204 KB en Go y 220 KB en Rust.

El tiempo medido en Rust 1.75 x64 aumenta de 0.015 a 0.046 s.

Las implementaciones base aceptadas [1036_dp.java](1036_dp.java), [1036_dp.py](1036_dp.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

`1036_dp_optimized.java`. Java mantiene la DP exacta de suma de cifras con BigInteger. Rechaza un total impar o una suma de mitad imposible. Sustituir cada cifra d por 9-d establece una biyección entre sumas T y 9N-T, de modo que se usa el menor objetivo. Cada nueva celda suma diez celdas antiguas consecutivas; una suma deslizante BigInteger añade el término que entra y resta el que sale. Reutiliza dos arreglos y eleva al cuadrado el conteo final para las dos mitades independientes. Realiza O(N·(T+1)) sumas/restas de enteros grandes y usa O(T+1) posiciones para ellos, incluyendo el objetivo cero, con aritmética exacta.

Frente a `1036_dp.java`: tiempo 0.140 s → 0.109 s; memoria 5728 KB → 1 524 KB.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- **C++**, **Rust**: un pequeño tipo de enteros grandes en base `10^9` con
  suma y multiplicación.
- **Go**: `math/big`; **Java**: `BigInteger`; **Python**: enteros
  integrados.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1036_dp.cpp](1036_dp.cpp) | G++ 13.2 x64 | dp | O(N·S) big additions | AC | 0.031 s | 280 KB | 11278472 |
| [1036_dp.go](1036_dp.go) | Go 1.14 x64 | dp | O(N·S) big additions | AC | 0.015 s | 2728 KB | 11278473 |
| [1036_dp.java](1036_dp.java) \* | Java 1.8 | dp | O(N·S) big additions | AC | 0.140 s | 5728 KB | 11278476 |
| [1036_dp.py](1036_dp.py) \* | Python 3.12 x64 | dp | O(N·S) big additions | AC | 0.093 s | 512 KB | 11278474 |
| [1036_dp.rs](1036_dp.rs) | Rust 1.75 x64 | dp | O(N·S) big additions | AC | 0.015 s | 336 KB | 11278477 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1036_dp_optimized.cpp](1036_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N·S) big integer operations | AC | 0.015 s | 116 KB | 11310337 |
| [1036_combinatorics.go](1036_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N²) big integer operations | AC | 0.015 s | 1204 KB | 11310374 |
| [1036_dp_optimized.rs](1036_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N·S) big integer operations | AC | 0.046 s | 220 KB | 11310376 |
| [1036_dp_optimized.java](1036_dp_optimized.java) | Java 1.8 | dp | O(N·(T+1)) big additions; T=min(S/2,9N-S/2) | AC | 0.109 s | 1524 KB | 11324788 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
