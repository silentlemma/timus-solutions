# 1028. Contar los puntos por debajo y a la izquierda de cada punto

[Timus 1028](https://acm.timus.ru/problem.aspx?space=1&num=1028) · dificultad 264 · fenwick, segment_tree

Problema original del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan `N` puntos distintos (`1 ≤ N ≤ 15 000`) con coordenadas enteras
`0 ≤ x, y ≤ 32 000`, en orden creciente de `y` y, a igual `y`, de `x`. El
**nivel** de un punto es el número de otros puntos con `x' ≤ x` e `y' ≤ y`.
Para cada `k` de 0 a `N - 1`, imprime cuántos puntos tienen nivel `k`.

Límite de tiempo: 0.25 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas `x y` en el orden descrito.

## Salida

`N` líneas: el número de puntos de nivel 0, 1, ..., `N - 1`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
2 0
6 0
0 2
4 2
4 4
1 6
```

Salida:

```
2
2
1
1
0
0
```

### Ejemplo 2

Entrada:

```
1
32000 32000
```

Salida:

```
1
```

## Solución

El orden de la entrada hace la mitad del trabajo. Cuando llega un punto, ya
han llegado todos los puntos con `y` menor y los de igual `y` y `x` menor; y
ningún punto posterior tiene a la vez `y' ≤ y` y `x' ≤ x`, salvo el mismo
punto. Así que el nivel de un punto es el número de puntos **ya vistos** con
`x' ≤ x`.

Es un conteo de prefijo sobre `x` con inserciones: un **árbol de Fenwick**
sobre las coordenadas `0..32 000` responde «cuántos valores insertados son
`≤ x`» e inserta un valor en `O(log C)` cada uno, siendo `C` el rango de
coordenadas. Se procesan los puntos en orden: consulta, se anota el nivel,
inserción. `O(N log C)` en total.

Un árbol de segmentos sobre las coordenadas funciona igual, algo más lento.

Detalles a tener en cuenta:

- `x` puede ser 0 y los árboles de Fenwick empiezan en 1: desplaza en uno;
- contar los puntos anteriores de forma cuadrática son `10^8`
  comparaciones, demasiado para el límite de 0.25 segundos;
- `N` números en la salida: constrúyela en un búfer.

## Notas por lenguaje

- **C++**: un árbol de Fenwick y un árbol de segmentos de abajo arriba.
- **Go**, **Python**, **Java**, **Rust**: un árbol de Fenwick; en Python los
  bucles son mínimos (solo se convierten las coordenadas `x`, y se baja con
  `j &= j - 1`).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1028_fenwick.cpp](1028_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(N log C), C = 32001 | AC | 0.031 s | 348 KB |
| [1028_fenwick.go](1028_fenwick.go) | Go 1.14 x64 | fenwick | O(N log C), C = 32001 | AC | 0.046 s | 1512 KB |
| [1028_fenwick.java](1028_fenwick.java) | Java 1.8 | fenwick | O(N log C), C = 32001 | AC | 0.093 s | 888 KB |
| [1028_fenwick.py](1028_fenwick.py) | Python 3.12 x64 | fenwick | O(N log C), C = 32001 | AC | 0.109 s | 3644 KB |
| [1028_fenwick.rs](1028_fenwick.rs) | Rust 1.75 x64 | fenwick | O(N log C), C = 32001 | AC | 0.031 s | 1076 KB |
| [1028_segment_tree.cpp](1028_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(N log C), C = 32001 | AC | 0.031 s | 472 KB |
