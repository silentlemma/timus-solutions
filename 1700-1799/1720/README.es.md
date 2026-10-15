# 1720. Summit Online Judge

[Timus 1720](https://acm.timus.ru/problem.aspx?space=1&num=1720) · dificultad 978 · math

Problema original de Alex Samsonov, de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada concurso tiene de x a y problemas. Un tamaño de volumen es
correcto si algún número de concursos puede reunir exactamente esa
cantidad de problemas. Contar los tamaños correctos de l a r.

## Entrada

x, y, l y r (1 ≤ x ≤ y ≤ 10¹⁸, 1 ≤ l ≤ r ≤ 10¹⁸).

## Salida

El número de tamaños correctos en [l, r].

## Ejemplos

### Ejemplo 1

Entrada:

```
4 5 7 13
```

Salida:

```
5
```

## Solución

Con k concursos los totales alcanzables son exactamente el intervalo
[kx, ky]. El intervalo k + 1 empieza en (k + 1)x. Toca al intervalo k,
cuyo último número es ky, cuando (k + 1)x ≤ ky + 1, es decir
k(y − x) ≥ x − 1. Esto vale desde algún K, y desde K·x todo número
queda cubierto. Antes de K los intervalos están separados. Así que se
cuentan los números cubiertos hasta t y la respuesta es C(r) − C(l − 1):

- si x = y, los cubiertos son los múltiplos de x, así que C(t) = ⌊t/x⌋;
- si no, K = max(1, ⌈(x − 1)/(y − x)⌉). Los intervalos k < K que
  terminan a más tardar en t, los de k ≤ ⌊t/y⌋, suman
  (y − x)·f(f + 1)/2 + f para su cantidad f;
- el siguiente intervalo puede terminar más allá de t y suma
  t − kx + 1 si empieza a más tardar en t;
- desde K·x, todo hasta t cuenta.

En el ejemplo, K = 3: los intervalos [4, 5] y [8, 10] están separados,
y todo desde 12 está cubierto, así que 8, 9, 10, 12 y 13 son correctos.
`O(1)`.

Trampas:

- con x = 1 el primer intervalo ya se une al resto:
  ⌈0/(y − x)⌉ = 0, así que K debe ser al menos 1;
- K·x puede llegar a 10³⁶, así que se compara K ≤ ⌊t/x⌋ en vez de
  K·x ≤ t; la suma de los intervalos separados queda por debajo de t y
  cabe en 64 bits;
- con x = y no hay punto de unión.

Los conteos coinciden con una búsqueda exhaustiva para todos los x, y y
t hasta cotas pequeñas, y con una implementación aceptada independiente
en 700 casos aleatorios hasta 10¹⁸.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1720_math.cpp](1720_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1720_math.go](1720_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1108 KB |
| [1720_math.java](1720_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1608 KB |
| [1720_math.py](1720_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 496 KB |
| [1720_math.rs](1720_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 224 KB |
