# 1823. Gas ideal

[Timus 1823](https://acm.timus.ru/problem.aspx?space=1&num=1823) · dificultad 348 · math

Problema original atribuido a Benoît Paul Émile Clapeyron y Dmitri Mendeléiev, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La ley de los gases ideales pV = nRT relaciona la presión p, la
cantidad de sustancia n, el volumen V y la temperatura T, con
R = 8.314. Se dan tres de los cuatro valores; hallar el cuarto. El
volumen y la temperatura deben ser positivos. Imprimir "error" si los
datos se contradicen y "undefined" si el valor no queda determinado de
forma única.

## Entrada

Tres líneas "X = value" para tres magnitudes distintas X entre p, n, V
y T, cada valor un entero no negativo de hasta 1000. Los V y T dados
son positivos.

## Salida

"X = value" con error absoluto o relativo de como mucho 10⁻⁶, o
"error", o "undefined".

## Ejemplos

### Ejemplo 1

Entrada:

```
p = 1
n = 1
V = 1
```

Salida:

```
T = 0.120279
```

## Solución

Se despeja el valor que falta de pV = nRT; los valores dados son
enteros, así que toda comprobación de cero es exacta.

- p = nRT/V y n = pV/(RT): V y T están dados y son positivos, así que
  el resultado siempre está definido, quizá 0.
- V = nRT/p: si p = 0 la ecuación queda 0 = nRT, que vale para todo V
  cuando n = 0 ("undefined") y para ninguno cuando n > 0 ("error"). Si
  p > 0 y n = 0, V saldría 0, lo que no se permite ("error").
- T = pV/(nR) funciona igual, con n en lugar de p.

`O(1)`.

En el ejemplo T = 1·1/(1·8.314) ≈ 0.120279.

Trampas:

- una presión nula o una cantidad de gas nula están permitidas y son
  una respuesta válida cuando la incógnita es p o n;
- un volumen o una temperatura calculados iguales a cero son un error,
  no una respuesta;
- las líneas pueden venir en cualquier orden.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1823_math.cpp](1823_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 420 KB |
| [1823_math.go](1823_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1124 KB |
| [1823_math.java](1823_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1764 KB |
| [1823_math.py](1823_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 500 KB |
| [1823_math.rs](1823_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 444 KB |
