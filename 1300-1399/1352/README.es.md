# 1352. Primos de Mersenne

[Timus 1352](https://acm.timus.ru/problem.aspx?space=1&num=1352) · dificultad 132 · number_theory

Problema original de Vladimir Yakovlev, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un primo de Mersenne es un primo de la forma 2^p − 1. Dadas T
consultas, cada una con un número N ≤ 38, hay que imprimir el exponente
p del N-ésimo primo de Mersenne en orden creciente.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

T, luego T líneas con N.

## Salida

T líneas con los exponentes.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
13
18
32
24
21
19
34
27
33
20
30
28
29
22
```

Salida:

```
3217
756839
19937
9689
4253
1257787
44497
859433
4423
132049
86243
110503
9941
```

## Solución

Ningún programa puede hallar estos primos en un segundo: el exponente
38 es 6 972 593, y comprobar un solo número de ese tamaño exige muchísimo
cálculo. El orden de los primeros 38 primos de Mersenne se estableció
hace tiempo, así que las soluciones guardan la lista de sus exponentes
como una tabla constante y responden cada consulta con un acceso por
índice. `O(T)`.

Detalles a tener en cuenta:

- N cuenta desde 1: el primer primo de Mersenne es 2² − 1 = 3, con
  exponente 2 (prueba 03);
- todos los exponentes caben en enteros de 32 bits.

Las primeras 22 entradas se comprobaron con la prueba de Lucas–Lehmer
para todos los exponentes primos hasta 10 000; el resto viene de la
lista publicada y coincide con el ejemplo y con los valores que cita el
enunciado.

## Soluciones optimizadas

`1352_number_theory_optimized.rs`. Conserva tabla exacta de primeros 38 exponentes Mersenne del enunciado. Lee Q índices en flujo y emite cada entero por runtime C, sin Strings completos ni to_string por respuesta. O(Q) tiempo y O(1) espacio auxiliar para tabla fija; no introduce otro test de primalidad ni tabla de respuestas.

Frente a `1352_number_theory.rs`: tiempo 0.001 s → 0.001 s; memoria 216 KB → 56 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1352_parsing_optimized.go`. Se usa conversión directa por tipos con un búfer recargable de 256 bytes y salida compacta con escrituras completas. Los negativos se acumulan con signo, incluido el mínimo entero, sin reflexión de entrada ni despacho genérico de salida. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios. Los dígitos completos se convierten dentro del bloque, manteniendo local el cursor hasta un límite. La acumulación negativa admite el mínimo con signo y evita una rama o llamada por dígito, conservando EOF y signos opcionales.

Accepted #11329135 (Go 1.14 x64): **0.015 s / 796 KB**. Comparación archivada: `1352_number_theory.go` (Go 1.14 x64) — 0.031 s / 1084 KB (#11285182).

## Notas por lenguaje

El código CPython sin cambios se midió tres veces más: (0.078 s, 468 KB), (0.093 s, 400 KB) y (0.046 s, 312 KB). La tabla usa el último par real Accepted; repetir la medición no constituye una mejora algorítmica. En la muestra guardada de intérpretes actuales comparables, esa ejecución comparte el puesto 1/30 en tiempo y ocupa el 11/30 en memoria. Por debajo de 1 MiB, la admisión considera el puesto por tiempo. La versión sencilla ya cumple el criterio, por lo que no se añade una copia Python con nombre optimized.

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1352_number_theory_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1352_number_theory.cpp](1352_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T) | AC | 0.001 s | 128 KB | 11285181 |
| [1352_number_theory.go](1352_number_theory.go) | Go 1.14 x64 | number_theory | O(T) | AC | 0.031 s | 1084 KB | 11285182 |
| [1352_number_theory.java](1352_number_theory.java) | Java 1.8 | number_theory | O(T) | AC | 0.078 s | 444 KB | 11285186 |
| [1352_number_theory.py](1352_number_theory.py) | Python 3.12 x64 | number_theory | O(T) | AC | 0.046 s | 312 KB | 11326033 |
| [1352_number_theory.rs](1352_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T) | AC | 0.001 s | 216 KB | 11285188 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1352_number_theory_optimized.rs](1352_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(Q) time; O(1) auxiliary space | AC | 0.001 s | 56 KB | 11325503 |
| [1352_parsing_optimized.go](1352_parsing_optimized.go) | Go 1.14 x64 | parsing | O(T) | AC | 0.015 s | 796 KB | 11329135 |
