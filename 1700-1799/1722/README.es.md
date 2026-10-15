# 1722. Mirador

[Timus 1722](https://acm.timus.ru/problem.aspx?space=1&num=1722) · dificultad 1354 · geometry

Problema original de Eugene Kurpilyansky, del Concurso Regional de Programación por Equipos de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La ciudad es un disco de radio R alrededor del origen. El mirador es la
azotea de un edificio redondo de radio r_old alrededor del origen; un
edificio redondo nuevo de radio r_new está en (x, y). Ambos están
dentro de la ciudad y no se tocan. Un punto de la ciudad está oculto si
desde todo punto del mirador el segmento hasta él toca el edificio
nuevo. Hallar la parte oculta de la ciudad en porcentaje.

## Entrada

R, r_old y r_new (1 ≤ r_old < r_new < R ≤ 1000) y luego los enteros x
e y.

## Salida

La parte oculta de la ciudad en porcentaje, con al menos seis cifras
tras el punto decimal.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 1 3
-1 4
```

Salida:

```
20.9346176061
```

## Solución

Se fija un punto P. Los puntos Q para los que el segmento PQ toca el
edificio nuevo forman un conjunto convexo: el cono desde P alrededor
del edificio, cortado por el lado del edificio cercano a P. P está
oculto cuando todo el mirador está dentro, es decir, cuando P está
entre las dos tangentes comunes exteriores de los edificios, detrás del
nuevo o dentro de él. Como r_new > r_old, las tangentes se separan
detrás del edificio nuevo y la parte oculta llega al borde de la
ciudad.

Sean d la distancia entre los centros y k = (r_new − r_old)/d. Las
normales unitarias de las tangentes forman con la dirección al edificio
nuevo un ángulo de coseno −k, así que lo tocan en C + r_new·n por el
lado que mira al mirador y se alejan de él a lo largo de
C + (r_new − r_old)·n. Cada una sale de la ciudad donde |T + tD| = R,
una ecuación cuadrática en t.

El área sale de recorrer la parte oculta en sentido antihorario y sumar
áreas con signo vistas desde el centro nuevo C: el sector del edificio
entre los puntos de tangencia del lado del mirador, de anchura
2·acos k; los triángulos de C a cada tramo de tangente; y el arco del
borde, que es el triángulo de C a sus extremos más el trozo de ciudad
que corta su cuerda. Con áreas con signo la suma es correcta sea cual
sea la forma. `O(1)`.

Trampas:

- los puntos de tangencia están del lado del mirador, así que el sector
  que se suma es el de 2·acos k, no el lejano;
- la base del edificio nuevo también está oculta;
- `M_PI` no es C++ estándar y falta en el juez, así que la solución en
  C++ usa `acos(-1)`.

Las respuestas coinciden con una estimación en rejilla hecha
directamente a partir de la definición en ciudades pequeñas, y con una
implementación aceptada independiente en las diez cifras impresas en
500 casos aleatorios, incluidos edificios que tocan el borde o casi se
tocan entre sí.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1722_geometry.cpp](1722_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 452 KB |
| [1722_geometry.go](1722_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1176 KB |
| [1722_geometry.java](1722_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1836 KB |
| [1722_geometry.py](1722_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 812 KB |
| [1722_geometry.rs](1722_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 264 KB |
