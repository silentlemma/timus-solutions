# 1716. Solución alternativa

[Timus 1716](https://acm.timus.ru/problem.aspx?space=1&num=1716) · dificultad 727 · probability

Problema original de Alexander Pronchenkov, preparado por Daniil Ayzenshteyn, de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada test de un problema tiene la respuesta YES (3 bytes) o NO
(2 bytes). Un programa tramposo imprime YES en el primer test y en cada
test siguiente la respuesta del anterior. Dados el número de tests n y
el tamaño total s de las respuestas, hallar el número esperado de tests
fallados sobre todos los órdenes de los tests, igualmente probables.

## Entrada

n y s (1 ≤ n ≤ 5000, 2n ≤ s ≤ 3n).

## Salida

El número esperado de tests fallados, con un error de a lo sumo 10⁻⁵.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 7
```

Salida:

```
2.0000000
```

## Solución

Los tamaños dan las cantidades: y = s − 2n respuestas son YES y
k = n − y son NO. Por la linealidad de la esperanza, se suman las
probabilidades de que falle cada test. El primero falla cuando su
respuesta es NO, con probabilidad k/n. Cada test posterior falla cuando
su respuesta difiere de la anterior. Dos lugares dados contienen un YES
y un NO en cualquier orden con probabilidad 2yk/(n(n − 1)). Los n − 1
tests posteriores suman 2yk/n, así que la esperanza es

k/n + 2yk/n = k(2y + 1)/n.

El ejemplo tiene y = 1 y k = 2, lo que da 2 · 3/3 = 2. `O(1)`.

Trampas:

- el primer test se compara con un YES imaginario, no con nada;
- k(2y + 1) llega a unos 1,25 · 10⁷, muy dentro de los enteros de
  64 bits, y solo se divide al final;
- n = 1 no necesita un caso especial, pues en la fórmula no queda
  n − 1.

La fórmula coincide con una enumeración exhaustiva de todos los órdenes
para todo n hasta 7 y todo número de respuestas YES.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1716_probability.cpp](1716_probability.cpp) | G++ 13.2 x64 | probability | O(1) | AC | 0.015 s | 140 KB |
| [1716_probability.go](1716_probability.go) | Go 1.14 x64 | probability | O(1) | AC | 0.031 s | 1084 KB |
| [1716_probability.java](1716_probability.java) | Java 1.8 | probability | O(1) | AC | 0.109 s | 1820 KB |
| [1716_probability.py](1716_probability.py) | Python 3.12 x64 | probability | O(1) | AC | 0.078 s | 416 KB |
| [1716_probability.rs](1716_probability.rs) | Rust 1.75 x64 | probability | O(1) | AC | 0.062 s | 268 KB |
