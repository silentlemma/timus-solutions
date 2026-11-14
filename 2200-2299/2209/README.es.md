# 2209. La M-ésima fracción del nivel N del árbol de Stern–Brocot

[Timus 2209](https://acm.timus.ru/problem.aspx?space=1&num=2209) · dificultad 651 · math

Problema original de Vadim Barinov, de la Olimpiada Académica Universitaria Escolar de Informática 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El árbol de Stern–Brocot tiene 1/1 en la raíz y las cotas 0/1 y 1/0, y
cada nodo es la mediante de sus ancestros izquierdo y derecho más
cercanos. Hallar la M-ésima fracción desde la izquierda en la
profundidad N. Los límites son 0.5 segundos y 256 MB.

## Entrada

N y M, 1 ≤ N ≤ 10⁹, 1 ≤ M ≤ min(2^(N−1), 10⁹).

## Salida

El numerador y el denominador.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 1
```

Salida:

```
1 1
```

### Ejemplo 2

Entrada:

```
3 3
```

Salida:

```
3 2
```

### Ejemplo 3

Entrada:

```
5 7
```

Salida:

```
5 7
```

## Solución

La profundidad N tiene 2^(N−1) nodos, y el camino de la raíz al
M-ésimo es M − 1 escrito con N − 1 dígitos binarios, 0 para un paso a la
izquierda y 1 para uno a la derecha. Al bajar se guardan las dos cotas
a/b y c/d del nodo actual, que es (a + c)/(b + d): un paso a la
izquierda convierte el nodo en la nueva cota derecha, y uno a la derecha
en la nueva cota izquierda.

N puede valer 10⁹, pero M ≤ 10⁹ significa que a lo sumo 30 dígitos son
unos, así que el camino empieza con N − 1 − k ceros, donde k es la
longitud en bits de M − 1. Bajar z veces a la izquierda desde la raíz
solo cambia la cota derecha a 1/z, así que el recorrido empieza con las
cotas 0/1 y 1/z (1/0 si z = 0) y procesa solo los últimos k dígitos.

Los números crecen a lo sumo como z por un número de Fibonacci de 30
pasos, muy dentro de 64 bits.

En el segundo ejemplo M − 1 = 2 = 10 en binario con dos dígitos: a la
derecha hasta 2/1 y luego a la izquierda hasta 3/2.

Esto cuesta O(log M).

## Soluciones optimizadas

Python lee el camino desde el bit menos significativo y calcula los coeficientes de los dos límites iniciales. Los primeros pasos a la izquierda se incorporan al denominador de una vez. El envío 11317193 tardó 0,093 s y usó 428 KB frente a 0,093 s y 456 KB en la base. Ocupa el puesto 10 en tiempo y el 3 en memoria entre los envíos comparables del corte.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321834 · Go 1.14 x64 №11321835 · Java 1.8 №11322409 · Rust 1.75 x64 №11321837 · Python 3.12 x64 №11322446.

Esta variante lee el camino desde el bit menos significativo, acumula los coeficientes de los límites iniciales e incorpora de una vez los primeros pasos a la izquierda. G++ 13.2 x64, envío 11322447. Tiempo 0,015 → 0,015 s, memoria 424 → 112 KB.

Esta variante lee el camino desde el bit menos significativo, acumula los coeficientes de los límites iniciales e incorpora de una vez los primeros pasos a la izquierda. Go 1.14 x64, envío 11322448. Tiempo 0,031 → 0,031 s, memoria 1112 → 796 KB.

Esta variante lee el camino desde el bit menos significativo, acumula los coeficientes de los límites iniciales e incorpora de una vez los primeros pasos a la izquierda. Rust 1.75 x64, envío 11322449. Tiempo 0,062 → 0,046 s, memoria 224 → 212 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2209_math.cpp](2209_math.cpp) | G++ 13.2 x64 | math | O(log M) | AC | 0.015 s | 424 KB | 11321834 |
| [2209_math.go](2209_math.go) | Go 1.14 x64 | math | O(log M) | AC | 0.031 s | 1112 KB | 11321835 |
| [2209_math.java](2209_math.java) | Java 1.8 | math | O(log M) | AC | 0.109 s | 368 KB | 11322409 |
| [2209_math.py](2209_math.py) | Python 3.12 x64 | math | O(log M) | AC | 0.093 s | 456 KB | 11322446 |
| [2209_math.rs](2209_math.rs) | Rust 1.75 x64 | math | O(log M) | AC | 0.062 s | 224 KB | 11321837 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2209_math_optimized.py](2209_math_optimized.py) \* | Python 3.12 x64 | math | O(log M) | AC | 0.093 s | 428 KB | 11317193 |
| [2209_math_optimized.cpp](2209_math_optimized.cpp) | G++ 13.2 x64 | math | O(log M) | AC | 0.015 s | 112 KB | 11322447 |
| [2209_math_optimized.go](2209_math_optimized.go) | Go 1.14 x64 | math | O(log M) | AC | 0.031 s | 796 KB | 11322448 |
| [2209_math_optimized.rs](2209_math_optimized.rs) | Rust 1.75 x64 | math | O(log M) | AC | 0.046 s | 212 KB | 11322449 |

\* La versión aceptada en Python aún puede mejorar en la clasificación objetivo.
