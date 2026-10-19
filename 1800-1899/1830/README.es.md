# 1830. Ayuda del NatOS

[Timus 1830](https://acm.timus.ru/problem.aspx?space=1&num=1830) · dificultad 952 · math

Problema original de Evgeny Kurpilyansky (idea de Stanislav Vasiliev), del XV Campeonato Abierto de los Urales de Programación Competitiva, abril de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un sistema de ayuda tiene páginas 1, …, n. F1 abre o cierra la
página 1. Cada página salvo la última tiene botones que abren o cierran
la siguiente, pero solo la página abierta menos detallada, la de menor
número, es visible y usable. Hallar el menor número de pulsaciones que
convierten un conjunto de páginas abiertas en otro.

## Entrada

n (1 ≤ n ≤ 50), luego los conjuntos inicial y deseado como cadenas de n
ceros y unos; el carácter i-ésimo dice si la página i está abierta.

## Salida

El menor número de pulsaciones.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
111
000
```

Salida:

```
5
```

## Solución

Es el rompecabezas de los anillos chinos. En cualquier estado hay como
mucho dos movimientos: cambiar la página 1 o cambiar la página justo
después de la primera abierta. Léase la página i como el bit i − 1 de
una palabra binaria. Entonces estos son exactamente los dos tipos de
paso del código Gray reflejado, que cambia el bit 0 un paso sí y otro
no, y si no el bit justo encima del bit 1 más bajo. Así, los 2ⁿ estados
están en un único camino en orden de código Gray, y el lugar de un
estado en él es su palabra decodificada del código Gray: el xor de la
palabra y todos sus desplazamientos a la derecha. La respuesta es la
diferencia de los dos lugares. `O(n)`.

En el ejemplo 111 es la palabra 7, cuyo lugar es 7 xor 3 xor 1 = 5, y
000 está en el lugar 0: cinco pulsaciones.

Trampas:

- el primer carácter es la página 1, el bit más bajo, así que la cadena
  se lee al revés;
- la respuesta llega a 2⁵⁰ − 1, que necesita enteros de 64 bits;
- una búsqueda en anchura sobre 2⁵⁰ estados no tiene esperanza.

Las respuestas coinciden con una búsqueda en anchura para n hasta 9 y
con una implementación aceptada independiente en pares aleatorios de
hasta 50 páginas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1830_math.cpp](1830_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 132 KB |
| [1830_math.go](1830_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1076 KB |
| [1830_math.java](1830_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1588 KB |
| [1830_math.py](1830_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 476 KB |
| [1830_math.rs](1830_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 232 KB |
