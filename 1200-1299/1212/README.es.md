# 1212. Sitios para un barco más en la batalla naval

[Timus 1212](https://acm.timus.ru/problem.aspx?space=1&num=1212) · dificultad 493 · geometry

Problema original de Anton Botov y Anatoly Uglov, del USU Open Collegiate Programming Contest, octubre de 2002, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tablero de batalla naval tiene `N` filas y `M` columnas, ambas hasta
30000, y en él ya hay hasta 30 barcos de una a cuatro casillas. Los
barcos no pueden tocarse, ni siquiera por una esquina. Hay que contar las
formas de colocar un barco más de `K` casillas, en horizontal o en
vertical.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`, `M` y el número de barcos `L`; luego cada barco como la columna y
la fila de su casilla superior izquierda, su longitud y `V` o `H`; y
luego `K`.

## Salida

El número de sitios para el barco nuevo.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4 2
1 2 2 V
3 1 2 H
2
```

Salida:

```
4
```

## Solución

Cada barco colocado prohíbe el rectángulo que lo rodea, una casilla más
ancho por cada lado. Primero se cuentan los sitios horizontales. Las
filas se parten en franjas en el borde superior y justo debajo del borde
inferior de cada rectángulo prohibido; dentro de una franja cada fila
corta los mismos rectángulos, así que todas sus filas cuentan lo mismo.
Para una fila de la franja se toman en orden los tramos de columnas
prohibidos y se suma `max(0, longitud − K + 1)` por cada tramo libre
entre ellos; se multiplica por la altura de la franja. Los sitios
verticales son la misma cuenta con el tablero girado. Un barco de una
casilla es igual en ambos sentidos, así que entonces se cuenta una sola
vez. Con como mucho 61 franjas, `O(L² log L)`.

Detalles a tener en cuenta:

- el primer número de un barco es su columna y el segundo su fila;
- un barco de una casilla no debe contarse dos veces;
- los rectángulos prohibidos sobresalen de los bordes del tablero y hay
  que recortarlos al cortar las franjas;
- la respuesta puede llegar a unos `1.8·10⁹`, más de 32 bits.

Las respuestas se compararon con una fuerza bruta casilla a casilla en
450 tableros pequeños aleatorios, y con una solución escrita aparte en
todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes dan campos con nombre a los rectángulos prohibidos
  y reutilizan la misma función de conteo para ambos sentidos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1212_geometry.cpp](1212_geometry.cpp) | G++ 13.2 x64 | geometry | O(L² log L) | AC | 0.031 s | 432 KB |
| [1212_geometry.go](1212_geometry.go) | Go 1.14 x64 | geometry | O(L² log L) | AC | 0.031 s | 1144 KB |
| [1212_geometry.java](1212_geometry.java) | Java 1.8 | geometry | O(L² log L) | AC | 0.140 s | 1940 KB |
| [1212_geometry.py](1212_geometry.py) | Python 3.12 x64 | geometry | O(L² log L) | AC | 0.078 s | 684 KB |
| [1212_geometry.rs](1212_geometry.rs) | Rust 1.75 x64 | geometry | O(L² log L) | AC | 0.046 s | 232 KB |
