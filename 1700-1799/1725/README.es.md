# 1725. ¡Agotado!

[Timus 1725](https://acm.timus.ru/problem.aspx?space=1&num=1725) · dificultad 141 · math

Problema original de Denis Dublennykh (preparado por Oleg Dolgorukov), del Concurso Regional Escolar de Programación de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Vasya se sienta primero en una fila de n asientos, en el asiento k; los
demás llegan uno a uno hasta llenar la fila. Cada uno entra por el
extremo con menos gente ya sentada entre ese extremo y su asiento, o,
si hay empate, por el extremo más cercano. Hallar el mayor número de
personas que pueden tropezar con las piernas de Vasya.

## Entrada

n y k (1 ≤ k ≤ n ≤ 50, n par).

## Salida

El mayor número de personas que tropiezan con Vasya.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 1
```

Salida:

```
1
```

## Solución

Se llama lado lejano a la parte más larga de la fila más allá de
Vasya; tiene max(k − 1, n − k) asientos. La respuesta es esa cantidad
menos 2, pero no menos de 0. `O(1)`.

Los dos asientos del extremo lejano nunca tropiezan. Más allá del
último no hay nadie, y más allá del penúltimo hay a lo sumo una
persona, mientras que al otro lado está Vasya, y en el empate su propio
extremo está más cerca.

Todos los demás del lado lejano pueden tropezar. Se sientan primero los
dos asientos del extremo y luego se llena el lado lejano desde su
extremo hacia Vasya. Así cada persona nueva tiene en el camino desde el
extremo de Vasya solo a Vasya, y desde el otro extremo al menos a dos
personas, por lo que pasa junto a Vasya.

La gente del lado cercano también puede tropezar, pero solo cuando ese
lado ya está mucho más lleno que el lejano, y entonces la gente del
lado lejano encuentra demasiada gente del lado de Vasya y deja de
tropezar. Nunca sale a cuenta.

En el ejemplo el lado lejano tiene tres asientos, así que tropieza una
persona: la del asiento 2, después de ocuparse los asientos 3 y 4.

Trampas:

- con n = 2 o con Vasya en medio de cuatro asientos la respuesta es 0,
  no un número negativo;
- el lado lejano puede estar a cualquier lado de Vasya.

La fórmula coincide con una búsqueda exhaustiva de todos los órdenes de
llegada para todo n par hasta 16 y todo k.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1725_math.cpp](1725_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 396 KB |
| [1725_math.go](1725_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB |
| [1725_math.java](1725_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1592 KB |
| [1725_math.py](1725_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 340 KB |
| [1725_math.rs](1725_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 236 KB |
