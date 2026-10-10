# 1125. Deshacer cambios de color a distancias enteras en una cuadrícula

[Timus 1125](https://acm.timus.ru/problem.aspx?space=1&num=1125) · dificultad 236 · bitmask

Problema original de Dmitry Filimonenkov, del sexto concurso universitario de programación de la Universidad Estatal de los Urales, 21 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un campo de `M × N` celdas unitarias (`0 ≤ M, N ≤ 50`) está pintado de
negro (`B`) y blanco (`W`). Cada vez que se visita una celda, cambian de
color todas las celdas cuyo centro está a distancia entera de su centro,
incluida la propia celda visitada (distancia 0). Dados los colores
finales y cuántas veces se visitó cada celda (hasta `2·10^9`), imprime los
colores iniciales.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

`M N`, luego `M` líneas con los colores finales y luego `M` líneas de `N`
números de visitas.

## Salida

`M` líneas con los colores iniciales.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 6
BWBBWW
BWBBWB
BBWWBW
BBBBBW
BBWWWW
BBWBBW
2 0 12 46 2 0
3 0 0 0 0 200
4 2 1 1 4 2
4 2 1 1 4 4
0 0 0 0 0 0
2 56 24 4 2 2
```

Salida:

```
WWBBWW
WBWWBW
WBBBBW
WBWWBW
WBWWBW
WBWWBW
```

## Solución

Solo importa la paridad de los cambios, y por tanto solo la paridad de
cada número de visitas. Una celda `(r, c)` cambia una vez por cada celda
con visitas impares en un desplazamiento `(dr, dc)` de longitud entera, es
decir con `dr² + dc²` cuadrado perfecto. En un campo de 50 × 50 solo hay
405 desplazamientos así: la propia celda, su fila y su columna, y los
pitagóricos como `(3, 4)`.

Cada fila de visitas impares se guarda como máscara de bits. Las celdas de
la fila `r` que cambia el desplazamiento `(dr, dc)` son la fila `r + dr`
desplazada `dc`, así que la paridad de cambios de toda la fila `r` es el
XOR de esas máscaras desplazadas sobre todos los desplazamientos.
Cambiando los colores finales según esa paridad se recupera el inicio.
`O(M · K)` operaciones con máscaras para `K ≤ 405` desplazamientos, unas
20 000.

Detalles a tener en cuenta:

- la celda visitada también cambia: la distancia 0 es entera;
- los números de visitas de hasta `2·10^9` solo importan por su paridad;
- `M` o `N` pueden ser 0, y entonces no hay celdas que imprimir.

Las respuestas se comprobaron con un cálculo directo sobre todos los
pares de celdas, sumando las visitas a distancia entera, en todas las
pruebas y en 30 campos aleatorios.

## Notas por lenguaje

- C++, Go, Java y Rust guardan las filas en palabras de 64 bits; Python
  usa sus enteros. Java desplaza con `>>>`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1125_bitmask.cpp](1125_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(M·K), K ≤ 405 offsets | AC | 0.001 s | 456 KB |
| [1125_bitmask.go](1125_bitmask.go) | Go 1.14 x64 | bitmask | O(M·K), K ≤ 405 offsets | AC | 0.031 s | 1092 KB |
| [1125_bitmask.java](1125_bitmask.java) | Java 1.8 | bitmask | O(M·K), K ≤ 405 offsets | AC | 0.078 s | 968 KB |
| [1125_bitmask.py](1125_bitmask.py) | Python 3.12 x64 | bitmask | O(M·K), K ≤ 405 offsets | AC | 0.046 s | 900 KB |
| [1125_bitmask.rs](1125_bitmask.rs) | Rust 1.75 x64 | bitmask | O(M·K), K ≤ 405 offsets | AC | 0.015 s | 240 KB |
