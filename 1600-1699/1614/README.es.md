# 1614. Proyecto nacional «Tranvías»

[Timus 1614](https://acm.timus.ru/problem.aspx?space=1&num=1614) · dificultad 846 · constructive

Problema original de Alexander Ipatov (idea de Magaz Asanov), del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad tiene 2n paradas de tranvía (1 ≤ n ≤ 100). Hay que trazar
exactamente n rutas, cada una una secuencia de exactamente 2n paradas
(una parada puede repetirse), de modo que dos paradas cualesquiera sean
vecinas en alguna ruta: se puede ir de una a otra sin paradas
intermedias. Imprime las rutas, o `-1` si es imposible. Se acepta
cualquier conjunto válido.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

n.

## Salida

n líneas, cada una con las 2n paradas de una ruta.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
1 6 2 1 3 4
2 3 6 5 4 6
5 1 4 2 5 3
```

## Solución

Hay n(2n − 1) pares de paradas, y n rutas de 2n paradas tienen
exactamente n(2n − 1) lugares de vecindad, así que cada par debe
aparecer exactamente una vez. Dividimos el grafo completo de 2n
vértices en n caminos que pasan por todos los vértices. Siempre es
posible.

Numeremos las paradas 0 … 2n − 1 en un círculo. La ruta k va k, k + 1,
k − 1, k + 2, k − 2, …, k + n (módulo 2n): visita cada parada una vez, y
sus pares vecinos alternan entre las sumas 2k + 1 y 2k módulo 2n: todos
los pares {k − j, k + 1 + j} y todos los pares {k + j, k − j}. Todo par de
paradas distintas tiene una suma s módulo 2n y pertenece a la ruta
⌊s / 2⌋, así que las n rutas cubren todos los pares. `O(n²)`.

Detalles a tener en cuenta:

- con n = 1 hay una sola ruta con las dos paradas (prueba 02);
- las rutas del ejemplo son otras pero también válidas, así que un
  verificador comprueba que cada par está cubierto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1614_constructive.cpp](1614_constructive.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.015 s | 128 KB |
| [1614_constructive.go](1614_constructive.go) | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1260 KB |
| [1614_constructive.java](1614_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.156 s | 2012 KB |
| [1614_constructive.py](1614_constructive.py) | Python 3.12 x64 | constructive | O(n²) | AC | 0.109 s | 452 KB |
| [1614_constructive.rs](1614_constructive.rs) | Rust 1.75 x64 | constructive | O(n²) | AC | 0.046 s | 428 KB |
