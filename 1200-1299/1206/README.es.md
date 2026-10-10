# 1206. Pares de números cuyas sumas de cifras se suman

[Timus 1206](https://acm.timus.ru/problem.aspx?space=1&num=1206) · dificultad 124 · combinatorics

Problema original de Leonid Volkov, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sea `S(N)` la suma de las cifras de `N`. Para `2 ≤ K ≤ 50`, hay que
contar los pares ordenados de números de `K` cifras `A` y `B`, sin ceros
a la izquierda, con `S(A + B) = S(A) + S(B)`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`K`.

## Salida

El número de pares.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
1980
```

## Solución

Cada acarreo en la suma convierte un 10 en una posición en un 1 en la
siguiente, y baja la suma de cifras en 9. Así que la igualdad se cumple
exactamente cuando no hay acarreos, es decir, cuando las cifras de cada
posición suman como mucho 9. Entonces las posiciones son independientes.
En la posición más alta ambas cifras van de 1 a 9, lo que da
`8 + 7 + … + 1 = 36` pares; en cada una de las otras `K − 1` posiciones
las cifras van de 0 a 9, lo que da `10 + 9 + … + 1 = 55` pares. La
respuesta es `36 · 55^(K−1)`, un número de hasta 87 cifras. `O(K²)` con
la multiplicación escolar.

Detalles a tener en cuenta:

- la respuesta supera los 64 bits ya con `K = 12`;
- las cifras más altas no pueden ser 0, así que su número de pares es
  distinto.

La fórmula se comprobó por fuerza bruta sobre todos los pares para
`K = 2` y `K = 3`, y cada `K` se comparó con una solución escrita aparte.

## Notas por lenguaje

- Python usa sus propios enteros, Go `math/big` y Java `BigInteger`;
  C++ y Rust multiplican `K − 1` veces por 55 un arreglo de cifras
  decimales.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1206_combinatorics.cpp](1206_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 188 KB |
| [1206_combinatorics.go](1206_combinatorics.go) | Go 1.14 x64 | combinatorics | O(K²) | AC | 0.031 s | 1200 KB |
| [1206_combinatorics.java](1206_combinatorics.java) | Java 1.8 | combinatorics | O(K²) | AC | 0.140 s | 1748 KB |
| [1206_combinatorics.py](1206_combinatorics.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.109 s | 416 KB |
| [1206_combinatorics.rs](1206_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(K²) | AC | 0.015 s | 212 KB |
