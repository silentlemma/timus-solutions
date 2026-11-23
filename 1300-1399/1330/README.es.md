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

`1330_prefix_sums_optimized.py`. Conserva prefijos y respuesta before[j]-before[i-1] para [i,j]. Analiza bloques de 65536 bytes con split/map, llevando el número parcial entre bloques en vez de otro generador por línea. Guarda prefijos en una lista Python y emite hasta 4096 respuestas por lote. O(N+Q) tiempo, O(N) estado más lotes acotados; no guarda todas las consultas ni toda la salida.

Accepted exacto CPython 3.12 #11326660: 0.156 s / 2648 KB. Comparación guardada 2026-11-20 de compiladores actuales: tiempo 5/34, memoria 5/34. Ambas métricas exigidas pasan diez primeros o 15% superior, redondeando el corte porcentual hacia arriba. El asterisco sigue la meta separada Python de primer puesto en ambas.

El envío optimizado documentado antes #11303743 (Python 3.12 x64) registró 0.203 s / 1440 KB. El actual CPython 3.12 registra menor tiempo y mayor memoria. Son medidas emparejadas de ejecuciones distintas; la comparación incluye elección de intérprete y variabilidad del juez. La base simple conservada es más rápida, 0.125 s; esta versión favorece menor memoria.

- `1330_prefix_sums_optimized.py`: 0.156 s / 2648 KB; base didáctica conservada `1330_prefix_sums.py` (Python 3.12 x64): 0.125 s / 27608 KB.

Las soluciones optimizadas en C++ y Java guardan las sumas de prefijos
como enteros de 32 bits, suficientes para sumas entre −10⁸ y 10⁸. C++
analiza los números y escribe las respuestas a mano mediante búferes de
4 KB y guarda las sumas en un arreglo estático: 0.015 s en lugar de
0.125 s y 132 KB en lugar de 2784 KB.

La solución optimizada en Java lee la entrada en bloques de 4 KB y la analiza a mano en lugar de usar `StreamTokenizer`, y escribe las respuestas en un búfer de bytes de 4 KB en lugar de construir cadenas: 0.125 s en lugar de 0.156 s y 452 KB en lugar de 7324 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1330_prefix_sums_optimized.rs`. Se mantienen el algoritmo y los tipos enteros. Los tokens decimales se convierten directamente; los negativos se acumulan con su signo para representar también el mínimo entero con signo. No cambian el almacenamiento de entrada ni la complejidad del algoritmo.

Accepted #11328541 (Rust 1.75 x64): **0.015 s / 3676 KB**. Comparación archivada: `1330_prefix_sums.rs` (Rust 1.75 x64) — 0.046 s / 3736 KB (#11285004).

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
| [1330_prefix_sums_optimized.py](1330_prefix_sums_optimized.py) | Python 3.12 x64 | prefix_sums | O(N+Q) time; O(N+B+S) space | AC | 0.156 s | 2648 KB | 11326660 |
| [1330_prefix_sums_optimized.rs](1330_prefix_sums_optimized.rs) | Rust 1.75 x64 | prefix_sums | O(N + Q) | AC | 0.015 s | 3676 KB | 11328541 |
