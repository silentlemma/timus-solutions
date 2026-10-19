# 1831. La lección de Tsyfirkin

[Timus 1831](https://acm.timus.ru/problem.aspx?space=1&num=1831) · dificultad 2244 · probability

Problema original de Evgeny Kurpilyansky (idea de Alexander Ipatov), del XV Campeonato Abierto de los Urales de Programación Competitiva, abril de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un alumno suma dos números en columna, de derecha a izquierda.
Escribir una cifra o una marca de acarreo lleva un segundo. Sumar dos
números lleva un segundo si uno es 0 o 1 y dos segundos si no, pero una
suma ya calculada en esta lección, en cualquier orden, se recuerda en
un segundo. En cada posición el alumno suma las dos cifras, añade el
acarreo entrante si lo hay, escribe la última cifra y marca el acarreo
si hace falta; un acarreo que sale de la última posición se escribe
como cifra. Para dos números aleatorios de k cifras sin ceros a la
izquierda, hallar el tiempo esperado.

## Entrada

k (1 ≤ k ≤ 5000).

## Salida

El tiempo esperado, con error absoluto o relativo de como mucho 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
7.51530864
```

## Solución

Se reparte el tiempo por linealidad de la esperanza.

- Cada posición escribe una cifra y calcula una suma de cifras: 2k
  segundos, más un segundo por cada suma de dos cifras mayores que 1
  vista por primera vez.
- Cada acarreo se marca y luego o bien se suma en la posición siguiente
  (un segundo, pues uno de los sumandos es 1) o bien, al salir de la
  última posición, se escribe: dos segundos por acarreo.

Los acarreos forman una cadena de Márkov. Con cifras aleatorias 0 … 9
aparece un acarreo con probabilidad 45/100 sin acarreo entrante y
55/100 con él; en la posición principal las cifras son 1 … 9 y las
probabilidades son 45/81 y 53/81. Iterando la probabilidad de acarreo
posición a posición se obtiene el número esperado de acarreos.

Un par {a, b} de cifras de 2 … 9 aparece en una posición baja con
probabilidad 2/100 (1/100 si a = b) y en la principal con probabilidad
2/81 (1/81), de forma independiente entre posiciones. Así que aparece
al menos una vez con probabilidad 1 − (1 − q)^(k−1)(1 − r), y los 36
pares así suman estas probabilidades. `O(k)`.

Para k = 2: 4 segundos de escritura y sumas, acarreos 0.45 y 0.6 que
suman 2·1.05 = 2.1, y los pares vistos por primera vez suman 1.41531,
en total 7.51531.

Trampas:

- las cifras principales nunca son 0, así que la posición principal
  tiene sus propias probabilidades de acarreo y de pares;
- una suma con 0 o 1 nunca cuesta dos segundos, así que solo importa
  recordar pares de cifras de 2 … 9;
- sumar el acarreo es una suma aparte de un segundo.

Los valores coinciden con un recuento exhaustivo sobre todos los pares
de números para k hasta 3 y con una implementación aceptada
independiente para todos los k probados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1831_probability.cpp](1831_probability.cpp) | G++ 13.2 x64 | probability | O(k) | AC | 0.015 s | 148 KB |
| [1831_probability.go](1831_probability.go) | Go 1.14 x64 | probability | O(k) | AC | 0.031 s | 1080 KB |
| [1831_probability.java](1831_probability.java) | Java 1.8 | probability | O(k) | AC | 0.125 s | 1828 KB |
| [1831_probability.py](1831_probability.py) | Python 3.12 x64 | probability | O(k) | AC | 0.093 s | 524 KB |
| [1831_probability.rs](1831_probability.rs) | Rust 1.75 x64 | probability | O(k) | AC | 0.031 s | 252 KB |
