# 1426. Rectángulos

[Timus 1426](https://acm.timus.ru/problem.aspx?space=1&num=1426) · dificultad 5158 · geometry

Problema original de Nikita Rybak, Dmitry Kovalioff e Ilya Grebnov, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada uno de N cuadros (N ≤ 10 000) se dan cuatro puntos con
coordenadas enteras de −5000 a 5000; algunos pueden coincidir. Hay que
dibujar un rectángulo, girado de cualquier forma, sin vértices iguales,
dentro del cuadrado de −10 000 a 10 000, de modo que cada uno de los
cuatro puntos esté en uno de sus lados. Se imprime «+» y los vértices
en orden alrededor del rectángulo con al menos seis cifras tras el
punto, o «-» si no existe; vale cualquier rectángulo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas de ocho números: los cuatro puntos.

## Salida

Una línea por cuadro.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1 0 0 1 3 2 1 2
0 1 0 -1 1 0 -1 0
```

Salida:

```
+ 0.000000 0.000000 0.000000 2.000000 3.1234567890 2.000000 3.1234567890 0.000000
+ 0.000000 -1.000000 1.000000 0.000000 0.000000 1.000000 -1.000000 0.000000
```

## Solución

Se fija una dirección para los lados. Los cuatro puntos deben estar en
el rectángulo, y un punto solo puede estar en un lado que toque el
conjunto, así que basta mirar la caja envolvente en esa dirección:
sirve justo cuando cada punto es extremo en una de las dos coordenadas
giradas. Si todos los puntos comparten una coordenada la caja es plana,
y se le da anchura 1 hacia un lado, lo que mantiene todos los puntos en
un lado.

Al girar la dirección, el conjunto de direcciones buenas es cerrado, y
cada extremo suyo es un momento en que dos puntos empatan en una
coordenada girada, es decir, cuando los lados son paralelos o
perpendiculares al segmento entre ellos. Así que basta probar las como
mucho seis direcciones de un punto a otro (una dirección vale también
por su perpendicular). Tomando la propia dirección (dx, dy) como marco,
las coordenadas giradas x·dx + y·dy e y·dx − x·dy son enteras y la
prueba es exacta; solo los vértices se calculan en coma flotante. Si
todos los puntos coinciden, sirve un cuadrado pequeño con esa esquina.

La caja de puntos dentro de ±5000 nunca sale de ±10 000: los puntos
están en un disco de radio 5000·√2, y cualquier cuadrado alrededor de
ese disco tiene sus vértices a no más de 10 000 del centro. `O(N)`.

Detalles a tener en cuenta:

- un punto dentro del triángulo de los otros nunca puede estar en un
  lado (pruebas 03, 06);
- los puntos alineados o repetidos necesitan un rectángulo de anchura
  positiva (pruebas 02, 04, 07);
- la caja puede llegar justo al borde del lienzo (prueba 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1426_geometry.cpp](1426_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.125 s | 1980 KB |
| [1426_geometry.go](1426_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.109 s | 5888 KB |
| [1426_geometry.java](1426_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.312 s | 10072 KB |
| [1426_geometry.py](1426_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.390 s | 11424 KB |
| [1426_geometry.rs](1426_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.046 s | 2276 KB |
