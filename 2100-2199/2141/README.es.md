# 2141. Suma alterna máxima de un segmento

[Timus 2141](https://acm.timus.ru/problem.aspx?space=1&num=2141) · dificultad 251 · dp

Problema original de Alexander Lozhkin, del Concurso por Equipos de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elegir un segmento contiguo de una sucesión, posiblemente vacío, y
sumarlo con signos alternos: el primer elemento elegido con más, el
segundo con menos y así sucesivamente. Hallar el mayor valor posible.
Los límites son 1 segundo y 256 MB.

## Entrada

n, 1 ≤ n ≤ 10⁵, y luego a₁ … aₙ, −10⁵ ≤ aᵢ ≤ 10⁵.

## Salida

La mayor suma alterna (0 para el segmento vacío).

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1 2 3 4 5
```

Salida:

```
5
```

### Ejemplo 2

Entrada:

```
5
1 -2 3 -4 5
```

Salida:

```
15
```

### Ejemplo 3

Entrada:

```
5
-1 -2 -3 -4 -5
```

Salida:

```
2
```

## Solución

Se recorre la sucesión guardando dos valores para los segmentos que
terminan en el elemento actual: P, la mejor suma cuando este elemento
lleva más, y M, cuando lleva menos. Un elemento con más empieza un
segmento nuevo o va tras uno con menos, y un elemento con menos siempre
va tras uno con más:

- P = a + max(0, M anterior),
- M = P anterior − a.

El primer elemento solo puede llevar más, así que se empieza con P = a₁,
y M se pone a 0, lo que en el paso siguiente solo significa "empezar de
nuevo". La respuesta es el mayor P o M visto, o 0. Las sumas llegan a
10¹⁰, así que hacen falta enteros de 64 bits. El recorrido cuesta O(n).

En el segundo ejemplo 1 − (−2) + 3 − (−4) + 5 = 15.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2141_dp.cpp](2141_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.078 s | 140 KB |
| [2141_dp.go](2141_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.078 s | 1916 KB |
| [2141_dp.java](2141_dp.java) | Java 1.8 | dp | O(n) | AC | 0.125 s | 496 KB |
| [2141_dp.py](2141_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.125 s | 12312 KB |
| [2141_dp.rs](2141_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.031 s | 2148 KB |
