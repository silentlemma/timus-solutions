# 1082. Una entrada que hace contar a un quicksort un número dado de pasos

[Timus 1082](https://acm.timus.ru/problem.aspx?space=1&num=1082) · dificultad 127 · constructive

Problema original de Nikita Shamgunov, de la Tercera Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 4 de marzo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un programa dado lee `N` enteros (`1 ≤ N ≤ 1000`) y los ordena con un
quicksort: el pivote es el primer elemento del rango, y dos índices se
mueven uno hacia el otro, `j` desde la derecha mientras los elementos son
mayores que el pivote e `i` desde la izquierda mientras son menores,
intercambiando mientras no se crucen (partición de Hoare). El programa
cuenta cada movimiento de `i` y de `j` en todas las llamadas y gana si
el total es exactamente `(N² + 3N − 4)/2`. Imprime `N` enteros de valor
absoluto hasta `10^9` que lo hagan ganar.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

`N` enteros separados por espacios.

## Evaluación

Se acepta cualquier conjunto de números adecuado. El comprobador ejecuta
la misma partición sobre la salida y compara la cuenta con
`(N² + 3N − 4)/2`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
1 2 3
```

## Solución

Se imprimen los números ordenados `1, 2, …, N`. En un rango ordenado de
longitud `k` con el pivote en su extremo izquierdo, `j` recorre desde el
extremo derecho hasta el propio pivote, `k` movimientos, e `i` hace un
movimiento hasta el pivote; se encuentran enseguida, así que el rango se
parte en el pivote solo y los otros `k − 1` elementos, todavía
ordenados. La cuenta es `k + 1` para cada `k` de `N` a 2:

`(N + 1) + N + … + 3 = (N² + 3N − 4)/2`,

que es exactamente el objetivo. `O(N)`.

Detalles a tener en cuenta:

- otros órdenes dan otras cuentas: con `3 2 1` el programa cuenta 8
  movimientos en lugar de 7, porque el intercambio cambia cómo se parten
  los rangos;
- con `N = 1` el programa no cuenta nada, y el objetivo también es 0.

El comprobador simula la partición con una pila explícita y compara la
cuenta.

## Soluciones optimizadas

`1082_constructive_optimized.java`. Conserva la construcción ascendente 1..N para el peor caso exigido de quicksort. Emite cada entero con un arreglo de dígitos reutilizado y búfer de 4096 bytes, sin construir todo el StringBuilder. Trabajo proporcional a los dígitos emitidos, O(N log N), y espacio auxiliar fijo. Conserva el argumento constructivo y la base didáctica.

Accepted exacto Java 1.8 #11327337: 0.078 s / 336 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/165, memoria 1/165. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Ambas métricas son primeras; cumple también la meta propia del lenguaje, sin asterisco. El registro optimizado documentado antes #11304423 era 0.109 s / 364 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1082_constructive_optimized.java`: 0.078 s / 336 KB; base didáctica conservada `1082_constructive.java`: 0.093 s / 1592 KB.

La versión de Python imprime la misma secuencia ordenada en bloques de hasta 128 números para limitar el tamaño de cada cadena temporal.

### Mejora medida

Cada versión optimizada obtuvo Accepted y satisface el criterio de clasificación o reduce al menos un 30% el tiempo o la memoria frente a la versión básica. Se conservan los fuentes básicos. El asterisco solo se refiere al objetivo de clasificación.

- `1082_constructive_optimized.py` usa 440 KB frente a los 452 KB de la versión básica y tarda 0.078 s en lugar de 0.062 s. En la clasificación del 16 de noviembre de 2026 para los intérpretes vigentes de Python/PyPy ocupa el puesto 4 por tiempo y el 12 por memoria, de 45. Está entre el 30% superior en ambas métricas y mejora el puesto 15 de la versión básica en memoria.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1082_constructive.cpp](1082_constructive.cpp).

- Todos los lenguajes imprimen `1 … N` separados por espacios.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1082_constructive.cpp](1082_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 128 KB | 11279016 |
| [1082_constructive.go](1082_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 1116 KB | 11279017 |
| [1082_constructive.java](1082_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.093 s | 1592 KB | 11279019 |
| [1082_constructive.py](1082_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.062 s | 452 KB | 11279018 |
| [1082_constructive.rs](1082_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 252 KB | 11279020 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1082_constructive_optimized.java](1082_constructive_optimized.java) | Java 1.8 | constructive | O(N log N) time; O(1) auxiliary space | AC | 0.078 s | 336 KB | 11327337 |
| [1082_constructive_optimized.py](1082_constructive_optimized.py) \* | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 440 KB | 11307455 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
