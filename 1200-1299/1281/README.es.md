# 1281. Cuenca fluvial

[Timus 1281](https://acm.timus.ru/problem.aspx?space=1&num=1281) · dificultad 1771 · geometry

Problema original de Sergey Volchenkov, Vladimir Pinaev y Michael Kopachev, del cuarto de final de la región central de Rusia del ACM ICPC 2003–2004, Rybinsk, 15–16 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un mapa muestra N ≤ 10 ríos como poligonales, cada uno de la fuente a
la desembocadura, con 1000 puntos como mucho en total. Un río cuya
desembocadura está en un vértice interior de otro río es afluente de
este. La cuenca de un río es el menor polígono convexo que contiene el
río, sus afluentes, los afluentes de estos, etc. Hay que imprimir la
mayor área de cuenca con dos cifras tras el punto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego, para cada río, el número de puntos y los puntos, que pueden
ser fraccionarios.

## Salida

La mayor área de cuenca.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
4
6 9
5 11
3 12
1 7
3
7 9
5 7
5 5.5
6
3 10
5 8
4 6
5 5.5
6 5
3 5
```

Salida:

```
16.00
```

### Ejemplo 2

Entrada:

```
2
4
6 9
5 11
3 12
1 7
6
3 10
5 8
4 6
5 5.5
6 5
3 5
```

Salida:

```
12.00
```

## Solución

Los afluentes se hallan buscando el último punto de cada río entre los
vértices interiores de todos los ríos. La cuenca de un río contiene sus
propios puntos y, recursivamente, los de sus afluentes, y su área es la
de su envolvente convexa: la cadena monótona da la envolvente y la
fórmula del cordón su área. Los ríos forman un bosque, así que la
recursión termina. P es el número total de puntos.

Detalles a tener en cuenta:

- los afluentes pueden tener afluentes, y todos pertenecen a la cuenca
  (prueba 05);
- un río recto tiene área cero (prueba 03);
- las desembocaduras se emparejan con vértices interiores mediante claves exactas de las coordenadas leídas;
- un área puede acabar justo en la mitad de la última cifra impresa y
  redondearse hacia cualquier lado, así que estas pruebas comparan con
  una tolerancia de 0,01.

Las respuestas se compararon con una implementación independiente en 90
mapas generados; solo diferían en esas mitades, por 0,01.

## Notas por lenguaje

- Todos usan doubles; las claves de coordenadas de Java y Rust distinguen `-0.0` de `0.0`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1281_geometry.cpp](1281_geometry.cpp) | G++ 13.2 x64 | geometry | O(N · P log P) | AC | 0.015 s | 388 KB |
| [1281_geometry.go](1281_geometry.go) | Go 1.14 x64 | geometry | O(N · P · (N + log P)) | AC | 0.031 s | 1836 KB |
| [1281_geometry.java](1281_geometry.java) | Java 1.8 | geometry | O(N · P log P) | AC | 0.203 s | 4484 KB |
| [1281_geometry.py](1281_geometry.py) | Python 3.12 x64 | geometry | O(N · P · (N + log P)) | AC | 0.093 s | 1044 KB |
| [1281_geometry.rs](1281_geometry.rs) | Rust 1.75 x64 | geometry | O(N · P log P) | AC | 0.046 s | 560 KB |
