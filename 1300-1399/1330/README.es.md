# 1330. Intervalos

[Timus 1330](https://acm.timus.ru/problem.aspx?space=1&num=1330) · dificultad 95 · prefix_sums

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 10 000 sensores dan lecturas enteras de −10 000 a 10 000. Hay que
responder hasta 100 000 preguntas: la suma de las lecturas de los
sensores i a j, con i ≤ j.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego N lecturas, luego Q y Q pares i, j.

## Salida

Una suma por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1
2
3
-1
4
3
1 5
4 4
1 4
```

Salida:

```
9
-1
5
```

## Solución

Se guarda before[i], la suma de las primeras i lecturas, con
before[0] = 0. La suma de i a j es before[j] − before[i − 1], una resta
por pregunta. `O(N + Q)`.

Detalles a tener en cuenta:

- las sumas están entre −10⁸ y 10⁸, lo que cabe en un entero de 32
  bits;
- puede no haber ninguna pregunta (prueba 03);
- con 100 000 preguntas, la entrada y la salida se leen y escriben en
  bloques grandes para no pasar de 0,5 segundos.

## Soluciones optimizadas

Las soluciones optimizadas en C++ y Java guardan las sumas de prefijos
como enteros de 32 bits, suficientes para sumas entre −10⁸ y 10⁸. C++
analiza los números y escribe las respuestas a mano mediante búferes de
4 KB y guarda las sumas en un arreglo estático: 0.015 s en lugar de
0.125 s y 132 KB en lugar de 2784 KB.

La solución optimizada en Java lee la entrada en bloques de 4 KB y la
analiza a mano en lugar de usar `StreamTokenizer`, y escribe las
respuestas en un búfer de bytes de 4 KB en lugar de construir cadenas:
0.125 s en lugar de 0.156 s y 452 KB en lugar de 7324 KB. La solución
optimizada en Python analiza la entrada línea a línea en lugar de
dividirla toda de una vez y escribe las respuestas en lotes de 1024
líneas: 1440 KB en lugar de 27608 KB, aunque el tiempo sube de 0.125 s a
0.203 s.

## Notas por lenguaje

- La solución sencilla en Java lee con `StreamTokenizer`, que admite las
  lecturas negativas, y reúne las respuestas en una sola cadena.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1330_prefix_sums.cpp](1330_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 2784 KB | 11284999 |
| [1330_prefix_sums.go](1330_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 2828 KB | 11285000 |
| [1330_prefix_sums.java](1330_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + Q) | AC | 0.156 s | 7324 KB | 11303461 |
| [1330_prefix_sums.py](1330_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 27608 KB | 11285001 |
| [1330_prefix_sums.rs](1330_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 3736 KB | 11285004 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1330_prefix_sums_optimized.cpp](1330_prefix_sums_optimized.cpp) | G++ 13.2 x64 | prefix_sums | O(N + Q) | AC | 0.015 s | 132 KB | 11303598 |
| [1330_prefix_sums_optimized.java](1330_prefix_sums_optimized.java) | Java 1.8 | prefix_sums | O(N + Q) | AC | 0.125 s | 452 KB | 11303742 |
| [1330_prefix_sums_optimized.py](1330_prefix_sums_optimized.py) \* | Python 3.12 x64 | prefix_sums | O(N + Q) | AC | 0.203 s | 1440 KB | 11303743 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
