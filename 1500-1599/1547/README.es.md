# 1547. Búsqueda de contraseñas

[Timus 1547](https://acm.timus.ru/problem.aspx?space=1&num=1547) · dificultad 857 · math

Problema original de Vladimir Yakovlev, del XI Campeonato Universitario por Equipos de Programación de los Urales, Ekaterimburgo, 21 de abril de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Todas las contraseñas de letras minúsculas de longitud 1 a N se listan
por longitud y luego alfabéticamente: a, …, z, aa, …, zz, …. Hay que
partir la lista en M rangos consecutivos lo más iguales posible, los
primeros con una más si hace falta, y escribir cada rango como
primera-última (1 ≤ N, M ≤ 50; hay al menos M contraseñas).

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M.

## Salida

M líneas «primera-última».

## Ejemplos

### Ejemplo 1

Entrada:

```
5 4
```

Salida:

```
a-fssst
fsssu-mmmmn
mmmmo-tgggg
tgggh-zzzzz
```

## Solución

Hay T = 26 + 26² + … + 26ᴺ contraseñas, hasta unas 6·10⁷⁰. Con
T = q·M + r, el procesador i (desde 0) cubre las contraseñas numeradas
de i·q + min(i, r) + 1 a (i + 1)·q + min(i + 1, r).

Listar cadenas por longitud y luego alfabéticamente es la numeración
biyectiva en base 26: la k-ésima contraseña (desde 1) es k escrito con
las cifras a = 1, …, z = 26. Para convertir, se toma una y otra vez
(k − 1) mod 26 como última letra y se sigue con ⌊(k − 1) / 26⌋.

Python, Go y Java usan sus enteros grandes. C++ y Rust guardan los
números como listas de cifras en base 26: T es 11…10 en esa base, la
división entre M es una división larga, los extremos de los rangos son q
por un número pequeño más un número pequeño, y la conversión resta 1 y
quita la cifra más baja. `O(M·N)` operaciones con cifras.

Detalles a tener en cuenta:

- un rango de una sola contraseña se escribe igualmente como
  primera-última, como a-a (prueba 03);
- las cantidades llegan a 71 cifras (prueba 04);
- los primeros T mod M procesadores se llevan las contraseñas de más
  (prueba 07).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1547_math.cpp](1547_math.cpp) | G++ 13.2 x64 | math | O(M * N) | AC | 0.015 s | 200 KB |
| [1547_math.go](1547_math.go) | Go 1.14 x64 | math | O(M * N) | AC | 0.031 s | 1348 KB |
| [1547_math.java](1547_math.java) | Java 1.8 | math | O(M * N) | AC | 0.125 s | 3264 KB |
| [1547_math.py](1547_math.py) | Python 3.12 x64 | math | O(M * N) | AC | 0.093 s | 400 KB |
| [1547_math.rs](1547_math.rs) | Rust 1.75 x64 | math | O(M * N) | AC | 0.015 s | 240 KB |
