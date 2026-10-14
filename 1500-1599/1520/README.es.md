# 1520. El Imperio contraataca

[Timus 1520](https://acm.timus.ru/problem.aspx?space=1&num=1520) · dificultad 2430 · geometry

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una república es el disco de radio R (1 ≤ R ≤ 1000) centrado en el
origen, con N fábricas (1 ≤ N ≤ 300) en puntos enteros dentro de él.
Sobre cada fábrica cae una bomba de un radio común. Hay que hallar el
menor radio con el que las bombas cubren juntas todo el disco, con al
menos cinco cifras decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y R, y luego las coordenadas de las N fábricas.

## Salida

El menor radio.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
0 2
0 -2
2 0
-2 0
```

Salida:

```
2.94725152
```

## Solución

La respuesta es la mayor distancia de un punto del disco a su fábrica
más cercana. Los puntos más cercanos a la fábrica i forman su celda de
Voronoi, un polígono convexo; se recorta un cuadrado alrededor del
disco con las mediatrices con las demás fábricas, de la más cercana a
la más lejana, y se para cuando la siguiente está a más del doble del
alcance de la celda, porque ninguna mediatriz más lejana la corta. La
distancia a la fábrica es una función convexa, así que en la parte de
la celda dentro del disco alcanza su máximo en un vértice de la celda
dentro del disco, en un punto donde un lado de la celda cruza la
circunferencia, o en algún arco de la circunferencia dentro de la
celda, donde el máximo está en el punto opuesto a la fábrica si ese
punto está en la celda. Se toma el mayor de todos estos candidatos en
todas las celdas. Unos `O(N²)` pasos de recorte con celdas pequeñas.

Detalles a tener en cuenta:

- el punto más lejano suele estar en el borde, donde una mediatriz
  corta la circunferencia (prueba 01, prueba 04);
- un arco del borde puede tener el punto más lejano en su interior, en
  el punto opuesto a la fábrica (pruebas 02, 03);
- las fábricas pueden repetirse, y dos puntos iguales no tienen
  mediatriz, así que se omiten (prueba 05, gen5);
- una sola fábrica da R más su distancia al centro (pruebas 02, 03,
  gen3).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1520_geometry.cpp](1520_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2) | AC | 0.031 s | 248 KB |
| [1520_geometry.go](1520_geometry.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.062 s | 6044 KB |
| [1520_geometry.java](1520_geometry.java) | Java 1.8 | geometry | O(N^2) | AC | 0.203 s | 6652 KB |
| [1520_geometry.py](1520_geometry.py) | Python 3.12 x64 | geometry | O(N^2) | AC | 0.375 s | 888 KB |
| [1520_geometry.rs](1520_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2) | AC | 0.046 s | 296 KB |
