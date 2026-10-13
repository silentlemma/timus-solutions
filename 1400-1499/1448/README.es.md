# 1448. Iluminación en Hogwarts

[Timus 1448](https://acm.timus.ru/problem.aspx?space=1&num=1448) · dificultad 581 · constructive

Problema original de Alexander Mironenko (idea) y Stanislav Vasiliev (texto y programación), del Décimo Campeonato Universitario de Programación por Equipos de los Urales, 24–25 de marzo de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un pasillo tiene N lámparas en fila (1 ≤ N ≤ 10⁶), cada una encendida
del todo o apagada. Argus Filch quiere un brillo de b por ciento
(0 ≤ b ≤ 100) repartido lo más uniformemente posible: hay que imprimir
una fila de N cifras 0 y 1 tal que en cada tramo de L lámparas seguidas
el número de encendidas difiera de L b / 100 como mucho en 2.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego b.

## Salida

La fila de lámparas. Se acepta cualquier fila válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
33
```

Salida:

```
0100100100
```

## Solución

La lámpara i (contando desde 0) se enciende justo cuando
⌊(i + 1) b / 100⌋ es mayor que ⌊i b / 100⌋. Entonces entre las k
primeras hay ⌊k b / 100⌋ encendidas, así que un tramo de l a r tiene
⌊r b / 100⌋ − ⌊l b / 100⌋, que difiere de (r − l) b / 100 en menos de
1, holgadamente dentro de los 2 permitidos. El patrón se repite cada 100
lámparas, porque sumar 100 a i suma exactamente b a ambos suelos.
`O(N)`.

Detalles a tener en cuenta:

- con b = 0 y b = 100 la fila es de una sola cifra (pruebas 02, 03, 05,
  gen1, gen2);
- un millón de cifras debe escribirse de una vez, no con una llamada por
  cifra (gen1 a gen7);
- la fila del ejemplo es solo una de muchas respuestas válidas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1448_constructive.cpp](1448_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 1164 KB |
| [1448_constructive.go](1448_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 2088 KB |
| [1448_constructive.java](1448_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.109 s | 3036 KB |
| [1448_constructive.py](1448_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 2244 KB |
| [1448_constructive.rs](1448_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 2056 KB |
