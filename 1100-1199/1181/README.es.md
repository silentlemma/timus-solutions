# 1181. Cortar un polígono de tres colores en triángulos tricolores

[Timus 1181](https://acm.timus.ru/problem.aspx?space=1&num=1181) · dificultad 456 · constructive

Problema original de Dmitry Filimonenkov, del Tercer Concurso Individual de Programación de la Universidad Estatal de los Urales, Ekaterimburgo, 16 de febrero de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los vértices de un polígono convexo de `4 ≤ N ≤ 1000` vértices están
pintados de R, G y B; aparecen los tres colores y ningún par de vecinos
comparte color. Hay que cortar el polígono con diagonales que no se
crucen en triángulos que tengan un vértice de cada color, o imprimir 0 si
es imposible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego los colores en orden alrededor del polígono.

## Salida

El número de diagonales y luego las diagonales como pares de números de
vértice.

## Evaluación

Se acepta cualquier corte cuyas `N − 3` diagonales distintas no se crucen
y en el que cada triángulo tenga los tres colores. Un corte así siempre
existe, así que `0` nunca es correcto.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
RBGBRGB
```

Salida:

```
4
1 3
3 7
5 7
5 3
```

## Solución

Si algún color aparece una sola vez, se trazan todas las diagonales desde
ese vértice. Cada triángulo del abanico tiene ese vértice y dos vértices
vecinos del resto, que difieren entre sí y de él.

Si no, cada color aparece al menos dos veces. Hay un vértice cuyos dos
vecinos tienen colores distintos: si todo vértice tuviera vecinos iguales,
los colores se repetirían con periodo dos alrededor del polígono y solo
habría dos colores. Se corta ese vértice con la diagonal entre sus
vecinos; el triángulo tiene tres colores, el resto sigue teniendo los
tres colores (el del vértice quitado aparece en otra parte) y ningún par
de vecinos iguales. Se repite hasta que un color quede solo o quede un
triángulo. Así que la respuesta siempre existe, con `N − 3` diagonales.
`O(N²)` borrando de una lista sin más.

Detalles a tener en cuenta:

- la respuesta nunca es 0, aunque el enunciado lo mencione;
- tras un corte cambian las cuentas de colores, así que un color puede
  quedar solo más tarde, y entonces el abanico termina el trabajo;
- un polígono impar no puede alternar dos colores, otra forma de ver que
  la búsqueda de un vértice con vecinos distintos nunca falla.

Cada corte impreso pasó el comprobador en 200 polígonos aleatorios de
hasta 33 vértices y en todas las pruebas, incluidos polígonos de mil
vértices.

## Soluciones optimizadas

La versión lineal conserva la prueba de las orejas tricolores y el abanico final desde un vértice de color único. Los arreglos left y right forman una lista circular doblemente enlazada, de modo que cada eliminación cuesta O(1). Se actualizan los contadores de colores tras cada corte. La cola empieza con los vértices cuyos vecinos tienen colores distintos; solo los dos vecinos supervivientes pueden cambiar después. Se omiten las entradas obsoletas o eliminadas. Mientras cada color aparece dos veces, existe una oreja válida: de lo contrario, solo alternarían dos colores. Al quedar un color único, se termina con su abanico. Hay como máximo N entradas iniciales y dos nuevas por corte, por lo que tiempo y espacio son O(N). Se conservan los números originales.

El envío aceptado en Python 3.12 x64 tarda 0.093 s frente a 0.203 s de la base y usa 900 KB frente a 760 KB.

## Notas por lenguaje

Las implementaciones originales con listas se conservan como versiones sencillas O(N²). Todas las nuevas usan la cola lineal y vecinos enlazados. C++, Go y Rust dimensionan sus arreglos con N ≤ 1000; bastan 3N entradas de cola. Go y Rust almacenan la salida en 12000 bytes, suficientes para N−3 parejas de índices de cuatro dígitos. Go usa manejadores estándar y Rust E/S acotada del C runtime con entrada C. Python usa deque y Java una cola en un arreglo de enteros. Se acepta cualquier triangulación tricolor válida.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1181_constructive.cpp](1181_constructive.cpp) | G++ 13.2 x64 | constructive | O(N²) | AC | 0.015 s | 408 KB | 11283313 |
| [1181_constructive.go](1181_constructive.go) | Go 1.14 x64 | constructive | O(N²) | AC | 0.031 s | 1188 KB | 11283315 |
| [1181_constructive.java](1181_constructive.java) | Java 1.8 | constructive | O(N²) | AC | 0.218 s | 6632 KB | 11283326 |
| [1181_constructive.py](1181_constructive.py) | Python 3.12 x64 | constructive | O(N²) | AC | 0.203 s | 760 KB | 11283321 |
| [1181_constructive.rs](1181_constructive.rs) | Rust 1.75 x64 | constructive | O(N²) | AC | 0.031 s | 476 KB | 11283329 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1181_constructive_optimized.cpp](1181_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 132 KB | 11314704 |
| [1181_constructive_optimized.go](1181_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 388 KB | 11314727 |
| [1181_constructive_optimized.java](1181_constructive_optimized.java) \* | Java 1.8 | constructive | O(N) | AC | 0.109 s | 552 KB | 11314749 |
| [1181_constructive_optimized.py](1181_constructive_optimized.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.093 s | 900 KB | 11314762 |
| [1181_constructive_optimized.rs](1181_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(N) | AC | 0.015 s | 92 KB | 11314780 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
