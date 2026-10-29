# 1457. La tubería de calefacción

[Timus 1457](https://acm.timus.ru/problem.aspx?space=1&num=1457) · dificultad 69 · math

Problema original de Nikita Rybak, Dmitry Kovalioff e Ilya Grebnov, de Timus Top Coders: Second Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tubería de calefacción recta pasa bajo N lugares (1 ≤ N ≤ 1000) en
las posiciones P[i] (0 ≤ P[i] ≤ 10⁶). El esfuerzo de recorrer una
distancia es proporcional a su cuadrado. Hay que hallar el punto de la
tubería con el menor esfuerzo medio para llegar a los lugares, con al
menos seis cifras tras el punto decimal.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego las N posiciones.

## Salida

El mejor punto.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
7 4 5
```

Salida:

```
5.333333
```

## Solución

La media de (x − P[i])² es una parábola en x cuya derivada
2 (x − media) se anula en la media aritmética de las posiciones, así
que la respuesta es la suma dividida entre N. La suma es como mucho 10⁹
y cabe en un entero de 32 bits con signo. `O(N)`.

Detalles a tener en cuenta:

- el redondeo a seis cifras puede variar entre lenguajes cuando la media
  termina justo en un cinco, como 1/128 (prueba 05); se acepta cualquier
  respuesta dentro de la precisión pedida.

## Soluciones optimizadas

La solución optimizada en Java analiza los números a mano en lugar de
`Scanner` e imprime la media sin formateador: redondea el valor exacto
con enteros, `(sum · 10⁶ + N / 2) / N`, y escribe la parte entera y seis
cifras de la parte fraccionaria: 412 KB en lugar de 2612 KB, con el
mismo tiempo.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1457_math.cpp](1457_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.001 s | 144 KB | 11286425 |
| [1457_math.go](1457_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1120 KB | 11286427 |
| [1457_math.java](1457_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 2612 KB | 11286431 |
| [1457_math.py](1457_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 504 KB | 11286429 |
| [1457_math.rs](1457_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 252 KB | 11286434 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1457_math_optimized.java](1457_math_optimized.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 412 KB | 11303608 |
