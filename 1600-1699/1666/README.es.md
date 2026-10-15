# 1666. Vasya Ferrari

[Timus 1666](https://acm.timus.ru/problem.aspx?space=1&num=1666) · dificultad 1285 · math

Problema original de Igor Chevdar, del Ural SU Contest en el campus de invierno de Petrozavodsk, enero de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Factorizar x⁴ + ax³ + bx² + cx + d en tantos factores con coeficientes
enteros como sea posible. Imprimir `Irreducible` si no hay
factorización y, si no, los factores entre paréntesis, sin espacios,
términos nulos, coeficientes unitarios ni exponentes 1 (el término
constante 1 sí se escribe).

## Entrada

Enteros a, b, c, d de valor absoluto a lo sumo 20000.

## Salida

La factorización o `Irreducible`.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 0 0 0
```

Salida:

```
(x)(x)(x)(x)
```

### Ejemplo 2

Entrada:

```
-4 -3 24 45
```

Salida:

```
(x2+3x+3)(x2-7x+15)
```

### Ejemplo 3

Entrada:

```
1 1 1 1
```

Salida:

```
Irreducible
```

## Solución

El polinomio es mónico, así que por el lema de Gauss toda factorización
sobre los enteros puede hacerse con factores mónicos, y la que tiene más
factores es la factorización en irreducibles.

1. Se sacan las raíces enteras una a una. Una raíz entera de un polinomio
   mónico entero divide su término constante (un término constante nulo
   significa la raíz 0), así que probando los divisores del término
   constante se encuentra. Cada raíz r separa x − r y la división
   sintética deja el cociente.
2. Si no quedan raíces, un resto cúbico o cuadrático es irreducible.
3. Una cuártica sin raíces es irreducible o producto de dos cuadráticas
   (x² + px + q)(x² + rx + s). Comparando coeficientes: qs = d,
   p + r = a, q + s + pr = b, ps + qr = c. Para cada divisor q de d,
   s = d / q; si q ≠ s, eliminar r da p(s − q) = c − aq, así que p
   queda fijado; si q = s, p y r son las raíces de t² − at + (b − 2q),
   enteras solo si el discriminante es un cuadrado perfecto. Cada
   candidato se comprueba con las dos últimas ecuaciones.

Aquí B = max(1, |a|, |b|, |c|, |d|) ≤ 20000, y todos los valores
quedan por debajo de 10¹⁸.

Detalles a tener en cuenta:

- los factores pueden ir en cualquier orden; un comprobador los
  multiplica, los cuenta y revisa cómo está escrito cada uno;
- x⁴ + 4 no tiene raíces pero se parte en (x² + 2x + 2)(x² − 2x + 2)
  (prueba 11);
- constantes iguales en las dos cuadráticas necesitan la vía del
  discriminante (prueba 06).

Las respuestas coinciden con una implementación aceptada independiente
en entradas aleatorias y construidas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1666_math.cpp](1666_math.cpp) | G++ 13.2 x64 | math | O(√B) | AC | 0.031 s | 200 KB |
| [1666_math.go](1666_math.go) | Go 1.14 x64 | math | O(√B) | AC | 0.031 s | 1100 KB |
| [1666_math.java](1666_math.java) | Java 1.8 | math | O(√B) | AC | 0.125 s | 1716 KB |
| [1666_math.py](1666_math.py) | Python 3.12 x64 | math | O(√B) | AC | 0.093 s | 752 KB |
| [1666_math.rs](1666_math.rs) | Rust 1.75 x64 | math | O(√B) | AC | 0.031 s | 240 KB |
