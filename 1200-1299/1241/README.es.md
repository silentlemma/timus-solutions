# 1241. Contar los triángulos que dejan unos cortes rectos

[Timus 1241](https://acm.timus.ru/problem.aspx?space=1&num=1241) · dificultad 1707 · geometry

Problema original de Elena Kruchkova, del concurso regional ACM ICPC del noreste de Europa 2002–2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una placa de M × N (M, N ≤ 50) se corta K veces (K ≤ 296). Cada corte es
una recta de un punto del borde a otro, ambos de coordenadas enteras, en
vertical, en horizontal o a 45° de los lados; todos los cortes son
distintos. Hay que contar las piezas que son triángulos rectángulos
isósceles, de cualquier tamaño.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

M, N y K, y luego cada corte como `X1 Y1 X2 Y2`.

## Salida

El número de piezas triangulares.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4 4
1 4 1 0
0 4 4 0
0 0 4 4
0 2 4 2
```

Salida:

```
6
```

### Ejemplo 2

Entrada:

```
7 4 6
6 0 7 1
1 4 1 0
0 4 4 0
0 0 4 4
0 2 7 2
7 0 3 4
```

Salida:

```
8
```

## Solución

Un corte va de borde a borde, así que es una recta entera a través de la
placa, de uno de cuatro tipos: `x = c`, `y = c`, `x − y = c` o
`x + y = c`, con c entero. Solo importa qué rectas están cortadas, y hay
apenas (M − 1) + (N − 1) + 2(M + N − 1), 296 para la placa más grande.

Partimos cada cuadrado unidad con sus dos diagonales en cuatro triángulos
pequeños. Cualquier corte posible va por aristas de estos triángulos, así
que cada pieza es una unión de ellos: se unen dos triángulos pequeños
vecinos salvo que su arista común esté sobre una recta cortada, con una
estructura de conjuntos disjuntos de como mucho 10 000 elementos.

Para reconocer un triángulo, cada pieza es convexa, pues es la placa
cortada por rectas, y sus lados apuntan solo en 8 direcciones posibles,
un lado por dirección. Así que una pieza tiene tantos lados como
direcciones exteriores distintas tienen sus aristas. Cada triángulo
pequeño anota las direcciones exteriores de sus aristas que están sobre
un corte o sobre el borde; una pieza cuya unión de direcciones tiene
exactamente 3 es un triángulo, y con ángulos de solo 45° y 90° es
rectángulo isósceles. `O(M·N)`.

Detalles a tener en cuenta:

- el corte viene dado por sus dos extremos, en cualquier orden; solo
  importan el tipo de recta y su constante;
- una pieza puede ser un triángulo grande formado por muchos pequeños,
  así que la forma se juzga por sus lados, no por su área.

Los recuentos se compararon con una división exacta del polígono de la
placa por cada recta de corte en 400 placas pequeñas aleatorias.

## Notas por lenguaje

- Todos los lenguajes guardan las direcciones como una máscara de 8 bits
  por triángulo pequeño y cuentan sus bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1241_geometry.cpp](1241_geometry.cpp) | G++ 13.2 x64 | geometry | O(M·N) | AC | 0.015 s | 236 KB |
| [1241_geometry.go](1241_geometry.go) | Go 1.14 x64 | geometry | O(M·N) | AC | 0.031 s | 1356 KB |
| [1241_geometry.java](1241_geometry.java) | Java 1.8 | geometry | O(M·N) | AC | 0.093 s | 604 KB |
| [1241_geometry.py](1241_geometry.py) | Python 3.12 x64 | geometry | O(M·N) | AC | 0.109 s | 2116 KB |
| [1241_geometry.rs](1241_geometry.rs) | Rust 1.75 x64 | geometry | O(M·N) | AC | 0.046 s | 380 KB |
