# 1783. Carrera nuclear

[Timus 1783](https://acm.timus.ru/problem.aspx?space=1&num=1783) · dificultad 471 · simulation

Problema original de Pavel Atnashev, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un país planea tener exactamente aᵢ cabezas nucleares al final del mes
i. Su rival empieza sin ninguna y, al comienzo del mes i, conociendo
los planes aᵢ, …, aᵢ₊ₘ₋₁, elige el menor cambio entero xᵢ tal que
cambiar sus existencias en xᵢ cada uno de los m meses siguientes las
mantendría al nivel del plan o por encima al final de cada uno. Solo se
hace el cambio de ese mes; al mes siguiente se vuelve a elegir.
Imprimir x₁, …, xₙ.

## Entrada

n y m (1 ≤ n ≤ 10000, 1 ≤ m ≤ 50) y luego a₁, …, aₙ₊ₘ₋₁
(0 ≤ aᵢ ≤ 10⁵).

## Salida

x₁, …, xₙ.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
0 0 4 2 1 0
```

Salida:

```
2 1 1 -1
```

## Solución

Con existencias s al comienzo del mes i, tras t meses del mismo cambio
x las existencias son s + t·x, que debe ser al menos aᵢ₊ₜ₋₁. Así que x es
el mayor de ⌈(aᵢ₊ₜ₋₁ − s)/t⌉ para t = 1…m. Después las existencias crecen
en x y el mes siguiente se repite. El redondeo debe ser hacia arriba
también con números negativos, donde la división entera de muchos
lenguajes redondea hacia cero. `O(n·m)`.

En el ejemplo la primera orden debe llegar a 4 en tres meses: 2. Con 2
en existencias, los planes siguientes 0, 4, 2 piden ⌈2/2⌉ = 1; luego,
con 3, los planes 4, 2, 1 piden 1; y con 4 los planes 2, 1, 0 permiten
−1.

Trampas:

- las órdenes pueden ser negativas cuando los planes bajan;
- ⌈−3/2⌉ es −1, no −2 ni 0, así que la división debe redondear hacia
  arriba de forma explícita;
- cada vez solo se lleva a cabo el primero de los meses planeados.

Las respuestas coinciden con una implementación aceptada independiente
en 60 casos aleatorios, desde unos pocos meses hasta 10000 meses de
planes aleatorios, ondulados y con picos raros.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1783_simulation.cpp](1783_simulation.cpp) | G++ 13.2 x64 | simulation | O(n m) | AC | 0.031 s | 280 KB |
| [1783_simulation.go](1783_simulation.go) | Go 1.14 x64 | simulation | O(n m) | AC | 0.031 s | 1384 KB |
| [1783_simulation.java](1783_simulation.java) | Java 1.8 | simulation | O(n m) | AC | 0.156 s | 2388 KB |
| [1783_simulation.py](1783_simulation.py) | Python 3.12 x64 | simulation | O(n m) | AC | 0.187 s | 2472 KB |
| [1783_simulation.rs](1783_simulation.rs) | Rust 1.75 x64 | simulation | O(n m) | AC | 0.046 s | 840 KB |
