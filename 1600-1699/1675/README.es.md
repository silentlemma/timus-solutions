# 1675. Código lunar 2

[Timus 1675](https://acm.timus.ru/problem.aspx?space=1&num=1675) · dificultad 1793 · combinatorics

Problema original de Igor Chevdar, del Ural SU Contest en el campus de verano de Petrozavodsk, agosto de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Contar las matrices M × N de ceros y unos con exactamente K filas y
exactamente L columnas formadas solo por ceros, módulo 10⁹ + 7.

## Entrada

M, N, K, L (1 ≤ M, N ≤ 100000; 0 ≤ K ≤ M; 0 ≤ L ≤ N).

## Salida

La cuenta módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2 0 0
```

Salida:

```
7
```

### Ejemplo 2

Entrada:

```
2 3 1 1
```

Salida:

```
6
```

## Solución

Se eligen qué K filas y qué L columnas son las nulas, de C(M, K) · C(N, L)
maneras. Todos los unos quedan entonces en el bloque restante a × b, con
a = M − K y b = N − L, y cada fila y cada columna de ese bloque debe
contener un uno.

Las matrices a × b sin filas ni columnas nulas se cuentan por
inclusión-exclusión sobre las columnas obligadas a ser nulas: si j
columnas dadas son nulas, cada una de las a filas es cualquiera de los
2^(b − j) − 1 patrones no nulos en las demás, así que

f(a, b) = Σⱼ (−1)ʲ C(b, j) (2^(b − j) − 1)^a.

La fórmula es simétrica en a y b, así que la suma recorre el lado más
corto. Los factoriales y sus inversos hasta max(M, N) dan los
coeficientes binomiales. `O(max(M, N) + min(a, b) log max(a, b))`.

Detalles a tener en cuenta:

- si todas las filas son nulas, también lo son todas las columnas: K = M
  obliga a L = N (pruebas 06 y 07); la fórmula lo recoge, pues con a = 0
  la suma es Σ (−1)ʲ C(b, j), que vale 1 si b = 0 y 0 si no;
- 0⁰ cuenta como 1 en esa suma.

Las respuestas coinciden con un recuento de todas las matrices hasta
4 × 4 para todo K y L, y con una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1675_combinatorics.cpp](1675_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.015 s | 1760 KB |
| [1675_combinatorics.go](1675_combinatorics.go) | Go 1.14 x64 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.031 s | 2696 KB |
| [1675_combinatorics.java](1675_combinatorics.java) | Java 1.8 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.218 s | 3132 KB |
| [1675_combinatorics.py](1675_combinatorics.py) | Python 3.12 x64 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.500 s | 8372 KB |
| [1675_combinatorics.rs](1675_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.031 s | 1792 KB |
