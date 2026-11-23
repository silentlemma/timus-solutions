# 1731. Eneldo

[Timus 1731](https://acm.timus.ru/problem.aspx?space=1&num=1731) · dificultad 106 · constructive

Problema original de Eugene Kurpilyansky (preparado por Sofia Tekhazheva), del Concurso Regional de Programación por Equipos de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elegir las masas de n cajas de eneldo de la primera clase y m cajas de
la segunda, todas enteros positivos distintos hasta 10⁹, de modo que no
haya forma de regalar a dos vecinos una caja de cada clase con pesos
totales iguales.

## Entrada

n y m (2 ≤ n, m ≤ 50).

## Salida

Las n masas de la primera clase en una línea y las m de la segunda en
la siguiente. Se acepta cualquier elección válida.

## Evaluación

El repositorio usa un comprobador semántico y acepta cualquier salida que satisfaga estas condiciones. El comprobador del repositorio exige dos líneas con n y m masas enteras. Las n+m masas deben ser distintas y estar en [1,10^9], y las n*m sumas cruzadas ser distintas. Siempre existe una construcción; no se acepta un mensaje de imposibilidad.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
```

Salida:

```
1 2
5 10 12
```

## Solución

Dos regalos a + b y a′ + b′ no comparten cajas, y dos sumas con una
caja en común ya difieren porque todas las masas son distintas. Así
que la condición es que las n·m sumas a_i + b_j sean todas distintas.

Se toma a_i = i para i = 1..n y b_j = (j + 1)·n + 1 para
j = 0..m − 1. Entonces a_i + b_j = (j + 1)·n + 1 + i, y como i recorre
1..n, la suma determina tanto i como j, igual que un número en base n
determina su última cifra y el resto. Todas las masas son distintas y
la mayor es menor que 3000. `O(n + m)`.

Para el ejemplo salen 1 2 y 3 5 7, con sumas 4, 6, 8, 5, 7, 9.

Trampas:

- la respuesta siempre existe, así que nunca se imprime
  "It is a lie!";
- la segunda clase no debe repetir masas de la primera, por eso empieza
  por encima de n.

El comprobador verifica las cantidades, el rango, que las masas sean
distintas y que todas las sumas difieran.

## Soluciones optimizadas

La solución optimizada en C++ lee n y m con `scanf` en lugar de
`std::cin`, así que el programa no incluye `iostream` en absoluto; las
masas se imprimen igual: {1731_constructive_optimized.cpp}.

La solución optimizada en Java lee n y m cifra a cifra directamente
desde `System.in` en lugar de crear un `Scanner`, cuya preparación
cuesta más que el resto del programa; la salida se construye igual:
{1731_constructive_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1731_constructive_optimized.cpp`: reducción de tiempo +0.00%;
  reducción de memoria +67.02%; base: `1731_constructive.cpp`.

- `1731_constructive_optimized.java`: reducción de tiempo +45.61%;
  reducción de memoria +76.20%; base: `1731_constructive.java`.

`1731_constructive_optimized.py`. Mantiene masas 1..n para el primer tipo y j*n+1, j=1..m, para el segundo. El primer grupo queda por debajo del segundo, y las sumas de masas sucesivas del segundo ocupan intervalos disjuntos de n valores: cada regalo pesa distinto. Con n,m<=50 ninguna masa supera 2501. Emite las dos líneas en O(n+m) operaciones numéricas acotadas. Construye y une cada línea como antes; la primera usa map(str,range(...)). Las cadenas unidas aún requieren O(n+m) espacio máximo, no salida en flujo de espacio constante. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1731_constructive.py`: tiempo 0.093 s → 0.125 s; memoria 416 KB → 208 KB.

`1731_constructive_optimized.rs`. Mantiene masas 1..n para el primer tipo y j*n+1, j=1..m, para el segundo. El primer grupo queda por debajo del segundo, y las sumas de masas sucesivas del segundo ocupan intervalos disjuntos de n valores: cada regalo pesa distinto. Con n,m<=50 ninguna masa supera 2501. Emite las dos líneas en O(n+m) operaciones numéricas acotadas. Imprime cada masa al generarla, sin los dos Vec<String> ni las líneas unidas. Estado auxiliar O(1). La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1731_constructive.rs`: tiempo 0.046 s → 0.031 s; memoria 220 KB → 56 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1731_constructive_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328592 (Go 1.14 x64): **0.031 s / 972 KB**. Comparación archivada: `1731_constructive.go` (Go 1.14 x64) — 0.046 s / 1104 KB (#11289416).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1731_constructive_optimized.py`: puesto de tiempo 24/40 y de memoria 1/40 en esta muestra comparable.

`1731_constructive_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1731_constructive.cpp](1731_constructive.cpp) | G++ 13.2 x64 | constructive | O(n + m) | AC | 0.015 s | 376 KB | 11304041 |
| [1731_constructive.go](1731_constructive.go) | Go 1.14 x64 | constructive | O(n + m) | AC | 0.046 s | 1104 KB | 11289416 |
| [1731_constructive.java](1731_constructive.java) | Java 1.8 | constructive | O(n + m) | AC | 0.171 s | 1580 KB | 11289419 |
| [1731_constructive.py](1731_constructive.py) | Python 3.12 x64 | constructive | O(n + m) | AC | 0.093 s | 416 KB | 11289417 |
| [1731_constructive.rs](1731_constructive.rs) | Rust 1.75 x64 | constructive | O(n + m) | AC | 0.046 s | 220 KB | 11304042 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1731_constructive_optimized.cpp](1731_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(n + m) | AC | 0.015 s | 124 KB | 11304262 |
| [1731_constructive_optimized.java](1731_constructive_optimized.java) | Java 1.8 | constructive | O(n + m) | AC | 0.093 s | 376 KB | 11304040 |
| [1731_constructive_optimized.py](1731_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(n+m) | AC | 0.125 s | 208 KB | 11325001 |
| [1731_constructive_optimized.rs](1731_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(n+m) | AC | 0.031 s | 56 KB | 11325108 |
| [1731_constructive_optimized.go](1731_constructive_optimized.go) | Go 1.14 x64 | constructive | O(n + m) | AC | 0.031 s | 972 KB | 11328592 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
