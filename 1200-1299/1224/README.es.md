# 1224. Los giros de un robot que barre un rectángulo en espiral

[Timus 1224](https://acm.timus.ru/problem.aspx?space=1&num=1224) · dificultad 66 · math

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un robot empieza en la casilla superior izquierda de un campo de `N`
filas y `M` columnas, ambas hasta `2³¹ − 1`, mirando a la derecha, y
recorre todas las casillas siguiendo una espiral en sentido horario que
se cierra hacia el centro. Hay que contar sus giros.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `M`.

## Salida

El número de giros.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5
```

Salida:

```
4
```

## Solución

El camino alterna tramos horizontales y verticales, empezando por uno
horizontal, y gira una vez entre dos tramos. Cada tramo horizontal gasta
una fila y cada tramo vertical una columna, porque la espiral pela el
campo desde fuera.

Si `N ≤ M`, primero se agotan las filas, tras `N` tramos horizontales y
`N − 1` verticales: `2N − 1` tramos y `2(N − 1)` giros. Si no, primero se
agotan las columnas, tras `M` tramos de cada tipo: `2M` tramos y
`2M − 1` giros. `O(1)`.

Detalles a tener en cuenta:

- una sola fila no necesita ningún giro, pero una sola columna necesita
  uno, porque el robot empieza mirando a la derecha;
- la respuesta llega a unos `4.3·10⁹`, más de 32 bits.

La fórmula se comprobó simulando el robot en todos los campos hasta
14 × 14, y se comparó con una solución escrita aparte en todas las
pruebas.

## Notas por lenguaje

- Todos los lenguajes aplican la misma fórmula con enteros de 64 bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1224_math.cpp](1224_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1224_math.go](1224_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1076 KB |
| [1224_math.java](1224_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1564 KB |
| [1224_math.py](1224_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 372 KB |
| [1224_math.rs](1224_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 208 KB |
