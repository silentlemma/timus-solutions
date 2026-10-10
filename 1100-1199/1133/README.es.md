# 1133. Hallar un término de una sucesión de tipo Fibonacci a partir de otros dos

[Timus 1133](https://acm.timus.ru/problem.aspx?space=1&num=1133) · dificultad 224 · number_theory

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una sucesión entera, infinita en ambos sentidos, cumple
`F(k + 2) = F(k + 1) + F(k)` para todo `k`. Dados `F(i)` y `F(j)` con
`i ≠ j`, halla `F(n)`. Todos los índices están en `[−1000, 1000]`, y cada
término desde el menor hasta el mayor de `i, j, n` está dentro de
`±2·10⁹`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Cinco enteros: `i`, `F(i)`, `j`, `F(j)`, `n`.

## Salida

`F(n)`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5 -1 4 5
```

Salida:

```
12
```

## Solución

Sea `i < j` (si no, se intercambian los pares). Cada término es una
combinación entera fija de `F(i)` y `F(i + 1)`:
`F(j) = A·F(i) + B·F(i + 1)`, donde `A` y `B` son números de Fibonacci que
se obtienen avanzando el par de coeficientes desde `(1, 0)` y `(0, 1)`
durante `j − i` pasos. Así, la incógnita `F(i + 1) = (F(j) − A·F(i)) / B`,
y luego se recorre la sucesión hacia delante o hacia atrás desde `i`
hasta `n` con `F(k − 1) = F(k + 1) − F(k)`.

El problema es el tamaño: `B` puede ser el número de Fibonacci 2000,
mucho más allá de 64 bits, mientras que la respuesta es pequeña. Por eso
todo se calcula módulo el primo `P = 4294967291`. Es mayor que las
`4·10⁹ + 1` respuestas posibles, así que el resto de `F(n)` la determina:
un resto mayor que `P / 2` representa un valor negativo. Es menor que
`2³²`, así que el producto de dos restos cabe en un entero sin signo de 64
bits. La división es una multiplicación por `B^(P−2)`, que funciona porque
ningún número de Fibonacci con índice de 1 a 2000 es divisible por `P`
(comprobado directamente). Lineal en la anchura `W` del rango de índices:
como mucho 4000 pasos.

Detalles a tener en cuenta:

- los valores intermedios `A` y `B` son enormes aunque todas las entradas
  y la respuesta sean pequeñas; la aritmética normal de 64 bits desborda;
- `n` puede estar fuera del intervalo de `i` a `j`, por cualquier lado;
- los índices dados pueden venir en cualquier orden;
- la sucesión nula permite índices separados por 2000, así que el
  recorrido tiene hasta 2000 pasos.

Las respuestas se compararon con un cálculo exacto con enteros grandes en
todas las pruebas y en 200 consultas aleatorias, que además comprobó que
las entradas cumplen el límite de `±2·10⁹`.

## Notas por lenguaje

- Todos los lenguajes usan el mismo módulo y el mismo recorrido.
- Java no tiene tipo de 64 bits sin signo, pero `Long.remainderUnsigned`
  reduce correctamente el producto desbordado.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1133_number_theory.cpp](1133_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(W) | AC | 0.015 s | 128 KB |
| [1133_number_theory.go](1133_number_theory.go) | Go 1.14 x64 | number_theory | O(W) | AC | 0.015 s | 1064 KB |
| [1133_number_theory.java](1133_number_theory.java) | Java 1.8 | number_theory | O(W) | AC | 0.156 s | 1688 KB |
| [1133_number_theory.py](1133_number_theory.py) | Python 3.12 x64 | number_theory | O(W) | AC | 0.078 s | 436 KB |
| [1133_number_theory.rs](1133_number_theory.rs) | Rust 1.75 x64 | number_theory | O(W) | AC | 0.015 s | 220 KB |
