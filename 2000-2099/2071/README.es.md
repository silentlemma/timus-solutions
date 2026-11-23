# 2071. Orden de los cócteles con menos vertidos

[Timus 2071](https://acm.timus.ru/problem.aspx?space=1&num=2071) · dificultad 641 · bitmask, dp

Problema original de Mikhail Rubinchik, preparado por Nickolai Permyakov y Alexey Danilyuk, del Concurso Regional de Programación por Equipos de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de n clientes pide un cóctel: un conjunto no vacío de los zumos
A, B y P. Los vasos se ponen en fila en algún orden, y un vertido llena
un tramo de vasos consecutivos con un zumo (primero manzana, luego
plátano y luego piña, así que el orden de los vertidos no es problema).
Cada vaso debe recibir exactamente los zumos de su cóctel. Ordenar los
vasos para necesitar el menor número de vertidos. Los límites son
1 segundo y 64 MB.

## Entrada

n, 1 ≤ n ≤ 10⁵, y después n líneas, cada una A, B, P, AB, AP, BP o ABP.

## Salida

El menor número de vertidos y después los números de los vasos en el
orden de la fila. Se acepta cualquier orden óptimo.

## Evaluación

Un comprobador compara el número de vertidos y recuenta los vertidos que
necesita el orden impreso.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
A
B
ABP
```

Salida:

```
3
1 3 2
```

## Solución

Con la fila fija, cada zumo necesita un vertido por cada tramo maximal de
vasos que lo contienen, así que el coste es el número de lugares donde
un zumo está en un vaso pero no en el anterior (el primer vaso cuenta
todos sus zumos). Quitar un vaso no crea nuevos tramos. Colocarlo junto a otro del
mismo tipo solo alarga los tramos existentes. Así, se pueden agrupar
los vasos por tipo de cóctel y ordenar como máximo siete grupos.

Se ordenan con una DP sobre subconjuntos: best[S][last] es el menor
número de vertidos para una fila hecha de los cócteles de S que termina
en last. Añadir el cóctel k cuesta los zumos de k que faltan en last, es
decir popcount(k & ~last). La respuesta es el mínimo sobre last para el
conjunto completo, y los predecesores guardados dan el orden. Con siete
cócteles son 2⁷ · 7 · 7 pasos, así que el trabajo es O(n) para leer e
imprimir.

En el ejemplo el orden B, ABP, A necesita tres vertidos: un tramo por
zumo.

## Soluciones optimizadas

La versión en C++ enumera los órdenes de hasta siete tipos de cóctel. Los índices de los vasos de cada tipo forman una lista enlazada en un único arreglo. La entrada y la salida cuestan O(n), enumerar k tipos cuesta O(k! · k) y se usan O(n) de memoria. El envío 11317118 tardó 0.046 s y usó 560 KB frente a 0.078 s y 420 KB de la base.

Java analiza la entrada byte a byte, guarda los costes y predecesores en arreglos de bytes y enlaza los índices mediante un arreglo de enteros. El envío 11317279 tardó 0,125 s y usó 832 KB frente a 0,14 s y 8836 KB en la base.

Go lee un elemento a la vez y enlaza los índices de los vasos mediante un arreglo de 32 bits. La programación dinámica por subconjuntos usa arreglos de bytes para los costes y los predecesores. El envío 11317277 tardó 0,031 s y usó 1288 KB frente a 0,031 s y 8040 KB en la base.

Python usa arreglos de bytes para los costes y los predecesores, lee los pedidos línea por línea y escribe por bloques los índices almacenados en arreglos compactos. El envío 11317276 tardó 0,109 s y usó 1408 KB frente a 0,171 s y 16872 KB en la base.

Rust guarda el coste y el predecesor de cada estado de la programación dinámica en un byte cada uno. Los índices de los vasos de cada tipo se enlazan mediante un arreglo común de 32 bits. El envío 11317274 tardó 0,046 s y usó 584 KB frente a 0,046 s y 7676 KB en la base.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11318364 · Java 1.8 №11318369 · Rust 1.75 x64 №11318371.

La DP por subconjuntos de C++ lee y escribe por bloques y enlaza en un solo arreglo los índices de cada tipo de cóctel. G++ 13.2 x64, envío 11321988. Tiempo 0,078 → 0,015 s, memoria 420 → 516 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`2071_bitmask_dp_implementation_optimized.py`. Se almacenan los recuentos de bits de las máscaras pequeñas y se usan listas para costes y predecesores. Las transiciones y la reconstrucción no cambian; las listas intercambian memoria por acceso más barato. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328669 (Python 3.12 x64): **0.093 s / 1428 KB**. Comparación archivada: `2071_bitmask_dp_optimized.py` (Python 3.12 x64) — 0.109 s / 1408 KB (#11317276).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2071_bitmask_dp.cpp](2071_bitmask_dp.cpp) | G++ 13.2 x64 | bitmask, dp | O(n) | AC | 0.078 s | 420 KB | 11318364 |
| [2071_bitmask_dp.go](2071_bitmask_dp.go) | Go 1.14 x64 | bitmask, dp | O(n) | AC | 0.031 s | 8040 KB | 11322036 |
| [2071_bitmask_dp.java](2071_bitmask_dp.java) | Java 1.8 | bitmask, dp | O(n) | AC | 0.14 s | 8836 KB | 11318369 |
| [2071_bitmask_dp.py](2071_bitmask_dp.py) | Python 3.12 x64 | bitmask, dp | O(n) | AC | 0.171 s | 16872 KB | 11322037 |
| [2071_bitmask_dp.rs](2071_bitmask_dp.rs) | Rust 1.75 x64 | bitmask, dp | O(n) | AC | 0.046 s | 7676 KB | 11318371 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2071_bruteforce.cpp](2071_bruteforce.cpp) \* | G++ 13.2 x64 | bruteforce | O(n) | AC | 0.046 s | 560 KB | 11317118 |
| [2071_bitmask_dp_optimized.go](2071_bitmask_dp_optimized.go) | Go 1.14 x64 | bitmask, dp | O(n) | AC | 0.031 s | 1288 KB | 11317277 |
| [2071_bitmask_dp_optimized.java](2071_bitmask_dp_optimized.java) | Java 1.8 | bitmask, dp | O(n) | AC | 0.125 s | 832 KB | 11317279 |
| [2071_bitmask_dp_optimized.py](2071_bitmask_dp_optimized.py) \* | Python 3.12 x64 | bitmask, dp | O(n) | AC | 0.109 s | 1408 KB | 11317276 |
| [2071_bitmask_dp_optimized.rs](2071_bitmask_dp_optimized.rs) | Rust 1.75 x64 | bitmask, dp | O(n) | AC | 0.046 s | 584 KB | 11317274 |
| [2071_bitmask_dp_optimized.cpp](2071_bitmask_dp_optimized.cpp) | G++ 13.2 x64 | bitmask, dp | O(n) | AC | 0.015 s | 516 KB | 11321988 |
| [2071_bitmask_dp_implementation_optimized.py](2071_bitmask_dp_implementation_optimized.py) | Python 3.12 x64 | bitmask, dp, implementation | O(n) | AC | 0.093 s | 1428 KB | 11328669 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
