# 1460. Cables

[Timus 1460](https://acm.timus.ru/problem.aspx?space=1&num=1460) · dificultad 3931 · geometry

Problema original de Dmitry Ivankov, del concurso de la Universidad Estatal de los Urales en el campus de invierno de Petrozavodsk, enero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuatro terminales de una placa, con coordenadas enteras de −200 a 200,
deben quedar conectados con tramos rectos de cable; se pueden añadir
hasta tres terminales auxiliares en cualquier sitio. Para cada uno de N
conjuntos (1 ≤ N ≤ 100) hay que hallar la menor longitud total de
cable, con al menos cuatro cifras tras el punto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego N conjuntos de cuatro puntos, opcionalmente separados por líneas vacías.

## Salida

La menor longitud de cada conjunto, una por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 0
2 0
2 1
3 0

0 0
0 1
1 0
1 1
```

Salida:

```
3.9093
2.7321
```

## Solución

Es el árbol de Steiner euclídeo de cuatro puntos. En un árbol óptimo
cada punto auxiliar une exactamente tres cables a 120°, así que hay como
mucho dos puntos auxiliares, y todo árbol óptimo tiene una de tres
formas completas, posiblemente degenerada: los terminales {a, b} cuelgan
de un punto auxiliar, {c, d} del otro, y los dos puntos
auxiliares están unidos. Para una forma así, la construcción de Melzak
da los puntos auxiliares: se sustituyen a y b por el vértice e de un
triángulo equilátero sobre ab; el segundo punto es entonces el punto de
Fermat de e, c y d, y el primero el punto de Fermat de a, b y el segundo
(puntos de Fermat como en el problema 1451). Se prueban los dos lados de
ab para el vértice y los dos sentidos de cada emparejamiento.

Cuando la forma no encaja de verdad, la construcción puede dar puntos
extraños, así que siempre se cuenta la longitud real del árbol
construido con ellos, nunca la fórmula |e e'|; así cada candidato es un
árbol de verdad y ninguno queda por debajo del óptimo. Las formas
degeneradas se añaden directamente: el árbol generador mínimo, y un
punto auxiliar en el punto de Fermat de tres terminales con el cuarto
unido al más cercano de los cuatro puntos. La respuesta es el menor
candidato. `O(1)` por conjunto.

Detalles a tener en cuenta:

- el árbol óptimo puede no tener puntos auxiliares (terminales en una
  recta), tener uno o dos (pruebas 01, 02);
- un cuadrado necesita dos puntos auxiliares, no sus diagonales
  (ejemplo 1, caso 2);
- una construcción que no se aplica nunca debe dar una longitud menor
  que el óptimo real, por eso se miden longitudes reales de árboles.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1460_geometry.cpp](1460_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) per set | AC | 0.015 s | 220 KB |
| [1460_geometry.go](1460_geometry.go) | Go 1.14 x64 | geometry | O(1) per set | AC | 0.031 s | 1184 KB |
| [1460_geometry.java](1460_geometry.java) | Java 1.8 | geometry | O(1) per set | AC | 0.218 s | 5264 KB |
| [1460_geometry.py](1460_geometry.py) | Python 3.12 x64 | geometry | O(1) per set | AC | 0.109 s | 1200 KB |
| [1460_geometry.rs](1460_geometry.rs) | Rust 1.75 x64 | geometry | O(1) per set | AC | 0.015 s | 284 KB |
