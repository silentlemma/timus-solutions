# 1855. Gremios comerciales de Erathia

[Timus 1855](https://acm.timus.ru/problem.aspx?space=1&num=1855) · dificultad 1263 · fenwick

Problema original de Alexander Fetisov (preparado por Denis Dublennykh), del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n ciudades están a lo largo de un camino comercial, y cada tramo entre
ciudades vecinas tiene un peaje, al principio 0. Los sucesos llegan en
orden: un cambio suma d al peaje de cada tramo entre las ciudades a y
b, y un gremio nuevo trabaja en las ciudades a … b, con caravanas que
van con la misma frecuencia entre cada par de esas ciudades. Para cada
gremio nuevo imprimir el peaje medio que paga en ese momento una de sus
caravanas.

## Entrada

n y m (2 ≤ n ≤ 10⁵, 1 ≤ m ≤ 10⁵), luego m sucesos "change a b d" o
"establish a b" con 1 ≤ a < b ≤ n y |d| ≤ 10 000. Todo peaje se queda
entre 0 y 10 000.

## Salida

La media de cada gremio nuevo, con error absoluto o relativo de como
mucho 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 5
change 1 4 2
change 1 2 -1
establish 1 2
establish 2 4
establish 1 4
```

Salida:

```
1.00000000
2.66666667
2.83333333
```

## Solución

Sea tᵢ el peaje del tramo de la ciudad i a la i + 1. Un gremio en las
ciudades a … b tiene (b − a + 1)(b − a)/2 rutas, y el tramo i está en
(i − a + 1)(b − i) de ellas, las que empiezan en i o antes y terminan
después. Desarrollando el producto, el peaje total es
−S₂ + (a + b − 1)·S₁ + b(1 − a)·S₀ con S_k = Σ iᵏ·tᵢ para
i = a … b − 1, así que bastan sumas en rango de tᵢ, i·tᵢ e i²·tᵢ con
incrementos en rango.

Los peajes se guardan como sumas prefijas de diferencias dif_j: un
cambio suma d en a y −d en b. Entonces la suma de iᵏ·tᵢ para i ≤ x es
P_k(x)·Σ dif_j − Σ dif_j·P_k(j − 1) para j ≤ x, donde P_k(x) es la suma
de iᵏ para i = 1 … x, precalculada. Cuatro árboles de Fenwick sobre las
diferencias, uno simple y los ponderados por P₀, P₁ y P₂, atienden cada
suceso en `O(log n)`.

En el ejemplo los peajes acaban siendo 1, 2 y 2. El gremio en las
ciudades 1 … 4 tiene seis rutas que pagan 1, 3, 5, 2, 4 y 2, es decir
17/6 ≈ 2,8333.

Trampas:

- los enteros de Python son exactos, y las otras soluciones calculan
  módulo 2⁶⁴, lo que es exacto para el total final porque queda por
  debajo de 2,5·10¹⁸;
- el total de un gremio no necesita ninguna división hasta el final;
- la solución en Python corre en PyPy.

Las medias coinciden con un cálculo directo en doscientos casos
pequeños y con una implementación aceptada independiente en las pruebas
grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1855_fenwick.cpp](1855_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n + m log n) | AC | 0.375 s | 4484 KB |
| [1855_fenwick.go](1855_fenwick.go) | Go 1.14 x64 | fenwick | O(n + m log n) | AC | 0.109 s | 8196 KB |
| [1855_fenwick.java](1855_fenwick.java) | Java 1.8 | fenwick | O(n + m log n) | AC | 0.421 s | 15736 KB |
| [1855_fenwick.py](1855_fenwick.py) | PyPy 3.10 x64 | fenwick | O(n + m log n) | AC | 0.406 s | 37656 KB |
| [1855_fenwick.rs](1855_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n + m log n) | AC | 0.046 s | 11256 KB |
