# 1813. Reproducción aleatoria

[Timus 1813](https://acm.timus.ru/problem.aspx?space=1&num=1813) · dificultad 1570 · number_theory

Problema original del Tavrida NU Akai Contest, sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La sucesión x₀ = 0, xᵢ = (a·xᵢ₋₁ + b) mod m debe pasar por cada número
de 0 a m − 1 una vez en sus m primeros términos y volver a 0. Sobre
todos los pares (a, b) con 0 ≤ a, b < m que lo cumplen, hallar la media
de a redondeada hacia abajo.

## Entrada

Hasta 100 líneas, cada una con m (1 < m < 10⁹).

## Salida

Para cada m, la media redondeada hacia abajo.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
36
100
123
```

Salida:

```
1
13
41
1
```

## Solución

La sucesión debe ser un único ciclo de longitud m, el periodo completo
de un generador lineal congruencial. Por el teorema de Hull–Dobell esto
ocurre exactamente cuando b es coprimo con m, a − 1 es divisible por
cada factor primo de m, y a − 1 es divisible por 4 si m lo es. Así que,
con c el producto de los primos distintos de m, duplicado cuando 4
divide a m, los valores buenos de a son 1, 1 + c, 1 + 2c, … menores que
m: m/c de ellos, ya que c divide a m. El número de b buenos no depende
de a, así que la media sobre los pares es la media de esta progresión,
(m − c + 2)/2. Factorizar m por división de prueba hasta √m cuesta
`O(√m)` por valor.

Para m = 36 = 2²·3², c = 2·3·2 = 12 y a es 1, 13 o 25, con media 13.
Para m = 123 = 3·41, c = 123 y solo sirve a = 1.

Trampas:

- el factor 2 extra para los múltiplos de 4: con m = 4 el valor a = 3
  falla;
- la media sobre pares es la media sobre a solo porque cada a bueno
  tiene el mismo número de b buenos;
- a = 0 nunca sirve, pues entonces la sucesión repite b.

Las respuestas coinciden con una simulación completa de todos los pares
(a, b) para todo m de 2 a 60, y con una implementación aceptada
independiente en valores aleatorios, productos de primos pequeños,
primos grandes y sus cuadrados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1813_number_theory.cpp](1813_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt(m)) per value | AC | 0.015 s | 128 KB |
| [1813_number_theory.go](1813_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt(m)) per value | AC | 0.031 s | 1104 KB |
| [1813_number_theory.java](1813_number_theory.java) | Java 1.8 | number_theory | O(sqrt(m)) per value | AC | 0.078 s | 528 KB |
| [1813_number_theory.py](1813_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt(m)) per value | AC | 0.093 s | 704 KB |
| [1813_number_theory.rs](1813_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt(m)) per value | AC | 0.031 s | 232 KB |
