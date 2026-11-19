# 1161. El resultado más ligero de fusionar criaturas con el doble de la media geométrica

[Timus 1161](https://acm.timus.ru/problem.aspx?space=1&num=1161) · dificultad 93 · greedy

Problema original de Nick Durov, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 100` criaturas tienen pesos enteros de 1 a 10000. Dos de ellas
pueden fusionarse en una de peso `2·√(m₁·m₂)`, y las fusiones siguen
hasta que queda una. Halla el menor peso final posible, con dos cifras
decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego los `N` pesos.

## Salida

El menor peso final.

## Evaluación

Las pruebas del repositorio comparan tokens numéricos con |resultado-referencia| <= 0.011·max(1,|referencia|), rechazan valores no finitos y comparan exactamente los tokens no numéricos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
72
50
```

Salida:

```
120.00
```

### Ejemplo 2

Entrada:

```
3
72
30
50
```

Salida:

```
120.00
```

## Solución

Se fusionan primero las dos más pesadas, luego el resultado con la
siguiente más pesada, y así hasta la más ligera. En cualquier orden de
fusiones, cada peso acaba dentro de varias raíces cuadradas anidadas: un
peso fusionado `k` veces entra en el resultado como su raíz de orden
`2^k`, por constantes que solo dependen de la forma de las fusiones. El
peso final es mínimo cuando los pesos mayores pasan por más raíces, y la
cadena desde el más pesado hacia abajo hace justo eso, dando a los pesos
mayores las posiciones más profundas. Ordenar y una pasada:
`O(N log N)`.

Detalles a tener en cuenta:

- con una sola criatura, su peso es la respuesta;
- el orden importa: fusionar primero las ligeras puede dar un resultado más
  pesado;
- el peso nunca pasa de 40000, muy dentro de la precisión de double.

Las respuestas se compararon con probar todos los órdenes de fusión en 150
colonias aleatorias de hasta siete criaturas.

## Soluciones optimizadas

La solución optimizada en C++ guarda los a lo sumo 100 pesos en un
arreglo de tamaño fijo en lugar de un `vector`, así que no reserva
memoria en el montón: 136 KB en lugar de 216 KB. La ordenación y el
redondeo son los mismos.

La solución optimizada en Java lee la entrada en bloques de 4 KB y
analiza los números a mano en lugar de usar `Scanner`, y redondea sin
`BigDecimal`. Un `double` es exactamente una mantisa entera menor que
`2^53` dividida por `2^shift`. Cada fusión da como mucho `2·√(x·10000)`,
así que el total se mantiene por debajo de 40000 y el desplazamiento va
de 37 a 52; 100 veces la mantisa es menor que `100·2^53` y sigue
cabiendo en un `long`. Por eso 100 veces el total es una fracción exacta
de dos `long`, y el código la redondea con empates al par, como
`printf`: 0.093 s en lugar de 0.140 s y 444 KB en lugar de 1912 KB.

`1161_greedy_optimized.rs`. Conserva el orden voraz de pesos descendentes y el cálculo f64 total=2*sqrt(total*weight). La ordenación in situ no estable evita el búfer temporal de la estable; printf emite dos decimales sin formato Rust. El vector de pesos sigue ocupando O(N), con tiempo O(N log N). La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1161_greedy.rs`: tiempo 0.015 s → 0.046 s; memoria 248 KB → 104 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1161_greedy_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1161_greedy.cpp](1161_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 216 KB | 11281794 |
| [1161_greedy.go](1161_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1096 KB | 11281809 |
| [1161_greedy.java](1161_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 1912 KB | 11281833 |
| [1161_greedy.py](1161_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 364 KB | 11281821 |
| [1161_greedy.rs](1161_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 248 KB | 11281889 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1161_greedy_optimized.cpp](1161_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 136 KB | 11303573 |
| [1161_greedy_optimized.java](1161_greedy_optimized.java) | Java 1.8 | greedy | O(N log N) | AC | 0.093 s | 444 KB | 11303959 |
| [1161_greedy_optimized.rs](1161_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.046 s | 104 KB | 11325086 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
