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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2209_math.cpp](2209_math.cpp) | G++ 13.2 x64 | math | O(log M) | AC | 0.015 s | 228 KB |
| [2209_math.go](2209_math.go) | Go 1.14 x64 | math | O(log M) | AC | 0.031 s | 896 KB |
| [2209_math.java](2209_math.java) | Java 1.8 | math | O(log M) | AC | 0.109 s | 204 KB |
| [2209_math.py](2209_math.py) | Python 3.12 x64 | math | O(log M) | AC | 0.093 s | 248 KB |
| [2209_math.rs](2209_math.rs) | Rust 1.75 x64 | math | O(log M) | AC | 0.046 s | 24 KB |
