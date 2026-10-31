# 1628. Rachas blancas

[Timus 1628](https://acm.timus.ru/problem.aspx?space=1&num=1628) · dificultad 164 · implementation

Problema original de Alexander Ipatov, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un calendario es una tabla m × n: la fila i es una semana y la columna j
un día de la semana. Hay k celdas pintadas de negro (los días malos) y el
resto son blancas. Un segmento es un rectángulo de celdas de 1 × l o
l × 1. Hay que contar las rachas blancas: los segmentos blancos maximales
por inclusión.

## Entrada

La primera línea contiene m, n y k (1 ≤ m, n ≤ 30000, 0 ≤ k ≤ 60000).
Cada una de las k líneas siguientes contiene una celda negra x y
(1 ≤ x ≤ m, 1 ≤ y ≤ n); las celdas son distintas.

## Salida

El número de rachas blancas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5 4
1 1
1 5
2 2
3 3
```

Salida:

```
8
```

### Ejemplo 2

Entrada:

```
5 1 2
2 1
3 1
```

Salida:

```
2
```

## Solución

En cada fila las celdas negras la dividen en tramos blancos, y lo mismo
en cada columna. Un tramo de longitud 2 o más es una racha. Una celda
blanca aislada es distinta: es un segmento 1 × 1 en ambas direcciones,
así que se cuenta una sola vez y solo si no puede crecer hacia ningún
lado, es decir, cuando sus vecinas de fila y de columna son todas negras
o quedan fuera de la tabla. Si no, la celda ya está en una racha más
larga.

Así, las filas cuentan sus tramos de longitud al menos 2 más sus celdas
aisladas cerradas arriba y abajo, y las columnas solo sus tramos de
longitud al menos 2. Cada fila y cada columna ordena sus celdas negras,
y un conjunto comprueba las vecinas: ordenado en C++, hash en los demás.
C++: `O(m + n + (m + k) log(k + 1))`; los demás: `O(m + n + k log k)`.

Detalles a tener en cuenta:

- una celda blanca aislada no debe contarse dos veces, una por dirección
  (prueba 05);
- con una sola fila o una sola columna, toda celda blanca queda cerrada
  por el borde en la otra dirección (el segundo ejemplo);
- una tabla toda blanca con m, n > 1 tiene m + n rachas, así que las filas
  y columnas sin celdas negras también cuentan (prueba 06).

Las respuestas coinciden con una implementación aceptada independiente
en 120 calendarios aleatorios y en el más grande.

## Soluciones optimizadas

La solución optimizada en C++ guarda dos arreglos planos de claves en
lugar de un `vector` por fila y por columna y un `set` de pares:
`x · (n + 2) + y` ordena las casillas negras por filas,
`y · (m + 2) + x` por columnas. Tras ordenarlos, una pasada por cada
arreglo recorre todas las filas o todas las columnas, y una casilla
blanca suelta se comprueba arriba y abajo con una búsqueda binaria de
las claves de sus vecinas en el arreglo de filas. Las claves quedan por
debajo de `30000 · 30002 + 30001 < 2³¹`, ya que m, n ≤ 30000, así que
caben en `int`. Los números se analizan a mano desde un búfer de 4 KB
que se rellena con `fread`: {1628_implementation_optimized.cpp}.

La solución optimizada en Go guarda dos slices planos de claves en lugar
de un slice por fila y por columna y un conjunto hash de casillas:
`x · (n + 2) + y` ordena las casillas negras por filas,
`y · (m + 2) + x` por columnas. Tras ordenarlos, una pasada por cada
slice recorre todas las filas o todas las columnas, y una casilla blanca
suelta se comprueba arriba y abajo con una búsqueda binaria de las
claves de sus vecinas en el slice de filas. Los números se analizan a
mano desde un búfer de 4 KB en lugar de `fmt.Fscan`:
{1628_implementation_optimized.go}.

La solución optimizada en Java guarda dos arreglos planos de claves
`int` en lugar de un arreglo por fila y por columna y un `HashSet` de
claves `Long`: `x · (n + 2) + y` ordena las casillas negras por filas,
`y · (m + 2) + x` por columnas. Tras ordenarlos, una pasada por cada
arreglo recorre todas las filas o todas las columnas, y una casilla
blanca suelta se comprueba arriba y abajo con una búsqueda binaria de
las claves de sus vecinas en el arreglo de filas. Las claves quedan por
debajo de `30000 · 30002 + 30001 < 2³¹`, ya que m, n ≤ 30000, así que
caben en `int`. Los números se analizan a mano desde bloques de 4 KB de
la entrada: {1628_implementation_optimized.java}.

La solución optimizada en Python guarda dos listas planas de claves
enteras en lugar de una lista por fila y por columna y un conjunto de
tuplas de coordenadas: `x · (n + 2) + y` ordena las casillas negras por
filas, `y · (m + 2) + x` por columnas. Tras ordenarlas, una pasada por
cada lista recorre todas las filas o todas las columnas, y una casilla
blanca suelta se comprueba arriba y abajo con `bisect_left` sobre las
claves de sus vecinas en la lista de filas. La entrada se lee en trozos
de 4 KB en lugar de toda de golpe: {1628_implementation_optimized.py}.

La solución optimizada en Rust guarda dos vectores planos de claves
`i32` en lugar de un vector por fila y por columna y un conjunto hash de
casillas: `x · (n + 2) + y` ordena las casillas negras por filas,
`y · (m + 2) + x` por columnas. Tras ordenarlos, una pasada por cada
vector recorre todas las filas o todas las columnas, y una casilla
blanca suelta se comprueba arriba y abajo con una búsqueda binaria de
las claves de sus vecinas en el vector de filas. Las claves quedan por
debajo de `30000 · 30002 + 30001 < 2³¹`, ya que m, n ≤ 30000, así que
caben en `i32`. Los números se analizan a mano desde un búfer de 4 KB en
lugar de leer toda la entrada en un `String`:
{1628_implementation_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1628_implementation_optimized.cpp`: reducción de tiempo +86.24%;
  reducción de memoria +90.75%; base: `1628_implementation.cpp`.

- `1628_implementation_optimized.go`: reducción de tiempo +63.20%;
  reducción de memoria +84.94%; base: `1628_implementation.go`.

- `1628_implementation_optimized.java`: reducción de tiempo -14.68%;
  reducción de memoria +86.68%; base: `1628_implementation.java`.

- `1628_implementation_optimized.py`: reducción de tiempo -7.34%;
  reducción de memoria +75.34%; base: `1628_implementation.py`.

- `1628_implementation_optimized.rs`: reducción de tiempo +0.00%;
  reducción de memoria +92.97%; base: `1628_implementation.rs`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1628_implementation.cpp](1628_implementation.cpp) | G++ 13.2 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.109 s | 6528 KB | 11288406 |
| [1628_implementation.go](1628_implementation.go) | Go 1.14 x64 | implementation | O(m + n + k log k) | AC | 0.125 s | 13204 KB | 11288407 |
| [1628_implementation.java](1628_implementation.java) | Java 1.8 | implementation | O(m + n + k log k) | AC | 0.109 s | 10240 KB | 11288409 |
| [1628_implementation.py](1628_implementation.py) | Python 3.12 x64 | implementation | O(m + n + k log k) | AC | 0.218 s | 25760 KB | 11288408 |
| [1628_implementation.rs](1628_implementation.rs) | Rust 1.75 x64 | implementation | O(m + n + k log k) | AC | 0.031 s | 9440 KB | 11304016 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1628_implementation_optimized.cpp](1628_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.015 s | 604 KB | 11307222 |
| [1628_implementation_optimized.go](1628_implementation_optimized.go) | Go 1.14 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.046 s | 1988 KB | 11307224 |
| [1628_implementation_optimized.java](1628_implementation_optimized.java) | Java 1.8 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.125 s | 1364 KB | 11307223 |
| [1628_implementation_optimized.py](1628_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.234 s | 6352 KB | 11307226 |
| [1628_implementation_optimized.rs](1628_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.031 s | 664 KB | 11307225 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
