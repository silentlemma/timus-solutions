# 1637. Juego del triángulo 2

[Timus 1637](https://acm.timus.ru/problem.aspx?space=1&num=1637) · dificultad 3281 · geometry

Problema original de Alexander Ipatov, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un mapa hay un triángulo dibujado y una ficha de cartón en otro
lugar. Cada movimiento refleja la ficha respecto de cualquier recta. Hay
que hallar el menor número de movimientos que hacen que la ficha cubra
exactamente el triángulo, o decir que no es posible.

## Entrada

Dos líneas de seis enteros: los vértices del triángulo dibujado y los
vértices actuales de la ficha, todos de valor absoluto hasta 2000. El
triángulo dibujado no es degenerado.

## Salida

El menor número de movimientos o `IMPOSSIBLE`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 0 6 3 7 0
0 0 2 3 3 0
```

Salida:

```
2
```

## Solución

La ficha debe llegar al triángulo mediante una isometría, que lleva sus
vértices a los dibujados en uno de los seis órdenes; un orden solo es
posible si coinciden las tres longitudes de los lados. Toda isometría
del plano es producto de reflexiones, y el mínimo de reflexiones depende
solo de su tipo:

- la identidad: 0;
- un giro o una traslación (conserva la orientación): 2, porque una
  sola reflexión siempre invierte la orientación;
- una reflexión: 1;
- una reflexión con deslizamiento (invierte la orientación y no tiene
  recta de puntos fijos): 3, ya que dos reflexiones nunca invierten la
  orientación.

La orientación compara los signos de los productos cruzados de los dos
triángulos. Si se invierte, la isometría es una sola reflexión
exactamente cuando una recta encaja: cada vértice que se mueve tiene con
su imagen la misma mediatriz, y cada vértice que no se mueve está sobre
ella. Las rectas a x + b y = c con a = 2(x' − x), b = 2(y' − y),
c = x'² + y'² − x² − y² se comparan multiplicando en cruz, todo en
enteros de 64 bits. La respuesta es el mínimo sobre los seis órdenes.
`O(1)`.

Detalles a tener en cuenta:

- los vértices pueden venir en cualquier orden, así que importan las
  seis correspondencias (prueba 03);
- en un triángulo isósceles, una reflexión con deslizamiento bajo una
  correspondencia es un medio giro bajo otra, y la respuesta es 2, no 3
  (prueba 07);
- triángulos congruentes de orientación distinta no se pueden hacer
  coincidir solo con giros; hace falta una reflexión más.

Las respuestas coinciden con una implementación aceptada independiente
en 240 isometrías aleatorias de la red.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1637_geometry.cpp](1637_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 192 KB |
| [1637_geometry.go](1637_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1100 KB |
| [1637_geometry.java](1637_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1644 KB |
| [1637_geometry.py](1637_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 760 KB |
| [1637_geometry.rs](1637_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 240 KB |
