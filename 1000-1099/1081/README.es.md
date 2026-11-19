# 1081. La K-ésima cadena binaria sin dos unos seguidos

[Timus 1081](https://acm.timus.ru/problem.aspx?space=1&num=1081) · dificultad 271 · dp

Problema original de Emil Kelevedzhiev, del Torneo de Informática del Festival Matemático de Invierno, Varna 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Considera todas las cadenas de longitud `N` (`0 < N < 44`) formadas por 0
y 1 sin dos unos seguidos, ordenadas lexicográficamente. Imprime la
`K`-ésima (`0 < K < 10^9`), o `-1` si hay menos de `K`.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `K`.

## Salida

La cadena, o `-1`.

## Evaluación

Comparar la cadena binaria de N caracteres, o -1 si el rango no existe. El nuevo código Python exacto pasó 15 pruebas del repositorio con PyPy 3.10. Además 239 comprobaciones exhaustivas de cadenas cortas y rangos. Las otras variantes conservan sus propias pruebas de destino y Accepted exactos. La salida se compara según el verificador del problema.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 1
```

Salida:

```
000
```

## Solución

Sea `count[r]` el número de cadenas válidas de longitud `r`: una cadena
empieza o bien con 0 y cualquier resto válido, o bien con `10` y
cualquier resto válido, así que `count[r] = count[r − 1] + count[r − 2]`
con `count[0] = 1` y `count[1] = 2`, los números de Fibonacci.

La respuesta se construye de izquierda a derecha. Si el carácter anterior
es 1, este debe ser 0. Si no, las cadenas con 0 aquí van primero en el
orden, y hay `count[rest]` de ellas, donde `rest` es el número de
posiciones después de esta (el 0 no restringe el siguiente carácter). Si
`K ≤ count[rest]`, se escribe 0; si no, se resta `count[rest]` a `K` y se
escribe 1. Si desde el principio `K > count[N]`, se imprime `-1`. `O(N)`.

Detalles a tener en cuenta:

- `count[43] = 1 134 903 170` es mayor que cualquier `K`, así que para
  `N = 43` siempre hay respuesta; aun así los conteos se guardan en
  enteros de 64 bits;
- tras un 1 el siguiente carácter es forzoso y `K` no cambia;
- las cadenas se cuentan desde `K = 1`, la cadena de solo ceros.

Las respuestas se comprobaron con la lista ordenada de todas las cadenas
válidas para `N ≤ 20`, y para cadenas más largas calculando de vuelta la
posición de la respuesta con un conteo memorizado.

## Soluciones optimizadas

`1081_dp_optimized.rs`. Mantiene conteos Fibonacci y reconstrucción por rango sin unos adyacentes. Para n<=43 caben en u32: sustituye vector u64 creciente por 44 u32 fijos. Emite cada bit inmediatamente sin String y analiza dos enteros directamente. O(n) tiempo y conteos O(n), acotados aquí a 44 celdas. Rechaza k superior al total como antes.

Frente a `1081_dp.rs`: tiempo 0.046 s → 0.031 s; memoria 216 KB → 64 KB.

Se conserva la tabla clara de Fibonacci. Las variantes compactas retienen dos conteos vecinos y revierten la recurrencia al reconstruir. Si el rango residual desde cero alcanza el conteo con prefijo cero, lo restan y emiten uno; en otro caso cero. Tras un uno, el intervalo residual queda por debajo del siguiente conteo cero, forzando el siguiente bit sin caso especial. El total detecta rangos inválidos. Python acumula bits en un entero y lo formatea con N posiciones: conserva la respuesta de O(N) bits, sin tabla de conteos.

- `1081_dp_optimized.java`: 0.078 s / 372 KB; base `1081_dp.java`: 0.125 s / 1640 KB; cambio respecto a la base: tiempo -37.6%, memoria -77.3%.
- `1081_dp_optimized.py`: 0.125 s / 284 KB; base `1081_dp.py`: 0.093 s / 476 KB; cambio respecto a la base: tiempo +34.4%, memoria -40.3%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1081_dp_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1081_dp.cpp](1081_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 200 KB | 11279006 |
| [1081_dp.go](1081_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.015 s | 1084 KB | 11279009 |
| [1081_dp.java](1081_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 1640 KB | 11279012 |
| [1081_dp.py](1081_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.093 s | 476 KB | 11279010 |
| [1081_dp.rs](1081_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.046 s | 216 KB | 11279014 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1081_dp_optimized.java](1081_dp_optimized.java) | Java 1.8 | dp | O(N) | AC | 0.078 s | 372 KB | 11309292 |
| [1081_dp_optimized.py](1081_dp_optimized.py) \* | PyPy 3.10 x64 | dp | O(N) | AC | 0.125 s | 284 KB | 11309684 |
| [1081_dp_optimized.rs](1081_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(n) time; O(n) counts | AC | 0.031 s | 64 KB | 11325496 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
