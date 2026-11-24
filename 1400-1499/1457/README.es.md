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

## Evaluación

Las pruebas del repositorio comparan tokens numéricos con |resultado-referencia| <= 0.0000011·max(1,|referencia|), rechazan valores no finitos y comparan exactamente los tokens no numéricos.

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

`1457_math_optimized.py`. Lee todos los enteros de la entrada binaria en una lista. El primer elemento es el número de posiciones N. La suma comienza en −N para cancelar la cabecera y obtener exactamente la suma de las coordenadas. Así, la función sum recorre la lista sin copiar una porción. Divide el total por N e imprime seis decimales. Tanto el tiempo como el espacio auxiliar son O(N).

La versión sencilla en CPython obtuvo 0.078 s / 504 KB en el envío #11286429. La implementación anterior en PyPy obtuvo 0.156 s / 248 KB en el envío #11324843. El nuevo envío #11328147 en CPython obtuvo 0.062 s / 432 KB.

`1457_math_optimized.rs`. Conserva la media que minimiza la suma de distancias cuadradas. Suma exactamente N posiciones enteras y realiza solo la división final flotante con seis decimales. N<=1000 y posiciones<=10^6 acotan la suma a10^9, exacta en f64. Tiempo O(N), mismo significado y precisión. Acumula al leer, eliminando String y vector. Estado auxiliar O(1); printf emite la única media f64. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1457_math.rs`: tiempo 0.015 s → 0.031 s; memoria 252 KB → 88 KB.

La solución optimizada en Java analiza los números a mano en lugar de
`Scanner` e imprime la media sin formateador: redondea el valor exacto
con enteros, `(sum · 10⁶ + N / 2) / N`, y escribe la parte entera y seis
cifras de la parte fraccionaria: 412 KB en lugar de 2612 KB, con el
mismo tiempo.

## Notas por lenguaje

La comparación de Rust usa la muestra del 18 de noviembre de 2026. Ambas muestras consideran otros autores en los compiladores actuales y asignan el mismo puesto a los empates.

`1457_math_optimized.py`. En la muestra del 18 de noviembre de 2026, el envío de CPython ocupa el puesto 3/71 en tiempo y el 23/71 en memoria. Con un consumo de 432 KB, el puesto en tiempo basta para la admisión estricta. El asterisco señala la meta independiente de alcanzar el primer puesto en ambas métricas.

`1457_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

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
| [1457_math_optimized.py](1457_math_optimized.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 432 KB | 11328147 |
| [1457_math_optimized.rs](1457_math_optimized.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 88 KB | 11324854 |
