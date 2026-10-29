# 1910. La terna consecutiva de mayor suma

[Timus 1910](https://acm.timus.ru/problem.aspx?space=1&num=1910) · difficulty 34 · implementation

Problema original de Denis Dublennykh, NEERC 2012, Eastern subregional contest.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una secuencia de valores positivos, encuentra los tres consecutivos
con mayor suma. Imprime esa suma y la posición del elemento central,
numerada desde uno. Se garantiza que la terna óptima es única.
Límites: 1 segundo y 64 MB.

## Entrada

Primero n, 3≤n≤1000, seguido de n enteros aᵢ con 1≤aᵢ≤10⁶.
Los espacios y los saltos de línea son separadores equivalentes.

## Salida

La suma máxima y la posición central numerada desde uno.

## Evaluación

Dos enteros exactos, comparados por tokens.

## Ejemplos

```
6
1 4 4 4 1 1
```

```
12 3
```

## Solución

Se prueba cada sección, de la segunda a la penúltima, como la del medio
de las tres: se suma con sus dos vecinas y se guarda la mayor suma con
su número. El enunciado promete que el mejor trío es único, así que
basta una comparación estricta. `O(n)`; una suma es a lo sumo 3·10⁶ y
cabe en un entero de 32 bits.

Detalles a tener en cuenta:

- la respuesta es el número de la sección del medio, contando desde 1;
- con n = 3 solo hay un trío.

## Soluciones optimizadas

La solución optimizada en C++ no guarda las secciones: las lee una a una
con `scanf` y recuerda solo las dos anteriores a la actual, que es todo
lo que necesita un trío: 128 KB en lugar de 192 KB, con el mismo tiempo.

La solución optimizada en Java guarda solo los dos tramos anteriores al
actual, como la de C++, y analiza la entrada a mano en lugar de usar
`Scanner`: 0.125 s en lugar de 0.156 s y 380 KB en lugar de 2372 KB.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1910_implementation.cpp](1910_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 192 KB | 11303319 |
| [1910_implementation.go](1910_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1108 KB | 11303324 |
| [1910_implementation.java](1910_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.156 s | 2372 KB | 11303327 |
| [1910_implementation.py](1910_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.062 s | 452 KB | 11303331 |
| [1910_implementation.rs](1910_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 236 KB | 11303334 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1910_implementation_optimized.cpp](1910_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11303648 |
| [1910_implementation_optimized.java](1910_implementation_optimized.java) \* | Java 1.8 | implementation | O(n) | AC | 0.125 s | 380 KB | 11303787 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
