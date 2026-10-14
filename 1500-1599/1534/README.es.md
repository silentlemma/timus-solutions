# 1534. Fútbol en Gondor

[Timus 1534](https://acm.timus.ru/problem.aspx?space=1&num=1534) · dificultad 585 · math

Problema original de Sergey Pupyrev, del Octavo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 3 de marzo de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un equipo jugó N partidos, marcó K goles y recibió L en total
(0 ≤ K, L ≤ 10⁹, 1 ≤ N ≤ 10⁹). Una victoria da 3 puntos, un empate 1 y
una derrota 0. Hay que hallar el mayor y el menor número de puntos que
pudo tener el equipo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

K, L y N en una línea.

## Salida

El mayor y el menor número de puntos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2 2
```

Salida:

```
4 3
```

### Ejemplo 2

Entrada:

```
3 1 2
```

Salida:

```
6 3
```

### Ejemplo 3

Entrada:

```
3 0 4
```

Salida:

```
10 6
```

### Ejemplo 4

Entrada:

```
3 0 1
```

Salida:

```
3 3
```

## Solución

Con W victorias y R derrotas el equipo tiene 3W + (N − W − R) =
N + 2W − R puntos. Los goles de cada partido se separan en una parte
igual para ambos lados y la diferencia: las partes iguales suman algún
X ≥ 0 en ambos lados, las diferencias de las victorias K − X y las de
las derrotas L − X, y cada victoria o derrota necesita al menos un gol
de diferencia. Cualquier X sirve, porque la parte igual cabe en
cualquier partido. Así, W victorias y R derrotas son posibles
exactamente cuando

- W = R = 0 y K = L;
- R = 0, W ≥ 1 y K − L ≥ W (todo L va a la parte igual);
- W = 0, R ≥ 1 y L − K ≥ R;
- W ≥ 1, R ≥ 1, W ≤ K y R ≤ L, con W + R ≤ N en todos los casos.

Queda maximizar y minimizar N + 2W − R en cada caso: con d = K − L, sin
derrotas se obtiene como mucho N + 2·min(d, N) y como poco N + 2 (o N si
d = 0); sin victorias, como mucho N − 1 y como poco N − min(−d, N); con
victorias y derrotas, como mucho N − 1 + 2·min(K, N − 1) y como poco
N + 2 − min(L, N − 1), lo que requiere K, L ≥ 1 y N ≥ 2. La respuesta es
lo mejor entre los casos posibles. Los valores llegan a 3·10⁹, así que
hacen falta enteros de 64 bits. `O(1)`.

Detalles a tener en cuenta:

- el mínimo puede mezclar victorias y derrotas: en el ejemplo 1 una
  victoria y una derrota dan 3 puntos, menos que una victoria y un
  empate;
- un equipo que no recibió goles ganó al menos una vez, así que el
  mínimo es N + 2 y no N (pruebas 03, 10);
- 1:1 en un único partido solo puede ser empate (prueba 09);
- 3·10⁹ − 3 no cabe en enteros de 32 bits (prueba 06).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1534_math.cpp](1534_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 404 KB |
| [1534_math.go](1534_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1084 KB |
| [1534_math.java](1534_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1680 KB |
| [1534_math.py](1534_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 488 KB |
| [1534_math.rs](1534_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 228 KB |
