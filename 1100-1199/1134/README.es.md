# 1134. Comprobar si son posibles los números leídos en cartas que muestran k − 1 y k

[Timus 1134](https://acm.timus.ru/problem.aspx?space=1&num=1134) · dificultad 197 · greedy

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `n ≤ 1000` cartas; la carta `k` muestra `k − 1` por un lado y `k` por
el otro. Un niño tomó `m ≤ n` cartas distintas en algún orden y leyó un
lado de cada una. Dados los `m` números leídos, decide si pudieron salir
de alguna elección de cartas y lados.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` y `m`, y luego los `m` números, cada uno de `0` a `n`.

## Salida

`YES` si la lectura es posible, y `NO` en otro caso.

## Evaluación

Se comparan los tokens; los espacios adicionales no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 4
2 0 1 2
```

Salida:

```
NO
```

## Solución

La pregunta es si cada lectura puede recibir su propia carta. El número
`x` aparece en las cartas `x` y `x + 1` (`0` solo en la carta 1, `n` solo
en la carta `n`), así que cada lectura puede usar una de dos cartas
vecinas. Se cuentan las lecturas de cada número y se sube desde `0`. Las
lecturas de `x` toman primero la carta `x` y luego la carta `x + 1`. Tomar
primero la carta inferior es seguro: la carta `x` solo muestra `x − 1` y
`x`, y todas las lecturas de `x − 1` ya están colocadas, así que nada
posterior puede usarla. Si alguna lectura de `x` encuentra ocupadas sus
dos cartas, no hay asignación posible. `O(n + m)`.

Detalles a tener en cuenta:

- `0` y `n` aparecen cada uno en una sola carta;
- el mismo número puede leerse varias veces, como mucho dos para una
  respuesta `YES`;
- las lecturas vienen en orden arbitrario; solo importan sus cantidades.

Las respuestas se compararon con el emparejamiento bipartito de Kuhn en
todas las pruebas y en 400 casos aleatorios.

## Soluciones optimizadas

`1134_greedy_optimized.rs`. Mantiene asignación voraz ascendente a tarjeta x y luego x+1. Un tercer valor repetido es imposible: lo rechaza inmediatamente y usa contadores de un byte. Sustituye todo array de tarjetas usadas por una bandera de si el paso anterior ocupó la actual. Lee m valores en flujo sin retener tokens. O(n+m) tiempo y O(n) espacio, con límites 0 y n exactos.

Frente a `1134_greedy.rs`: tiempo 0.015 s → 0.015 s; memoria 204 KB → 72 KB.

Se conserva la asignación voraz de la menor carta posible. Un contador de bytes por valor reemplaza las tablas separadas de frecuencia y ocupación; un único estado transmite la ocupación entre elecciones vecinas. Procesar por valor y consumir siempre la menor carta disponible deja las mayores para demandas posteriores. Un centinela elimina los casos especiales de los extremos. Las tablas indican el intérprete Python real y el ahorro medido.

- `1134_greedy_optimized.py`: 0.140 s / 288 KB; base `1134_greedy.py`: 0.078 s / 492 KB; cambio respecto a la base: tiempo +79.5%, memoria -41.5%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1134_greedy_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1134_greedy.cpp](1134_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.015 s | 192 KB | 11279396 |
| [1134_greedy.go](1134_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.031 s | 1104 KB | 11279398 |
| [1134_greedy.java](1134_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.078 s | 432 KB | 11279401 |
| [1134_greedy.py](1134_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.078 s | 492 KB | 11279399 |
| [1134_greedy.rs](1134_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.015 s | 204 KB | 11279402 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1134_greedy_optimized.py](1134_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(N+M) | AC | 0.140 s | 288 KB | 11309377 |
| [1134_greedy_optimized.rs](1134_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(n+m) time; O(n) space | AC | 0.015 s | 72 KB | 11325514 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
