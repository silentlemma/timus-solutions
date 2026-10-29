# 1319. Hotel

[Timus 1319](https://acm.timus.ru/problem.aspx?space=1&num=1319) · dificultad 39 · implementation, math

Problema original de Stanislav Vasiliev, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El casillero de correo de un hotel es un bloque de N × N celdas
(1 ≤ N ≤ 100), numeradas por diagonales: el número 1 está en la esquina
superior derecha, cada diagonal va de arriba abajo, y las diagonales se
suceden hacia la esquina inferior izquierda, donde está N². Hay que
imprimir la tabla numerada.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

N líneas de N números separados por espacios.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
4 2 1
7 5 3
9 8 6
```

## Solución

Las celdas de una misma diagonal tienen la misma diferencia
columna − fila. Recorriendo esa diferencia de N − 1 hasta −(N − 1), y
las filas de cada diagonal desde arriba, las celdas salen en el orden
de la numeración. `O(N²)`.

Detalles a tener en cuenta:

- la primera diagonal es la celda superior derecha sola, no la diagonal
  principal (prueba 01);
- N = 1 es una sola celda con 1 (prueba 02).

## Soluciones optimizadas

**Fórmula** (C++, Java, Rust). No se guarda la tabla: el número de cada
casilla se calcula a partir de su posición, y las líneas se imprimen a
medida que se calculan. La diagonal de la casilla de la fila `r` y la
columna `c` tiene `len = N − |c − r|` casillas. En la diagonal principal
o por encima (`c ≥ r`), las diagonales anteriores contienen
`1 + 2 + … + (len − 1) = len·(len − 1)/2` números, y la casilla es la
número `r + 1` de la suya, así que contiene `len·(len − 1)/2 + r + 1`.
Por debajo se cuenta desde el final: las diagonales posteriores y el
resto de la propia dejan `N² − len·(len + 1)/2 + c + 1`. Java y Rust
además leen `N` byte a byte. Java necesita 0.062 s en lugar de 0.093 s y
508 KB en lugar de 2008 KB; C++ y Rust ocupan menos memoria con el mismo
tiempo: 124 KB en lugar de 244 KB y 200 KB en lugar de 364 KB.

La fórmula también está escrita en Python e imprime cada línea en cuanto
la calcula: 296 KB en lugar de 888 KB, aunque el tiempo sube de 0.046 s
a 0.078 s.

## Notas por lenguaje

- Las soluciones sencillas llenan la tabla de la misma manera y la
  imprimen al final.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1319_implementation.cpp](1319_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.015 s | 244 KB | 11284938 |
| [1319_implementation.go](1319_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.001 s | 1188 KB | 11284939 |
| [1319_implementation.java](1319_implementation.java) | Java 1.8 | implementation | O(N^2) | AC | 0.093 s | 2008 KB | 11284941 |
| [1319_implementation.py](1319_implementation.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.046 s | 888 KB | 11284940 |
| [1319_implementation.rs](1319_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.001 s | 364 KB | 11284942 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1319_math.cpp](1319_math.cpp) | G++ 13.2 x64 | math | O(N^2) | AC | 0.001 s | 124 KB | 11303594 |
| [1319_math.java](1319_math.java) | Java 1.8 | math | O(N^2) | AC | 0.062 s | 508 KB | 11303596 |
| [1319_math.py](1319_math.py) \* | Python 3.12 x64 | math | O(N^2) | AC | 0.078 s | 296 KB | 11303740 |
| [1319_math.rs](1319_math.rs) | Rust 1.75 x64 | math | O(N^2) | AC | 0.001 s | 200 KB | 11303597 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
