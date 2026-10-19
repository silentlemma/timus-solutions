# 2114. El triángulo rectángulo más pesado de un tamaño dado en una cuadrícula

[Timus 2114](https://acm.timus.ru/problem.aspx?space=1&num=2114) · dificultad 1001 · prefix_sums

Problema original de Valentin Zuev, de la Olimpiada Académica Universitaria Escolar de Informática 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cuadrícula n × m contiene números no negativos. El agua vertida en
la casilla (x₀, y₀) cubre las casillas (x, y) con x ≥ x₀, y ≥ y₀ y
x + y ≤ x₀ + y₀ + k, un triángulo rectángulo con catetos de k + 1
casillas. Para cada uno de los q valores de k, hallar una casilla donde
la suma cubierta sea la mayor e imprimir la suma y la casilla. Los
límites son 3 segundos y 256 MB.

## Entrada

n y m, 1 ≤ n, m ≤ 500, la cuadrícula, 0 ≤ aᵢⱼ ≤ 10⁹, luego q,
1 ≤ q ≤ 50, y los valores 1 ≤ kᵢ ≤ 10⁵.

## Salida

Para cada k, la mayor suma y una casilla que la da.

## Evaluación

Un comprobador acepta cualquier casilla con la mayor suma.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5
1 4 7 4 1
4 7 9 7 4
1 4 7 4 1
1
3
```

Salida:

```
50 1 2
```

### Ejemplo 2

Entrada:

```
3 3
1 2 3
4 5 6
7 8 9
4
2 3 4 5
```

Salida:

```
30 2 1
39 2 1
45 1 1
45 1 1
```

### Ejemplo 3

Entrada:

```
3 5
3 4 3 2 1
2 3 4 3 2
1 2 3 4 3
2
2 3
```

Salida:

```
18 1 2
25 1 2
```

### Ejemplo 4

Entrada:

```
9 4
8 1 8 718
88 88 1 8
8 818 1 8
888 8 1 8
1 88 88 8
1 888 8 8
1 8 88 81
1 8 788 1
188 8 8 1
3
3 5 7
```

Salida:

```
2626 1 1
2992 2 1
4001 3 1
```

### Ejemplo 5

Entrada:

```
15 6
888 88 1 88 8 8
88 88 1 1 88 88
8 8 111 111 8 8
88 11 1 1 11 88
8 1 88 1 881 88
8 1 88 1 88 118
811 88 1 88 1 8
8 1 88 1 88 118
8 111 1 1 111 8
81 8 1 111 8 18
88 88 1 1 88 88
8 1 88 1 88 188
8 8 188 881 8 8
88 88 1 1 88 88
888 88 1 88 8 8
5
7 13 14 8 7
```

Salida:

```
3245 9 1
6371 3 1
6725 2 1
3883 1 1
3245 9 1
```

## Solución

Sea T(x, y) la suma del triángulo en (x, y). El triángulo en
(x + 1, y − 1) tiene la misma hipotenusa x + y + k. Comparado con él, el
triángulo en (x, y) añade las casillas de la fila x desde la columna y
hasta la y + k y pierde las de la columna y − 1 desde la fila x + 1
hasta la x + k + 1. Con sumas prefijas por filas y por columnas ambas
partes cuestan O(1), así que

T(x, y) = T(x + 1, y − 1) + parte de fila − parte de columna.

En la primera columna no hay vecino izquierdo: T(x, 1) es T(x + 1, 1)
más la parte de fila, menos las casillas de la diagonal x + y = x + k + 2
por debajo de la fila x, que salen del triángulo al subirlo. Las sumas
prefijas a lo largo de cada antidiagonal dan también esa parte en O(1).

Yendo de la fila de abajo hacia arriba, cada fila de valores sale de la
de debajo, así que una consulta cuesta O(n m), y todas O(q n m) más las
sumas prefijas. Una k que llega a la esquina opuesta cubre toda la
cuadrícula desde (1, 1). Las sumas llegan a 2.5 · 10¹⁴ y necesitan
enteros de 64 bits.

En el primer ejemplo el triángulo desde (1, 2) con k = 3 cubre
4 + 7 + 4 + 1 + 7 + 9 + 7 + 4 + 7 = 50.

## Notas por lenguaje

- Python se ejecuta con PyPy: con CPython 3.12 supera el límite de tiempo
  en el test 101 (3.05 s), mientras que con PyPy 3.10 se acepta en 2.0 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2114_prefix_sums.cpp](2114_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(q n m) | AC | 0.109 s | 3892 KB |
| [2114_prefix_sums.go](2114_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(q n m) | AC | 0.140 s | 14424 KB |
| [2114_prefix_sums.java](2114_prefix_sums.java) | Java 1.8 | prefix_sums | O(q n m) | AC | 0.343 s | 8400 KB |
| [2114_prefix_sums.py](2114_prefix_sums.py) | PyPy 3.10 x64 | prefix_sums | O(q n m) | AC | 2.000 s | 46644 KB |
| [2114_prefix_sums.rs](2114_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(q n m) | AC | 0.125 s | 10584 KB |
