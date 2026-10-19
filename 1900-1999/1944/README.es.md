# 1944. Un mapa ASCII con prioridad para los puntos

[Timus 1944](https://acm.timus.ru/problem.aspx?space=1&num=1944) · difficulty 238 · implementation

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dibujar puntos enteros distintos en una cuadrícula cartesiana: x crece
a la derecha e y hacia arriba, una celda por coordenada. Usar * para
puntos, + para origen, - para eje x, | para eje y y . como fondo.
Un punto tapa ejes y origen; incluso pueden ocultarse todos los ejes.
Dibujar el rectángulo mínimo que contiene puntos y origen.
Límites: 1 segundo, 64 MB.

## Entrada

n con 1≤n≤250, seguido de n pares enteros distintos (x,y), −100≤x,y≤100.
No hay dos puntos coincidentes.

## Salida

Filas desde U=max(0,max y) bajando hasta D=min(0,min y), inclusive.
Columnas desde L=min(0,min x) hasta R=max(0,max x). Hay H=U−D+1 filas
de W=R−L+1 símbolos. Imprimir solo el dibujo.

## Evaluación

Se compara el dibujo completo con símbolos exactos por fila/columna;
un espacio no sustituye un punto. Cada fila termina en salto de línea.

## Ejemplos

```
8
-10 5
-7 3
-4 2
-9 4
0 1
6 -1
3 0
8 -3
```

```
*.........|........
.*........|........
...*......|........
......*...|........
..........*........
----------+--*-----
..........|.....*..
..........|........
..........|.......*
```

## Solución

Iniciar los cuatro límites en cero y ampliarlos con los puntos.
(x,y) se transforma en row=U−y, column=x−L, biyección a índices
0..H−1 y 0..W−1 con la orientación requerida.

Rellenar una matriz H×W de puntos. Poner | en columna −L de cada fila.
Rellenar fila U de -, después cambiar su columna −L por +. Finalmente
sobrescribir con * cada punto de entrada. Emitir filas en orden de índice.

El relleno representa el fondo; las dos pasadas marcan exactamente x=0
e y=0. Su intersección se sustituye por + y la última pasada da prioridad
a los puntos, que se mapean a celdas distintas. Los límites iniciados
en cero incluyen el origen aunque todos los puntos estén en un cuadrante;
ningún rectángulo menor contiene todas las coordenadas necesarias.
Así quedan probados forma, símbolos y orientación, incluso con una fila
o una columna.

Tiempo y espacio O(n+WH), incluyendo puntos y salida. W,H≤201 y la
salida máxima ocupa H(W+1)≤40602 bytes ASCII con saltos, menos de 64 KiB.
Los índices y límites caben en enteros ordinarios con signo.

Incluir cero en ambos rangos. Al crecer la fila disminuye y; no confundir
desplazamientos de fila/columna. El origen solo es + si no hay punto;
un punto sobre un eje sigue siendo *. No añadir etiquetas, espacios,
marcos o márgenes.

## Notas por lenguaje

Python usa bytearray, Go segmentos de bytes, C++ cadenas, Java matrices
char y Rust vectores de bytes. Java añade contenido de filas, no la
representación del objeto matriz. Solo ASCII. Emitir directamente el
dibujo ya terminado en salto, evitando una línea vacía adicional.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1944_implementation.cpp](1944_implementation.cpp) | G++ 13.2 x64 | implementation | O(n+WH) | AC | 0.015 s | 472 KB |
| [1944_implementation.go](1944_implementation.go) | Go 1.14 x64 | implementation | O(n+WH) | AC | 0.031 s | 1420 KB |
| [1944_implementation.java](1944_implementation.java) | Java 1.8 | implementation | O(n+WH) | AC | 0.125 s | 844 KB |
| [1944_implementation.py](1944_implementation.py) | Python 3.12 x64 | implementation | O(n+WH) | AC | 0.093 s | 636 KB |
| [1944_implementation.rs](1944_implementation.rs) | Rust 1.75 x64 | implementation | O(n+WH) | AC | 0.031 s | 348 KB |
