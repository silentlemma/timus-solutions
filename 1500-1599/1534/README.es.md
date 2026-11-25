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
de diferencia. La parte igual cabe en cualquier partido. Así, W victorias
y R derrotas son posibles
exactamente cuando

- W = R = 0 y K = L;
- R = 0, W ≥ 1 y K − L ≥ W (todo L va a la parte igual);
- W = 0, R ≥ 1 y L − K ≥ R;
- W ≥ 1, R ≥ 1, W ≤ K y R ≤ L, con W + R ≤ N en todos los casos.

Queda maximizar y minimizar N + 2W − R en cada caso: con d = K − L, sin
derrotas se obtiene como mucho N + 2·min(d, N) y como poco N + 2 (o N si
d = 0); con d < 0 y sin victorias, como mucho N − 1 y como poco
N − min(−d, N); con victorias y derrotas, como mucho N − 1 + 2·min(K, N − 1) y como poco
N + 2 − min(L, N − 1), lo que requiere K, L ≥ 1 y N ≥ 2. La respuesta es
lo mejor entre los casos posibles. Los valores llegan a 3·10⁹, así que
hacen falta enteros de 64 bits. `O(1)`.

Detalles a tener en cuenta:

- el mínimo puede mezclar victorias y derrotas: en el ejemplo 1 una
  victoria y una derrota dan 3 puntos, menos que una victoria y un
  empate;
- un equipo que marcó y no recibió goles ganó al menos una vez, así que el
  mínimo es N + 2 y no N (pruebas 03, 10);
- 1:1 en un único partido solo puede ser empate (prueba 09);
- 3·10⁹ − 3 no cabe en enteros de 32 bits (prueba 06).

## Soluciones optimizadas

Java lee los tres enteros en un búfer de tamaño fijo y aplica las mismas fórmulas de puntuación. El envío 11318275 tardó 0,109 s y usó 480 KB.

Rust calcula directamente los límites de puntuación y escribe ambos enteros en un búfer fijo. Rust 1.75 x64, envío 11323307. Tiempo 0,031 → 0,046 s, memoria 216 → 48 KB.

Python calcula directamente las puntuaciones mínima y máxima. Si ambos equipos marcaron, también considera reservar un partido para el resultado opuesto. Python 3.12 x64, envío 11320787. Tiempo 0,093 → 0,093 s, memoria 488 → 484 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321851 · Go 1.14 x64 №11322271 · Java 1.8 №11322272 · Python 3.12 x64 №11322274 · Rust 1.75 x64 №11322276.

Go lee los tres enteros en un búfer fijo y escribe ambos totales en una sola llamada. Go 1.14 x64, envío 11322414. Tiempo 0,031 → 0,046 s, memoria 1152 → 796 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1534_math.cpp](1534_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 388 KB | 11321851 |
| [1534_math.go](1534_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1152 KB | 11322271 |
| [1534_math.java](1534_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1656 KB | 11322272 |
| [1534_math.py](1534_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.109 s | 456 KB | 11322274 |
| [1534_math.rs](1534_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 216 KB | 11322276 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1534_math_optimized.java](1534_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 480 KB | 11318275 |
| [1534_math_optimized.rs](1534_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 48 KB | 11323307 |
| [1534_math_optimized.py](1534_math_optimized.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 484 KB | 11320787 |
| [1534_math_optimized.go](1534_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 796 KB | 11322414 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
