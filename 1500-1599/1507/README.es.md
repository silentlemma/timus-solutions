# 1507. Decisión difícil

[Timus 1507](https://acm.timus.ru/problem.aspx?space=1&num=1507) · dificultad 447 · math

Problema original de Evgeny Krokhalev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una matriz A de n × n (2 ≤ n ≤ 50) de enteros de 0 a 100, hay que
decidir si la matriz
B = A^(n(n−1)) + A^(n(n−1)+1) + … + A^(n(n+1)) tiene algún elemento
nulo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y luego las n filas de A.

## Salida

«No» si B tiene un elemento nulo; si no, «Yes».

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 7
15 30
```

Salida:

```
Yes
```

### Ejemplo 2

Entrada:

```
3
100 35 40
0 22 0
10 11 0
```

Salida:

```
No
```

## Solución

Los elementos son enormes, pero solo importa si son nulos, y con
elementos no negativos una suma solo es nula si lo son todos sus
términos, y un producto solo si lo es algún factor. Así que A se ve como un grafo dirigido con una arista
i → j donde el elemento no es nulo: (A^k)[i][j] no es nulo justo cuando
algún camino de longitud k lleva de i a j, y B no tiene ceros justo
cuando cada j se alcanza desde cada i por un camino de longitud entre
n(n−1) y n(n+1).

Cada fila de una matriz booleana se guarda como máscara de bits, y un
producto combina con OR las filas del segundo factor elegidas por los
bits del primero. Se calcula A^(n(n−1)) por cuadrados sucesivos y luego
las 2n + 1 potencias consecutivas, una multiplicación cada vez,
uniéndolas con OR. Unos 125 productos de `O(n²)` operaciones sobre
palabras.

De hecho la respuesta es «Yes» justo cuando el grafo es fuertemente
conexo: una comprobación de todos los grafos con n ≤ 4 y de grafos
aleatorios hasta n = 12 no encontró excepciones. La ventana de 2n + 1
longitudes consecutivas cubre todos los restos de una estructura
cíclica, así que incluso un solo ciclo, cuyas potencias nunca son
positivas, la cumple.

Detalles a tener en cuenta:

- la fórmula solo aparece como imagen en el enunciado: las potencias
  van de n(n−1) a n(n+1);
- los valores reales desbordan los enteros de 64 bits, así que solo se
  calcula si son nulos o no (prueba 06);
- un solo ciclo no tiene ninguna potencia positiva, pero B no tiene
  ceros (pruebas 03, 07);
- un enlace en un solo sentido entre dos partes, o un vértice sin
  aristas de salida o de entrada, dan ceros (pruebas 04, 08, gen3).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1507_math.cpp](1507_math.cpp) | G++ 13.2 x64 | math | O(n^3) | AC | 0.015 s | 188 KB |
| [1507_math.go](1507_math.go) | Go 1.14 x64 | math | O(n^3) | AC | 0.031 s | 1184 KB |
| [1507_math.java](1507_math.java) | Java 1.8 | math | O(n^3) | AC | 0.171 s | 524 KB |
| [1507_math.py](1507_math.py) | Python 3.12 x64 | math | O(n^3) | AC | 0.140 s | 740 KB |
| [1507_math.rs](1507_math.rs) | Rust 1.75 x64 | math | O(n^3) | AC | 0.046 s | 256 KB |
