# 1626. Segmento que interfiere

[Timus 1626](https://acm.timus.ru/problem.aspx?space=1&num=1626) · dificultad 7564 · geometry

Problema original del SPbSU ITMO Contest en el campus de Petrozavodsk, invierno de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un polígono simple tiene N vértices (3 ≤ N ≤ 800, coordenadas enteras de
valor absoluto a lo sumo 10⁴, sin tres vértices consecutivos alineados),
y un segmento S está estrictamente dentro de él. Las triangulaciones
aquí usan solo vértices del polígono, y ningún vértice puede estar en un
lado de un triángulo salvo sus propias esquinas. Halla un triángulo de
alguna triangulación que contenga S estrictamente dentro e imprime sus
tres números de vértice, o imprime `Impossible`. Se acepta cualquier
triángulo así.

Límite de tiempo: 5 segundos. Límite de memoria: 64 MB.

## Entrada

N, los vértices en orden y luego los extremos de S.

## Salida

Tres números de vértice, o `Impossible`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 0
0 3
4 3
1 2 2 2
```

Salida:

```
1 2 3
```

### Ejemplo 2

Entrada:

```
4
0 0
2 0
2 3
0 3
1 1 1 2
```

Salida:

```
Impossible
```

## Solución

Un triángulo pertenece a alguna triangulación exactamente cuando sus
lados son aristas del polígono o diagonales (dentro del polígono, sin
tocar otros vértices) y no hay vértices dentro: el resto del polígono se
parte entonces en polígonos más pequeños que se pueden triangular. Así
que la tarea es hallar un triángulo así alrededor de S.

Todo se hace con conjuntos de bits de los N vértices. Tras orientar el
polígono en sentido antihorario, para cada par a < b se guarda el
conjunto de vértices estrictamente a la izquierda de la recta a → b. Un
par i, j es una diagonal si j está dentro del ángulo interior en i e i
dentro del de j, si ninguna arista cruza propiamente el segmento y si no
hay vértices sobre él. Las aristas que podrían cruzarlo se hallan de una
vez: sus dos extremos difieren en estar a la izquierda de la recta i → j
(el conjunto izquierdo combinado por xor consigo mismo desplazado una
posición), y su recta separa i de j; solo esas pocas se comprueban
exactamente.

Luego, para cada diagonal o arista a → b con ambos extremos de S
estrictamente a su izquierda, los terceros vértices k son los vecinos
comunes de a y b que además dejan ambos extremos de S dentro del
triángulo, otra vez un «y» de conjuntos de bits. El triángulo a, b, k
está vacío cuando los tres conjuntos izquierdos no tienen ningún vértice
común aparte de sus esquinas. El primer triángulo así es la respuesta.
`O(N³ / 64)` operaciones de palabra.

Python construye los conjuntos izquierdos de otra forma: alrededor de
cada vértice los demás se ordenan por ángulo, así que cada conjunto
izquierdo es un rango circular de ese orden y sale de dos conjuntos de
prefijo con O(1) operaciones de números grandes, mientras que el vértice
más cercano en cada dirección marca qué segmentos no tienen otros
vértices. Solo guarda los conjuntos del vértice actual, así que la
prueba de triángulo vacío mira las esquinas: ninguna arista del
polígono en una esquina puede apuntar hacia el triángulo. El borde no
puede cruzar los lados, así que queda fuera, y con él todos los
vértices.

Detalles a tener en cuenta:

- un vértice puede estar exactamente sobre una supuesta diagonal
  (pruebas 03, 04);
- en un rectángulo ambas diagonales pueden cruzar S (el segundo
  ejemplo);
- el triángulo del ejemplo puede imprimirse con sus esquinas en
  cualquier orden, así que un verificador comprueba cada condición.

Las respuestas pasan el verificador en todas las pruebas, y una
implementación aceptada independiente da el mismo veredicto en cada
polígono generado.

## Notas por lenguaje

- Python se ejecuta con PyPy: CPython tarda unos 2,4 s en las pruebas más
  grandes de aquí con un límite de 5 s, demasiado justo para el juez, y
  PyPy unos 0,9 s. PyPy libera las máscaras de bits de vida corta solo
  al recolectar, por eso la solución llama al recolector cada 64 filas;
  sin eso la basura sola superaba el límite de 64 MB.
- Java construye los conjuntos izquierdos con aritmética int, que las
  coordenadas de hasta 10⁴ permiten; eso reduce su tiempo a la mitad.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1626_geometry.cpp](1626_geometry.cpp) | G++ 13.2 x64 | geometry | O(N³ / 64) | AC | 1.468 s | 35068 KB |
| [1626_geometry.go](1626_geometry.go) | Go 1.14 x64 | geometry | O(N³ / 64) | AC | 2.343 s | 40844 KB |
| [1626_geometry.java](1626_geometry.java) | Java 1.8 | geometry | O(N³ / 64) | AC | 4.531 s | 41600 KB |
| [1626_geometry.py](1626_geometry.py) | PyPy 3.10 x64 | geometry | O(N³ / 64) | AC | 3.281 s | 17224 KB |
| [1626_geometry.rs](1626_geometry.rs) | Rust 1.75 x64 | geometry | O(N³ / 64) | AC | 2.500 s | 37932 KB |
