# 1207. Una recta por dos puntos que parte en dos el resto

[Timus 1207](https://acm.timus.ru/problem.aspx?space=1&num=1207) · dificultad 120 · geometry

Problema original de Pavel Atnashev, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay un número par `4 ≤ N ≤ 10000` de puntos con coordenadas enteras de
valor absoluto hasta `10⁶`, sin tres en una misma recta. Hay que elegir
dos de modo que la recta que pasa por ellos divida los demás puntos en
dos mitades del mismo tamaño.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego las coordenadas de cada punto.

## Salida

Los números de los dos puntos elegidos.

## Evaluación

Sirven muchos pares, así que se aceptan dos puntos distintos cualesquiera
si su recta deja `(N − 2)/2` puntos a cada lado.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
1 0
0 1
1 1
```

Salida:

```
1 4
```

## Solución

Se toma el punto más bajo, y el de más a la izquierda si dos comparten
la menor altura. Todos los demás están por encima o a su derecha a la
misma altura, dentro de media vuelta, así que se pueden ordenar por el
ángulo a su alrededor usando solo el signo del producto vectorial, sin
coma flotante. En ese orden, todos los puntos antes del `k`-ésimo quedan
a un lado de la recta del punto más bajo al `k`-ésimo, y todos los de
después al otro. Con `N − 1` puntos restantes, el que ocupa el índice
`(N − 2)/2` contando desde cero tiene `(N − 2)/2` antes y después.
`O(N log N)`.

Detalles a tener en cuenta:

- si el punto más bajo se elige solo por la altura, un punto a la misma
  altura a su izquierda quedaría a media vuelta y rompería el orden;
- los productos vectoriales llegan a `8·10¹²`, más de 32 bits;
- un comparador debe devolver «igual» al comparar un elemento consigo
  mismo, o algunas rutinas de ordenación lo rechazan.

Cada respuesta se comprobó contando los puntos de cada lado, y una
solución escrita aparte pasa el mismo verificador en todas las pruebas.

## Notas por lenguaje

- Python ordena con `functools.cmp_to_key`; Java ordena índices
  envueltos con una lambda que usa `Long.compare`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1207_geometry.cpp](1207_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 296 KB |
| [1207_geometry.go](1207_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.046 s | 1512 KB |
| [1207_geometry.java](1207_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.171 s | 5544 KB |
| [1207_geometry.py](1207_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.140 s | 3516 KB |
| [1207_geometry.rs](1207_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 908 KB |
