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

Se conserva la asignación voraz de la menor carta posible. Un contador de bytes por valor reemplaza las tablas separadas de frecuencia y ocupación; un único estado transmite la ocupación entre elecciones vecinas. Procesar por valor y consumir siempre la menor carta disponible deja las mayores para demandas posteriores. Un centinela elimina los casos especiales de los extremos. Las tablas indican el intérprete Python real y el ahorro medido.

- `1134_greedy_optimized.py`: 0.140 s / 288 KB; base `1134_greedy.py`: 0.078 s / 492 KB; cambio respecto a la base: tiempo +79.5%, memoria -41.5%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1134_greedy.cpp`; versión que cubre `1134_greedy.cpp`; puestos tiempo/memoria 1/3, registros de otros autores 69/69.

- Go: base didáctica preferida `1134_greedy.go`; versión que cubre `1134_greedy.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1134_greedy.java`; versión que cubre `1134_greedy.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1134_greedy.py`; versión que cubre `1134_greedy_optimized.py`; puestos tiempo/memoria 12/1, registros de otros autores 12/12.

- Rust: base didáctica preferida `1134_greedy.rs`; versión que cubre `1134_greedy.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

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

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
