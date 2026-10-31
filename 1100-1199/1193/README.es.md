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

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1193_greedy.go](1193_greedy.go).
- [1193_greedy.rs](1193_greedy.rs).

- Todos los lenguajes ordenan a los estudiantes por tiempo de preparación
  y hacen el mismo bucle.

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
