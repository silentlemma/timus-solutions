# 1066. El extremo más bajo de una guirnalda que cuelga

[Timus 1066](https://acm.timus.ru/problem.aspx?space=1&num=1066) · dificultad 580 · math

Problema original del concurso regional ACM ICPC del noreste de Europa 2000–2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una guirnalda de `N` lámparas (`3 ≤ N ≤ 1000`) cuelga de sus extremos.
Cada lámpara interior cuelga 1 milímetro por debajo de la altura media de
sus dos vecinas: `H(i) = (H(i−1) + H(i+1)) / 2 − 1`. La primera lámpara
está a altura `A` (`10 ≤ A ≤ 1000`, un número real). Ninguna lámpara puede
quedar bajo el suelo, aunque algunas pueden tocarlo (`H(i) ≥ 0`). Halla la
menor altura posible `B` de la última lámpara.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `A` en una línea.

## Salida

`B`, con al menos dos cifras tras el punto decimal.

## Evaluación

Los números se comparan con un error absoluto de 0.011: las respuestas se
imprimen con dos decimales, así que la última cifra puede diferir en uno.

## Ejemplos

### Ejemplo 1

Entrada:

```
8 15
```

Salida:

```
9.75
```

### Ejemplo 2

Entrada:

```
692 532.81
```

Salida:

```
446113.34
```

## Solución

La regla equivale a `H(i+1) = 2·H(i) − H(i−1) + 2`: la segunda diferencia
de las alturas siempre vale 2. Así que la segunda altura `x` fija toda la
guirnalda:

`H(i) = A + (i−1)·(x − A) + (i−1)·(i−2)`.

La última altura crece con `x` (su coeficiente `N − 1` es positivo), así
que la respuesta sale del menor `x` que deja todas las lámparas a altura 0
o más. Para la lámpara `k + 1` la condición `H(k+1) ≥ 0` significa
`x ≥ A − A/k − (k − 1)`, y `x` es la mayor de estas cotas para
`k = 1 … N−1` (la cota para `k = 1` es `x ≥ 0`). Luego `B = H(N)`. `O(N)`.

Detalles a tener en cuenta:

- la lámpara que toca el suelo no siempre está en el medio: la cota es
  máxima donde `A/k + k` es mínimo, cerca de `k = √A`, y cuando eso queda
  más allá del final de la guirnalda es la propia última lámpara la que
  toca el suelo y `B = 0`;
- `B` crece como `N^2` y llega a unos `10^6`, que un `double` guarda con
  holgura;
- una búsqueda binaria sobre la segunda altura también funciona, pero la
  fórmula no necesita iteraciones ni tolerancia.

Las respuestas se comprobaron con fracciones exactas: la recurrencia
avanzada desde la segunda altura elegida deja todas las lámparas a altura
0 o más, y una de ellas exactamente en 0.

## Notas por lenguaje

- Python halla la segunda altura con un solo `max` sobre un generador.
- Java lee `A` con `Locale.US`, así que el punto decimal se acepta sea
  cual sea la configuración regional del sistema.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1066_math.cpp](1066_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 156 KB |
| [1066_math.go](1066_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1084 KB |
| [1066_math.java](1066_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 2008 KB |
| [1066_math.py](1066_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.093 s | 392 KB |
| [1066_math.rs](1066_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 272 KB |
