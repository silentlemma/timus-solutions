# 1628. Rachas blancas

[Timus 1628](https://acm.timus.ru/problem.aspx?space=1&num=1628) · dificultad 168 · implementation

Problema original de Alexander Ipatov, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un calendario es una tabla m × n: la fila i es una semana y la columna j
un día de la semana. Hay k celdas pintadas de negro (los días malos) y el
resto son blancas. Un segmento es un rectángulo de celdas de 1 × l o
l × 1. Hay que contar las rachas blancas: los segmentos blancos que no
se pueden alargar en su dirección.

## Entrada

La primera línea contiene m, n y k (1 ≤ m, n ≤ 30000, 0 ≤ k ≤ 60000).
Cada una de las k líneas siguientes contiene una celda negra x y
(1 ≤ x ≤ m, 1 ≤ y ≤ n); las celdas son distintas.

## Salida

El número de rachas blancas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5 4
1 1
1 5
2 2
3 3
```

Salida:

```
8
```

### Ejemplo 2

Entrada:

```
5 1 2
2 1
3 1
```

Salida:

```
2
```

## Solución

En cada fila las celdas negras la dividen en tramos blancos, y lo mismo
en cada columna. Un tramo de longitud 2 o más es una racha. Una celda
blanca aislada es distinta: es un segmento 1 × 1 en ambas direcciones,
así que se cuenta una sola vez y solo si no puede crecer hacia ningún
lado, es decir, cuando sus vecinas de fila y de columna son todas negras
o quedan fuera de la tabla. Si no, la celda ya está en una racha más
larga.

Así, las filas cuentan sus tramos de longitud al menos 2 más sus celdas
aisladas cerradas arriba y abajo, y las columnas solo sus tramos de
longitud al menos 2. Cada fila y cada columna ordena sus celdas negras,
y un conjunto hash responde si una vecina es negra.
`O(m + n + k log k)`.

Detalles a tener en cuenta:

- una celda blanca aislada no debe contarse dos veces, una por dirección
  (prueba 05);
- con una sola fila o una sola columna, toda celda blanca queda cerrada
  por el borde en la otra dirección (el segundo ejemplo);
- una tabla toda blanca tiene m + n rachas, así que las filas y columnas
  sin celdas negras también cuentan (prueba 06).

Las respuestas coinciden con una implementación aceptada independiente
en 120 calendarios aleatorios y en el más grande.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1628_implementation.cpp](1628_implementation.cpp) | G++ 13.2 x64 | implementation | O(m + n + k log k) | AC | 0.109 s | 6528 KB |
| [1628_implementation.go](1628_implementation.go) | Go 1.14 x64 | implementation | O(m + n + k log k) | AC | 0.125 s | 13204 KB |
| [1628_implementation.java](1628_implementation.java) | Java 1.8 | implementation | O(m + n + k log k) | AC | 0.109 s | 10240 KB |
| [1628_implementation.py](1628_implementation.py) | Python 3.12 x64 | implementation | O(m + n + k log k) | AC | 0.218 s | 25760 KB |
| [1628_implementation.rs](1628_implementation.rs) | Rust 1.75 x64 | implementation | O(m + n + k log k) | AC | 0.046 s | 9408 KB |
