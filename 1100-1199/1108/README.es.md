# 1108. Fracciones unitarias que dejan el menor resto positivo

[Timus 1108](https://acm.timus.ru/problem.aspx?space=1&num=1108) · dificultad 252 · math

Problema original de Pavlin Peev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elige enteros positivos `a_1 ≤ a_2 ≤ … ≤ a_N` (`1 ≤ N ≤ 18`) de modo que
`1 − (1/a_1 + … + 1/a_N)` sea positivo y lo más pequeño posible.
Imprímelos en ese orden, uno por línea.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

`a_1`, …, `a_N`, cada uno en su propia línea.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
2
3
```

## Solución

Cada fracción se toma de forma voraz: la mayor fracción unitaria que aún
deja algo. Así sale la sucesión de Sylvester `a_1 = 2`,
`a_{k+1} = a_k (a_k − 1) + 1`, y por inducción el resto tras `k` términos
es exactamente `1 / (a_{k+1} − 1)`, de modo que la siguiente mayor
fracción admisible es `1/a_{k+1}`. Que la elección voraz sea además la
mejor para todo `N` es un resultado clásico sobre fracciones egipcias
(Curtiss, 1922).

Los términos se elevan al cuadrado en cada paso: `a_18` tiene unas 26 700
cifras y la salida entera unos 53 000 caracteres, así que hacen falta
enteros grandes. Una multiplicación por término, `O(D²)` con el método
escolar para `D` cifras, basta de sobra.

Detalles a tener en cuenta:

- los enteros de 64 bits se desbordan ya en `a_8`;
- Python se niega por defecto a convertir a texto enteros de más de 4300
  cifras, y `a_16` ya los supera;
- los denominadores deben imprimirse completos, sin notación científica
  ni redondeo.

Las respuestas se comprobaron con una búsqueda sobre todos los
denominadores no decrecientes con fracciones exactas para `N ≤ 4`, y para
todo `N` verificando con fracciones exactas que el resto es
`1 / (a_1 ⋯ a_N)`, el valor que da el argumento voraz.

## Notas por lenguaje

- Go y Java usan `math/big` y `BigInteger`; los enteros propios de Python
  necesitan `sys.set_int_max_str_digits(0)` antes de imprimir.
- C++ y Rust guardan el número en cifras de base `10^9` y calculan
  `a · (a − 1) + 1` con la multiplicación escolar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1108_math.cpp](1108_math.cpp) | G++ 13.2 x64 | math | O(D²) per term | AC | 0.015 s | 232 KB |
| [1108_math.go](1108_math.go) | Go 1.14 x64 | math | O(D²) per term | AC | 0.015 s | 1920 KB |
| [1108_math.java](1108_math.java) | Java 1.8 | math | O(D²) per term | AC | 0.187 s | 6508 KB |
| [1108_math.py](1108_math.py) | Python 3.12 x64 | math | O(D²) per term | AC | 0.031 s | 1144 KB |
| [1108_math.rs](1108_math.rs) | Rust 1.75 x64 | math | O(D²) per term | AC | 0.015 s | 356 KB |
