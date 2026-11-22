# 1740. ¡Mejor los renos!

[Timus 1740](https://acm.timus.ru/problem.aspx?space=1&num=1740) · dificultad 138 · math

Problema original de Sergey Pupyrev (preparado por Daniil Ayzenshteyn), del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El camino al colegio electoral mide l km. Los renos pueden correr como
quieran, siempre que cada tramo de k km tarde exactamente h horas.
Hallar el menor y el mayor tiempo posible para todo el camino.

## Entrada

Los enteros l, k y h (1 ≤ k ≤ l ≤ 1000, 1 ≤ h ≤ 1000).

## Salida

El menor y el mayor tiempo, con un error de a lo sumo 10⁻⁵.

## Evaluación

Las pruebas del repositorio comparan tokens numéricos con |resultado-referencia| <= 1e-5·max(1,|referencia|), rechazan valores no finitos y comparan exactamente los tokens no numéricos.

## Ejemplos

### Ejemplo 1

Entrada:

```
30 10 1
```

Salida:

```
3.00000000 3.00000000
```

## Solución

Sea t(x) el tiempo para llegar al kilómetro x. Cada tramo de k km tarda
h horas, así que t(x + k) = t(x) + h: t crece h cada k km más una parte
que se repite cada k km. Con l = nk + r, el camino entero tarda
nh + t(r), y t(r) está entre t(0) = 0 y t(k) = h. Los renos pueden
gastar casi nada en los primeros r km de cada tramo, o casi todo, así
que las respuestas son nh y, si r > 0, (n + 1)h. `O(1)`.

En el ejemplo 30 km son tres tramos de 10 km, 3 horas en cualquier caso.

Trampas:

- cuando k divide a l las dos respuestas coinciden;
- los tiempos son enteros; el código los imprime con ocho decimales.

## Soluciones optimizadas

`1740_math_optimized.java`. Conserva l=qk+r y los límites enteros exactos qh y (q+[r>0])h. Un búfer de 1024 bytes sustituye StreamTokenizer y decodificación. La salida añade ocho ceros decimales literales sin convertir a flotante, preservando los valores. Aritmética y espacio auxiliar O(1); mantiene la base.

Accepted de fuente exacto Java 1.8 #11326958: 0.093 s / 368 KB. Comparación guardada de Java actual, 2026-11-20: tiempo 4/90, memoria 1/90. Al usar menos de 1024 KB, la admisión estricta usa solo tiempo.

- `1740_math_optimized.java`: 0.093 s / 368 KB; base didáctica conservada `1740_math.java`: 0.14 s / 1792 KB; cambio de tiempo -33.6%; cambio de memoria -79.5%.

La solución optimizada en C++ lee los tres números con `scanf` en lugar
de `std::cin`, así que el programa no lleva la maquinaria de `iostream`;
el cálculo y la salida son los mismos: {1740_math_optimized.cpp}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1740_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +72.28%; base: `1740_math.cpp`.

`1740_math_optimized.py`. Conserva l=q*k+r. El mínimo es q*h y el máximo (q+[r!=0])*h. Ambos son enteros: emite tokens enteros en vez de convertir a flotantes y dar ocho decimales. La comprobación numérica acepta esos valores equivalentes. Los productos no superan 10^6; tiempo y estado O(1). Reutiliza divmod para cociente y resto y evita el formato decimal. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1740_math.py`: tiempo 0.078 s → 0.125 s; memoria 404 KB → 188 KB.

`1740_math_optimized.rs`. Conserva l=q*k+r. El mínimo es q*h y el máximo (q+[r!=0])*h. Ambos son enteros: emite tokens enteros en vez de convertir a flotantes y dar ocho decimales. La comprobación numérica acepta esos valores equivalentes. Los productos no superan 10^6; tiempo y estado O(1). Usa cociente y resto i64 y escritura manual de enteros en vez de f64 y formato flotante de Rust. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1740_math.rs`: tiempo 0.046 s → 0.015 s; memoria 252 KB → 48 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1740_math_optimized.py`: puesto de tiempo 22/29 y de memoria 1/29 en esta muestra comparable.

`1740_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1740_math.cpp](1740_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 404 KB | 11289483 |
| [1740_math.go](1740_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1092 KB | 11289484 |
| [1740_math.java](1740_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1792 KB | 11304069 |
| [1740_math.py](1740_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 404 KB | 11289486 |
| [1740_math.rs](1740_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 252 KB | 11304070 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1740_math_optimized.cpp](1740_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 112 KB | 11304455 |
| [1740_math_optimized.java](1740_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.093 s | 368 KB | 11326958 |
| [1740_math_optimized.py](1740_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 188 KB | 11324913 |
| [1740_math_optimized.rs](1740_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 48 KB | 11325145 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
