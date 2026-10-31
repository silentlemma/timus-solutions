# 1821. Biatlón

[Timus 1821](https://acm.timus.ru/problem.aspx?space=1&num=1821) · dificultad 178 · sorting

Problema original de Alexander Ipatov y Alexey Samsonov, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En una carrera con salida individual los esquiadores salen uno a uno,
con 30 segundos de intervalo. Un marcador muestra al esquiador con el
mejor tiempo entre los que ya han llegado. Dados los esquiadores en
orden de salida con sus tiempos de carrera, listar a todos los que
aparecieron en el marcador.

## Entrada

n (1 ≤ n ≤ 100), luego n líneas: un apellido no vacío (hasta 20 letras
inglesas, la primera mayúscula y las demás minúsculas) y un tiempo
"mm:ss.d". Todos los apellidos son distintos. Nadie llega a la vez que
otro y no hay dos tiempos iguales.

## Salida

El número de esquiadores que lideraban al llegar, y luego sus
apellidos en orden lexicográfico, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
Zaitseva 21:38.2
Hauswald 21:21.0
Boulygina 22:04.4
Henkel 22:06.1
Wilhelm 21:11.1
Jonsson 22:05.8
```

Salida:

```
3
Hauswald
Wilhelm
Zaitseva
```

## Solución

Se trabaja en décimas de segundo. El esquiador i (desde 0) sale en
300·i y llega en 300·i más su tiempo. Se ordenan los esquiadores por
momento de llegada y se reproduce la carrera: uno entra en el marcador
cuando su tiempo mejora todos los ya registrados. Se ordenan los
apellidos reunidos y se imprimen. `O(n log n)`.

En el ejemplo las llegadas van en el orden Zaitseva (12982), Hauswald
(13110), Boulygina (13844), Wilhelm (13911), Henkel (14161), Jonsson
(14758) en décimas; el mejor tiempo baja con Zaitseva, Hauswald y
Wilhelm.

Trampas:

- el orden de llegada no es el de salida, así que se ordena por el
  momento de llegada, no por el tiempo de carrera;
- el marcador muestra el mejor tiempo hasta el momento, no al primero
  en llegar;
- al comparar las llegadas se suma el desfase de salida: en la prueba
  06, Late llega en 6000 décimas y Early en 6601, por lo que solo Late
  lidera;
- la respuesta va ordenada por apellido, no en el orden en que cambió
  el marcador.

## Soluciones optimizadas

La solución optimizada en C++ lee cada esquiador con un solo `scanf` que
además parte el tiempo en `:` y `.`, en lugar de `iostream` y subcadenas
convertidas con `stoi`, y guarda a los esquiadores en un arreglo
estático de 100 registros con un nombre de 21 bytes, suficiente porque
`n ≤ 100` y un apellido tiene como mucho 20 letras, en lugar de un
vector de tuplas con `std::string`. El marcador guarda punteros a los
nombres, ordenados con `strcmp`: {1821_sorting_optimized.cpp}.

La solución optimizada en Java lee las líneas con `BufferedReader` y
`StringTokenizer`, que además parte el tiempo en `:` y `.`, en lugar de
`Scanner` y subcadenas, y ordena un arreglo de registros que implementan
`Comparable` en lugar de índices `Integer` empaquetados con un
comparador lambda: {1821_sorting_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1821_sorting_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +73.21%; base: `1821_sorting.cpp`.

- `1821_sorting_optimized.java`: reducción de tiempo +30.13%; reducción
  de memoria +83.13%; base: `1821_sorting.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1821_sorting.go](1821_sorting.go).
- [1821_sorting.rs](1821_sorting.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1821_sorting.cpp](1821_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 448 KB | 11304255 |
| [1821_sorting.go](1821_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.031 s | 1136 KB | 11290261 |
| [1821_sorting.java](1821_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.156 s | 3936 KB | 11290273 |
| [1821_sorting.py](1821_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.093 s | 460 KB | 11290266 |
| [1821_sorting.rs](1821_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 228 KB | 11290275 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1821_sorting_optimized.cpp](1821_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 120 KB | 11307289 |
| [1821_sorting_optimized.java](1821_sorting_optimized.java) | Java 1.8 | sorting | O(n log n) | AC | 0.109 s | 664 KB | 11307294 |
