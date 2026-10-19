# 1862. Topo muy acaudalado

[Timus 1862](https://acm.timus.ru/problem.aspx?space=1&num=1862) · dificultad 1270 · math

Problema original de Denis Dublennykh, del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un topo sabe convertir un número x en 2x, en 2x + 1 o en ⌊x/2⌋, un paso
cada vez. Para cada par 1 ≤ x < y ≤ 2ˡ − 1 el topo convierte x en y con
el menor número de pasos. ¿Cuántos pasos se dan en total, módulo
10⁹ + 7?

## Entrada

l (2 ≤ l ≤ 10¹⁸).

## Salida

El número total de pasos módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
4
```

## Solución

Los números 1 … 2ˡ − 1 forman un árbol binario perfecto con raíz 1, en
el que x es padre de 2x y de 2x + 1, y los tres pasos se mueven por sus
aristas. El menor número de pasos de x a y es la distancia en el árbol,
así que la respuesta es la suma de distancias sobre todos los pares.

Se cuentan en cambio los pares que cruzan cada arista. La arista sobre
un nodo de profundidad k (1 ≤ k ≤ l − 1) separa los 2^(l−k) − 1 nodos de
su subárbol de los otros 2ˡ − 2^(l−k), y hay 2ᵏ aristas así. Su aporte
es 2ˡ·(2^(l−k) − 1)(2ᵏ − 1), y sumando sobre k se obtiene
2ˡ·((l − 1)(2ˡ + 1) − 2(2ˡ − 2)) = 2ˡ·((l − 3)·2ˡ + l + 3). Con 2ˡ por
exponenciación rápida y l reducido módulo 10⁹ + 7, esto es `O(log l)`.

Para l = 2 el árbol es 1 con hijos 2 y 3: los pares (1, 2) y (1, 3)
están a un paso y (2, 3) a dos, 4 en total.

Trampas:

- l llega a 10¹⁸, así que hay que reducirlo antes de multiplicar;
- las diferencias pueden quedar negativas módulo 10⁹ + 7; hay que volver
  a sumar el módulo.

La fórmula coincide con sumar todas las distancias directamente para l
hasta 9 y con una implementación aceptada independiente para alturas
hasta 10¹⁸, incluidas algunas en múltiplos del módulo y a su alrededor.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1862_math.cpp](1862_math.cpp) | G++ 13.2 x64 | math | O(log l) | AC | 0.015 s | 128 KB |
| [1862_math.go](1862_math.go) | Go 1.14 x64 | math | O(log l) | AC | 0.031 s | 1084 KB |
| [1862_math.java](1862_math.java) | Java 1.8 | math | O(log l) | AC | 0.125 s | 1740 KB |
| [1862_math.py](1862_math.py) | Python 3.12 x64 | math | O(log l) | AC | 0.093 s | 412 KB |
| [1862_math.rs](1862_math.rs) | Rust 1.75 x64 | math | O(log l) | AC | 0.046 s | 240 KB |
