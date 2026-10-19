# 1828. Aproximación por una progresión

[Timus 1828](https://acm.timus.ru/problem.aspx?space=1&num=1828) · dificultad 478 · math

Problema original de Alexey Samsonov, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados los enteros a₁, …, aₙ, hallar la progresión aritmética b₁, …, bₙ,
no necesariamente entera, que minimiza Σ(aᵢ − bᵢ)².

## Entrada

n (2 ≤ n ≤ 10⁴), luego a₁, …, aₙ, cada uno de valor absoluto no mayor
que 10⁴.

## Salida

El primer término y la diferencia, con error absoluto o relativo de
como mucho 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 6 10 15
```

Salida:

```
0.400 4.900
```

### Ejemplo 2

Entrada:

```
4
-2 -2 -2 -2
```

Salida:

```
-2 0
```

## Solución

Una progresión es bᵢ = b + d·xᵢ con xᵢ = i − 1, así que se trata de la
recta de mínimos cuadrados ajustada a los puntos (xᵢ, aᵢ). Igualar a cero las
derivadas respecto de b y d da las ecuaciones normales, cuya solución
es

d = (n·Σxa − Σx·Σa) / (n·Σx² − (Σx)²),  b = (Σa − d·Σx) / n.

Las cuatro sumas son enteros que caben en 64 bits (n·Σxa queda por
debajo de 10¹⁶). Después C++, Go, Java y Rust usan coma flotante;
Python conserva fracciones exactas hasta la salida. El denominador
vale n²(n² − 1)/12, nunca 0 para n ≥ 2. `O(n)`.

Para el primer ejemplo x̄ = 1.5 y ā = 7.75; Σ(x − x̄)(a − ā) = 24.5 y
Σ(x − x̄)² = 5, así que d = 4.9 y b = 7.75 − 4.9·1.5 = 0.4.

Trampas:

- la progresión se ajusta a las posiciones 0 … n − 1, no solo a los
  valores: la media no basta;
- Σx² ronda 3·10¹¹ y n·Σx² ronda 3·10¹⁵, más allá de 32 bits;
- el primer término es b₁, el valor en la primera posición, no la
  ordenada en otro origen.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1828_math.cpp](1828_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.031 s | 144 KB |
| [1828_math.go](1828_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1256 KB |
| [1828_math.java](1828_math.java) | Java 1.8 | math | O(n) | AC | 0.140 s | 1004 KB |
| [1828_math.py](1828_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 1824 KB |
| [1828_math.rs](1828_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 540 KB |
