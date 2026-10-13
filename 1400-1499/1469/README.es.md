# 1469. ¡Prohibido fumar!

[Timus 1469](https://acm.timus.ru/problem.aspx?space=1&num=1469) · dificultad 899 · geometry

Problema original de Ilya Shishkov, del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N cigarrillos (1 ≤ N ≤ 50000) sobre una mesa como segmentos de
longitud no nula con extremos enteros de −10000 a 10000. Solo se puede
coger un cigarrillo que toque o cruce a otro. Hay que imprimir «YES» y
los números de dos cigarrillos con un punto común, o «NO» si no los hay.

Límite de tiempo: 1.5 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego N líneas x1 y1 x2 y2.

## Salida

«YES» y dos números, o «NO». Se acepta cualquier par que se toque.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 0 2 2
0 2 2 0
```

Salida:

```
YES
1 2
```

### Ejemplo 2

Entrada:

```
2
0 0 0 5
5 0 5 10
```

Salida:

```
NO
```

## Solución

Es el barrido de Shamos–Hoey. Se mueve una recta vertical de izquierda a
derecha y se guardan los segmentos que corta en una lista ordenada por
altura. Mientras dos segmentos no se encuentren, ese orden no cambia, y
el primer punto de encuentro por la izquierda siempre está entre dos
vecinos de la lista. Así que basta probar un segmento nuevo con sus
vecinos al insertarlo, y los dos segmentos que quedan vecinos cuando
uno sale.

Los casos degenerados requieren cuidado. Primero se cizalla el plano
con x' = 20001 x + y: los extremos enteros distintos tienen distinto x', así que ningún
segmento es vertical, y tocar o cruzar se conserva. En un mismo x', los
segmentos que empiezan ahí se insertan antes de quitar los que terminan
ahí, y los segmentos que pasan por un mismo punto se ordenan por
pendiente. Todas las comparaciones usan productos vectoriales enteros
exactos, y la prueba de encuentro cuenta extremos que se tocan y
solapamientos en una recta. La lista es un arreglo ordenado: insertar o
borrar puede desplazar N elementos. `O(N log N)` comparaciones y
`O(N^2)` tiempo total.

Detalles a tener en cuenta:

- tocar cuenta: un extremo sobre otro cigarrillo, dos extremos en un
  punto, solapamientos en una recta (pruebas 04, 05, 07, 12);
- cigarrillos verticales, que el cizallamiento resuelve (pruebas 07,
  11);
- probar todos los pares es demasiado lento para 50000 cigarrillos.

## Notas por lenguaje

- Python se ejecuta con PyPy: CPython excede el límite de 1,5 s en la
  prueba 3 del juez, y PyPy tarda 0,88 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1469_geometry.cpp](1469_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2) | AC | 0.250 s | 4952 KB |
| [1469_geometry.go](1469_geometry.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.625 s | 10184 KB |
| [1469_geometry.java](1469_geometry.java) | Java 1.8 | geometry | O(N^2) | AC | 0.375 s | 7668 KB |
| [1469_geometry.py](1469_geometry.py) | PyPy 3.10 x64 | geometry | O(N^2) | AC | 0.875 s | 36680 KB |
| [1469_geometry.rs](1469_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2) | AC | 0.625 s | 9372 KB |
