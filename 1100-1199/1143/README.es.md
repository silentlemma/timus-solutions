# 1143. El camino más corto por todos los vértices de un polígono convexo

[Timus 1143](https://acm.timus.ru/problem.aspx?space=1&num=1143) · dificultad 589 · dp

Problema original del concurso de selección del equipo de Vietnam para la IOI.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 200` campamentos están en los vértices de un polígono convexo,
dados en sentido antihorario con coordenadas reales. Halla la longitud
del camino más corto que empieza en cualquier campamento y visita todos,
impresa con tres cifras decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas con las coordenadas de los vértices.

## Salida

La longitud del camino más corto, con tres decimales.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
50.0 1.0
5.0 1.0
0.0 0.0
45.0 0.0
```

Salida:

```
50.211
```

## Solución

Un camino más corto nunca se cruza a sí mismo: si dos de sus tramos se
cruzan, invertir la parte entre ellos los sustituye por dos tramos que
juntos son más cortos, por la desigualdad triangular. Con puntos en
posición convexa esto tiene una consecuencia fuerte: en todo momento los
vértices visitados forman un arco del polígono, y el camino está en un
extremo de ese arco. Si no, el camino tendría que saltar por encima del
arco al otro lado, y un tramo posterior cruzaría uno anterior.

Así que el estado es un arco `(i, length)` y el extremo donde está el
camino. Un arco crece un vértice por cualquier lado, desde cualquier
extremo, lo que da cuatro transiciones. Sean `at[i]` y `at_end[i]` los
caminos más cortos por el arco que empieza en el vértice `i`, situados en
su primer o en su último vértice. Se empieza con todos los arcos de
longitud 1 a coste 0, se hacen crecer hasta longitud `N` y se toma el
menor valor. `O(N²)` en tiempo, `O(N)` de memoria por longitud.

Detalles a tener en cuenta:

- dar la vuelta al polígono no siempre es lo mejor: en un polígono largo
  y estrecho el camino va en zigzag entre los dos lados largos;
- `N = 1` da `0.000`;
- los arcos pasan por el final de la lista de vértices, así que los
  índices se toman módulo `N`;
- la respuesta se imprime con exactamente tres decimales.

Las respuestas se compararon con la búsqueda de Held–Karp sobre todos los
subconjuntos, que no usa la convexidad, en 120 polígonos aleatorios de
hasta 11 vértices, entre ellos elipses estrechas y vértices amontonados
en un arco corto.

## Notas por lenguaje

- Todos los lenguajes hacen la misma programación dinámica por arcos con
  dos arrays por longitud.
- Java formatea la respuesta con `Locale.US` para que el separador
  decimal sea un punto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1143_dp.cpp](1143_dp.cpp) | G++ 13.2 x64 | dp | O(N²) | AC | 0.015 s | 240 KB |
| [1143_dp.go](1143_dp.go) | Go 1.14 x64 | dp | O(N²) | AC | 0.031 s | 1864 KB |
| [1143_dp.java](1143_dp.java) | Java 1.8 | dp | O(N²) | AC | 0.203 s | 1836 KB |
| [1143_dp.py](1143_dp.py) | Python 3.12 x64 | dp | O(N²) | AC | 0.156 s | 2244 KB |
| [1143_dp.rs](1143_dp.rs) | Rust 1.75 x64 | dp | O(N²) | AC | 0.046 s | 272 KB |
