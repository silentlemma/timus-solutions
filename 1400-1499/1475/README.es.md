# 1475. La gallina Riaba

[Timus 1475](https://acm.timus.ru/problem.aspx?space=1&num=1475) · dificultad 3694 · math

Problema original de Alexander Ipatov (idea de Alexander Toropov), del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La vertiente izquierda de un tejado sube desde (0, 0) pasando por
(l, H), que no es la cumbre. Un huevo se suelta a una altura h sobre
(l, H), cae con g = 10, rebota elásticamente en la vertiente (el ángulo
de incidencia es igual al de reflexión, incluso en el punto más bajo) y
así sucesivamente hasta salir del tejado. Hay que contar los golpes en
hasta 1000 pruebas con 1 ≤ H, l ≤ 10¹⁰⁰ y 1 ≤ h ≤ 10.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

El número de pruebas y luego líneas H l h.

## Salida

El número de golpes de cada prueba.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1 2 1
1 2 10
```

Salida:

```
1
1
```

## Solución

Sea a el ángulo de la vertiente con el suelo y tómense ejes a lo largo
de ella, cuesta abajo, y perpendicular a ella. La gravedad tiene
entonces componentes g·sin a a lo largo y −g·cos a perpendicular. El
huevo llega con velocidad v = √(2gh) en vertical; tras el golpe se
aleja de la vertiente a v·cos a y baja por ella a v·sin a. El movimiento
perpendicular es el mismo tras cada golpe, así que cada vuelo dura
2v/g, mientras que la velocidad a lo largo crece 2v·sin a por vuelo.
Sumando los vuelos, el k-ésimo golpe tras el primero queda
4h·sin a·k(k + 1) más abajo.

La vertiente desde (l, H) hasta abajo mide L = √(l² + H²) y
sin a = H / L, así que ese golpe ocurre cuando 4hH·k(k + 1) ≤ l² + H².
Con q = ⌊(l² + H²) / (4hH)⌋, el mayor k así cumple (2k + 1)² ≤ 4q + 1,
es decir, k = (⌊√(4q + 1)⌋ − 1) / 2, y la respuesta es k + 1 contando
el primer golpe. `O(D²)` por prueba para números de D cifras.

Detalles a tener en cuenta:

- H y l llegan a 10¹⁰⁰ y sus cuadrados a 10²⁰⁰, así que todo debe ser
  entero exacto; la coma flotante falla en el límite (prueba 02, gen3);
- un golpe justo en el punto más bajo de la vertiente también cuenta
  (prueba 02);
- la respuesta es al menos 1, aunque h sea grande y la vertiente corta
  (pruebas 01, 03).

## Notas por lenguaje

- C++ y Rust no traen enteros grandes: las soluciones guardan los
  números en bloques de 32 bits y fijan k bit a bit desde arriba,
  comprobando 4hH·k(k + 1) ≤ l² + H² solo con multiplicaciones; es
  `O(D³)` por prueba, rápido igualmente para 100 cifras.
- Java 8 no tiene `BigInteger.sqrt`, así que la raíz se calcula con el
  método de Newton.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1475_math.cpp](1475_math.cpp) | G++ 13.2 x64 | math | O(D^2) per test | AC | 0.046 s | 208 KB |
| [1475_math.go](1475_math.go) | Go 1.14 x64 | math | O(D^2) per test | AC | 0.015 s | 2020 KB |
| [1475_math.java](1475_math.java) | Java 1.8 | math | O(D^2) per test | AC | 0.125 s | 4748 KB |
| [1475_math.py](1475_math.py) | Python 3.12 x64 | math | O(D^2) per test | AC | 0.062 s | 604 KB |
| [1475_math.rs](1475_math.rs) | Rust 1.75 x64 | math | O(D^2) per test | AC | 0.046 s | 356 KB |
