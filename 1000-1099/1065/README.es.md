# 1065. El subpolígono más corto que conserva puntos dados dentro

[Timus 1065](https://acm.timus.ru/problem.aspx?space=1&num=1065) · dificultad 1413 · dp, geometry

Problema original del concurso regional ACM ICPC del noreste de Europa 2000–2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan un polígono convexo de `N` vértices (`3 ≤ N ≤ 50`, en sentido
horario, coordenadas enteras de valor absoluto hasta 10000; varios vértices
pueden estar en un mismo lado) y `M` puntos dentro de él
(`0 ≤ M ≤ 1000`). Elige algunos de los vértices, manteniendo su orden, de
modo que formen un polígono de área no nula con los `M` puntos
estrictamente dentro y con el menor perímetro posible. Imprime el
perímetro con dos decimales.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `M`, luego `N` líneas con los vértices en sentido horario y luego
`M` líneas con los puntos.

## Salida

El menor perímetro, con al menos dos cifras tras el punto decimal.

## Evaluación

Los números se comparan con un error absoluto de 0.011: las respuestas se
imprimen con dos decimales, así que la última cifra puede diferir en uno.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 0
8 9
0 -7
-8 -7
-8 1
-8 9
```

Salida:

```
27.31
```

### Ejemplo 2

Entrada:

```
5 2
8 9
0 -7
-8 -7
-8 1
-8 9
-4 -3
-1 -5
```

Salida:

```
51.78
```

## Solución

Los vértices de un polígono convexo tomados en su orden siempre forman un
polígono convexo, así que la única pregunta es qué lados `i → j` se pueden
usar. El nuevo polígono también va en sentido horario, así que su interior
está a la derecha de cada lado: un lado es válido cuando todos los puntos
están estrictamente a su derecha (producto vectorial negativo). Eso cuesta
`O(N^2 · M)`.

El nuevo borde es entonces un ciclo que da una vuelta por lados válidos.
Para cada primer vértice `s`, una DP sobre los vértices siguientes en orden
da el camino más corto de `s` a cada uno, y un lado válido de vuelta a `s`
cierra el borde. `O(N^3)`.

Sin puntos (`M = 0`) todos los lados son válidos, pero el borde no debe
degenerar: tres vértices de un mismo lado del polígono original no tienen
área. Todo polígono convexo contiene un triángulo de sus propios vértices
con un perímetro no mayor, así que la respuesta es el triángulo de
vértices más corto con área no nula. Con al menos un punto el borde lo
rodea, de modo que no puede aparecer un borde degenerado.

Detalles a tener en cuenta:

- los puntos deben estar estrictamente dentro: un punto sobre un lado no
  vale;
- vértices colineales del polígono original: un «triángulo» de tres de
  ellos no es un polígono;
- las diferencias de coordenadas llegan a `2 · 10^4`, así que un producto
  vectorial llega a `8 · 10^8`: cabe en enteros de 32 bits por muy poco, y
  las soluciones usan enteros de 64 bits.

Las respuestas se comprobaron con todos los subconjuntos de vértices para
`N` pequeños.

## Notas por lenguaje

- Todos los lenguajes calculan los productos vectoriales exactamente con
  enteros y usan coma flotante solo para las longitudes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1065_dp_geometry.cpp](1065_dp_geometry.cpp) | G++ 13.2 x64 | dp, geometry | O(N^2 · M + N^3) | AC | 0.015 s | 276 KB |
| [1065_dp_geometry.go](1065_dp_geometry.go) | Go 1.14 x64 | dp, geometry | O(N^2 · M + N^3) | AC | 0.015 s | 1188 KB |
| [1065_dp_geometry.java](1065_dp_geometry.java) | Java 1.8 | dp, geometry | O(N^2 · M + N^3) | AC | 0.125 s | 1172 KB |
| [1065_dp_geometry.py](1065_dp_geometry.py) | Python 3.12 x64 | dp, geometry | O(N^2 · M + N^3) | AC | 0.656 s | 1056 KB |
| [1065_dp_geometry.rs](1065_dp_geometry.rs) | Rust 1.75 x64 | dp, geometry | O(N^2 · M + N^3) | AC | 0.031 s | 340 KB |
