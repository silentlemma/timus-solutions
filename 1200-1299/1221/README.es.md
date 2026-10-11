# 1221. El mayor cuadrado negro con un rombo blanco dentro

[Timus 1221](https://acm.timus.ru/problem.aspx?space=1&num=1221) · dificultad 422 · implementation

Problema original de Nikita Shamgunov, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una hoja de `N × N` casillas, `N ≤ 100`, está pintada de negro (1) y
blanco (0). Hay que recortar el mayor cuadrado, con lados sobre la
cuadrícula, que sea negro salvo un cuadrado blanco girado 45 grados cuyos
vértices tocan el centro de sus lados. Se imprime su tamaño, o
`No solution`. La entrada trae varias hojas y termina con `0`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Para cada hoja, `N` y `N` filas de casillas; y luego `0`.

## Salida

Para cada hoja, el tamaño de la mayor figura así o `No solution`.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
1 1 0 1 1 0
1 0 0 0 1 1
0 0 0 0 0 0
1 0 0 0 1 1
1 1 0 1 1 1
0 1 1 1 1 1
4
1 0 0 1
0 0 0 0
0 0 0 0
1 0 0 1
0
```

Salida:

```
5
No solution
```

## Solución

El rombo blanco tiene una casilla central y llega al centro de cada lado,
así que la figura tiene tamaño impar `2r + 1` con `r ≥ 1`: una casilla a
desplazamiento `(d, e)` del centro es blanca exactamente cuando
`|d| + |e| ≤ r`. La fila `d` de la figura es, por tanto, `|d|` casillas
negras, un tramo blanco de `2(r − |d|) + 1` casillas y otra vez `|d|`
negras, y con sumas prefijas de casillas negras por fila cada fila se
comprueba en tiempo constante.

Se prueban los radios de mayor a menor y, para cada uno, todos los
centros; la primera figura encontrada es la respuesta. La mayoría de los
candidatos caen al instante por tres casillas sueltas (el centro y la
punta superior deben ser blancos, la esquina superior izquierda negra), y
el resto suele fallar en la primera fila comprobada. `O(N⁴)` en el peor
caso, mucho menos en la práctica.

Detalles a tener en cuenta:

- una sola casilla blanca no es una figura: el rombo necesita sitio
  dentro de un cuadrado negro, así que la figura más pequeña es de
  3 × 3, como muestra la segunda hoja del ejemplo;
- las figuras solo tienen tamaño impar;
- varias hojas se suceden hasta el `0`.

Las respuestas se compararon con una solución escrita aparte en 300
archivos de hojas aleatorias, con figuras plantadas y de un solo color.

## Notas por lenguaje

- Todos los lenguajes leen las casillas cifra a cifra, así que valen las
  filas con o sin espacios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1221_implementation.cpp](1221_implementation.cpp) | G++ 13.2 x64 | implementation | O(N⁴) | AC | 0.015 s | 316 KB |
| [1221_implementation.go](1221_implementation.go) | Go 1.14 x64 | implementation | O(N⁴) | AC | 0.001 s | 2116 KB |
| [1221_implementation.java](1221_implementation.java) | Java 1.8 | implementation | O(N⁴) | AC | 0.062 s | 936 KB |
| [1221_implementation.py](1221_implementation.py) | Python 3.12 x64 | implementation | O(N⁴) | AC | 0.140 s | 1908 KB |
| [1221_implementation.rs](1221_implementation.rs) | Rust 1.75 x64 | implementation | O(N⁴) | AC | 0.031 s | 500 KB |
