# 1727. Los números mágicos de Znaika

[Timus 1727](https://acm.timus.ru/problem.aspx?space=1&num=1727) · dificultad 200 · greedy

Problema original de Ivan Burmistrov, del Concurso Regional Escolar de Programación de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hallar un conjunto de enteros positivos distintos menores que 10⁵ cuyas
cifras sumen n en total, o imprimir −1 si no lo hay.

## Entrada

n (0 < n < 10⁵).

## Salida

El tamaño del conjunto y luego sus números, o −1. Se acepta cualquier
conjunto válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
17
```

Salida:

```
3
7 12 43
```

## Solución

Siempre existe un conjunto: las cifras de todos los números de 1 a
99 999 suman 5 · 45 · 10⁴ = 2 250 000, mucho más que n.

Se baja desde 99 999 y se toma cada número cuya suma de cifras aún
cabe en lo que queda de n. Los números grandes tienen sumas de cifras
cercanas a 45 y gastan pronto casi todo n; cuando el resto se hace
pequeño, el voraz salta a números con sumas de cifras pequeñas, como
20 000 o 10 000, y al final los números de una cifra 9, 8, …, 1 forman
cualquier resto hasta 45. Las sumas de cifras se construyen de
antemano como s(i) = s(i / 10) + i mod 10. `O(10⁵)`.

Para n = 17 el voraz imprime 98 000, que por sí solo tiene suma de
cifras 17. Se acepta cualquier conjunto con el total correcto.

Trampas:

- −1 nunca es la respuesta;
- los números deben ser distintos y menores que 10⁵, así que 99 999
  solo puede usarse una vez;
- para n = 99 999 el conjunto tiene 3261 números, así que conviene
  armar la salida de una vez.

El voraz llega exactamente a n para cada n de 1 a 99 999, comprobado
uno por uno. El comprobador verifica el rango, que sean distintos y el
total de las cifras.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1727_greedy.cpp](1727_greedy.cpp) | G++ 13.2 x64 | greedy | O(10⁵) | AC | 0.015 s | 616 KB |
| [1727_greedy.go](1727_greedy.go) | Go 1.14 x64 | greedy | O(10⁵) | AC | 0.031 s | 2268 KB |
| [1727_greedy.java](1727_greedy.java) | Java 1.8 | greedy | O(10⁵) | AC | 0.125 s | 2196 KB |
| [1727_greedy.py](1727_greedy.py) | Python 3.12 x64 | greedy | O(10⁵) | AC | 0.093 s | 1636 KB |
| [1727_greedy.rs](1727_greedy.rs) | Rust 1.75 x64 | greedy | O(10⁵) | AC | 0.046 s | 1096 KB |
