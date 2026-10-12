# 1333. Bombardeo con genios 2

[Timus 1333](https://acm.timus.ru/problem.aspx?space=1&num=1333) · dificultad 219 · geometry

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hasta 10 bombas caen sobre el cuadrado unidad 0 ≤ x, y ≤ 1. Cada una
alcanza un disco de centro (x, y) y radio r, todos entre 0 y 1. Hay que
imprimir la parte del cuadrado alcanzada por al menos una bomba, en
porcentaje, con un error de un punto como mucho.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas con x, y y r.

## Salida

El porcentaje del cuadrado alcanzado.

## Comprobación

Nuestras pruebas aceptan respuestas a 0.01 o menos de la esperada. Los
ejemplos del enunciado están algo redondeados: el segundo vale unos
80.746, no 80.743.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
0.5 0.5 0.5
```

Salida:

```
78.539816
```

### Ejemplo 2

Entrada:

```
2
0.2 0.2 0.5
0.8 0.8 0.5
```

Salida:

```
80.74292
```

## Solución

Se corta el cuadrado en 20 000 franjas verticales finas y se toma la
recta por el centro de cada una. En esa recta cada disco cubre un
intervalo de y, recortado a [0, 1]. Ordenando los intervalos y
recorriéndolos se obtiene la longitud de su unión. La suma de esas
longitudes por el ancho de una franja es el área alcanzada.
`O(S · N log N)` para S franjas.

El error solo viene de los bordes de los discos, donde la longitud de
la cuerda cambia deprisa. Aun así, aquí ronda 10⁻⁵ puntos porcentuales:
con un millón de franjas el segundo ejemplo cambia menos de 10⁻⁵. Eso
queda muy dentro del punto permitido, así que no hace falta una fórmula
exacta para la unión de discos.

Detalles a tener en cuenta:

- los discos pueden salirse del cuadrado, y solo cuenta la parte de
  dentro (pruebas 02 y 05);
- los discos pueden repetirse o estar uno dentro de otro, y la unión
  debe contar esa área una sola vez (prueba 07);
- puede no haber bombas, o haber bombas de radio 0 (pruebas 03 y 06).

Las respuestas se compararon con el conteo de una cuadrícula de
700 × 700 puntos en 60 casos aleatorios; la mayor diferencia fue de
0.005 puntos.

## Notas por lenguaje

- Las cinco soluciones usan el mismo número de franjas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1333_geometry.cpp](1333_geometry.cpp) | G++ 13.2 x64 | geometry | O(S·N log N) | AC | 0.031 s | 224 KB |
| [1333_geometry.go](1333_geometry.go) | Go 1.14 x64 | geometry | O(S·N log N) | AC | 0.046 s | 5944 KB |
| [1333_geometry.java](1333_geometry.java) | Java 1.8 | geometry | O(S·N log N) | AC | 0.187 s | 6560 KB |
| [1333_geometry.py](1333_geometry.py) | Python 3.12 x64 | geometry | O(S·N log N) | AC | 0.156 s | 504 KB |
| [1333_geometry.rs](1333_geometry.rs) | Rust 1.75 x64 | geometry | O(S·N log N) | AC | 0.046 s | 268 KB |
