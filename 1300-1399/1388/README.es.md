# 1388. Fotografía

[Timus 1388](https://acm.timus.ru/problem.aspx?space=1&num=1388) · dificultad 13892 · geometry, strings

Problema original de Andrew Rumyantsev, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un río corre a lo largo de y = 0 con una presa en el origen, y en ambas
orillas crecen hasta 100 000 árboles con coordenadas enteras de valor
absoluto hasta 20 000. Desde la presa se hace una foto con una cámara
de casi 180 grados: la película es una recta, los árboles delante de
ella se proyectan sobre ella a través del origen, y un árbol detrás de
otro en el mismo rayo no se ve. Luego se recorta un trozo de película
con árboles de una sola orilla y se escala. Hay que hallar el mayor
número de árboles en dos fotos iguales de las dos orillas, donde iguales
significa con la misma disposición de árboles a lo largo de la foto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Líneas con las coordenadas de los árboles, terminadas con la línea 0 0.

## Salida

El mayor número de árboles en dos fotos iguales.

## Ejemplos

### Ejemplo 1

Entrada:

```
-1 1
0 1
2 1
3 1
7 2
3 -2
1 -1
0 -1
0 -5
-4 -2
-3 -1
0 0
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
0 1
1 1
2 1
-3 -1
-2 -2
-1 -3
0 0
```

Salida:

```
3
```

## Solución

Un árbol se ve a lo largo de la recta por el origen, así que solo
importa c = x / y, y los árboles con la misma c se tapan entre sí. Con
la película de frente, mirando lejos del río, la posición de un árbol en
la foto es c en ambas orillas, con el lado derecho de la foto a la
derecha. Girar la película cambia las posiciones por una transformación
proyectiva de c que conserva el orden cíclico, y escalar es una
aplicación afín de factor positivo. La dirección del río, c = ∞, nunca
queda dentro de un trozo de película.

Así, una foto es un tramo de valores consecutivos en la lista ordenada
de las c distintas de una orilla, y dos tramos coinciden justo cuando
una transformación proyectiva que conserva la orientación lleva el
primer valor de uno al primero del otro, el segundo al segundo, y así
sucesivamente. Tres puntos cualesquiera pueden llevarse a otros tres en
el mismo orden, así que los tramos de hasta tres árboles siempre
coinciden. Después, cada punto queda fijado por los tres anteriores, de
modo que la razón doble de cada cuatro puntos consecutivos debe
coincidir:

(c₃ − c₁)(c₄ − c₂) / ((c₃ − c₂)(c₄ − c₁)).

Con c = p / q los denominadores se cancelan, y cada factor es un
determinante 2 × 2 de a lo sumo 8·10⁸, así que la razón doble es una
fracción irreducible exacta de enteros de 64 bits. Se numeran las
fracciones de ambas orillas, y la respuesta es 3 más la subcadena común
más larga de las dos secuencias, hallada con un autómata de sufijos de
una de ellas; si una orilla tiene menos de cuatro direcciones, es el
menor de los recuentos, sin pasar de 3. `O(n log n)`.

Detalles a tener en cuenta:

- una imagen especular no cuenta: en el ejemplo 1 una coincidencia
  invertida daría 5 árboles, y la respuesta es 4 (la prueba 08 es el
  caso especular);
- un árbol detrás de otro en el mismo rayo no sale en la foto (prueba
  07);
- una transformación proyectiva puede llevar una dirección del tramo a
  la del río, y entonces la imagen se parte en dos (prueba generada 3);
- los tramos de hasta tres árboles siempre coinciden, y una orilla sin
  árboles da 0 (pruebas 02 a 06).

Las respuestas se compararon en 500 conjuntos pequeños aleatorios, la
mitad con una orilla que contiene una imagen proyectiva de la otra, con
una búsqueda que construye la transformación a partir de los tres
primeros puntos de cada par de tramos y extiende la coincidencia
mientras se cumple.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1388_strings.cpp](1388_strings.cpp) | G++ 13.2 x64 | strings | O(n log n) | AC | 0.078 s | 5700 KB |
| [1388_strings.go](1388_strings.go) | Go 1.14 x64 | strings | O(n log n) | AC | 0.062 s | 11080 KB |
| [1388_strings.java](1388_strings.java) | Java 1.8 | strings | O(n log n) | AC | 0.250 s | 17148 KB |
| [1388_strings.py](1388_strings.py) | Python 3.12 x64 | strings | O(n log n) | AC | 0.343 s | 27468 KB |
| [1388_strings.rs](1388_strings.rs) | Rust 1.75 x64 | strings | O(n log n) | AC | 0.031 s | 9440 KB |
