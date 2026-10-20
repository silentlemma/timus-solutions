# 2171. Números hasta N cubiertos por alguna de K progresiones aritméticas

[Timus 2171](https://acm.timus.ru/problem.aspx?space=1&num=2171) · dificultad 1518 · math, number_theory

Problema original de Konstantin Rychkov, del Concurso Escolar de Programación de los Urales 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Contar los enteros de 1 a N que pertenecen a al menos una de K
progresiones aritméticas crecientes infinitas bᵢ, bᵢ + dᵢ, … Los límites
son 2 segundos y 256 MB.

## Entrada

N y K, 1 ≤ N ≤ 10⁹, 1 ≤ K ≤ 18, y luego los pares bᵢ, dᵢ,
1 ≤ bᵢ, dᵢ ≤ 10⁹.

## Salida

La cuenta.

## Ejemplos

### Ejemplo 1

Entrada:

```
15 2
3 5
6 2
```

Salida:

```
7
```

## Solución

Por inclusión y exclusión la respuesta es la suma sobre los subconjuntos
no vacíos de progresiones de (−1)^(tamaño + 1) por el número de valores
hasta N comunes a todas ellas. Los valores comunes de varias
progresiones forman otra progresión, o nada: dos se encuentran cuando la
diferencia de sus inicios es divisible por el mcd de los pasos, y
entonces el algoritmo de Euclides extendido da el primer valor común no
anterior a ambos inicios, con el mcm como paso (el teorema chino del
resto).

Los subconjuntos se recorren en profundidad, añadiendo una progresión
cada vez a la intersección actual. Una rama se detiene en cuanto la
intersección está vacía o empieza después de N, porque añadir más
progresiones no puede recuperarla. Cuando el paso supera lo que queda
hasta N, la intersección es un único valor y se guarda con paso 0, lo
que además mantiene pequeños los números. Se visitan a lo sumo 2¹⁸
subconjuntos, cada uno en O(log).

En el ejemplo 3, 8, 13 y 6, 8, 10, 12, 14 comparten el 8, así que la
respuesta es 3 + 5 − 1 = 7.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2171_math_number_theory.cpp](2171_math_number_theory.cpp) | G++ 13.2 x64 | math, number_theory | O(2^K log C) | AC | 0.031 s | 216 KB |
| [2171_math_number_theory.go](2171_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(2^K log C) | AC | 0.046 s | 900 KB |
| [2171_math_number_theory.java](2171_math_number_theory.java) | Java 1.8 | math, number_theory | O(2^K log C) | AC | 0.156 s | 312 KB |
| [2171_math_number_theory.py](2171_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(2^K log C) | AC | 0.703 s | 492 KB |
| [2171_math_number_theory.rs](2171_math_number_theory.rs) | Rust 1.75 x64 | math, number_theory | O(2^K log C) | AC | 0.046 s | 24 KB |
