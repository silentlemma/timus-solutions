# 2144. Ordenar cajas cerradas en una sola fila ordenada

[Timus 2144](https://acm.timus.ru/problem.aspx?space=1&num=2144) · dificultad 221 · sorting

Problema original de Ivan Smirnov, del Concurso Escolar de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n cajas, cada una con una fila fija de tamaños de figuras que no se
puede reordenar ni invertir. Decidir si las cajas se pueden poner en
algún orden de modo que todos los tamaños juntos formen una fila no
decreciente. Los límites son 0.5 segundos y 256 MB.

## Entrada

n, 1 ≤ n ≤ 100, y luego para cada caja kᵢ, 1 ≤ kᵢ ≤ 100, y sus tamaños,
1 ≤ aᵢⱼ ≤ 10⁴.

## Salida

YES o NO.

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
2 1 2
3 7 7 7
1 5
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
2
2 1 3
1 2
```

Salida:

```
NO
```

## Solución

Cada caja debe ser no decreciente por dentro. Después solo importan su
primer tamaño f y su último tamaño l, y un orden válido necesita que l de
cada caja sea a lo sumo f de la siguiente.

En cualquier orden válido los primeros tamaños no decrecen, porque
f ≤ l ≤ f de la caja siguiente. Entre las cajas con el mismo primer
tamaño f, todas menos la última tienen l ≤ f, es decir, l = f. Por eso
ordenar las cajas por (f, l) da un orden válido siempre que exista, y
basta comprobar los vecinos en ese orden. El trabajo es
O(Σ kᵢ + n log n).

En el primer ejemplo las cajas (1, 2), (5, 5) y (7, 7) encajan en ese
orden; en el segundo (1, 3) y (2, 2) se solapan.

## Soluciones optimizadas

Se leen en flujo los elementos de cada caja y se rechaza una inversión interna inmediatamente. Una caja válida solo necesita sus dos extremos. Empaquetarlos en un entero acotado permite obtener el orden lexicográfico de intervalos mediante ordenación numérica; se recuperan para la misma comprobación de vecinos de la prueba simple. Java evita objetos y comparadores con claves primitivas; Python evita toda la entrada y tuplas temporales.

- `2144_sorting_optimized.java`: 0.109 s / 2064 KB; base `2144_sorting.java`: 0.187 s / 6916 KB; cambio respecto a la base: tiempo -41.7%, memoria -70.2%.
- `2144_sorting_optimized.py`: 0.078 s / 420 KB; base `2144_sorting.py`: 0.093 s / 1040 KB; cambio respecto a la base: tiempo -16.1%, memoria -59.6%.

`2144_sorting_optimized.rs`. Lee cada caja una vez, comprobando tamaños consecutivos y reteniendo solo el primero y último. Ordena in situ los n pares de extremos de forma lexicográfica no estable y verifica cajas vecinas. Frente a la base, no crea un vector de todos los tamaños de cada caja ni conserva la entrada decodificada. La prueba del orden no cambia. Tiempo O(Σk+n log n), espacio O(n). La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `2144_sorting.rs`: tiempo 0.015 s → 0.015 s; memoria 320 KB → 76 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`2144_sorting_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2144_sorting.cpp](2144_sorting.cpp) | G++ 13.2 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 168 KB | 11309245 |
| [2144_sorting.go](2144_sorting.go) | Go 1.14 x64 | sorting | O(sum k + n log n) | AC | 0.031 s | 1328 KB | 11294957 |
| [2144_sorting.java](2144_sorting.java) | Java 1.8 | sorting | O(sum k + n log n) | AC | 0.187 s | 6916 KB | 11309246 |
| [2144_sorting.py](2144_sorting.py) | Python 3.12 x64 | sorting | O(sum k + n log n) | AC | 0.093 s | 1040 KB | 11309247 |
| [2144_sorting.rs](2144_sorting.rs) | Rust 1.75 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 320 KB | 11309248 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2144_sorting_optimized.java](2144_sorting_optimized.java) | Java 1.8 | sorting | O(total sizes+N log N) | AC | 0.109 s | 2064 KB | 11308445 |
| [2144_sorting_optimized.py](2144_sorting_optimized.py) \* | Python 3.12 x64 | sorting | O(total sizes+N log N) | AC | 0.078 s | 420 KB | 11308442 |
| [2144_sorting_optimized.rs](2144_sorting_optimized.rs) \* | Rust 1.75 x64 | sorting | O(Σk+n log n) | AC | 0.015 s | 76 KB | 11325121 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
