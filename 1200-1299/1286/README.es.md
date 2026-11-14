# 1286. La nave de la fábrica VAZ

[Timus 1286](https://acm.timus.ru/problem.aspx?space=1&num=1286) · dificultad 654 · number_theory

Problema original de Alexander Klepinin, del Concurso Individual de la Universidad Estatal de los Urales 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una nave en el punto entero (x, y) solo puede saltar como un caballo
generalizado: (±p, ±q) o (±q, ±p). ¿Puede llegar a (x1, y1)? Todos los
números son enteros con valor absoluto como mucho 2 · 10⁹.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

p y q, luego x e y, y luego x1 e y1.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 6
0 0
10 10
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
4 6
0 0
9 9
```

Salida:

```
NO
```

## Solución

Sea g = mcd(|p|, |q|). Cada salto cambia ambas coordenadas en múltiplos
de g, así que el desplazamiento (dx, dy) debe ser divisible por g. Al
dividirlo todo por g quedan pasos coprimos a y b. Los saltos (a, b) y
(a, −b) suman (2a, 0), igual se alcanza (2b, 0), y por Bézout se
alcanzan (2, 0) y (0, 2). Entonces:

- si a y b son impares, cada salto cambia x + y en una cantidad par, así
  que dx/g + dy/g debe ser par; y el salto (a, b) desplazado por
  múltiplos de (2, 0) y (0, 2) da (1, 1), así que todos esos puntos se
  alcanzan;
- si no, pongamos a impar y b par: el salto (a, b) desplazado igual da
  (1, 0), el salto (b, a) da (0, 1), y se alcanza cualquier punto.

Si p = q = 0 la nave no puede moverse. `O(log max(|p|, |q|))`.

Detalles a tener en cuenta:

- p y q pueden ser ambos cero (pruebas 03, 04), o solo uno de ellos
  (prueba 05);
- los pasos pueden ser negativos (prueba 11);
- el desplazamiento llega a 4 · 10⁹, más que 32 bits (pruebas 08, 09);
- en los lenguajes tipo C el resto de un impar negativo es −1, así que
  la imparidad se comprueba con `% 2 != 0`.

Las respuestas se compararon con una búsqueda en anchura en un tablero
grande para todos los pasos de 0 a 4 y todos los destinos a menos de 8
del inicio.

## Notas por lenguaje

- Todos los lenguajes calculan el mismo mcd y la misma prueba de paridad.
  C++, Go, Java y Rust usan enteros con signo de 64 bits; Python usa
  enteros de precisión arbitraria.

## Soluciones optimizadas

Las versiones optimizadas comprueban la paridad mediante restos módulo el doble del máximo común divisor. Las coordenadas y los pasos conservan sus unidades originales.

Python 3.12 x64, envío 11318499. Tiempo 0,109 → 0,078 s, memoria 400 → 436 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322401 · Go 1.14 x64 №11322465 · Java 1.8 №11322466 · Python 3.12 x64 №11322467 · Rust 1.75 x64 №11322468.

Java 1.8, envío 11322444. Tiempo 0,093 → 0,093 s, memoria 1560 → 360 KB.

Go 1.14 x64, envío 11322469. Tiempo 0,015 → 0,015 s, memoria 1068 → 304 KB.

Rust usa el MCD binario para la divisibilidad y compara las potencias de dos para saber si ambos pasos normalizados son impares. Rust 1.75 x64, envío 11323306. Tiempo 0,015 → 0,015 s, memoria 208 → 52 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1286_number_theory.cpp](1286_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 112 KB | 11322401 |
| [1286_number_theory.go](1286_number_theory.go) | Go 1.14 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 1068 KB | 11322465 |
| [1286_number_theory.java](1286_number_theory.java) | Java 1.8 | number_theory | O(log max(abs p, abs q)) | AC | 0.093 s | 1560 KB | 11322466 |
| [1286_number_theory.py](1286_number_theory.py) | Python 3.12 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.109 s | 400 KB | 11322467 |
| [1286_number_theory.rs](1286_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 208 KB | 11322468 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1286_number_theory_optimized.py](1286_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.078 s | 436 KB | 11318499 |
| [1286_number_theory_optimized.java](1286_number_theory_optimized.java) | Java 1.8 | number_theory | O(log max(abs p, abs q)) | AC | 0.093 s | 360 KB | 11322444 |
| [1286_number_theory_optimized.go](1286_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 304 KB | 11322469 |
| [1286_number_theory_optimized.rs](1286_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 52 KB | 11323306 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
