# 1112. Conservar el mayor número de segmentos sin puntos interiores comunes

[Timus 1112](https://acm.timus.ru/problem.aspx?space=1&num=1112) · dificultad 165 · greedy

Problema original de la Olimpiada Nacional Búlgara de Informática, segundo día.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` segmentos en una recta (`1 ≤ N ≤ 99`), el segmento `i` va de
`A_i` a `B_i` con enteros `−999 ≤ A_i < B_i ≤ 999`. Quita los menos
segmentos posibles para que ningún par de los que quedan comparta un punto
interior; los extremos pueden tocarse. Imprime los segmentos que quedan.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas `A_i B_i`.

## Salida

El número `P` de segmentos conservados y luego `P` líneas `A B` en orden
creciente de los extremos izquierdos. Se acepta cualquier respuesta
óptima.

## Evaluación

Se acepta cualquier respuesta óptima. El comprobador calcula el mayor
número posible de segmentos con una programación dinámica cuadrática y
verifica que la salida conserva esa cantidad, los toma de la entrada, los
lista por su extremo izquierdo y no tiene dos que se solapen.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
3 6
1 3
2 5
```

Salida:

```
2
1 3
3 6
```

## Solución

Es el problema de selección de actividades. Se ordenan los segmentos por
su extremo derecho y se toma cada uno que empiece no antes del extremo
derecho del último tomado. El segmento que termina primero siempre forma
parte de alguna respuesta óptima: en cualquier conjunto óptimo, el
segmento con el extremo derecho más a la izquierda puede cambiarse por él
sin crear un solape. Repetir el argumento con el resto demuestra la
elección voraz. Los segmentos conservados son disjuntos, así que su orden
por extremo derecho es también su orden por extremo izquierdo.
`O(N log N)`.

Detalles a tener en cuenta:

- los segmentos que se tocan (uno termina donde empieza el siguiente) no
  comparten puntos interiores y pueden quedarse ambos;
- ordenar por extremo izquierdo o por longitud y elegir de forma voraz da
  respuestas erróneas: un segmento largo que empieza primero puede tapar
  varios cortos;
- los segmentos pueden repetirse; cada copia es un segmento aparte, pero
  como mucho una puede quedarse.

Las respuestas se comprobaron con el comprobador en todas las pruebas y en
150 conjuntos aleatorios, con cadenas de segmentos que se tocan,
segmentos repetidos y anidados.

## Soluciones optimizadas

`1112_greedy_optimized.py`. Conserva selección por fin más temprano y extremos tocándose. Ordena tuplas(fin,inicio) directamente, sin lista de entrada y función key. Compacta elegidos al prefijo sin otra lista ni salida unida. O(n log n) tiempo,O(n) espacio; empates permiten otro óptimo válido comprobado por checker constructivo. Vacía antes de salir PyPy.

Frente a `1112_greedy.py`: tiempo 0.078 s → 0.125 s; memoria 460 KB → 272 KB.

La solución optimizada en C++ guarda los segmentos en un único arreglo
global de 99 pares, ya que `N ≤ 99`, en lugar de dos `vector`, y escribe
los segmentos conservados al principio del mismo arreglo: un segmento
conservado solo ocupa el lugar de uno ya recorrido. No se reserva
memoria dinámica: {1112_greedy_optimized.cpp}.

La solución optimizada en Java lee la entrada en bloques de 4 KB y
analiza a mano los números con signo en lugar de usar `Scanner`, guarda
los extremos en dos arreglos de `int` en lugar de un arreglo por
segmento y los ordena por inserción, lo que con `N ≤ 99` es barato y no
necesita comparador; los segmentos conservados se escriben al principio
de los mismos arreglos: {1112_greedy_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1112_greedy_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +41.67%; base: `1112_greedy.cpp`.

- `1112_greedy_optimized.java`: reducción de tiempo +40.38%; reducción
  de memoria +89.45%; base: `1112_greedy.java`.

`1112_greedy_optimized.rs`. Mantiene la selección voraz por fin más temprano, admitiendo extremos que se tocan. Ordena el único vector con sort_unstable_by_key y compacta los segmentos elegidos en el prefijo ya recorrido. No necesita otro vector de elegidos ni un constructor de salida. Los finales iguales pueden reordenarse: se acepta cualquier conjunto válido óptimo. Tiempo O(N log N), espacio O(N). La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1112_greedy.rs`: tiempo 0.015 s → 0.031 s; memoria 232 KB → 64 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1112_greedy_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328499 (Go 1.14 x64): **0.015 s / 1000 KB**. Comparación archivada: `1112_greedy.go` (Go 1.14 x64) — 0.015 s / 1156 KB (#11279213).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1112_greedy_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1112_greedy.cpp](1112_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 192 KB | 11279212 |
| [1112_greedy.go](1112_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.015 s | 1156 KB | 11279213 |
| [1112_greedy.java](1112_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.156 s | 3944 KB | 11279215 |
| [1112_greedy.py](1112_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 460 KB | 11279214 |
| [1112_greedy.rs](1112_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 232 KB | 11279216 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1112_greedy_optimized.cpp](1112_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 112 KB | 11307228 |
| [1112_greedy_optimized.java](1112_greedy_optimized.java) | Java 1.8 | greedy | O(N²) | AC | 0.093 s | 416 KB | 11307227 |
| [1112_greedy_optimized.rs](1112_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.031 s | 64 KB | 11325084 |
| [1112_greedy_optimized.py](1112_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(n log n) time; O(n) space | AC | 0.125 s | 272 KB | 11325703 |
| [1112_greedy_optimized.go](1112_greedy_optimized.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.015 s | 1000 KB | 11328499 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
