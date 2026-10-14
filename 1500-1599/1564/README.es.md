# 1564. Contando unos

[Timus 1564](https://acm.timus.ru/problem.aspx?space=1&num=1564) · dificultad 681 · binary_search

Problema original de Sergey Pupyrev, del XII Campeonato de Programación de la Universidad Estatal de los Urales, 6 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Petya sube por las escaleras de un rascacielos desde el piso 1 y cuenta
los dígitos 1 de los números de piso por el camino. Dada la cuenta k
(1 ≤ k ≤ 10¹⁸), hay que imprimir el piso donde se contó el último de
esos unos, o `Petr lies` si ningún piso da exactamente k unos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número k.

## Salida

El número del piso o `Petr lies`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
11
```

### Ejemplo 2

Entrada:

```
3
```

Salida:

```
Petr lies
```

## Solución

Sea f(x) el número de unos en 1, …, x. Se cuenta posición a posición: en
la posición p (1, 10, 100, …) los números hasta x forman ⌊x / 10p⌋
bloques completos de 10p números con p unos ahí cada uno, y el último
bloque, incompleto, añade p unos si su dígito en esa posición es mayor
que 1, el resto de x por debajo de la posición más 1 si el dígito es 1,
y nada si es 0.

f solo crece, así que el piso donde se contó el k-ésimo uno es el primer
x con f(x) ≥ k, que se halla con búsqueda binaria en 1 … 10¹⁸
(f(10¹⁸) ronda 1.8·10¹⁸). Si f(x) es mayor que k, el piso x trajo varios
unos a la vez y la cuenta k nunca apareció, así que Petya miente. La
búsqueda da unos 60 pasos de O(log x) cada uno. Los resultados se
contrastaron con recorrer los pisos uno a uno para todas las cuentas
hasta 25000.

Detalles a tener en cuenta:

- un piso como el 11 añade dos unos a la vez, así que algunas cuentas
  nunca aparecen (el segundo ejemplo);
- la respuesta para k = 10¹⁸ ronda 5.2·10¹⁷, y las posiciones llegan a
  10¹⁸, así que p · 10 no debe calcularse más allá de 64 bits
  (prueba 05);
- una cuenta uno menor que el total en un piso lleno de unos es mentira
  (prueba 08).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1564_binary_search.cpp](1564_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(log^2 k) | AC | 0.015 s | 128 KB |
| [1564_binary_search.go](1564_binary_search.go) | Go 1.14 x64 | binary_search | O(log^2 k) | AC | 0.031 s | 1072 KB |
| [1564_binary_search.java](1564_binary_search.java) | Java 1.8 | binary_search | O(log^2 k) | AC | 0.125 s | 1608 KB |
| [1564_binary_search.py](1564_binary_search.py) | Python 3.12 x64 | binary_search | O(log^2 k) | AC | 0.078 s | 424 KB |
| [1564_binary_search.rs](1564_binary_search.rs) | Rust 1.75 x64 | binary_search | O(log^2 k) | AC | 0.015 s | 220 KB |
