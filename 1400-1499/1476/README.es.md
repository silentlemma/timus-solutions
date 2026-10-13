# 1476. Código lunar

[Timus 1476](https://acm.timus.ru/problem.aspx?space=1&num=1476) · dificultad 1263 · dp

Problema original de Alexander Ipatov (idea de Alexander Toropov), del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que contar las matrices M × N de ceros y unos (1 ≤ M, N ≤ 40) en las
que, para cada par de columnas vecinas i e i + 1, como mucho K filas
(0 ≤ K ≤ M) tienen un 0 en la columna i y un 1 en la columna i + 1.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

M, N y K.

## Salida

El número de esas matrices.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 1 0
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
2 2 1
```

Salida:

```
15
```

## Solución

Se rellena la matriz columna a columna. Que la columna siguiente esté
permitida depende de en qué filas de la actual hay ceros, pero el
número de formas de seguir solo depende de cuántos unos tiene la
columna. Desde una columna con c unos, una siguiente con d unos se
obtiene convirtiendo t ≤ K de los M − c ceros en unos y conservando
s = d − t de los c unos: step(c, d) = Σ C(M − c, t)·C(c, d − t) sobre
t ≤ K. Estos números no pasan de 2⁴⁰. La primera columna con c unos se
elige de C(M, c) maneras; cada columna más multiplica el vector de
cuentas por la tabla step, y la respuesta es la suma tras N columnas.
`O(M²(K + N))` operaciones aritméticas sobre números de hasta M·N + 1 bits.

Detalles a tener en cuenta:

- con K = M vale cualquier matriz, y 2¹⁶⁰⁰ necesita enteros grandes
  (prueba 03);
- una sola fila con K = 0 significa que la fila nunca pasa de 0 a 1:
  N + 1 matrices (prueba 05);
- una sola columna no tiene pares que comprobar: 2^M matrices
  (pruebas 01, 06).

## Notas por lenguaje

- C++ y Rust guardan las cuentas en bloques de base 10⁹ y usan
  aritmética de 128 bits para multiplicar por los valores step de 64
  bits y sumar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1476_dp.cpp](1476_dp.cpp) | G++ 13.2 x64 | dp | O(M^2(K + N)) arithmetic operations | AC | 0.031 s | 492 KB |
| [1476_dp.go](1476_dp.go) | Go 1.14 x64 | dp | O(M^2(K + N)) arithmetic operations | AC | 0.046 s | 2104 KB |
| [1476_dp.java](1476_dp.java) | Java 1.8 | dp | O(M^2(K + N)) arithmetic operations | AC | 0.125 s | 6228 KB |
| [1476_dp.py](1476_dp.py) | Python 3.12 x64 | dp | O(M^2(K + N)) arithmetic operations | AC | 0.093 s | 540 KB |
| [1476_dp.rs](1476_dp.rs) | Rust 1.75 x64 | dp | O(M^2(K + N)) arithmetic operations | AC | 0.031 s | 516 KB |
