# 1151. Localizar radiobalizas a partir de distancias en la métrica del máximo

[Timus 1151](https://acm.timus.ru/problem.aspx?space=1&num=1151) · dificultad 1041 · geometry

Problema original del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda en inglés.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay como mucho 10 radiobalizas en puntos enteros con coordenadas de 1 a
200. Desde `M ≤ 20` puntos de control de coordenadas conocidas se
midieron distancias a algunas balizas, donde la distancia entre `A` y `B`
es `max(|Ax − Bx|, |Ay − By|)`. Para cada baliza, en orden creciente de
identificador, imprime su posición si exactamente un punto del campo
cumple todas sus medidas, y `UNKNOWN` en otro caso. Las medidas son
coherentes.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`M` y luego `M` líneas de la forma `X,Y:ID-R,ID-R,…`: un punto de control
y luego identificadores de balizas con sus distancias.

## Salida

Una línea por baliza: `ID:x,y` o `ID:UNKNOWN`.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
15,15:16-7,5-3
10,10:5-2,16-2
```

Salida:

```
5:12,12
16:UNKNOWN
```

## Solución

En la métrica del máximo, los puntos a distancia exactamente `r` de un
punto de control forman el borde de un cuadrado de lado `2r` a su
alrededor, como mucho `8r` celdas, o el propio punto cuando `r = 0`. Cada
baliza tiene al menos una medida, así que sus candidatas son las celdas
del primer cuadrado de ese tipo que caen en el campo; cada una se conserva solo
si está a la distancia correcta de todos los demás puntos que midieron
esa baliza. Si queda exactamente una candidata es la respuesta; si no, la
posición es `UNKNOWN`. Con como mucho 1600 candidatas y 20 medidas por
baliza, es muy poco trabajo.

Las líneas de entrada mezclan comas, dos puntos y signos menos; todos solo
separan números, así que una línea se lee como la lista de sus tramos de
cifras: el punto de control y luego pares de identificador y distancia.

Detalles a tener en cuenta:

- el borde del campo recorta el cuadrado, y a menudo es eso lo que hace
  única la respuesta;
- una baliza puede medirse desde varios puntos y un punto puede medir
  varias balizas;
- las balizas se imprimen en orden creciente de identificador, no en el
  orden en que aparecen;
- una distancia `0` pone la baliza en el punto de control.

Las respuestas se compararon con la comprobación de cada celda del campo
en todas las pruebas y en 80 entradas aleatorias.

## Notas por lenguaje

- Todos los lenguajes filtran los mismos cuadrados. C++, Go y Java sacan
  a mano los tramos de cifras de una línea, Python usa una expresión
  regular y Rust corta la línea en cada carácter que no es cifra.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1151_geometry.cpp](1151_geometry.cpp) | G++ 13.2 x64 | geometry | O(M·R) | AC | 0.015 s | 428 KB |
| [1151_geometry.go](1151_geometry.go) | Go 1.14 x64 | geometry | O(M·R) | AC | 0.031 s | 1868 KB |
| [1151_geometry.java](1151_geometry.java) | Java 1.8 | geometry | O(M·R) | AC | 0.156 s | 3572 KB |
| [1151_geometry.py](1151_geometry.py) | Python 3.12 x64 | geometry | O(M·R) | AC | 0.062 s | 920 KB |
| [1151_geometry.rs](1151_geometry.rs) | Rust 1.75 x64 | geometry | O(M·R) | AC | 0.031 s | 372 KB |
