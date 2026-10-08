# 1019. El intervalo blanco más largo tras repintar una recta

[Timus 1019](https://acm.timus.ru/problem.aspx?space=1&num=1019) · dificultad 464 · sorting, dsu

Problema original del Ural State University Internal Contest '99 #2.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El segmento `[0, 10^9]` de la recta numérica es blanco. Luego se aplican en
orden `N` repintados (`1 ≤ N ≤ 5000`): el `i`-ésimo pinta el segmento de
`a_i` a `b_i` (`0 < a_i < b_i < 10^9`, enteros) de blanco o de negro.
Encuentra el intervalo blanco más largo del resultado; entre intervalos de
igual longitud, el de más a la izquierda.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas `a b c`, donde `c` es `w` (blanco) o `b` (negro).

## Salida

Los extremos `x y` (`x < y`) del intervalo blanco más largo.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
2 999999998 b
100 500 w
500 900 w
300 310 b
```

Salida:

```
310 900
```

### Ejemplo 2

Entrada:

```
1
1 999999999 w
```

Salida:

```
0 1000000000
```

## Solución

**Compresión de coordenadas.** Solo importan los puntos `0`, `10^9` y todos
los `a_i`, `b_i`: entre dos puntos vecinos de este conjunto ordenado el color
no cambia. Cortan la recta en como mucho `2N + 1` trozos `[x_k, x_{k+1})`, y
repintar `[a, b]` cubre exactamente los trozos desde el índice de `a` hasta
el índice de `b`, sin incluir este último.

**Pintar.** Se aplican los repintados a los trozos en orden: como mucho
`5000 · 10 001 = 5 · 10^7` asignaciones simples, bien para lenguajes
compilados.

**Pintar hacia atrás con DSU.** El color de un trozo es el del último
repintado que lo cubre. Se recorren los repintados desde el último y solo se
pintan los trozos aún sin pintar; un arreglo de punteros «siguiente trozo
sin pintar» con compresión de caminos (un DSU sobre la recta) salta los ya
pintados. Cada trozo se pinta como mucho una vez: `O((N + M) α)` tras
ordenar, donde `M` es el número de trozos. Los trozos a los que no llega
ningún repintado quedan blancos.

**La respuesta.** Se recorren los trozos de izquierda a derecha uniendo los
blancos vecinos en tramos; un tramo `[x_i, x_j)` mide `x_j - x_i`. El mejor
tramo se actualiza solo con una longitud estrictamente mayor, lo que deja el
de más a la izquierda entre los iguales. Siempre hay un tramo blanco: el
trozo `[0, min a)` nunca se repinta.

Detalles a tener en cuenta:

- segmentos blancos que se tocan, como `[10, 20]` y `[20, 30]`, forman un
  solo intervalo;
- un segmento negro dentro de uno blanco lo parte;
- los extremos `0` y `10^9` pertenecen a la recta aunque ningún repintado
  los mencione.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: compresión y pintado directo.
- **C++** y **Python** también pintan hacia atrás con el DSU, lo que mantiene
  lineal la versión en Python.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1019_dsu_sorting.cpp](1019_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(N log N) | AC | 0.015 s | 212 KB |
| [1019_dsu_sorting.py](1019_dsu_sorting.py) | Python 3.12 x64 | dsu, sorting | O(N log N) | AC | 0.078 s | 3560 KB |
| [1019_sorting.cpp](1019_sorting.cpp) | G++ 13.2 x64 | sorting | O(N^2) after sorting | AC | 0.031 s | 208 KB |
| [1019_sorting.go](1019_sorting.go) | Go 1.14 x64 | sorting | O(N^2) after sorting | AC | 0.031 s | 1784 KB |
| [1019_sorting.java](1019_sorting.java) | Java 1.8 | sorting | O(N^2) after sorting | AC | 0.203 s | 3960 KB |
| [1019_sorting.rs](1019_sorting.rs) | Rust 1.75 x64 | sorting | O(N^2) after sorting | AC | 0.046 s | 692 KB |
