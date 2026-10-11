# 1302. Onda delta

[Timus 1302](https://acm.timus.ru/problem.aspx?space=1&num=1302) · dificultad 351 · math

Problema original del Segundo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 3–4 de abril de 1998.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un triángulo infinito está dividido en triángulos unidad numerados fila
por fila: la fila 1 tiene la casilla 1, la fila 2 las casillas 2 a 4,
la fila k las 2k − 1 casillas de (k − 1)² + 1 a k², alternando
triángulos con la punta hacia arriba y hacia abajo. Un paso cruza una
arista hacia una casilla vecina (cruzar un vértice no vale). Hay que
hallar el mínimo de pasos de la casilla m a la n, 1 ≤ m, n ≤ 10⁹.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

m y n.

## Salida

La longitud de la ruta más corta.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 12
```

Salida:

```
3
```

## Solución

Las aristas de la malla están sobre tres familias de rectas paralelas:
las horizontales y dos familias inclinadas. Numeremos las franjas entre
las rectas de cada familia. Cada casilla tiene entonces tres números: su
fila r, su franja contada desde el borde izquierdo y su franja contada
desde el derecho. Para la casilla n con r = ⌈√n⌉ y lugar
p = n − (r − 1)² en su fila (de 1 a 2r − 1):

- franja izquierda ⌊(p + 1) / 2⌋, franja derecha ⌊(2r − p + 1) / 2⌋.

Cruzar una arista cruza exactamente una recta, así que cambia
exactamente uno de los tres números en 1. Por tanto toda ruta es al
menos tan larga como la suma de las tres diferencias, y en esta malla
esa suma siempre se alcanza, así que

respuesta = |Δfila| + |Δizquierda| + |Δderecha|.

En el ejemplo, la casilla 6 es (3, 1, 2) y la 12 es (4, 2, 3), así que
la respuesta es 1 + 1 + 1 = 3. La fila sale de una raíz cuadrada entera
exacta. `O(1)`.

Detalles a tener en cuenta:

- números consecutivos pueden estar lejos: k² cierra una fila y k² + 1
  abre la siguiente en el otro borde (pruebas 06 y 07);
- las casillas 1 y 2 solo se tocan en un vértice, así que están a 2
  pasos (prueba 03);
- la fila debe salir de una raíz cuadrada entera exacta: la fila acaba
  justo en k², y una raíz que falle por uno pone la casilla en otra
  fila.

La fórmula se comparó con una búsqueda en anchura sobre un tablero de
30 filas, para todos los pares con inicio menor que 120 y destino menor
que 625.

## Notas por lenguaje

- Python usa `math.isqrt`; los demás lenguajes ajustan una raíz en coma
  flotante hacia arriba o hacia abajo hasta que es exacta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1302_math.cpp](1302_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 132 KB |
| [1302_math.go](1302_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1068 KB |
| [1302_math.java](1302_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1576 KB |
| [1302_math.py](1302_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 504 KB |
| [1302_math.rs](1302_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 224 KB |
