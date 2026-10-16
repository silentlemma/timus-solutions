# 1761. Palíndromo binario

[Timus 1761](https://acm.timus.ru/problem.aspx?space=1&num=1761) · dificultad 1094 · strings

Problema original de Ilya Zvigintsev, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Escribir los números de 1 a n en binario uno tras otro. Hallar la
longitud del palíndromo más largo en la cadena de ceros y unos
resultante.

## Entrada

n en binario (1 ≤ n ≤ 2¹⁰⁰⁰⁰⁰⁰), es decir, hasta un millón y una
cifras.

## Salida

La longitud del palíndromo más largo.

## Ejemplos

### Ejemplo 1

Entrada:

```
101
```

Salida:

```
5
```

### Ejemplo 2

Entrada:

```
10100
```

Salida:

```
11
```

## Solución

Sea k el número de cifras binarias de n. Tres números seguidos de k
cifras dan un palíndromo: 2^(k−1) + 5 = 1 0…0 101, luego
2^(k−1) + 6 = 1 0…0 110 y luego las primeras k − 2 cifras de
2^(k−1) + 7 = 1 0…0 111, es decir 1 0…0 1, donde cada 0…0 tiene k − 4
ceros. Escrito, 1 0…0 1011 0…0 1101 0…0 1 se lee igual en ambos
sentidos y tiene 3k − 2 cifras. Aparece en cuanto n llega a
2^(k−1) + 7, lo que ocurre cuando tras la cifra inicial hay un uno en
algún lugar antes de las tres últimas, o cuando esas tres son todas
unos. Si no, el mismo patrón con una longitud menos da 3(k − 1) − 2.

Que no aparece nada más largo se comprueba aquí, no se demuestra: el
palíndromo más largo, hallado con el algoritmo de Manacher sobre toda
la cadena, coincide con la fórmula para todo n hasta 300 y, como añadir
números solo puede alargarlo, en ambos extremos de cada tramo de n con
una misma respuesta para cada k de 6 a 20. Por debajo de 32 el patrón
aún no vale y la cadena es lo bastante corta para buscar directamente.
Todo el trabajo es leer las cifras: `O(k)`.

Para n = 39 = 100111 la cadena termina en 100101 100110 100111, y
1001011001101001 es el palíndromo de 16 = 3·6 − 2 cifras.

Trampas:

- n tiene hasta un millón de cifras, así que nunca se convierte en
  número;
- el salto de 3k − 5 a 3k − 2 llega en 2^(k−1) + 7, no en 2^(k−1);
- la fórmula falla por debajo de 32; por ejemplo, n = 20 da 11, no 10.

Las respuestas coinciden con una implementación aceptada independiente
en 60 entradas aleatorias, incluidas entradas de un millón y una cifras
justo alrededor de 2^(k−1) + 7.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1761_strings.cpp](1761_strings.cpp) | G++ 13.2 x64 | strings | O(k) for k digits | AC | 0.046 s | 156 KB |
| [1761_strings.go](1761_strings.go) | Go 1.14 x64 | strings | O(k) for k digits | AC | 0.031 s | 1080 KB |
| [1761_strings.java](1761_strings.java) | Java 1.8 | strings | O(k) for k digits | AC | 0.125 s | 504 KB |
| [1761_strings.py](1761_strings.py) | Python 3.12 x64 | strings | O(k) for k digits | AC | 0.093 s | 3044 KB |
| [1761_strings.rs](1761_strings.rs) | Rust 1.75 x64 | strings | O(k) for k digits | AC | 0.031 s | 244 KB |
