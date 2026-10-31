# 1219. Un millón de letras sin letra, par ni trío demasiado frecuente

[Timus 1219](https://acm.timus.ru/problem.aspx?space=1&num=1219) · dificultad 121 · constructive

Problema original de Pavel Atnashev y Leonid Volkov, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que imprimir 1.000.000 de letras latinas minúsculas de modo que cada
letra aparezca como mucho 40.000 veces, cada dos letras consecutivas como
mucho 2.000 veces y cada tres letras consecutivas como mucho 100 veces.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

No hay entrada.

## Salida

Una línea con las letras.

## Evaluación

Se acepta cualquier secuencia que cumpla los tres límites.

## Ejemplos

No hay entrada, y el enunciado no da ninguna salida de ejemplo.

## Solución

Se reparten el millón de letras de la forma más uniforme posible. Hay 26
letras, `26² = 676` pares y `26³ = 17.576` tríos, así que un reparto
perfecto da unas 38.462, 1.479 y 57 apariciones, todo dentro de los
límites.

Una secuencia de De Bruijn de orden 3 sobre 26 letras es un ciclo de
17.576 letras en el que cada trío aparece exactamente una vez como tres
letras consecutivas, dando la vuelta al ciclo. Repetirla seguida deja
cada ventana de tres letras como una ventana del ciclo, así que tras unas
57 copias cada trío aparece 56 o 57 veces, cada par 26 veces más y cada
letra 676 veces más: aquí como mucho 38.532, 1.482 y 57. El ciclo sale de
la construcción clásica que une en orden lexicográfico las palabras de
Lyndon cuya longitud divide a 3. `O(L)` para `L = 10⁶`.

Detalles a tener en cuenta:

- las ventanas que pasan de una copia a la siguiente son ventanas
  cíclicas de la secuencia, así que no rompen el equilibrio;
- una secuencia aleatoria probablemente también pasaría, pero su trío más
  frecuente rondaría las 90 apariciones, cerca del límite.

La salida se comprobó con los tres límites, y las cifras de arriba son
sus máximos reales.

## Soluciones optimizadas

La solución optimizada en C++ construye el ciclo directamente como
17.576 bytes de letras y lo escribe 56 veces con `fwrite`, seguido de
sus primeras 15.744 letras, en lugar de llenar una cadena de un millón
de letras; la salida es la misma: {1219_constructive_optimized.cpp}.

La solución optimizada en Go convierte el ciclo en un bloque de
17.576 bytes de letras y lo escribe 56 veces con `bufio`, seguido de sus
primeras 15.744 letras, en lugar de llenar un slice de un millón de
bytes; la salida es la misma: {1219_constructive_optimized.go}.

La solución optimizada en Java construye el ciclo directamente como
17.576 bytes de letras y lo escribe 56 veces, seguido de sus primeras
15.744 letras, en lugar de usar un arreglo `int` y un arreglo de bytes
de un millón de elementos cada uno; la salida es la misma:
{1219_constructive_optimized.java}.

La solución optimizada en Python construye el ciclo directamente en un
`bytearray` de 17.576 letras y lo escribe 56 veces, seguido de sus
primeras 15.744 letras, en lugar de crear una lista de números y una
cadena de un millón de letras; la salida es la misma:
{1219_constructive_optimized.py}.

La solución optimizada en Rust convierte el ciclo en un bloque de
17.576 bytes de letras y lo escribe 56 veces con un `BufWriter`, seguido
de sus primeras 15.744 letras, en lugar de reunir un vector de un millón
de bytes; la salida es la misma: {1219_constructive_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1219_constructive_optimized.cpp`: reducción de tiempo +0.00%;
  reducción de memoria +91.89%; base: `1219_constructive.cpp`.

- `1219_constructive_optimized.go`: reducción de tiempo +0.00%;
  reducción de memoria +38.11%; base: `1219_constructive.go`.

- `1219_constructive_optimized.java`: reducción de tiempo +75.81%;
  reducción de memoria +95.58%; base: `1219_constructive.java`.

- `1219_constructive_optimized.py`: reducción de tiempo +60.26%;
  reducción de memoria +86.97%; base: `1219_constructive.py`.

- `1219_constructive_optimized.rs`: reducción de tiempo +0.00%;
  reducción de memoria +80.53%; base: `1219_constructive.rs`.

## Notas por lenguaje

- Todos los lenguajes generan el ciclo con la misma construcción
  recursiva y escriben la línea entera de una vez.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1219_constructive.cpp](1219_constructive.cpp) | G++ 13.2 x64 | constructive | O(L) | AC | 0.001 s | 1184 KB | 11283683 |
| [1219_constructive.go](1219_constructive.go) | Go 1.14 x64 | constructive | O(L) | AC | 0.015 s | 2624 KB | 11283684 |
| [1219_constructive.java](1219_constructive.java) | Java 1.8 | constructive | O(L) | AC | 0.062 s | 8868 KB | 11283687 |
| [1219_constructive.py](1219_constructive.py) | Python 3.12 x64 | constructive | O(L) | AC | 0.078 s | 3224 KB | 11283686 |
| [1219_constructive.rs](1219_constructive.rs) | Rust 1.75 x64 | constructive | O(L) | AC | 0.001 s | 2404 KB | 11283688 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1219_constructive_optimized.cpp](1219_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(L) | AC | 0.001 s | 96 KB | 11304363 |
| [1219_constructive_optimized.go](1219_constructive_optimized.go) | Go 1.14 x64 | constructive | O(L) | AC | 0.001 s | 1624 KB | 11304367 |
| [1219_constructive_optimized.java](1219_constructive_optimized.java) | Java 1.8 | constructive | O(L) | AC | 0.001 s | 392 KB | 11304365 |
| [1219_constructive_optimized.py](1219_constructive_optimized.py) \* | Python 3.12 x64 | constructive | O(L) | AC | 0.031 s | 420 KB | 11304366 |
| [1219_constructive_optimized.rs](1219_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(L) | AC | 0.015 s | 468 KB | 11304368 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
