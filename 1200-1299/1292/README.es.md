# 1292. Estaciones espaciales marcianas

[Timus 1292](https://acm.timus.ru/problem.aspx?space=1&num=1292) · dificultad 380 · math

Problema original de Denis Musin, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sea F(x) la suma de los cubos de las cifras decimales de x, así que
F(12) = 9. Unas bases espaciales están a lo largo de una ruta: la
primera a distancia K del extremo de la ruta, y si el tramo antes de la
base i mide x, el tramo después mide F(x). La clave K es múltiplo de 3.

Una nave está entre las bases N − 1 y N, a distancia L de la base
N − 1. Para cada una de T ≤ 33 333 consultas con 2 ≤ N ≤ 33 333 y
3 ≤ K ≤ 33 333, hay que imprimir la distancia de la nave a la base N.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

T y luego T líneas con N, K y L.

## Salida

T líneas con las distancias.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
4 6 123
7 93 49
```

Salida:

```
18
104
```

## Solución

Si el extremo de la ruta cuenta como base 0, el tramo antes de la base
N es F aplicada N − 1 veces a K, y la respuesta es ese tramo menos L. El
ejemplo lo confirma: 6 → 216 → 225 → 141, y 141 − 123 = 18.

Aplicar F hasta 33 332 veces por consulta sería demasiado lento para
33 333 consultas, pero la cadena se estabiliza casi enseguida. Como
d³ ≡ d (mod 3), F conserva el resto de la suma de cifras módulo 3, así
que los múltiplos de 3 siguen siéndolo. F(153) = 1 + 125 + 27 = 153, y
al comprobar todos los múltiplos de 3 hasta 33 333 se ve que cada uno
llega a 153 en 14 pasos como mucho (el más lento es 12 558). Por eso F
se aplica hasta completar N − 1 pasos o llegar a 153.
`O(T · 14 · cifras)`.

Detalles a tener en cuenta:

- el tramo antes de la base N lleva N − 1 pasos, no N − 2: la primera
  base ya está a K del extremo (prueba 01);
- una cadena puede cortarse justo antes de llegar a 153 (prueba 03);
- el tramo puede ser mucho mayor que K, por ejemplo F(99) = 1458
  (prueba 05).

Las respuestas se compararon con aplicar F las N − 1 veces completas.

## Soluciones optimizadas

Ambas versiones procesan cada consulta hasta el paso pedido o el punto fijo 153 y escriben con un búfer acotado. Go consulta los cubos de las cifras en una tabla de diez entradas. C++ suma dos resultados precalculados para bloques de tres cifras y mantiene el desplazamiento y la resta en enteros con signo de 64 bits. Go también usa desplazamientos de 64 bits con signo y búferes de bytes para entrada y salida, sin crear una cadena por número. El espacio auxiliar es constante.

Las implementaciones base aceptadas [1292_math.java](1292_math.java), [1292_math.py](1292_math.py), [1292_math.rs](1292_math.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- L no tiene cota superior indicada. Python usa enteros de precisión
  arbitraria; los demás lenguajes, enteros de 64 bits.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1292_math.cpp](1292_math.cpp) | G++ 13.2 x64 | math | O(T * 14 * digits) | AC | 0.046 s | 136 KB | 11284589 |
| [1292_math.go](1292_math.go) | Go 1.14 x64 | math | O(T * 14 * digits) | AC | 0.015 s | 1452 KB | 11284591 |
| [1292_math.java](1292_math.java) \* | Java 1.8 | math | O(T * 14 * digits) | AC | 0.109 s | 4740 KB | 11284593 |
| [1292_math.py](1292_math.py) \* | Python 3.12 x64 | math | O(T * 14 * digits) | AC | 0.265 s | 7972 KB | 11284592 |
| [1292_math.rs](1292_math.rs) \* | Rust 1.75 x64 | math | O(T * 14 * digits) | AC | 0.001 s | 2124 KB | 11284596 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1292_math_optimized.cpp](1292_math_optimized.cpp) | G++ 13.2 x64 | math | O(T · 14 · digits) | AC | 0.015 s | 84 KB | 11310876 |
| [1292_math_optimized.go](1292_math_optimized.go) \* | Go 1.14 x64 | math | O(T · 14 · digits) | AC | 0.001 s | 800 KB | 11311114 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
