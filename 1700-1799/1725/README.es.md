# 1725. ¡Agotado!

[Timus 1725](https://acm.timus.ru/problem.aspx?space=1&num=1725) · dificultad 142 · math

Problema original de Denis Dublennykh (preparado por Oleg Dolgorukov), del Concurso Regional Escolar de Programación de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Vasya se sienta primero en una fila de n asientos, en el asiento k; los
demás llegan uno a uno hasta llenar la fila. Cada uno entra por el
extremo con menos gente ya sentada entre ese extremo y su asiento, o,
si hay empate, por el extremo más cercano. Hallar el mayor número de
personas que pueden tropezar con las piernas de Vasya.

## Entrada

n y k (1 ≤ k ≤ n ≤ 50, n par).

## Salida

El mayor número de personas que tropiezan con Vasya.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 1
```

Salida:

```
1
```

## Solución

Se llama lado lejano a la parte más larga de la fila más allá de
Vasya; tiene max(k − 1, n − k) asientos. La respuesta es esa cantidad
menos 2, pero no menos de 0. `O(1)`.

Los dos asientos del extremo lejano nunca tropiezan. Más allá del
último no hay nadie, y más allá del penúltimo hay a lo sumo una
persona, mientras que al otro lado está Vasya, y en el empate su propio
extremo está más cerca.

Todos los demás del lado lejano pueden tropezar. Se sientan primero los
dos asientos del extremo y luego se llena el lado lejano desde su
extremo hacia Vasya. Así cada persona nueva tiene en el camino desde el
extremo de Vasya solo a Vasya, y desde el otro extremo al menos a dos
personas, por lo que pasa junto a Vasya.

La gente del lado cercano también puede tropezar, pero solo cuando ese
lado ya está mucho más lleno que el lejano, y entonces la gente del
lado lejano encuentra demasiada gente del lado de Vasya y deja de
tropezar. Nunca sale a cuenta.

En el ejemplo el lado lejano tiene tres asientos, así que tropieza una
persona: la del asiento 2, después de ocuparse los asientos 3 y 4.

Trampas:

- con n = 2 o con Vasya en medio de cuatro asientos la respuesta es 0,
  no un número negativo;
- el lado lejano puede estar a cualquier lado de Vasya.

La fórmula coincide con una búsqueda exhaustiva de todos los órdenes de
llegada para todo n par hasta 16 y todo k.

## Soluciones optimizadas

La solución optimizada en C++ lee los dos números con `scanf` e imprime
con `printf` en lugar de `std::cin` y `std::cout`, así que el programa
prescinde de la biblioteca `iostream` y sus búferes; la fórmula es la
misma: {1725_math_optimized.cpp}.

La solución optimizada en Java lee los dos números byte a byte con
`System.in.read` en lugar de crear un `Scanner`, así que la JVM no carga
el escáner ni sus expresiones regulares; la fórmula es la misma:
{1725_math_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1725_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +74.75%; base: `1725_math.cpp`.

- `1725_math_optimized.java`: reducción de tiempo +25.60%; reducción de
  memoria +77.89%; base: `1725_math.java`.

`1725_math_optimized.py`. Conserva max(0,max(k-1,n-k)-2): elige el lado más lejano y excluye sus dos asientos seguros del extremo. No busca órdenes de llegada. Los datos no superan 50; aritmética acotada y espacio O(1). Analiza los dos tokens enteros como bytes y conserva la fórmula directa. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1725_math.py`: tiempo 0.062 s → 0.125 s; memoria 340 KB → 188 KB.

`1725_math_optimized.rs`. Conserva max(0,max(k-1,n-k)-2): elige el lado más lejano y excluye sus dos asientos seguros del extremo. No busca órdenes de llegada. Los datos no superan 50; aritmética acotada y espacio O(1). Lee solo dos valores con signo, sin String completo; mantiene el límite inferior cero. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1725_math.rs`: tiempo 0.031 s → 0.015 s; memoria 244 KB → 60 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1725_math_optimized.py`: puesto de tiempo 27/34 y de memoria 1/34 en esta muestra comparable.

`1725_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1725_math.cpp](1725_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 396 KB | 11289360 |
| [1725_math.go](1725_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB | 11289361 |
| [1725_math.java](1725_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1592 KB | 11289365 |
| [1725_math.py](1725_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 340 KB | 11289363 |
| [1725_math.rs](1725_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 244 KB | 11304071 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1725_math_optimized.cpp](1725_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 100 KB | 11304482 |
| [1725_math_optimized.java](1725_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 352 KB | 11304483 |
| [1725_math_optimized.py](1725_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 188 KB | 11324909 |
| [1725_math_optimized.rs](1725_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 60 KB | 11325107 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
