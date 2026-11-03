# 1113. El menor combustible para un viaje de ida con depósitos

[Timus 1113](https://acm.timus.ru/problem.aspx?space=1&num=1113) · dificultad 265 · math

Problema original de la Olimpiada Nacional Búlgara de Informática, segundo día.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un vehículo debe cruzar `N` km de desierto gastando un litro por
kilómetro. Lleva como mucho `M` litros, con `M < N ≤ 5M` y `N < 32000`.
En la salida hay combustible ilimitado, y el vehículo puede dejar
cualquier cantidad de combustible en cualquier punto del camino y
recogerla después. Halla la menor cantidad total de combustible, en
litros, necesaria para llegar al destino, redondeada hacia arriba.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N M` en una línea.

## Salida

La menor cantidad de combustible, redondeada hacia arriba.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
1000 500
```

Salida:

```
3837
```

## Solución

Es el problema del jeep de ida. Se razona hacia atrás desde el destino.
Los últimos `M` km necesitan una carga completa. Para llevar dos cargas
al inicio de ese tramo, un tramo de `M/3` km anterior se recorre tres
veces (ida, vuelta, ida), lo que cuesta exactamente una carga más; en
general un tramo de `M/(2k − 1)` km transporta `k` cargas al precio de una
más. Así que se suman tramos `M, M/3, M/5, …` hasta llegar a la salida;
si hacen falta `k` cargas y los tramos anteriores al último cubren `s`
km, el combustible es `(k − 1)·M + (N − s)·(2k − 1)`. Con `5M ≥ N`, el
máximo exacto es `k = 3092`: para `H_j = Σ_{i=1}^j 1/(2i − 1)` se cumple
`H_3091 < 5 ≤ H_3092`. Hay `O(k)` iteraciones, pero la aritmética de
enteros grandes requiere tiempo `O(kB)` y espacio auxiliar `O(B)`, donde
`B` es la longitud máxima de un entero grande en palabras de máquina.
Con estos límites, el otro operando de cada multiplicación, división o
gcd cabe en una palabra de máquina, por lo que cada operación requiere
`O(B)` operaciones sobre palabras.

Detalles a tener en cuenta:

- el redondeo hacia arriba debe ser exacto: el combustible es a menudo un
  entero, y la suma en coma flotante de `M/(2i − 1)` queda justo por
  encima y añade un litro de más (por ejemplo, `N = 59, M = 35` da
  exactamente 143, pero un cálculo simple con `double` imprime 144);
- los tramos solo decrecen como la serie armónica de los impares, así que
  con `N = 5M` hacen falta 3092, no como máximo 3000
  ([prueba 08](tests/08.in): `5 1`); la fracción exacta crece hasta varios
  miles de cifras, por lo que contar solo iteraciones subestima el coste
  de la aritmética.

Las respuestas se comprobaron con otra formulación con fracciones
exactas: la distancia alcanzable con `F` litros es
`M · Σ_{i≤q} 1/(2i − 1) + (F − qM)/(2q + 1)` con `q = ⌊F/M⌋`, y una
búsqueda binaria halla el menor `F` entero que alcanza `N`; los 12 viajes
hechos a mano y 150 aleatorios, muchos con capacidades divisibles por
`3 · 5 · 7 · 9`, coincidieron.

## Soluciones optimizadas

Se mantiene la construcción inversa mediante términos armónicos impares. Las cotas inferior y superior de punto fijo suelen determinar el entero exacto sin construir una fracción grande en cada paso. La anchura del intervalo está acotada; solo los casos ambiguos usan racionales exactos. Se comprueban las etapas vecinas posibles y se toma el combustible máximo necesario. No se emplean epsilon ni tablas de respuestas, por lo que el redondeo no acepta combustible insuficiente.

k es el número de etapas. Un paso aritmético exacto no tiene coste binario constante: el caso racional depende de la longitud de numeradores y denominadores.

- `1113_math_optimized.cpp`: 0.015 s / 168 KB; base `1113_math.cpp`: 0.031 s / 616 KB; cambio respecto a la base: tiempo -51.6%, memoria -72.7%.
- `1113_math_optimized.go`: 0.015 s / 1044 KB; base `1113_math.go`: 0.046 s / 3364 KB; cambio respecto a la base: tiempo -67.4%, memoria -69.0%.
- `1113_math_optimized.java`: 0.078 s / 368 KB; base `1113_math.java`: 0.125 s / 6344 KB; cambio respecto a la base: tiempo -37.6%, memoria -94.2%.
- `1113_math_optimized.py`: 0.062 s / 480 KB; base `1113_math.py`: 0.125 s / 908 KB; cambio respecto a la base: tiempo -50.4%, memoria -47.1%.
- `1113_math_optimized.rs`: 0.015 s / 224 KB; base `1113_math.rs`: 0.062 s / 536 KB; cambio respecto a la base: tiempo -75.8%, memoria -58.2%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1113_math.cpp`; versión que cubre `1113_math_optimized.cpp`; puestos tiempo/memoria 1/4, registros de otros autores 25/25.

- Go: base didáctica preferida `1113_math.go`; versión que cubre `1113_math.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1113_math.java`; versión que cubre `1113_math_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1113_math.py`; versión que cubre `1113_math_optimized.py`; puestos tiempo/memoria 1/7, registros de otros autores 22/22.

- Rust: base didáctica preferida `1113_math.rs`; versión que cubre `1113_math.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1113_math.cpp](1113_math.cpp) | G++ 13.2 x64 | math | O(kB), k ≤ 3092 | AC | 0.031 s | 616 KB | 11279217 |
| [1113_math.go](1113_math.go) | Go 1.14 x64 | math | O(kB), k ≤ 3092 | AC | 0.046 s | 3364 KB | 11279218 |
| [1113_math.java](1113_math.java) | Java 1.8 | math | O(kB), k ≤ 3092 | AC | 0.125 s | 6344 KB | 11279220 |
| [1113_math.py](1113_math.py) | Python 3.12 x64 | math | O(kB), k ≤ 3092 | AC | 0.125 s | 908 KB | 11279219 |
| [1113_math.rs](1113_math.rs) | Rust 1.75 x64 | math | O(kB), k ≤ 3092 | AC | 0.062 s | 536 KB | 11279221 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1113_math_optimized.cpp](1113_math_optimized.cpp) | G++ 13.2 x64 | math | O(k) exact-arithmetic steps | AC | 0.015 s | 168 KB | 11309282 |
| [1113_math_optimized.go](1113_math_optimized.go) | Go 1.14 x64 | math | O(k) exact-arithmetic steps | AC | 0.015 s | 1044 KB | 11309284 |
| [1113_math_optimized.java](1113_math_optimized.java) | Java 1.8 | math | O(k) exact-arithmetic steps | AC | 0.078 s | 368 KB | 11309283 |
| [1113_math_optimized.py](1113_math_optimized.py) \* | Python 3.12 x64 | math | O(k) exact-arithmetic steps | AC | 0.062 s | 480 KB | 11309281 |
| [1113_math_optimized.rs](1113_math_optimized.rs) | Rust 1.75 x64 | math | O(k) exact-arithmetic steps | AC | 0.015 s | 224 KB | 11309285 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
