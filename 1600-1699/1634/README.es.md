# 1634. Ácaro araña

[Timus 1634](https://acm.timus.ru/problem.aspx?space=1&num=1634) · dificultad 2218 · combinatorics

Problema original de Igor Chevdar (preparado por Alexander Ipatov), del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tras cada fumigación, N macetas con árboles se reordenan según una
permutación fija P, y los huevos del ácaro mueren en cuanto todas las
macetas vuelven por primera vez a su lugar original. Con P elegida
uniformemente entre todas las permutaciones de N elementos, hay que
hallar el número esperado de fumigaciones e imprimir su parte entera.

## Entrada

Un entero N (1 ≤ N ≤ 50).

## Salida

La parte entera del número esperado de fumigaciones.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
1
```

## Solución

El número de fumigaciones es el orden de P: el mínimo común múltiplo de
las longitudes de sus ciclos. Un tipo de ciclos con m_k ciclos de longitud
k para cada k tiene probabilidad 1 / Π k^(m_k) m_k! al elegir
uniformemente una permutación (el conteo clásico de permutaciones de un
tipo de ciclos dado), así que la esperanza es una suma sobre tipos de ciclos.

Para N = 50 hay 204226 tipos de ciclos, pero muchos comparten el mismo
mcm. Una mochila sobre las longitudes de ciclo los agrupa: dp[s][l] es la
probabilidad de que una permutación aleatoria de s elementos use solo
las longitudes 1…k ya vistas y de que su mcm sea l. Añadir m ≥ 1 ciclos de
longitud k lleva el peso de dp[s][l] a dp[s + mk][mcm(l, k)],
multiplicado por 1 / (k^m m!), dividiendo el peso entre k · m en cada paso.
Para N = 50 solo hay unos mil valores distintos de mcm por tamaño (la
función de Landau los acota por 180180). La respuesta es
Σ l · dp[N][l]. L es el máximo número de estados por tamaño.

Bastan los double: en las 50 entradas, las esperanzas exactas (calculadas
aparte con fracciones) nunca quedan a menos de 0,005 del entero de
arriba, salvo N = 1, donde vale exactamente 1, y un empujón de 10⁻⁹ la
mantiene entera. La esperanza crece despacio: 1069,51 para N = 50.

Detalles a tener en cuenta:

- el orden es el mcm de las longitudes de ciclo, no su producto ni su
  suma;
- enumerar todas las particiones con números grandes exactos es correcto
  pero lento en algunos lenguajes; agrupar por mcm reduce mucho el
  trabajo;
- un entero exacto debe sobrevivir al truncado: una suma que saliera
  0,9999999… imprimiría 0 para N = 1 (prueba 02).

Las respuestas coinciden con los valores racionales exactos en las 50
entradas, y también con una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1634_combinatorics.cpp](1634_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N² log N · L log L) | AC | 0.046 s | 1520 KB |
| [1634_combinatorics.go](1634_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N² log N · L) | AC | 0.109 s | 6216 KB |
| [1634_combinatorics.java](1634_combinatorics.java) | Java 1.8 | combinatorics | O(N² log N · L) | AC | 0.203 s | 8348 KB |
| [1634_combinatorics.py](1634_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N² log N · L) | AC | 0.203 s | 2728 KB |
| [1634_combinatorics.rs](1634_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N² log N · L) | AC | 0.046 s | 1736 KB |
