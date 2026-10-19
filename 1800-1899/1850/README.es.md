# 1850. Turismo espacial

[Timus 1850](https://acm.timus.ru/problem.aspx?space=1&num=1850) · dificultad 2662 · fenwick

Problema original de Dmitry Ivankov, del Ural SU Contest en la sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n planetas están en un mismo rayo que sale de una estrella, cada uno a
su propia distancia y habitado por alguna raza. La nave de un turista
vuela como mucho d sin repostar, puede repostar en cualquier planeta y
solo funciona a distancias de la estrella dentro del rango del turista
[low, high]; al turista se le lleva a cualquier planeta de ese rango.
Para cada turista hallar el mayor número de razas distintas que puede
conocer.

## Entrada

n, s y d (1 ≤ n, s, d ≤ 10⁵), luego los n planetas con su distancia
(distintas, hasta 10⁶) y su raza (de 1 a s); luego m (1 ≤ m ≤ 10⁵) y
los rangos de los turistas, con extremos hasta 10⁶.

## Salida

La respuesta de cada turista, una por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 5 11
10 1
50 2
30 1
20 1
60 3
2
5 65
15 45
```

Salida:

```
2
1
```

## Solución

Se ordenan los planetas por distancia. Dentro de un rango, el turista
puede pasar de un planeta al siguiente exactamente cuando distan como
mucho d, así que los planetas del rango forman tramos, y la respuesta
es el mayor número de razas de un tramo. Los tramos son los trozos
globales de planetas partidos en los huecos mayores que d y recortados
por el rango: un rango que toca los trozos P₁ … Pₖ consta de una cola de
P₁, los trozos enteros P₂ … Pₖ₋₁ y una cabeza de Pₖ.

Así que se precalcula, dentro de cada trozo, el número de razas desde
su inicio hasta cada planeta (cabeza) y desde cada planeta hasta su fin
(cola), y el número de razas de cada trozo entero, con una tabla
dispersa para el mayor sobre un rango de trozos. Un rango que abarca
varios trozos se responde con dos consultas directas y una a la tabla.

Un rango dentro de un solo trozo necesita el número de razas distintas
entre planetas consecutivos. Esas consultas se responden fuera de línea,
ordenadas por su extremo derecho: avanzando a la derecha se mantiene un
árbol de Fenwick donde cada raza cuenta solo en su último planeta hasta
el momento; las razas de [l, r] son la suma en las posiciones l … r.
`O((n + m) log n)`.

En el ejemplo los planetas 10, 20 y 30 forman un trozo de la raza 1 y
los planetas 50 y 60 otro, de las razas 2 y 3, porque 50 − 30 > 11. El
primer turista ve ambos trozos y conoce como mucho dos razas; el
segundo solo ve 20 y 30.

Trampas:

- la nave no puede salir del rango ni siquiera para llegar a otro
  planeta del rango;
- un rango puede no contener ningún planeta;
- una misma raza puede vivir en varios planetas de un trozo.

Las respuestas coinciden con un conteo directo en trescientos casos
pequeños y con una implementación aceptada independiente en las pruebas
grandes. La solución en Python corre en PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1850_fenwick.cpp](1850_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((n + m) log n) | AC | 0.328 s | 9700 KB |
| [1850_fenwick.go](1850_fenwick.go) | Go 1.14 x64 | fenwick | O((n + m) log n) | AC | 0.171 s | 21420 KB |
| [1850_fenwick.java](1850_fenwick.java) | Java 1.8 | fenwick | O((n + m) log n) | AC | 0.171 s | 12204 KB |
| [1850_fenwick.py](1850_fenwick.py) | PyPy 3.10 x64 | fenwick | O((n + m) log n) | AC | 0.953 s | 54928 KB |
| [1850_fenwick.rs](1850_fenwick.rs) | Rust 1.75 x64 | fenwick | O((n + m) log n) | AC | 0.078 s | 27020 KB |
