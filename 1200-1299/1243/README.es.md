# 1243. Lo que sobra cuando siete enanos se reparten algo

[Timus 1243](https://acm.timus.ru/problem.aspx?space=1&num=1243) · dificultad 49 · math

Problema original de Stanislav Vasilyev, del Concurso Individual de la Universidad Estatal de los Urales, 1 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Siete enanos se reparten a partes iguales N cosas iguales
(1 ≤ N ≤ 10⁵⁰), y lo que no se puede repartir es para Blancanieves.
¿Cuántas cosas recibe?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

N mod 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
123456123456
```

Salida:

```
1
```

## Solución

La respuesta es el resto de dividir N entre 7, pero N tiene hasta 51
cifras, mucho más de 64 bits. Leyendo N como cadena y guardando solo el
resto de su prefijo se obtiene cifra a cifra:
`rest = (rest · 10 + cifra) mod 7`. `O(len N)`.

Detalles a tener en cuenta:

- ya 20 cifras desbordan un entero de 64 bits (prueba gen4).

## Soluciones optimizadas

La solución optimizada en C++ pliega las cifras a medida que las lee con
`getchar`, sin guardar el número como cadena, y escribe la respuesta de
una cifra como un byte: 84 KB en lugar de 380 KB, con el mismo tiempo.

La solución optimizada en Go lee las cifras byte a byte desde un lector
con búfer de 128 bytes en lugar de leer el número como cadena con
`fmt.Scan`, y escribe la respuesta de una cifra como dos bytes: 0.015 s
en lugar de 0.046 s y 912 KB en lugar de 1060 KB.

## Notas por lenguaje

- Los enteros de Python guardan N exactamente, así que basta
  `int(N) % 7`; los demás lenguajes van plegando las cifras.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1243_math.cpp](1243_math.cpp) | G++ 13.2 x64 | math | O(len N) | AC | 0.015 s | 380 KB | 11283900 |
| [1243_math.go](1243_math.go) | Go 1.14 x64 | math | O(len N) | AC | 0.046 s | 1060 KB | 11283901 |
| [1243_math.java](1243_math.java) | Java 1.8 | math | O(len N) | AC | 0.078 s | 400 KB | 11283907 |
| [1243_math.py](1243_math.py) | Python 3.12 x64 | math | O(len N) | AC | 0.046 s | 328 KB | 11283905 |
| [1243_math.rs](1243_math.rs) | Rust 1.75 x64 | math | O(len N) | AC | 0.046 s | 216 KB | 11283909 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1243_math_optimized.cpp](1243_math_optimized.cpp) | G++ 13.2 x64 | math | O(len N) | AC | 0.001 s | 84 KB | 11303584 |
| [1243_math_optimized.go](1243_math_optimized.go) | Go 1.14 x64 | math | O(len N) | AC | 0.015 s | 912 KB | 11303729 |
