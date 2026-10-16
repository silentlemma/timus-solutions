# 1803. Los fusiles de los checos

[Timus 1803](https://acm.timus.ru/problem.aspx?space=1&num=1803) · dificultad 717 · math

Problema original de Viktor Kamashev, de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El fusil i cuesta el i-ésimo número de Fibonacci en rublos (1, 1, 2,
3, …). Los billetes valen potencias de k, y cada fusil se paga con el
menor número de billetes. Ordenar los fusiles por el número de
billetes pagados, desempatando por el número de fusil.

## Entrada

k y n (2 ≤ k ≤ 10, 3 ≤ n ≤ 50000).

## Salida

Los números de los fusiles en el orden pedido.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 8
```

Salida:

```
1 2 3 4 8 7 5 6
```

## Solución

El menor número de billetes para una cantidad es la suma de sus cifras
en base k, así que cada fusil cuesta la suma de cifras de un número de
Fibonacci. F(50000) tiene unas 10⁴ cifras decimales, así que los
números se suman uno a partir de otro, guardados en base k. Las
soluciones compiladas guardan bloques en base k^m, la mayor potencia de
k que no pasa de un millón. Una tabla da la suma de cifras de cada
bloque, así que una suma da a la vez el número siguiente y su suma de
cifras. Una ordenación estable por la suma de cifras da el orden.
`O(n² / log B)` para bloques en base B.

La solución en Python guarda cada cifra en base k en un campo de 4 bits
de un entero grande. Cada campo guarda cifra + 16 − k, así que desborda
exactamente cuando la cifra en base k lleva acarreo, y una suma entera
normal propaga los acarreos. Los campos que acarrearon se hallan con el
o exclusivo de los sumandos y la suma, y recuperan el desplazamiento.
Los recuentos de bits de los cuatro planos de bits dan la suma de
cifras. Para k = 2 la suma de cifras es simplemente el número de unos.

En el ejemplo los precios son 1, 1, 2, 3, 5, 8, 13, 21 con sumas de
cifras 1, 1, 2, 3, 5, 8, 4, 3, lo que da 1 2 3 4 8 7 5 6.

Trampas:

- los números tienen miles de cifras, muy por encima de 64 bits;
- con igual número de billetes los fusiles van en orden creciente;
- convertir números grandes a texto en Python es demasiado lento para
  50000 de ellos.

Las respuestas coinciden con una implementación aceptada independiente
para cada base con la cantidad máxima y con muchas menores.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1803_math.cpp](1803_math.cpp) | G++ 13.2 x64 | math | O(n^2 / log B) | AC | 0.328 s | 4748 KB |
| [1803_math.go](1803_math.go) | Go 1.14 x64 | math | O(n^2 / log B) | AC | 0.593 s | 12320 KB |
| [1803_math.java](1803_math.java) | Java 1.8 | math | O(n^2 / log B) | AC | 0.531 s | 9896 KB |
| [1803_math.py](1803_math.py) | Python 3.12 x64 | math | O(n^2 / log B) | AC | 1.656 s | 26640 KB |
| [1803_math.rs](1803_math.rs) | Rust 1.75 x64 | math | O(n^2 / log B) | AC | 0.359 s | 6888 KB |
