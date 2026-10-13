# 1384. La cabra en el huerto 4

[Timus 1384](https://acm.timus.ru/problem.aspx?space=1&num=1384) · dificultad 4368 · geometry

Problema original de Alexander Ipatov, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un huerto es un polígono simple, no siempre convexo, con 3 ≤ N ≤ 25
vértices de coordenadas enteras entre 0 y 1000. Una cabra quedará atada
a una estaca en algún punto interior. Solo puede
tocar la cerca con la cuerda tensa. Hay que hallar la cuerda más larga de
ese tipo entre todos los lugares para la estaca, redondeada a 2 cifras
decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los N vértices en sentido antihorario.

## Salida

La longitud de la cuerda.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 0
200 0
0 200
```

Salida:

```
58.58
```

## Solución

La respuesta es el radio del mayor círculo dentro del polígono: la
mayor distancia de un punto interior a la cerca. La cerca se compone de
objetos: el interior de cada arista se representa por su recta, y cada
vértice cóncavo cuenta como objeto propio. El punto de la cerca más
cercano a un punto interior no puede ser un vértice convexo. Los puntos
a igual distancia de dos objetos forman una curva a lo largo de la cual
la distancia es lineal (dos rectas) o convexa (una recta y un vértice,
dos vértices), así que se puede elegir un máximo donde se juntan al
menos tres objetos.

Basta, pues, probar cada terna de objetos y hallar los puntos a igual
distancia de los tres:

- tres rectas: un sistema lineal n_i · p + c_i = r, con las normales
  unitarias hacia dentro;
- dos rectas y un vértice: se avanza por la bisectriz de las rectas,
  donde la distancia a ellas es lineal, y se resuelve una ecuación
  cuadrática para los puntos a la misma distancia del vértice;
- una recta y dos vértices: lo mismo sobre la mediatriz de los vértices;
- tres vértices: el centro de su circunferencia.

Cada candidato se comprueba con una prueba de punto en polígono y su
distancia mínima a todos los segmentos. Los candidatos interiores
adicionales no sobrestiman la respuesta, y entre los candidatos hay un
centro óptimo. Se revisan como máximo 28 590 candidatos en O(N) cada uno:
`O(N⁴)`.

Detalles a tener en cuenta:

- el círculo puede apoyarse solo en esquinas interiores: en una cruz de
  ancho 2 la respuesta es √2, por cuatro vértices cóncavos (prueba 03);
- en un giro en ángulo recto de un pasillo de ancho w el círculo tiene
  radio de unos 0,586·w, más de la mitad del pasillo (prueba 10);
- una ecuación cuadrática con el coeficiente principal casi nulo, o que
  solo toca el cero cuando un vértice está sobre la recta, necesita una
  forma estable de las raíces;
- los vértices en medio de un lado dan la misma recta dos veces, y el
  sistema para ellas es singular (prueba 12).

Las respuestas se compararon en 150 polígonos aleatorios, hechos con
puntos aleatorios deshaciendo cruces o en forma de estrella, con una
búsqueda en rejilla refinada por ascenso local. Las pruebas se juzgan
como números con una tolerancia de 0,011.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1384_geometry.cpp](1384_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^4) | AC | 0.031 s | 476 KB |
| [1384_geometry.go](1384_geometry.go) | Go 1.14 x64 | geometry | O(N^4) | AC | 0.031 s | 1780 KB |
| [1384_geometry.java](1384_geometry.java) | Java 1.8 | geometry | O(N^4) | AC | 0.187 s | 1488 KB |
| [1384_geometry.py](1384_geometry.py) | Python 3.12 x64 | geometry | O(N^4) | AC | 0.437 s | 2184 KB |
| [1384_geometry.rs](1384_geometry.rs) | Rust 1.75 x64 | geometry | O(N^4) | AC | 0.031 s | 532 KB |
