# 1214. Deshacer un procedimiento extraño

[Timus 1214](https://acm.timus.ru/problem.aspx?space=1&num=1214) · dificultad 102 · math

Problema original de Anatoly Uglov, del USU Open Collegiate Programming Contest, octubre de 2002, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un procedimiento recibe dos enteros `x` e `y`. Si ambos son positivos,
ejecuta `x + y` veces un cuerpo de bucle que hace `y ← x² + y`, luego
`x ← x² + y`, luego `y ← ⌊√(x − y)⌋`, y después resta `y` de `x` `2y`
veces; al final imprime `x` e `y`. A partir de lo impreso, ambos de
`−32000` a `32000`, hay que recuperar la entrada. Ninguna variable se
desborda nunca.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Los valores impresos `x` e `y`.

## Salida

Los valores de entrada `x` e `y`.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 1
```

Salida:

```
1 1
```

## Solución

Se sigue una vuelta del bucle desde `(x, y)`. Primero `y` pasa a valer
`x² + y`, luego `x` pasa a valer `2x² + y`. Su diferencia es `x²`, así que
la nueva `y` es `x`. Restarla `2x` veces quita `2x²` de `2x² + y` y deja
`y`. Así que cada vuelta solo intercambia los dos números, y la suma
`x + y`, que fija el número de vueltas, no cambia. Tras `x + y` vueltas
los números quedan intercambiados exactamente cuando la suma es impar.

Por tanto, el procedimiento intercambia su entrada cuando ambos números
son positivos y su suma es impar, y no cambia nada en otro caso. Esa
transformación es su propia inversa: se aplica la misma regla al par
impreso. `O(1)`.

Detalles a tener en cuenta:

- con un número cero o negativo el bucle no se ejecuta, así que ese par
  se imprime sin cambios;
- la paridad la decide la suma, no los números por separado.

Ejecutar el procedimiento en cada par de `−3` a `15` y deshacer el
resultado devolvió cada vez el par original.

## Notas por lenguaje

- Todos los lenguajes aplican la misma regla de una línea.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1214_math.cpp](1214_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1214_math.go](1214_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1068 KB |
| [1214_math.java](1214_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1584 KB |
| [1214_math.py](1214_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 444 KB |
| [1214_math.rs](1214_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 212 KB |
