# 1741. Monstruo de la comunicación

[Timus 1741](https://acm.timus.ru/problem.aspx?space=1&num=1741) · dificultad 289 · dp

Problema original de Alex Samsonov (preparado por Marina Mukhacheva), del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cliente con licencia de la versión 1 debe llegar a la versión n.
Cada actualización lleva la versión x a la versión y > x y tiene un
tamaño. Una actualización pirata vuelve pirata el cliente para
siempre; una crackeada se instala en cualquier cliente; una con
licencia solo se instala en un cliente que siga teniendo licencia.
Hallar el menor tamaño total de actualizaciones, o indicar que no se
puede llegar a la versión n.

## Entrada

n y m (2 ≤ n ≤ 10⁴, 1 ≤ m ≤ 10⁴) y luego m actualizaciones `x y d s`
(1 ≤ x < y ≤ n, 1 ≤ d ≤ 10⁶), donde s es `Pirated`, `Cracked` o
`Licensed`.

## Salida

`Online` y el menor tamaño total, o `Offline`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4
1 3 10 Licensed
1 2 2 Pirated
2 3 3 Licensed
2 3 6 Cracked
```

Salida:

```
Online
8
```

### Ejemplo 2

Entrada:

```
3 1
1 2 10 Licensed
```

Salida:

```
Offline
```

## Solución

Las actualizaciones solo suben la versión, así que las versiones se
pueden tratar en orden creciente, cada una después de todo lo que lleva
a ella. El estado es la versión junto con si el cliente sigue con
licencia o ya es pirata. Desde cada estado alcanzado, una actualización
pirata lleva al estado pirata de su destino, una crackeada conserva el
estado y una con licencia solo se permite desde el estado con licencia.
La respuesta es el menor de los dos valores de la versión n. `O(n + m)`.

En el primer ejemplo la pirata 1 → 2 de 2 y la crackeada 2 → 3 de 6
dan 8, más barato que la de licencia 1 → 3 de 10; la de licencia 2 → 3
de 3 no puede ir tras la pirata.

Trampas:

- el total puede llegar a unos 10¹⁰, más de lo que caben en 32 bits;
- una actualización crackeada deja con licencia a un cliente con
  licencia;
- no importa si la versión n termina con licencia.

Las respuestas coinciden con una implementación aceptada independiente,
una búsqueda de caminos más cortos, en 200 casos aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1741_dp.cpp](1741_dp.cpp) | G++ 13.2 x64 | dp | O(n + m) | AC | 0.015 s | 1092 KB |
| [1741_dp.go](1741_dp.go) | Go 1.14 x64 | dp | O(n + m) | AC | 0.046 s | 3284 KB |
| [1741_dp.java](1741_dp.java) | Java 1.8 | dp | O(n + m) | AC | 0.125 s | 5772 KB |
| [1741_dp.py](1741_dp.py) | Python 3.12 x64 | dp | O(n + m) | AC | 0.109 s | 6932 KB |
| [1741_dp.rs](1741_dp.rs) | Rust 1.75 x64 | dp | O(n + m) | AC | 0.015 s | 2164 KB |
