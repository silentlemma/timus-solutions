# 1058. El corte más corto que divide un polígono convexo por la mitad

[Timus 1058](https://acm.timus.ru/problem.aspx?space=1&num=1058) · dificultad 2756 · geometry

Problema original de la Academia Estatal de Aviación de Rybinsk.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un polígono convexo de `N` vértices (`4 ≤ N ≤ 50`, en sentido antihorario,
coordenadas de −100 a 100 con como mucho tres decimales) se corta con una
recta en dos partes de igual área. Halla la menor longitud posible del
corte, con un error de como mucho `10^-4`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas con las coordenadas de los vértices.

## Salida

La menor longitud de un corte que divide el área por la mitad.

## Evaluación

Los números se comparan con un error absoluto o relativo de `10^-4`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
4 0
4 3
0 3
```

Salida:

```
3.000000
```

### Ejemplo 2

Entrada:

```
4
0 -5
5 0
0 5
-5 0
```

Salida:

```
7.071068
```

## Solución

Se describe un corte por su primer extremo `P` en el borde, escrito como
una posición `u ∈ [0, N)`: `u = i + t` es el punto a una fracción `t` del
lado `i`. Por cada `P` pasa exactamente un corte que divide el área por la
mitad, y su otro extremo `Q` sale de las áreas:

- con sumas prefijas de los términos de la fórmula del área de Gauss, el
  doble del área del polígono `P, V[i+1], …, V[j]` es una expresión
  `O(1)`; crece con `j`, así que una búsqueda binaria encuentra el lado
  `j` que contiene a `Q`;
- en ese lado el área crece linealmente con la posición de `Q`, lo que da
  `Q` de forma exacta.

Así la longitud del corte `L(u)` se calcula en `O(log N)`. Al mover `u`,
`L(u)` es una función suave salvo cuando `P` o `Q` pasan por un vértice.
Los puntos de quiebre son los enteros y las parejas de los vértices (la
relación de pareja es simétrica), como mucho `2N`. En cada tramo suave las
soluciones toman 64 muestras y afinan cada mínimo local de las muestras,
también en los extremos del tramo, con una búsqueda de sección áurea; el
menor valor encontrado es la respuesta.

Es una búsqueda numérica, no una fórmula cerrada: supone que dentro de un
tramo la longitud no tiene dos mínimos más cercanos que el paso de
muestreo. Se comparó con un método completamente distinto (un barrido de
la dirección del corte, donde cada recta divisoria se halla por bisección
de su desplazamiento) en unos setenta polígonos aleatorios, regulares,
delgados y casi circulares y en unos cien polígonos aleatorios con
vértices sobre sus lados, un vértice repetido u orden horario, siempre
dentro de `10^-6`.

Detalles a tener en cuenta:

- el corte no tiene por qué pasar por un vértice ni ser perpendicular a
  un lado;
- los polígonos muy delgados tienen cortes muy cortos; importa la
  precisión relativa;
- el recorrido del borde necesita orden antihorario; las soluciones miran
  el signo del área e invierten una lista horaria en vez de fiarse del
  orden (una primera versión que se fiaba falló en el juez);
- cada corte se encuentra dos veces (desde cada extremo), lo que no
  molesta.

## Notas por lenguaje

- Todos los lenguajes hacen la misma búsqueda; los tamaños son pequeños,
  así que incluso en Python tarda unos milisegundos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1058_geometry.cpp](1058_geometry.cpp) | G++ 13.2 x64 | geometry | O(S·N log N), S = 64 samples | AC | 0.015 s | 232 KB |
| [1058_geometry.go](1058_geometry.go) | Go 1.14 x64 | geometry | O(S·N log N), S = 64 samples | AC | 0.031 s | 1140 KB |
| [1058_geometry.java](1058_geometry.java) | Java 1.8 | geometry | O(S·N log N), S = 64 samples | AC | 0.125 s | 2036 KB |
| [1058_geometry.py](1058_geometry.py) | Python 3.12 x64 | geometry | O(S·N log N), S = 64 samples | AC | 0.125 s | 976 KB |
| [1058_geometry.rs](1058_geometry.rs) | Rust 1.75 x64 | geometry | O(S·N log N), S = 64 samples | AC | 0.046 s | 276 KB |
