# 1599. Número de vueltas

[Timus 1599](https://acm.timus.ru/problem.aspx?space=1&num=1599) · dificultad 1843 · geometry

Problema original de Vladimir Yakovlev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un ferrocarril cerrado pasa por n uniones (3 ≤ n ≤ 5000) siguiendo vías
rectas, que pueden cruzarse y solaparse. Para cada uno de m puntos de
observación (m ≤ 5000) hay que imprimir `EDGE` si el punto está sobre una
vía y, si no, cuántas vueltas completas en sentido antihorario da quien
sigue al tren durante una vuelta: su número de vueltas. Las coordenadas
son enteros de valor absoluto hasta 10⁹.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y las uniones, luego m y los puntos de observación.

## Salida

`EDGE` o el número de vueltas para cada punto.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
-2 -2
-5 1
-2 4
1 3
-2 0
-3 1
-2 2
1 1
3
-2 1
0 0
1 2
```

Salida:

```
-2
EDGE
0
```

## Solución

Se mira a lo largo del rayo que sale del punto hacia la derecha. Cada vez
que el tren lo cruza hacia arriba pasa junto al punto en sentido
antihorario, y hacia abajo en sentido horario. Así que el número de
vueltas es el número de vías que cruzan el rayo hacia arriba menos las
que lo cruzan hacia abajo. Una vía de a a b lo cruza hacia arriba cuando
a.y ≤ p.y < b.y y el punto queda a su izquierda, es decir,
cross(b − a, p − a) > 0, y hacia abajo cuando b.y ≤ p.y < a.y y el punto
queda a su derecha. Contar el extremo inferior de cada vía pero no el
superior hace que un rayo que pasa por una unión la cuente exactamente
una vez, y las vías horizontales no cuentan nunca.

Un punto está sobre una vía cuando el producto vectorial es 0 y el punto
está dentro del rectángulo que la contiene. Se comprueba cada vía para
cada punto: `O(n·m)`, 2,5·10⁷ pasos solo con enteros.

Los resultados se contrastaron con sumar los ángulos de giro con atan2
en recorridos pequeños, incluidos recorridos que pasan por las filas de
los puntos y recorridos de ida y vuelta.

Detalles a tener en cuenta:

- el producto vectorial llega a 2·(2·10⁹)² = 8·10¹⁸, todavía por debajo
  de 2⁶³, así que bastan enteros de 64 bits, pero sin margen;
- un rayo que pasa por una unión o a lo largo de una vía horizontal no
  debe contar dos veces ni ninguna, y la prueba semiabierta
  a.y ≤ p.y < b.y lo resuelve;
- el recorrido puede volver sobre sí mismo, y puede haber vías de
  longitud cero: solo importan para `EDGE`.

## Notas por lenguaje

- Python se ejecuta con PyPy: 5000 puntos contra 5000 vías tardan unos
  5,5 s con CPython y unos 0,4 s con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1599_geometry.cpp](1599_geometry.cpp) | G++ 13.2 x64 | geometry | O(n·m) | AC | 0.250 s | 228 KB |
| [1599_geometry.go](1599_geometry.go) | Go 1.14 x64 | geometry | O(n·m) | AC | 0.515 s | 1572 KB |
| [1599_geometry.java](1599_geometry.java) | Java 1.8 | geometry | O(n·m) | AC | 0.781 s | 936 KB |
| [1599_geometry.py](1599_geometry.py) | PyPy 3.10 x64 | geometry | O(n·m) | AC | 0.906 s | 5464 KB |
| [1599_geometry.rs](1599_geometry.rs) | Rust 1.75 x64 | geometry | O(n·m) | AC | 0.328 s | 612 KB |
