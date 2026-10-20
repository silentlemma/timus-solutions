# 2125. Continuar una sucesión con su polinomio de menor grado

[Timus 2125](https://acm.timus.ru/problem.aspx?space=1&num=2125) · dificultad 3087 · math

Problema original de Alexey Danilyuk y Oleg Merkurev, del concurso t.me/umnik_team, campamento de Petrozavodsk, verano de 2018.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La complejidad de una sucesión a₁ … aₙ es el menor grado de un
polinomio p con p(x) ≡ aₓ módulo 998 244 353 para x = 1 … n. Continuar
la sucesión dada con m términos más de modo que la complejidad de toda
la sucesión sea la menor posible, e imprimir los términos nuevos. Los
límites son 4 segundos y 128 MB.

## Entrada

n y m, 1 ≤ n ≤ 10⁵, 1 ≤ m ≤ 8 · 10⁵, y luego a₁ … aₙ.

## Salida

b_{n+1} … b_{n+m}.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 10
1 4 9 16 25
```

Salida:

```
36 49 64 81 100 121 144 169 196 225
```

### Ejemplo 2

Entrada:

```
3 3
0 0 0
```

Salida:

```
0 0 0
```

### Ejemplo 3

Entrada:

```
5 10
1 2 4 8 16
```

Salida:

```
31 57 99 163 256 386 562 794 1093 1471
```

### Ejemplo 4

Entrada:

```
3 1
2 1 0
```

Salida:

```
998244352
```

## Solución

Sobre el cuerpo módulo el primo hay exactamente un polinomio de grado
menor que n que pasa por los n puntos dados, y todo polinomio que pasa
por ellos tiene al menos su grado. Continuar con ese polinomio conserva
la complejidad, así que la respuesta son sus valores en n + 1 … n + m.

Con los nodos en 0 … n − 1 (desplazados en uno), la fórmula de Lagrange
para un entero t ≥ n es

p(t) = t! / (t − n)! · Σᵢ wᵢ / (t − i), con
wᵢ = aᵢ · (−1)^{n−1−i} / (i! (n − 1 − i)!).

La suma es una convolución de la sucesión w con la sucesión 1/k, así que
una transformada teórico-numérica de longitud unas 2n + m da los m
valores a la vez; los factoriales y sus inversos salen de una sola
pasada. El módulo 998 244 353 = 119 · 2²³ + 1 tiene las raíces de la
unidad que necesita la transformada. El trabajo es
O((n + m) log(n + m)).

En el primer ejemplo los cuadrados se continúan con el polinomio x²:
36, 49, … 225.

## Notas por lenguaje

La solución en Python se ejecuta con PyPy y hace la misma transformada
sobre arreglos planos de números de 32 bits. Una versión anterior
multiplicaba las sucesiones empaquetadas en números decimales enormes;
con CPython superaba el límite de tiempo en el test 14, y con PyPy el
módulo decimal está escrito en Python puro y es mucho más lento.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2125_math.cpp](2125_math.cpp) | G++ 13.2 x64 | math | O((n + m) log(n + m)) | AC | 0.250 s | 19288 KB |
| [2125_math.go](2125_math.go) | Go 1.14 x64 | math | O((n + m) log(n + m)) | AC | 0.281 s | 41732 KB |
| [2125_math.java](2125_math.java) | Java 1.8 | math | O((n + m) log(n + m)) | AC | 1.687 s | 16320 KB |
| [2125_math.py](2125_math.py) | PyPy 3.10 x64 | math | O((n + m) log(n + m)) | AC | 1.343 s | 57604 KB |
| [2125_math.rs](2125_math.rs) | Rust 1.75 x64 | math | O((n + m) log(n + m)) | AC | 0.187 s | 49012 KB |
