# 1039. Una lista de invitados sin jefes directos

[Timus 1039](https://acm.timus.ru/problem.aspx?space=1&num=1039) · dificultad 386 · dp, trees

Problema original de Marat Bakirov, del V Campeonato por Equipos de Programación de la Universidad Estatal de los Urales, octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` empleados (`1 ≤ N ≤ 6000`) forman un árbol: todos salvo la raíz tienen
un jefe directo. Cada empleado tiene una valoración de −128 a 127. Elige un
conjunto de empleados en el que nadie esté invitado junto con su jefe
directo, con la mayor valoración total. El conjunto puede estar vacío.

Límite de tiempo: 0,5 segundos. Límite de memoria: 8 MB.

## Entrada

`N`, luego `N` líneas con las valoraciones de los empleados `1..N`, luego
líneas `L K` que indican que `K` es el jefe directo de `L`, terminadas con
la línea `0 0`.

## Salida

La mayor valoración total.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
1
1
1
1
1
1
1
1 3
2 3
6 4
7 4
4 5
3 5
0 0
```

Salida:

```
5
```

### Ejemplo 2

Entrada:

```
4
3
-5
4
2
1 2
3 2
2 4
0 0
```

Salida:

```
9
```

## Solución

La DP clásica sobre un árbol. Para cada empleado `v` se calculan dos
valores sobre el subárbol de `v`:

- `take[v]`: el mejor total si `v` está invitado: `rating[v]` más
  `skip[c]` para cada subordinado `c`;
- `skip[v]`: el mejor total si `v` no está invitado: la suma de
  `max(take[c], skip[c])` sobre los subordinados.

La respuesta es `max(take[root], skip[root])`. Una valoración negativa
nunca se impone a la suma: `skip` siempre permite dejar fuera al empleado,
así que con todas las valoraciones negativas la respuesta es `0`.

El árbol puede ser una cadena de 6000 niveles, así que las soluciones no
usan recursión: un orden en anchura desde la raíz pone a cada jefe antes
que a sus subordinados, y recorrerlo al revés termina cada subárbol antes
que su raíz, sumando los dos valores en el jefe. `O(N)`.

Detalles a tener en cuenta:

- la profundidad llega a 6000: un DFS recursivo puede desbordar la pila;
- valoraciones negativas: se puede no invitar a nadie (total 0);
- la raíz no se da explícitamente: es el empleado sin jefe.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: los hijos se guardan como listas
  enlazadas en dos arreglos (`first`, `next`), lo que encaja con el límite
  de 8 MB.
- **Python**: listas de hijos; la lista del orden crece mientras se
  recorre, lo que da el orden en anchura.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1039_dp.cpp](1039_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 296 KB |
| [1039_dp.go](1039_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1588 KB |
| [1039_dp.java](1039_dp.java) | Java 1.8 | dp | O(N) | AC | 0.093 s | 656 KB |
| [1039_dp.py](1039_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.093 s | 3120 KB |
| [1039_dp.rs](1039_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 528 KB |
