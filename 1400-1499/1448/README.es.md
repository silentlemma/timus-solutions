# 1448. Iluminación en Hogwarts

[Timus 1448](https://acm.timus.ru/problem.aspx?space=1&num=1448) · dificultad 580 · constructive

Problema original de Alexander Mironenko (idea) y Stanislav Vasiliev (texto y programación), del Décimo Campeonato Universitario de Programación por Equipos de los Urales, 24–25 de marzo de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un pasillo tiene N lámparas en fila (1 ≤ N ≤ 10⁶), cada una encendida
del todo o apagada. Argus Filch quiere un brillo de b por ciento
(0 ≤ b ≤ 100) repartido lo más uniformemente posible: hay que imprimir
una fila de N cifras 0 y 1 tal que en cada tramo de L lámparas seguidas
el número de encendidas difiera de L b / 100 como mucho en 2.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego b.

## Salida

La fila de lámparas. Se acepta cualquier fila válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
33
```

Salida:

```
0100100100
```

## Solución

La lámpara i (contando desde 0) se enciende justo cuando
⌊(i + 1) b / 100⌋ es mayor que ⌊i b / 100⌋. Entonces entre las k
primeras hay ⌊k b / 100⌋ encendidas, así que un tramo de l a r tiene
⌊r b / 100⌋ − ⌊l b / 100⌋, que difiere de (r − l) b / 100 en menos de
1, holgadamente dentro de los 2 permitidos. El patrón se repite cada 100
lámparas, porque sumar 100 a i suma exactamente b a ambas partes enteras.
`O(N)`.

Detalles a tener en cuenta:

- con b = 0 y b = 100 la fila tiene cifras idénticas (pruebas 02, 03, 05,
  gen1, gen2);
- almacena hasta un millón de cifras en un búfer para evitar una llamada
  por cifra (gen1 a gen7);
- la fila del ejemplo es solo una de muchas respuestas válidas.

## Soluciones optimizadas

La variante C++ genera un período manteniendo el resto módulo 100. Lo copia en un búfer fijo
de longitud múltiplo de 100 e imprime bloques completos y el prefijo final. La secuencia es
la misma, con tiempo O(N) y memoria adicional O(1). El envío 11316954 usó 112 KB frente a 1144 KB de la versión sencilla. Ambos tardaron 0.015 s.

Go llena el bloque de salida de tamaño fijo duplicando con `copy` el prefijo ya generado. El envío 11317198 tardó 0,015 s y usó 924 KB frente a 0,031 s y 2056 KB en la base.

Java repite el período con `System.arraycopy` y escribe bloques de tamaño fijo directamente en el flujo de salida. El envío 11317199 tardó 0.109 s y usó 364 KB, frente a 0.125 s y 3076 KB de la versión sencilla.

Python repite un período de 100 lámparas para formar un bloque de bytes de tamaño fijo, luego escribe los bloques completos y el prefijo final. El envío 11317212 usó 432 KB frente a 2276 KB de la versión sencilla. Ambos tardaron 0.078 s.

Rust llena un bloque fijo duplicando el período de 100 lámparas y escribe los bloques completos y el prefijo final. El envío 11317214 usó 204 KB y tardó 0,046 s frente a 2048 KB y 0,031 s en la base.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322145 · Go 1.14 x64 №11322146 · Java 1.8 №11322147 · Python 3.12 x64 №11322148 · Rust 1.75 x64 №11322149.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1448_constructive.cpp](1448_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 1144 KB | 11322145 |
| [1448_constructive.go](1448_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 2056 KB | 11322146 |
| [1448_constructive.java](1448_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.125 s | 3076 KB | 11322147 |
| [1448_constructive.py](1448_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 2276 KB | 11322148 |
| [1448_constructive.rs](1448_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 2048 KB | 11322149 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1448_constructive_optimized.cpp](1448_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 112 KB | 11316954 |
| [1448_constructive_optimized.go](1448_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 924 KB | 11317198 |
| [1448_constructive_optimized.java](1448_constructive_optimized.java) | Java 1.8 | constructive | O(N) | AC | 0.109 s | 364 KB | 11317199 |
| [1448_constructive_optimized.py](1448_constructive_optimized.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 432 KB | 11317212 |
| [1448_constructive_optimized.rs](1448_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 204 KB | 11317214 |

\* El corte de clasificación no contiene envíos comparables en Go de otros autores. En el corte de clasificación, Rust ocupa el segundo lugar en tiempo y el primero en memoria. La versión cumple el criterio de ahorro de memoria.
