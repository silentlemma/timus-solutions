# 1147. El área visible de cada color tras apilar rectángulos sobre una hoja

[Timus 1147](https://acm.timus.ru/problem.aspx?space=1&num=1147) · dificultad 736 · dsu

Problema original de Timus; no se indican autor ni fuente.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 1000` rectángulos de colores con lados paralelos a los ejes se
colocan uno tras otro sobre una hoja blanca de `A × B`, `A, B ≤ 10000`; la
hoja tiene el color 1 y los colores llegan hasta 2500. Visto desde
arriba, lista cada color visible con su área visible total, en orden
creciente de color.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`A`, `B` y `N`, y luego `N` líneas con la esquina inferior izquierda, la
superior derecha y el color de un rectángulo, del de abajo hacia arriba.

## Salida

Los colores visibles con sus áreas, uno por línea, por color.

## Ejemplos

### Ejemplo 1

Entrada:

```
20 20 3
2 2 18 18 2
0 8 19 19 3
8 0 10 19 4
```

Salida:

```
1 91
2 84
3 187
4 38
```

## Solución

Todas las esquinas dividen la hoja en como mucho `2001` franjas verticales
y `2001` bandas horizontales; dentro de una franja y una banda el color
visto desde arriba es constante. Se toman las franjas de una en una. En
una franja se recorren los rectángulos que la cruzan, del de arriba hacia
abajo: cada uno pinta las bandas que cubre y que ningún rectángulo más
alto ha pintado aún, y suma su altura por el ancho de la franja a su
color. Lo que queda sin pintar es blanco.

Para encontrar rápido las bandas sin pintar, `skip[j]` apunta desde la
banda `j` a la siguiente banda que aún puede estar sin pintar, como en una
unión de conjuntos disjuntos con reducción a la mitad de caminos; pintar
la banda `j` pone `skip[j] = j + 1`. Cada banda se pinta una vez por
franja, así que una franja cuesta `O(N + Y)` y todo el barrido
`O(X·(N + Y))` con `X, Y ≤ 2001`. Una franja termina antes en cuanto está
pintada entera.

Detalles a tener en cuenta:

- un rectángulo blanco encima se ve blanco, así que suma al color 1 como
  la hoja descubierta;
- los colores con área visible cero no se imprimen;
- las áreas llegan a `10⁸`, aún dentro de 32 bits, pero las sumas son de
  64 bits.

Las respuestas se compararon con pintar cada cuadrado unidad de la hoja
en 150 entradas aleatorias pequeñas.

## Notas por lenguaje

- C++, Go, Java y Rust comprueban cada rectángulo para cada franja.
- Python primero construye la lista de rectángulos sobre cada franja y se
  ahorra la comprobación; aun así es el más lento de los cinco aquí. En
  las pruebas más grandes tarda unos 0,8 s con CPython en nuestras
  ejecuciones, más que el límite de 0,5 s, así que la solución en Python
  se envía con PyPy 3.10, con el que Timus la acepta en 0,484 s, cerca del
  límite.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1147_dsu.cpp](1147_dsu.cpp) | G++ 13.2 x64 | dsu | O(X·(N + Y)) | AC | 0.078 s | 228 KB |
| [1147_dsu.go](1147_dsu.go) | Go 1.14 x64 | dsu | O(X·(N + Y)) | AC | 0.218 s | 1356 KB |
| [1147_dsu.java](1147_dsu.java) | Java 1.8 | dsu | O(X·(N + Y)) | AC | 0.281 s | 3796 KB |
| [1147_dsu.py](1147_dsu.py) | PyPy 3.10 x64 | dsu | O(X·(N + Y)) | AC | 0.484 s | 30596 KB |
| [1147_dsu.rs](1147_dsu.rs) | Rust 1.75 x64 | dsu | O(X·(N + Y)) | AC | 0.109 s | 264 KB |
