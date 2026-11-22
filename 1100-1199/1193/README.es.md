# 1193. ¿Cuánto antes debe empezar un examen oral para que todos terminen a tiempo?

[Timus 1193](https://acm.timus.ru/problem.aspx?space=1&num=1193) · dificultad 181 · greedy

Problema original de Anatoly Uglov, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 40` estudiantes reciben sus preguntas al empezar un examen oral. El
estudiante `i` se prepara `T1` minutos (todos distintos) y luego responde
durante `T2` minutos, de uno en uno, en el orden en que terminan de
prepararse; quien termina mientras otro responde espera en una cola. Cada
estudiante debe terminar como mucho `T3` minutos después del inicio
previsto. Hay que hallar el menor número de minutos que hay que adelantar
el examen para que todos terminen a tiempo.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` (`1 ≤ N ≤ 40`) y luego `T1 T2 T3` para cada estudiante, con
`0 ≤ T1 ≤ T3 ≤ 600` y `1 ≤ T2 ≤ 240`. Todos los valores `T1` son
distintos.

## Salida

El número de minutos, 0 si no hace falta adelantar.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
100 10 120
70 40 150
99 15 400
```

Salida:

```
15
```

### Ejemplo 2

Entrada:

```
2
100 10 110
80 15 100
```

Salida:

```
0
```

## Solución

Empezar `s` minutos antes lo desplaza todo en `s`: el orden de la cola y
cada espera siguen iguales, y solo los plazos quedan `s` minutos más tarde
respecto al inicio. Así que se simula el examen una vez, en orden de
`T1`: cada respuesta empieza cuando el estudiante está listo o cuando
termina la anterior, lo que sea más tarde. La respuesta es el mayor
retraso, el final menos `T3`, o 0 si nadie se retrasa. `O(N log N)` por la
ordenación.

Detalles a tener en cuenta:

- la cola va por el fin de la preparación, no por el orden de entrada;
- un estudiante listo cuando nadie responde empieza enseguida, así que
  puede haber ratos sin nadie respondiendo;
- el adelanto no puede ser negativo: si todos van sobrados, la respuesta
  es 0.

Las respuestas se compararon con una solución escrita aparte, que busca
el adelanto por bisección, en 300 exámenes aleatorios y en todas las
pruebas.

## Soluciones optimizadas

`1193_greedy_sorting.java`. La misma simulación por disponibilidad usa direccionamiento directo en vez de comparaciones: T1 distintos en 0..600. Guarda (T2<<10)|T3 en ranura T1; T2≥1 deja cero como vacío y T3≤600 cabe en diez bits. Recorre ranuras por tiempo, finish=max(finish,T1)+T2 y máximo retraso. O(N+601), 601 enteros y búfer decimal de 256 bytes. Implementación distinta llamada greedy_sorting; conserva ordenación didáctica y alternativa anterior.

Fuente exacto: Java 1.8 Accepted #11327835: 0.078 s / 356 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 1/42; 1/42. Admisión estricta usa solo tiempo bajo 1024 KB: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. Ambas son primeras, sin asterisco. La variante anterior conservada tiene su par propio #11307308 (Java 1.8): 0.125 s / 376 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `1193_greedy_sorting.java`: 0.078 s / 356 KB; base didáctica conservada `1193_greedy.java` (Java 1.8): 0.14 s / 3776 KB.

La solución optimizada en C++ guarda a los estudiantes en un arreglo
estático de 40 registros, suficiente porque `N ≤ 40`, en lugar de un
vector de tuplas reservado en el montículo; la ordenación y la
simulación son las mismas: {1193_greedy_optimized.cpp}.

La solución optimizada en Java lee los números byte a byte en bloques de
4 KB en lugar de con `Scanner` y guarda a los estudiantes en tres
arreglos `int`, colocando a cada uno en su sitio por inserción según se
lee, en lugar de ordenar un arreglo de ternas con un comparador lambda.
Con 40 estudiantes como mucho, la ordenación por inserción cuadrática no
cuesta nada: {1193_greedy_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1193_greedy_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +39.58%; base: `1193_greedy.cpp`.

- `1193_greedy_optimized.java`: reducción de tiempo +10.71%; reducción
  de memoria +90.04%; base: `1193_greedy.java`.

`1193_greedy_optimized.rs`. Mantiene el orden por tiempos distintos de preparación y busy=max(busy,ready)+talk. La respuesta es el mayor busy-deadline positivo. Ordena el vector de alumnos in situ de forma no estable, sin almacenamiento temporal de ordenación estable ni entrada completa decodificada. Tiempo O(N log N), espacio O(N). La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1193_greedy.rs`: tiempo 0.015 s → 0.046 s; memoria 236 KB → 76 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1193_greedy_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1193_greedy.cpp](1193_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 192 KB | 11283459 |
| [1193_greedy.go](1193_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1116 KB | 11283460 |
| [1193_greedy.java](1193_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 3776 KB | 11283464 |
| [1193_greedy.py](1193_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 380 KB | 11283463 |
| [1193_greedy.rs](1193_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 236 KB | 11283465 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1193_greedy_optimized.cpp](1193_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 116 KB | 11307306 |
| [1193_greedy_optimized.java](1193_greedy_optimized.java) | Java 1.8 | greedy | O(N²) | AC | 0.125 s | 376 KB | 11307308 |
| [1193_greedy_sorting.java](1193_greedy_sorting.java) | Java 1.8 | greedy, sorting | O(N+601) time; 601 integer slots | AC | 0.078 s | 356 KB | 11327835 |
| [1193_greedy_optimized.rs](1193_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.046 s | 76 KB | 11325093 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
