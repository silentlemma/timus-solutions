# 1423. Fábula de una cadena

[Timus 1423](https://acm.timus.ru/problem.aspx?space=1&num=1423) · dificultad 170 · strings

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las cadenas S y T tienen la misma longitud N (1 ≤ N ≤ 250 000) y
constan de caracteres con códigos de 33 a 255. Un desplazamiento cíclico
lleva el último carácter de una cadena al principio. Hay que imprimir un
número X (0 ≤ X < N) tal que X desplazamientos conviertan S en T, o −1
si no existe; vale cualquier X.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego S, luego T.

## Salida

X o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
11
abracadabra
racadabraab
```

Salida:

```
9
```

En el ejemplo, 9 desplazamientos convierten «abracadabra» en
«racadabraab».

## Solución

X desplazamientos a la derecha equivalen a N − X a la izquierda, y los
desplazamientos de S a la izquierda en k son justo las subcadenas de
longitud N de S + S que empiezan en k < N. Así que se busca T en
S + S: si empieza en la posición k, la respuesta es (N − k) mod N, y si
no aparece, −1. La búsqueda es Knuth–Morris–Pratt con la función de
prefijos de T, recorriendo S + S sin su último carácter; la búsqueda de
bytes integrada de Python también es lineal aquí. `O(N)`.

Detalles a tener en cuenta:

- una S periódica tiene varias respuestas, así que las pruebas usan un
  verificador (prueba 04);
- los caracteres por encima de 127 deben leerse como bytes; algunas
  formas de lectura los decodifican o incluso toman el código 160 por un
  espacio (prueba 05, gen3);
- una búsqueda ingenua de subcadenas puede ser cuadrática con cadenas de
  una sola letra repetida (gen2).

## Soluciones optimizadas

La solución optimizada en C++ guarda la función de prefijos en campos de
18 bits empaquetados en un arreglo de palabras de 32 bits, porque cada
valor es menor que N ≤ 250 000 < 2^18, y lee un campo de dos palabras
vecinas a la vez; esto cuesta unos desplazamientos por acceso, pero
ocupa unos 0.56 MB en lugar de 1 MB para valores `int`. Además recorre S
dos veces en lugar de construir S + S, y lee S y T con `scanf` en dos
búferes estáticos de 250 001 bytes en lugar de `std::string` con `cin`:
{1423_strings_optimized.cpp}.

La solución optimizada en Go guarda la función de prefijos en valores
`int32` en lugar de `int` de 8 bytes, porque cada valor es menor que
N ≤ 250 000, y lee S y T directamente en arreglos de exactamente N bytes
con `io.ReadFull`, contando con que ambas cadenas tienen longitud N, en
lugar de leer toda la entrada y partirla en campos:
{1423_strings_optimized.go}.

La solución optimizada en Java lee la entrada en bruto en bloques de
64 KB y recorta de ella S y T a mano como arreglos `byte`, comparando
bytes, en lugar de decodificar las líneas con `BufferedReader` en
arreglos `char`, que ocupan dos bytes por carácter:
{1423_strings_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1423_strings_optimized.cpp`: reducción de tiempo -106.67%; reducción
  de memoria +40.82%; base: `1423_strings.cpp`.

- `1423_strings_optimized.go`: reducción de tiempo +0.00%; reducción de
  memoria +40.39%; base: `1423_strings.go`.

- `1423_strings_optimized.java`: reducción de tiempo +19.87%; reducción
  de memoria +39.97%; base: `1423_strings.java`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1423_strings.cpp](1423_strings.cpp) | G++ 13.2 x64 | strings | O(N) | AC | 0.015 s | 1940 KB | 11286160 |
| [1423_strings.go](1423_strings.go) | Go 1.14 x64 | strings | O(N) | AC | 0.031 s | 4268 KB | 11286161 |
| [1423_strings.java](1423_strings.java) | Java 1.8 | strings | O(N) | AC | 0.156 s | 5744 KB | 11307252 |
| [1423_strings.py](1423_strings.py) | Python 3.12 x64 | strings | O(N) | AC | 0.109 s | 1372 KB | 11286163 |
| [1423_strings.rs](1423_strings.rs) | Rust 1.75 x64 | strings | O(N) | AC | 0.031 s | 3052 KB | 11286168 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1423_strings_optimized.cpp](1423_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(N) | AC | 0.031 s | 1148 KB | 11307257 |
| [1423_strings_optimized.go](1423_strings_optimized.go) | Go 1.14 x64 | strings | O(N) | AC | 0.031 s | 2544 KB | 11307255 |
| [1423_strings_optimized.java](1423_strings_optimized.java) | Java 1.8 | strings | O(N) | AC | 0.125 s | 3448 KB | 11307317 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
