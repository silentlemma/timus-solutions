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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1286_number_theory.cpp](1286_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 124 KB |
| [1286_number_theory.go](1286_number_theory.go) | Go 1.14 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 1092 KB |
| [1286_number_theory.java](1286_number_theory.java) | Java 1.8 | number_theory | O(log max(abs p, abs q)) | AC | 0.125 s | 1588 KB |
| [1286_number_theory.py](1286_number_theory.py) | Python 3.12 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.109 s | 464 KB |
| [1286_number_theory.rs](1286_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.031 s | 212 KB |
