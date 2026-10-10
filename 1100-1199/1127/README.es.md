# 1127. La torre de cubos más alta con cada uno de sus cuatro lados de un solo color

[Timus 1127](https://acm.timus.ru/problem.aspx?space=1&num=1127) · dificultad 322 · bruteforce

Problema original de Ekaterina Vasilyeva, del sexto concurso universitario de programación de la Universidad Estatal de los Urales, 21 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` cubos (`1 < N ≤ 1000`); cada cara de un cubo tiene un color (una
de 10 letras), y las seis caras de un cubo son todas distintas. Las caras
se dan como delantera, derecha, izquierda, trasera, superior e inferior.
Apila tantos cubos como sea posible, girando cada uno como se quiera, de
modo que cada una de las cuatro caras laterales de la torre sea de un solo
color. Imprime la altura.

Límite de tiempo: 0,4 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas de seis letras de color.

## Salida

La mayor altura.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
GYVABW
AOCGYV
CABVGO
OVYWGA
```

Salida:

```
3
```

## Solución

Una torre queda determinada por el anillo de colores de sus lados:
delantero, derecho, trasero, izquierdo. Un cubo encaja en un anillo si
una de sus 24 orientaciones muestra exactamente ese anillo. Como sus seis
colores son distintos, un cubo muestra cada anillo en como mucho una
orientación, así que contar para cada anillo los cubos que pueden
mostrarlo da la altura de la torre más alta con ese anillo. Las 24
orientaciones se generan una vez a partir de dos cuartos de vuelta, uno
alrededor del eje vertical y otro alrededor del eje izquierda-derecha,
como permutaciones de las seis posiciones de las caras. `O(24·N)`.

Detalles a tener en cuenta:

- los giros deben ser rotaciones, no reflexiones: un cuarto de vuelta
  lleva la cara delantera a la derecha, la derecha atrás, y así
  sucesivamente, conservando la orientación;
- la imagen especular de un cubo también encaja: volteada alrededor del
  eje delante-detrás muestra el mismo anillo de lados, solo con arriba y
  abajo intercambiados, y esos no importan;
- los colores de las caras superior e inferior nunca importan.

Las respuestas se comprobaron con una construcción aparte de las 24
rotaciones como matrices de permutación con signo y determinante +1 que
actúan sobre las normales de las caras, en todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes generan las orientaciones con una pequeña búsqueda
  sobre los dos giros y cuentan los anillos en una tabla hash.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1127_bruteforce.cpp](1127_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(24·N) | AC | 0.015 s | 300 KB |
| [1127_bruteforce.go](1127_bruteforce.go) | Go 1.14 x64 | bruteforce | O(24·N) | AC | 0.031 s | 1344 KB |
| [1127_bruteforce.java](1127_bruteforce.java) | Java 1.8 | bruteforce | O(24·N) | AC | 0.171 s | 6664 KB |
| [1127_bruteforce.py](1127_bruteforce.py) | Python 3.12 x64 | bruteforce | O(24·N) | AC | 0.093 s | 768 KB |
| [1127_bruteforce.rs](1127_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(24·N) | AC | 0.031 s | 440 KB |
