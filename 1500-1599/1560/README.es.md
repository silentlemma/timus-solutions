# 1560. Funciones simétricas elementales

[Timus 1560](https://acm.timus.ru/problem.aspx?space=1&num=1560) · dificultad 933 · fenwick

Problema original del Novosibirsk SU Contest en el campus de Petrozavodsk, septiembre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arreglo de N ≤ 80000 enteros recibe M ≤ 100000 consultas de dos
tipos: `I i d` suma d a A[i], y `C l r K` (1 ≤ K ≤ 4) pide los
polinomios simétricos elementales S(0), …, S(K) de A[l..r], donde S(j)
es la suma de los productos de todos los subconjuntos de j elementos.
Las respuestas se toman módulo un primo 1000 ≤ P ≤ 10⁹. Los valores y
los cambios son como mucho 10⁵ en valor absoluto.

Límite de tiempo: 4 segundos. Límite de memoria: 64 MB.

## Entrada

N, M y P, luego el arreglo y luego las consultas.

## Salida

Para cada consulta `C`, S(0) … S(K) como restos módulo P en una línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 6 1237
0 0 1 1 1 1 1
C 3 3 1
C 1 6 4
I 1 -1235
C 1 7 3
I 4 1
C 2 5 4
```

Salida:

```
1 1
1 4 6 4 1
1 7 20 30
1 4 5 2 0
```

## Solución

Las sumas de potencias p(j) = Σ a^j de un intervalo son fáciles de
mantener: cuatro árboles de Fenwick las guardan para j = 1…4, una
actualización cambia cada una en new^j − old^j, y una consulta toma la
diferencia de dos sumas prefijas. Los polinomios elementales salen de
las identidades de Newton,
k·S(k) = S(k−1)·p(1) − S(k−2)·p(2) + S(k−3)·p(3) − …, con S(0) = 1. P
es un primo mayor que 4, así que dividir entre k ≤ 4 es multiplicar por
su inverso módulo P.

Los nodos de los árboles guardan sus sumas sin reducir: cada una empieza
como una suma de como mucho N restos y cada actualización suma una
diferencia de dos restos, así que quedan por debajo de unos 2·10¹⁴ y
caben en 64 bits; solo se reducen cuando una consulta las lee. Cada
consulta tarda O(K log N), O((N + M) log N) en total. Los resultados se
contrastaron con un producto directo sobre el intervalo en pruebas
pequeñas aleatorias.

Detalles a tener en cuenta:

- los valores y los cambios pueden ser negativos, mientras que las
  respuestas deben ser restos de 0 a P − 1 (pruebas 03, 04);
- la cuarta potencia de un valor cercano a 10⁹ desborda 64 bits si no
  se reduce cada multiplicación (prueba 05);
- P puede ser menor que los valores, así que primero se reducen los
  valores (prueba 06).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1560_fenwick.cpp](1560_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((N + M) log N) | AC | 0.406 s | 4136 KB |
| [1560_fenwick.go](1560_fenwick.go) | Go 1.14 x64 | fenwick | O((N + M) log N) | AC | 0.156 s | 9028 KB |
| [1560_fenwick.java](1560_fenwick.java) | Java 1.8 | fenwick | O((N + M) log N) | AC | 0.250 s | 15908 KB |
| [1560_fenwick.py](1560_fenwick.py) | Python 3.12 x64 | fenwick | O((N + M) log N) | AC | 2.156 s | 48580 KB |
| [1560_fenwick.rs](1560_fenwick.rs) | Rust 1.75 x64 | fenwick | O((N + M) log N) | AC | 0.109 s | 10612 KB |
