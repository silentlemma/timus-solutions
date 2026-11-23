# 1268. El pequeño Chu

[Timus 1268](https://acm.timus.ru/problem.aspx?space=1&num=1268) · dificultad 722 · number_theory

Problema original de Pavel Atnashev, del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El pequeño Chu despierta K, K², K³, … días después de nacer y nunca
debe ver dos veces el mismo día de la semana; una semana tiene N días,
N primo (2 < N < 65 536), y K es como mucho una semana. Para cada uno de
T ≤ 6553 valores de N, hay que imprimir el K que da más despertares; el
ejemplo muestra que se espera el mayor de esos K.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

T, luego T primos N.

## Salida

K para cada N, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3
5
7
11
```

Salida:

```
2
3
5
8
```

## Solución

El día de la semana del i-ésimo despertar es K^i mod N. Estos valores
se repiten con el orden multiplicativo de K módulo N, así que el máximo
de despertares, N − 1, lo da una raíz primitiva. La respuesta es la
mayor raíz primitiva módulo N.

Un número g es raíz primitiva justo cuando g^((N−1)/q) ≠ 1 mod N para
cada primo q que divide N − 1. Se factoriza N − 1 con una criba de
menores factores primos hasta 65 536 y se prueban g = N − 1, N − 2, …
hasta que uno pase. Las raíces primitivas son una buena parte de los
residuos, así que se prueban pocos candidatos, cada uno con unas pocas
potencias rápidas. Los N repetidos se responden desde una tabla. Más o
menos `O(L log log L + T · k log N)` para el límite L de la criba y k
candidatos.

Detalles a tener en cuenta:

- cualquier raíz primitiva mantiene distintos los días, pero se espera
  la mayor (en el ejemplo, 8 para N = 11 y no 2);
- el límite de tiempo es un cuarto de segundo para hasta 6553
  consultas, así que conviene factorizar N − 1 con la criba y no
  probando divisores cada vez (pruebas 04, 05);
- cuando N − 1 es potencia de dos, basta una sola potencia de prueba
  (prueba 06).

Las respuestas se compararon con listar las potencias de cada candidato
para cada primo menor que 3000.

## Notas por lenguaje

- Todos los lenguajes construyen la misma criba y guardan una tabla de
  respuestas por N.

## Soluciones optimizadas

`1268_number_theory_optimized.cpp`. Conserva la criba de factores impares, las pruebas de raíz primitiva y la caché. Para residuos a,b<p<65536, a*b cabe en 32 bits. Precalcula floor(2^32/p); los 32 bits altos del producto por ese valor dan un cociente como máximo una unidad menor, y una resta condicional obtiene el resto EXACTO. Evita divisiones repetidas sin flotantes ni pruebas probabilísticas. Entrada y salida en bloques de16 KiB; no cambian búsqueda ni complejidad.

Accepted del fuente exacto #11326994: 0.015 s / 196 KB. Muestra G++ 13.2 guardada el 2026-11-20: tiempo 1/43, memoria 2/43. Se conservan los fuentes didácticos.

Las versiones optimizadas aplican la criba solo a los impares y comprueban el factor 2 por separado. Si se repite un módulo, reutilizan la respuesta guardada.

Python 3.12 x64, envío 11322010. Tiempo 0,156 → 0,125 s, memoria 4400 → 2368 KB.

Rust 1.75 x64, envío 11322011. Tiempo 0,031 → 0,031 s, memoria 1420 → 312 KB.

Go 1.14 x64, envío 11322012. Tiempo 0,015 → 0,031 s, memoria 2420 → 1004 KB.

G++ 13.2 x64, envío 11326994. Frente a la versión simple conservada: tiempo 0,031 → 0,015 s; memoria 692 → 196 KB.

Java 1.8, envío 11322014. Tiempo 0,109 → 0,078 s, memoria 2928 → 920 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322241 · Go 1.14 x64 №11322242 · Java 1.8 №11322243 · Python 3.12 x64 №11322244 · Rust 1.75 x64 №11322245.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1268_number_theory_parsing_optimized.py`. Las consultas se leen en un arreglo compacto de enteros sin signo de 16 bits y sus respuestas se guardan al primer uso. Se evita el conjunto temporal, conservando la factorización y la búsqueda de raíces. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328772 (Python 3.12 x64): **0.125 s / 1824 KB**. Comparación archivada: `1268_number_theory_optimized.py` (Python 3.12 x64) — 0.125 s / 2368 KB (#11322010).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1268_number_theory.cpp](1268_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 692 KB | 11322241 |
| [1268_number_theory.go](1268_number_theory.go) | Go 1.14 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.015 s | 2420 KB | 11322242 |
| [1268_number_theory.java](1268_number_theory.java) | Java 1.8 | number_theory | O(L log log L + T · k log N) | AC | 0.109 s | 2928 KB | 11322243 |
| [1268_number_theory.py](1268_number_theory.py) | Python 3.12 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.156 s | 4400 KB | 11322244 |
| [1268_number_theory.rs](1268_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 1420 KB | 11322245 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1268_number_theory_optimized.py](1268_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.125 s | 2368 KB | 11322010 |
| [1268_number_theory_optimized.rs](1268_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 312 KB | 11322011 |
| [1268_number_theory_optimized.go](1268_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 1004 KB | 11322012 |
| [1268_number_theory_optimized.cpp](1268_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.015 s | 196 KB | 11326994 |
| [1268_number_theory_optimized.java](1268_number_theory_optimized.java) | Java 1.8 | number_theory | O(L log log L + T · k log N) | AC | 0.078 s | 920 KB | 11322014 |
| [1268_number_theory_parsing_optimized.py](1268_number_theory_parsing_optimized.py) | Python 3.12 x64 | number_theory, parsing | O(L log log L + T · k log N) | AC | 0.125 s | 1824 KB | 11328772 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
