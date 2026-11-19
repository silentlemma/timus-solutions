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

`1457_math_optimized.py`. Conserva la media que minimiza la suma de distancias cuadradas. Suma exactamente N posiciones enteras y realiza solo la división final flotante con seis decimales. N<=1000 y posiciones<=10^6 acotan la suma a10^9, exacta en f64. Tiempo O(N), mismo significado y precisión. Suma un map de enteros de tokens en bytes, sin entrada decodificada ni otra lista entera; tokens y referencias de la sección siguen ocupando O(N). El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1457_math.py`: tiempo 0.078 s → 0.156 s; memoria 504 KB → 248 KB.

`1457_math_optimized.rs`. Conserva la media que minimiza la suma de distancias cuadradas. Suma exactamente N posiciones enteras y realiza solo la división final flotante con seis decimales. N<=1000 y posiciones<=10^6 acotan la suma a10^9, exacta en f64. Tiempo O(N), mismo significado y precisión. Acumula al leer, eliminando String y vector. Estado auxiliar O(1); printf emite la única media f64. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1457_math.rs`: tiempo 0.015 s → 0.031 s; memoria 252 KB → 88 KB.

La solución optimizada en Java analiza los números a mano en lugar de
`Scanner` e imprime la media sin formateador: redondea el valor exacto
con enteros, `(sum · 10⁶ + N / 2) / N`, y escribe la parte entera y seis
cifras de la parte fraccionaria: 412 KB en lugar de 2612 KB, con el
mismo tiempo.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1457_math_optimized.py`: puesto de tiempo 69/71 y de memoria 1/71 en esta muestra comparable.

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
| [1457_math_optimized.py](1457_math_optimized.py) \* | PyPy 3.10 x64 | math | O(N) | AC | 0.156 s | 248 KB | 11324843 |
| [1457_math_optimized.rs](1457_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 88 KB | 11324854 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
