# 1687. Numismática recreativa

[Timus 1687](https://acm.timus.ru/problem.aspx?space=1&num=1687) · dificultad 1275 · greedy

Problema original preparado por Vladimir Yakovlev, con agradecimiento especial a Vladislav Isenbaev, para el X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tras el descuento, cada caja de monedas cuesta 100 yenes, y un conjunto
de cajas vale 100 yenes por cada moneda deseada distinta que contenga.
Hallar el mayor conjunto de cajas, cada una con al menos una moneda
deseada, cuyo precio no supere su valor.

## Entrada

n (1 ≤ n ≤ 100) tipos de monedas y k (1 ≤ k ≤ 50) cajas, luego cada
caja con su tamaño y sus monedas distintas, y por último las m monedas
deseadas.

## Salida

El número de cajas y sus números. Se acepta cualquier conjunto máximo.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 4
5 2 7 6 1 3
6 6 7 10 2 9 4
5 1 8 3 9 2
5 4 3 7 6 1
4 8 5 4 9
```

Salida:

```
3
2 3 4
```

## Solución

Llamemos útil a una caja con alguna moneda deseada, y alcanzable a una
moneda deseada que está en alguna caja. Un conjunto S de cajas útiles
debe cumplir |S| ≤ (monedas deseadas en S), así que |S| no supera el
número de monedas alcanzables y, desde luego, tampoco el de cajas
útiles.

El menor de los dos se alcanza. Para cada moneda alcanzable aún no
cubierta se toma cualquier caja que la contenga: se usa como mucho una
caja por moneda y se cubren todas las alcanzables. Luego se añaden
otras cajas útiles mientras su número no supere el de monedas
alcanzables. El conjunto vale todas las monedas alcanzables y tiene
min(útiles, alcanzables) cajas. `O(k · n²)` con búsqueda lineal en cajas.

Trampas:

- la respuesta puede superar un emparejamiento máximo entre cajas y
  monedas: las cajas {1, 2, 3}, {1}, {1}, {1} con monedas deseadas
  1, 2, 3 permiten tres cajas, aunque solo dos pueden emparejarse
  (test 03);
- las cajas sin monedas deseadas no cuentan (test 04);
- si ninguna caja tiene una moneda deseada, la respuesta es 0 y una
  lista vacía.

El verificador acepta cualquier conjunto del tamaño esperado que salga
a cuenta. Las respuestas coinciden con una búsqueda exhaustiva sobre
todos los conjuntos de cajas en casos pequeños y con una implementación
aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1687_greedy.cpp](1687_greedy.cpp) | G++ 13.2 x64 | greedy | O(k · n²) | AC | 0.015 s | 236 KB |
| [1687_greedy.go](1687_greedy.go) | Go 1.14 x64 | greedy | O(k · n²) | AC | 0.031 s | 1176 KB |
| [1687_greedy.java](1687_greedy.java) | Java 1.8 | greedy | O(k · n²) | AC | 0.109 s | 612 KB |
| [1687_greedy.py](1687_greedy.py) | Python 3.12 x64 | greedy | O(k · n²) | AC | 0.093 s | 964 KB |
| [1687_greedy.rs](1687_greedy.rs) | Rust 1.75 x64 | greedy | O(k · n²) | AC | 0.062 s | 296 KB |
