# 1207. Una recta por dos puntos que parte en dos el resto

[Timus 1207](https://acm.timus.ru/problem.aspx?space=1&num=1207) · dificultad 117 · geometry

Problema original de Pavel Atnashev, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay un número par `4 ≤ N ≤ 10000` de puntos con coordenadas enteras de
valor absoluto hasta `10⁶`, sin tres en una misma recta. Hay que elegir
dos de modo que la recta que pasa por ellos divida los demás puntos en
dos mitades del mismo tamaño.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` en la primera línea y luego `N` líneas, cada una con las
coordenadas `x y` de un punto.

## Salida

Los números de los dos puntos elegidos.

## Evaluación

Sirven muchos pares, así que se aceptan dos puntos distintos cualesquiera
si su recta deja `(N − 2)/2` puntos a cada lado.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
1 0
0 1
1 1
```

Salida:

```
1 4
```

## Solución

Se toma el punto más bajo, y el de más a la izquierda si dos comparten
la menor altura. Todos los demás están por encima o a su derecha a la
misma altura, dentro de media vuelta, así que se pueden ordenar por el
ángulo a su alrededor usando solo el signo del producto vectorial, sin
coma flotante. En ese orden, todos los puntos antes del `k`-ésimo quedan
a un lado de la recta del punto más bajo al `k`-ésimo, y todos los de
después al otro. Con `N − 1` puntos restantes, el que ocupa el índice
`(N − 2)/2` contando desde cero tiene `(N − 2)/2` antes y después.
`O(N log N)`.

Detalles a tener en cuenta:

- con un pivote arbitrario, los rayos pueden abarcar más de media
  vuelta y romper el orden;
- los productos vectoriales llegan a `4·10¹²`, más de 32 bits;
- un comparador debe devolver «igual» al comparar un elemento consigo
  mismo, o algunas rutinas de ordenación lo rechazan.

Cada respuesta se comprobó contando los puntos de cada lado, y una
solución escrita aparte pasa el mismo verificador en todas las pruebas.

## Soluciones optimizadas

La solución optimizada en Java guarda las coordenadas en arreglos `int`,
ya que no pasan de `10⁶` en valor absoluto, ordena un arreglo de índices
primitivos con un heapsort propio en lugar de ordenar índices `Integer`
empaquetados con una lambda, calcula los productos cruzados en `long` y
analiza la entrada a mano en bloques de 4 KB en lugar de usar
`BufferedReader` y `StringTokenizer`: {1207_geometry_optimized.java}.

La solución optimizada en Python calcula una sola vez una clave entera
para cada punto y ordena por las claves en lugar de llamar `O(N log N)`
veces a un comparador escrito en Python. La clave es `−dx/dy`
multiplicado por `2⁴²` y redondeado hacia abajo, con `dx`, `dy` los
desplazamientos respecto al pivote; `−dx/dy` crece con el ángulo visto
desde el pivote. Los desplazamientos no pasan de `2·10⁶` en valor
absoluto, así que dos fracciones distintas difieren al menos en
`1/(2·10⁶)²`, y `2⁴²` supera `(2·10⁶)²`, de modo que las claves
redondeadas siguen siendo distintas y en el mismo orden; los puntos a la
altura del pivote reciben una clave menor que todas las demás. Las
coordenadas se leen línea a línea en arreglos de enteros de 32 bits:
{1207_geometry_optimized.py}.

La solución optimizada en Rust lee la entrada línea a línea en lugar de
guardar todo el texto y un vector con todos sus números, guarda cada
punto como dos coordenadas `i32` y su número en una estructura, ya que
las coordenadas no pasan de `10⁶` en valor absoluto, desplaza los puntos
una sola vez para que el pivote quede en el origen y los ordena con
`sort_unstable_by` y productos cruzados en `i64`:
{1207_geometry_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1207_geometry_optimized.java`: reducción de tiempo +36.26%; reducción
  de memoria +88.53%; base: `1207_geometry.java`.

- `1207_geometry_optimized.py`: reducción de tiempo +33.57%; reducción
  de memoria +49.37%; base: `1207_geometry.py`.

- `1207_geometry_optimized.rs`: reducción de tiempo -48.39%; reducción
  de memoria +56.39%; base: `1207_geometry.rs`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1207_geometry.cpp](1207_geometry.cpp).

- Python ordena con `functools.cmp_to_key`; Java ordena índices
  envueltos con una lambda que usa `Long.compare`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1207_geometry.cpp](1207_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 296 KB | 11283603 |
| [1207_geometry.go](1207_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.046 s | 1512 KB | 11283604 |
| [1207_geometry.java](1207_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.171 s | 5544 KB | 11283609 |
| [1207_geometry.py](1207_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.140 s | 3516 KB | 11283608 |
| [1207_geometry.rs](1207_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 908 KB | 11283610 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1207_geometry_optimized.java](1207_geometry_optimized.java) | Java 1.8 | geometry | O(N log N) | AC | 0.109 s | 636 KB | 11304352 |
| [1207_geometry_optimized.py](1207_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(N log N) | AC | 0.093 s | 1780 KB | 11304354 |
| [1207_geometry_optimized.rs](1207_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.046 s | 396 KB | 11304353 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
