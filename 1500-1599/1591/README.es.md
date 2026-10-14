# 1591. Pensamiento abstracto

[Timus 1591](https://acm.timus.ru/problem.aspx?space=1&num=1591) · dificultad 1050 · math

Problema original de Denis Musin, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n puntos (3 ≤ n ≤ 2000) a la misma distancia sobre una
circunferencia, y cada dos están unidos por una cuerda. Un triángulo
interesante lo forman tres cuerdas que se cortan dos a dos, con al menos
uno de los puntos de corte dentro del círculo y no sobre la
circunferencia. Hay que contar los triángulos interesantes.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n.

## Salida

El número de triángulos interesantes.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
5
```

Salida:

```
25
```

## Solución

Un triángulo queda fijado por el conjunto de extremos de sus cuerdas, así
que se cuenta por ese conjunto. Dos cuerdas se cortan dentro del círculo
exactamente cuando sus extremos se alternan sobre la circunferencia, lo
que solo depende del orden de los puntos.

- Tres vértices dentro: las cuerdas tienen seis extremos distintos, y de
  las formas de emparejar seis puntos solo las tres diagonales largas
  del hexágono se cortan todas entre sí; un triángulo por cada 6 puntos.
- Dos vértices dentro: dos cuerdas salen de un punto P y la tercera
  corta a ambas, así que sus extremos quedan a cada lado del par; con 5
  puntos el triángulo queda fijado por la elección de P: cinco por cada
  5 puntos.
- Un vértice dentro: los otros dos están en la circunferencia, así que
  una cuerda es un lado de un cuadrilátero y las otras dos son sus
  diagonales, que se cortan; un triángulo por lado, cuatro por cada 4
  puntos.

La respuesta es C(n, 6) + 5·C(n, 5) + 4·C(n, 4), en `O(1)`. Para
n ≤ 12 se contrastó con contar todas las ternas de cuerdas usando solo
el orden de sus extremos.

Detalles a tener en cuenta:

- en un polígono regular varias cuerdas pueden pasar por un mismo punto,
  por ejemplo las tres diagonales largas del hexágono por el centro; la
  respuesta cuenta igualmente esa terna como triángulo, igual que la
  fórmula;
- la respuesta llega a unos 9·10¹⁶, así que hacen falta enteros de 64
  bits, y C(n, k) se calcula como un producto que se divide en cada
  paso y se mantiene por debajo de C(n, k)·n.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1591_math.cpp](1591_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 128 KB |
| [1591_math.go](1591_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1124 KB |
| [1591_math.java](1591_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1584 KB |
| [1591_math.py](1591_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 432 KB |
| [1591_math.rs](1591_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 232 KB |
