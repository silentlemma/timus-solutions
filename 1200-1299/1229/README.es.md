# 1229. Una segunda capa de ladrillos que nunca repite la primera

[Timus 1229](https://acm.timus.ru/problem.aspx?space=1&num=1229) · dificultad 386 · constructive

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un campo de `N × M`, con ambos lados pares y como mucho 100, está
cubierto por una capa de ladrillos de 1 × 2, cada uno marcado con su
número en sus dos casillas. Hay que poner sobre todo el campo una segunda
capa de esos ladrillos de modo que ningún ladrillo de la segunda capa
quede exactamente sobre uno de la primera, o imprimir `-1` si es
imposible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `M`, y luego `N` filas de `M` números: la primera capa.

## Salida

`N` filas de `M` números que describen la segunda capa, o `-1`.

## Evaluación

Sirven muchas segundas capas, así que se acepta cualquiera en la que cada
número marque exactamente dos casillas vecinas y ningún ladrillo ocupe
las mismas dos casillas que un ladrillo de la primera capa.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 4
1 1 2 2
3 3 4 4
```

Salida:

```
2 1 1 4
2 3 3 4
```

## Solución

Se corta el campo en bloques de 2 × 2 y se cubre cada uno con dos
ladrillos, o ambos tumbados (uno en la fila de arriba, otro en la de
abajo) o ambos de pie (uno en cada columna). Un ladrillo tumbado solo
puede repetir la primera capa si un ladrillo de la primera ocupa
exactamente esa fila del bloque. Pero entonces ese ladrillo tiene una
casilla de cada columna del bloque, así que ningún ladrillo de la primera
capa puede ocupar una columna del bloque, y los ladrillos de pie son
seguros. Por tanto: se tumban los ladrillos salvo que la primera capa
tenga un ladrillo en la fila de arriba o de abajo del bloque, y en ese
caso se ponen de pie. Así que siempre existe una segunda capa, y nunca
hace falta `-1`. `O(NM)`.

Detalles a tener en cuenta:

- los ladrillos de la primera capa pueden cruzar los bordes de los
  bloques de 2 × 2; solo se pueden repetir los que quedan enteros dentro
  de un bloque, que es lo que mira la comprobación;
- la numeración de la segunda capa es libre; basta con numerar bloque a
  bloque.

Cada salida se comprobó con el verificador, y las de una solución escrita
aparte también lo pasan, en 100 primeras capas aleatorias obtenidas
girando pares de ladrillos.

## Soluciones optimizadas

Go y Rust leen dos filas a la vez y guardan una bandera de orientación por bloque de 2 × 2. Si alguna fila contiene un ladrillo horizontal de la primera capa, los dos nuevos se colocan verticales. En caso contrario se colocan horizontales. Las dos filas de salida se generan directamente a partir de las banderas y los números de bloque. Go sustituye Scanner, las conversiones de cadenas y el writer por búferes fijos de entrada y salida de 1 KiB y conversión decimal directa. El espacio auxiliar es O(M).

Las implementaciones base aceptadas [1229_constructive.cpp](1229_constructive.cpp), [1229_constructive.java](1229_constructive.java), [1229_constructive.py](1229_constructive.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes recorren los bloques de 2 × 2 en el mismo orden y
  numeran los ladrillos igual.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1229_constructive.cpp](1229_constructive.cpp) | G++ 13.2 x64 | constructive | O(NM) | AC | 0.015 s | 296 KB | 11283741 |
| [1229_constructive.go](1229_constructive.go) | Go 1.14 x64 | constructive | O(NM) | AC | 0.031 s | 1304 KB | 11283742 |
| [1229_constructive.java](1229_constructive.java) | Java 1.8 | constructive | O(NM) | AC | 0.093 s | 960 KB | 11283747 |
| [1229_constructive.py](1229_constructive.py) | Python 3.12 x64 | constructive | O(NM) | AC | 0.062 s | 1384 KB | 11283744 |
| [1229_constructive.rs](1229_constructive.rs) | Rust 1.75 x64 | constructive | O(NM) | AC | 0.015 s | 432 KB | 11283748 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1229_constructive_optimized.go](1229_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(NM) | AC | 0.031 s | 792 KB | 11311210 |
| [1229_constructive_optimized.rs](1229_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(NM) | AC | 0.001 s | 188 KB | 11310586 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
