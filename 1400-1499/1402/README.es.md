# 1402. Cócteles

[Timus 1402](https://acm.timus.ru/problem.aspx?space=1&num=1402) · dificultad 130 · combinatorics

Problema original de Sergey Pupyrev, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cóctel mezcla dos o más de N ≤ 21 bebidas, cada una a lo sumo una
vez, y el orden de las bebidas importa. Hay que contar los cócteles
distintos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N (1 ≤ N ≤ 21).

## Salida

El número de cócteles.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
12
```

## Solución

Un cóctel de k bebidas es una elección ordenada de k bebidas distintas,
y hay N·(N − 1)·…·(N − k + 1) de ellas. Se suman para k de 2 a N,
obteniendo cada producto a partir del anterior. `O(N)`.

Detalles a tener en cuenta:

- con una sola bebida no hay ningún cóctel (prueba 02);
- para N = 21 la respuesta es de unos 1,4·10²⁰, más de 64 bits, así que
  las soluciones usan enteros de 128 bits o enteros grandes (prueba 07).

Las pruebas se juzgan por comparación exacta.

## Soluciones optimizadas

`1402_combinatorics_optimized.py`. Conserva el factorial descendente acumulado: ways empieza en N, se multiplica por N-k+1 para k=2..N y se suma a total. Cuenta elecciones ordenadas sin tablas ni recalcular productos. N=1 da cero. Tiempo O(N) aritmética acotada y O(1) enteros con N<=21. Usa la misma recurrencia entera exacta de Python con entrada en bytes, sin cambiar la fórmula combinatoria. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1402_combinatorics.py`: tiempo 0.078 s → 0.125 s; memoria 388 KB → 244 KB.

`1402_combinatorics_optimized.rs`. Conserva el factorial descendente acumulado: ways empieza en N, se multiplica por N-k+1 para k=2..N y se suma a total. Cuenta elecciones ordenadas sin tablas ni recalcular productos. N=1 da cero. Tiempo O(N) aritmética acotada y O(1) enteros con N<=21. Conserva u128: la respuesta para21 bebidas supera64 bits. Un búfer decimal fijo de39 bytes guarda cualquier u128; la cota21*21! queda muy por debajo del máximo. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1402_combinatorics.rs`: tiempo 0.031 s → 0.062 s; memoria 232 KB → 56 KB.

La solución optimizada en C++ suma en el mismo entero de 128 bits, pero
escribe las cifras de atrás hacia delante en un arreglo fijo de
23 caracteres en lugar de insertar cada una al principio de un
`std::string`: como `N ≤ 21`, la respuesta es menor que 21·21! < 10²²,
así que 22 cifras y el cero final siempre caben. Sin `<string>` el
propio programa no reserva memoria dinámica:
{1402_combinatorics_optimized.cpp}.

La solución optimizada en Java lee N byte a byte de `System.in` en lugar
de crear un `Scanner`, cuyas expresiones regulares y datos de
configuración regional cuestan más que las propias multiplicaciones, que
no pasan de veinte; la suma sigue siendo un `BigInteger`:
{1402_combinatorics_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1402_combinatorics_optimized.cpp`: reducción de tiempo +0.00%;
  reducción de memoria +48.94%; base: `1402_combinatorics.cpp`.

- `1402_combinatorics_optimized.java`: reducción de tiempo +0.00%;
  reducción de memoria +73.70%; base: `1402_combinatorics.java`.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1402_combinatorics_optimized.py`: puesto de tiempo 62/71 y de memoria 1/71 en esta muestra comparable.

`1402_combinatorics_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1402_combinatorics.cpp](1402_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N) | AC | 0.015 s | 188 KB | 11286026 |
| [1402_combinatorics.go](1402_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N) | AC | 0.031 s | 1176 KB | 11286027 |
| [1402_combinatorics.java](1402_combinatorics.java) | Java 1.8 | combinatorics | O(N) | AC | 0.109 s | 1688 KB | 11286031 |
| [1402_combinatorics.py](1402_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N) | AC | 0.078 s | 388 KB | 11286029 |
| [1402_combinatorics.rs](1402_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N) | AC | 0.031 s | 232 KB | 11286032 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1402_combinatorics_optimized.cpp](1402_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(N) | AC | 0.001 s | 96 KB | 11304432 |
| [1402_combinatorics_optimized.java](1402_combinatorics_optimized.java) | Java 1.8 | combinatorics | O(N) | AC | 0.109 s | 444 KB | 11304433 |
| [1402_combinatorics_optimized.py](1402_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O(N) | AC | 0.125 s | 244 KB | 11324912 |
| [1402_combinatorics_optimized.rs](1402_combinatorics_optimized.rs) \* | Rust 1.75 x64 | combinatorics | O(N) | AC | 0.062 s | 56 KB | 11325095 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
