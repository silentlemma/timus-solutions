# 1117. Recorrer un árbol binario numerado en orden de un número a otro

[Timus 1117](https://acm.timus.ru/problem.aspx?space=1&num=1117) · dificultad 279 · math

Problema original de Alexander Somov, del USU Open Collegiate Programming Contest, octubre de 2001, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los nodos de un árbol binario perfecto están numerados `1, 2, 3, …` en
orden simétrico: cada nodo interno tiene un número entre los de sus dos
hijos, y todos los de un subárbol quedan del mismo lado. Un mensaje va del
número `i` al número `j` pasando por cada número intermedio, un paso cada
vez; un paso entre `k` y `k ± 1` cuesta tantos días como nodos del árbol
haya estrictamente entre ellos en el camino del árbol (0 para un padre y
su hijo). Halla el total de días para `1 ≤ i, j ≤ 2^31 − 1`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`i j` en una línea.

## Salida

El número de días.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 5
```

Salida:

```
2
```

## Solución

En un árbol perfecto numerado en orden simétrico, la altura del nodo `x`
sobre las hojas es el número de bits cero finales `tz(x)`: las hojas son
los impares, sus padres los `2 mod 4`, y así sucesivamente. De dos números
consecutivos uno es impar, una hoja, y el par `e` es su antepasado a
altura `tz(e)`, así que el paso cuesta `tz(e) − 1` días. Cada número par
estrictamente entre `i` y `j` se usa en dos pasos, y un extremo par en uno.

Con `c(e) = tz(e) − 1 = tz(e/2)`, la suma de `c` sobre los pares hasta `n`
es `Σ_{y ≤ n/2} tz(y) = m − popcount(m)` con `m = ⌊n/2⌋` (cada `y` aporta
sus ceros finales, y `Σ_{t≥1} ⌊m/2^t⌋ = m − popcount(m)`). Así, para
`i < j` la respuesta es `2·(G(j) − G(i − 1)) − c(i) − c(j)`, donde `G` es
esa suma y `c` de un impar vale 0. `O(1)`.

Detalles a tener en cuenta:

- la mayor respuesta, para `1` y `2^31 − 1`, es `2147483586`, solo 61 por
  debajo del límite de 32 bits con signo; las soluciones usan 64 bits por
  seguridad;
- el orden de `i` y `j` no importa;
- no se da el tamaño del árbol, pero no importa: los números en orden
  simétrico y las alturas son los mismos en cualquier árbol perfecto lo
  bastante grande para contener ambos números.

Las respuestas se comprobaron con un recorrido del árbol real (el padre
de `x` es `x ± 2^tz(x)`) que suma las longitudes de camino paso a paso,
para 300 pares aleatorios menores que 3000, y las pruebas grandes con un
bucle directo sobre cada paso.

## Notas por lenguaje

- Los ceros finales y la cuenta de bits salen de funciones incorporadas:
  `__builtin_ctzll` y `__builtin_popcountll`, `math/bits`,
  `Long.numberOfTrailingZeros` y `Long.bitCount`, `trailing_zeros` y
  `count_ones`; Python cuenta los unos de `bin(m)`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1117_math.cpp](1117_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1117_math.go](1117_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1052 KB |
| [1117_math.java](1117_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1616 KB |
| [1117_math.py](1117_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 436 KB |
| [1117_math.rs](1117_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 224 KB |
