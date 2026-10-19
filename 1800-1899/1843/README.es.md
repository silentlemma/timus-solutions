# 1843. Cortar un paralelepípedo

[Timus 1843](https://acm.timus.ru/problem.aspx?space=1&num=1843) · dificultad 3920 · constructive

Problema original de Mikhail Rubinchik, del Ural SU Contest en la sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una caja cuyas seis caras tienen seis colores distintos se serró con
cortes paralelos a sus caras, cada uno a través de toda la caja. Cada
pieza se da en una orientación desconocida, con sus tres medidas y los
colores de sus seis caras; las caras interiores llevan un punto.
Devolver cada pieza a su sitio: decir qué caras de la pieza quedan
delante y abajo, y las coordenadas de su vértice delantero inferior
izquierdo en la caja.

## Entrada

La caja: sus medidas w, d y h (de delante atrás, de abajo arriba y de
izquierda a derecha, cada una de 1 a 1000) y seis colores de "ROYGBV"
para las caras delantera, trasera, inferior, superior, izquierda y
derecha. Luego n (1 ≤ n ≤ 1000) y las n piezas en el mismo formato, con
"." en las caras que estaban dentro. Existe una solución.

## Salida

Para cada pieza en el orden de entrada, la letra de su cara que queda
delante y la de la que queda abajo (F, B, D, U, L o R para sus propias
caras delantera, trasera, inferior, superior, izquierda y derecha), y
luego su vértice delantero inferior izquierdo. Se acepta cualquier
colocación válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2 2 ROYGBV
2
1 2 2 R.YGBV
2 2 1 YGVBO.
```

Salida:

```
F D 0 0 0
R F 1 0 0
```

## Solución

Cada corte atraviesa toda la caja, así que las piezas forman una
rejilla: los cortes dividen cada eje en tramos, y cada celda de la
rejilla es una pieza. Una pieza toca una cara de la caja exactamente
cuando su celda es la primera o la última a lo largo del eje de esa
cara.

Los tramos. Sea el eje de izquierda a derecha. Las piezas con el color
delantero y el inferior forman la arista delantera inferior a lo largo
de él, una pieza por tramo. En cada una, los colores delantero e
inferior marcan dos de sus ejes, y su medida a lo largo del tercero es
la longitud de un tramo. La pieza que además tiene el color izquierdo
da el primer tramo y la que tiene el derecho, el último (puede ser la
misma pieza si no hay cortes). Los tramos del medio pueden ir en
cualquier orden, porque intercambiar dos rodajas interiores deja el
mismo conjunto de piezas. Los otros dos ejes se tratan igual.

La colocación. Ahora cada celda pide una pieza con medidas y colores
dados: el color de la caja en las caras de la superficie y un punto en
las demás. Se escribe una pieza en sus 24 giros y la menor escritura es
su clave; una celda recibe la misma clave exactamente cuando algún giro
de la pieza encaja en ella. Se agrupan las piezas por clave, se da a
cada celda cualquier pieza de su grupo y luego se busca el giro de esa
pieza que encaja exactamente. Los giros se generan con dos cuartos de
vuelta alrededor de ejes que se cruzan, y un giro se nombra por las
caras que quedan delante y abajo. `O(24·n)` en promedio; en C++ con
`std::map`, `O(24·n + n log n)`.

En el ejemplo la arista delantera inferior solo contiene la primera
pieza, así que el eje de izquierda a derecha es un tramo de longitud 2,
igual que el vertical. De delante atrás, las piezas con los colores
inferior e izquierdo son las dos, con medidas 1 y 1, así que la caja se
cortó una vez por la mitad. La segunda pieza entra en la celda de atrás
girando su cara derecha hacia delante y la delantera hacia abajo.

Trampas:

- varias piezas pueden compartir clave, como los cubos unidad del
  interior; cualquiera de ellas encaja en cualquier celda así;
- un giro es una rotación, nunca una imagen especular, así que los 24
  giros deben salir de rotaciones;
- un eje sin cortes tiene un único tramo que toca ambas caras.

Las colocaciones pasan un verificador que gira cada pieza y confirma
que las piezas llenan la caja sin solaparse y que las caras de la
superficie tienen los colores correctos, en cajas aleatorias de hasta
1000 piezas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1843_constructive.cpp](1843_constructive.cpp) | G++ 13.2 x64 | constructive | O(24 n + n log n) | AC | 0.015 s | 560 KB |
| [1843_constructive.go](1843_constructive.go) | Go 1.14 x64 | constructive | O(24 n) | AC | 0.046 s | 5864 KB |
| [1843_constructive.java](1843_constructive.java) | Java 1.8 | constructive | O(24 n) | AC | 0.171 s | 7512 KB |
| [1843_constructive.py](1843_constructive.py) | Python 3.12 x64 | constructive | O(24 n) | AC | 0.265 s | 1676 KB |
| [1843_constructive.rs](1843_constructive.rs) | Rust 1.75 x64 | constructive | O(24 n) | AC | 0.046 s | 652 KB |
