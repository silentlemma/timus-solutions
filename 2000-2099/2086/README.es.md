# 2086. Un triángulo colocado por un punto de uno de sus lados

[Timus 2086](https://acm.timus.ru/problem.aspx?space=1&num=2086) · dificultad 4667 · geometry, math

Problema original de Dmitry Ivankov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan los puntos V (Vanya) y E (Eugene). El lugar de Denis D está a
distancia X de V, una sala desconocida F está a distancia Y de V y a
distancia Z de D, y E está en el segmento DF. Las tres longitudes forman
un triángulo propio. Imprimir todas las posiciones posibles de D. Los
límites son 2 segundos y 256 MB.

## Entrada

X, Y, Z (de 1 a 10⁴, |X − Y| < Z < X + Y) y después las coordenadas
enteras de V y de E (hasta 10⁴ en valor absoluto), V ≠ E.

## Salida

El número de posiciones y después las posiciones con error absoluto o
relativo de a lo sumo 10⁻⁶, en cualquier orden.

## Evaluación

Un comprobador compara el número de puntos y empareja los puntos en
cualquier orden con el error permitido.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3 3
0 0
2 2
```

Salida:

```
4
2.968700210890 -0.432225702453
-0.432225702453 2.968700210890
2.354856947625 1.858668543938
1.858668543938 2.354856947625
```

### Ejemplo 2

Entrada:

```
1 1 1
0 0
100 500
```

Salida:

```
0
```

### Ejemplo 3

Entrada:

```
28 46 20
28 10
5 -6
```

Salida:

```
2
5.007867947356 -5.980045796986
5.021444895601 -5.999562660088
```

## Solución

El triángulo VDF queda fijado por sus lados salvo un movimiento. Un
punto a la fracción t del camino de D a F está, por el teorema de
Stewart, a distancia al cuadrado (1 − t) X² + t Y² − t (1 − t) Z² de V.
E debe ser un punto así con t ∈ [0, 1], y su distancia al cuadrado d² a
V es entera, así que t resuelve Z² t² + (Y² − X² − Z²) t + (X² − d²) = 0
con coeficientes enteros. El discriminante y las comparaciones de las
raíces con 0 y 1 se hacen de forma exacta en enteros de 64 bits
(comparando ±√disc con un entero al elevar al cuadrado), así que el
número de respuestas nunca depende del redondeo. Una raíz doble cuenta
una vez.

Para cada t válido se construye un triángulo modelo con V en el origen,
D en el eje x y F encima; el punto P a la fracción t cumple |P| = d. Un
giro que lleva P a E − V coloca el modelo, y lo mismo hace ese giro tras
reflejar el modelo en el eje x, así que cada t da dos posiciones
especulares de D. Solo coinciden cuando t = 0, es decir, cuando E es el
propio D (entonces d = X); en t = 1, E es la sala y cuentan ambas
imágenes. Todo es O(1).

En el primer ejemplo las dos raíces t están dentro de [0, 1] y dan
cuatro posiciones simétricas respecto de la recta por V y E.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2086_geometry_math.cpp](2086_geometry_math.cpp) | G++ 13.2 x64 | geometry, math | O(1) | AC | 0.031 s | 216 KB |
| [2086_geometry_math.go](2086_geometry_math.go) | Go 1.14 x64 | geometry, math | O(1) | AC | 0.031 s | 1112 KB |
| [2086_geometry_math.java](2086_geometry_math.java) | Java 1.8 | geometry, math | O(1) | AC | 0.140 s | 1880 KB |
| [2086_geometry_math.py](2086_geometry_math.py) | Python 3.12 x64 | geometry, math | O(1) | AC | 0.109 s | 768 KB |
| [2086_geometry_math.rs](2086_geometry_math.rs) | Rust 1.75 x64 | geometry, math | O(1) | AC | 0.062 s | 280 KB |
