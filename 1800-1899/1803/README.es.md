# 1803. Los fusiles de los checos

[Timus 1803](https://acm.timus.ru/problem.aspx?space=1&num=1803) · dificultad 716 · math

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
en base k, así que cada fusil requiere la suma de cifras de un número de
Fibonacci en billetes. F(50000) tiene unas 10⁴ cifras decimales, así que los
números se suman uno a partir de otro, guardados en base k. Las
soluciones compiladas guardan bloques en base k^m, la mayor potencia de
k que no pasa de un millón. Una tabla da la suma de cifras de cada
bloque, así que una suma da a la vez el número siguiente y su suma de
cifras. Una ordenación estable por la suma de cifras da el orden.
`O(n² / log B)` para bloques en base B.

La solución en Python guarda cada cifra en base k en un campo de 4 bits
de un entero grande. Cada campo de un sumando guarda cifra + 16 − k, así que desborda
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

## Soluciones optimizadas

En bases 2, 4 y 8 se cuentan los bits activos para obtener la suma de dígitos. Las demás bases usan una tabla de un byte por entrada para la suma de los dígitos de cada bloque.

G++ 13.2 x64, envío 11320151. Tiempo 0,375 → 0,14 s, memoria 4728 → 1380 KB.

Rust 1.75 x64, envío 11320179. Tiempo 0,359 → 0,187 s, memoria 6884 → 1420 KB.

En las demás bases, cada acarreo resta k − 1 a la suma de dígitos, de modo que el programa la actualiza contando los acarreos. Python 3.12 x64, envío 11320239. Tiempo 1,687 → 1,062 s, memoria 26824 → 29780 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321959 · Java 1.8 №11321967 · Rust 1.75 x64 №11321960 · Go 1.14 x64 №11322289 · Python 3.12 x64 №11322290.

Go 1.14 x64, envío 11322008. Tiempo 0,609 → 0,312 s, memoria 12108 → 2564 KB.

Java 1.8, envío 11322348. Tiempo 0,562 → 0,89 s, memoria 9876 → 3796 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1803_math.cpp](1803_math.cpp) | G++ 13.2 x64 | math | O(n^2 / log B) | AC | 0.375 s | 4728 KB | 11321959 |
| [1803_math.go](1803_math.go) | Go 1.14 x64 | math | O(n^2 / log B) | AC | 0.609 s | 12108 KB | 11322289 |
| [1803_math.java](1803_math.java) | Java 1.8 | math | O(n^2 / log B) | AC | 0.562 s | 9876 KB | 11321967 |
| [1803_math.py](1803_math.py) | Python 3.12 x64 | math | O(n^2) | AC | 1.687 s | 26824 KB | 11322290 |
| [1803_math.rs](1803_math.rs) | Rust 1.75 x64 | math | O(n^2 / log B) | AC | 0.359 s | 6884 KB | 11321960 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1803_math_optimized.cpp](1803_math_optimized.cpp) \* | G++ 13.2 x64 | math | O(n^2 / log B) | AC | 0.14 s | 1380 KB | 11320151 |
| [1803_math_optimized.rs](1803_math_optimized.rs) \* | Rust 1.75 x64 | math | O(n^2 / log B) | AC | 0.187 s | 1420 KB | 11320179 |
| [1803_math_optimized.py](1803_math_optimized.py) \* | Python 3.12 x64 | math | O(n^2) | AC | 1.062 s | 29780 KB | 11320239 |
| [1803_math_optimized.go](1803_math_optimized.go) | Go 1.14 x64 | math | O(n^2 / log B) | AC | 0.312 s | 2564 KB | 11322008 |
| [1803_math_optimized.java](1803_math_optimized.java) | Java 1.8 | math | O(n^2 / log B) | AC | 0.89 s | 3796 KB | 11322348 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
