# 1354. Palíndromo. Otra vez palíndromo

[Timus 1354](https://acm.timus.ru/problem.aspx?space=1&num=1354) · dificultad 138 · strings

Problema original de Denis Nazarov, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una palabra S1 de hasta 10 000 letras latinas, hay que hallar la
palabra no vacía más corta S2 tal que S1S2 sea un palíndromo, e imprimir
S1S2.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La palabra S1 en una línea.

## Salida

La palabra S1S2.

## Ejemplos

### Ejemplo 1

Entrada:

```
No
```

Salida:

```
NoN
```

### Ejemplo 2

Entrada:

```
OnLine
```

Salida:

```
OnLineniLnO
```

### Ejemplo 3

Entrada:

```
AbabaAab
```

Salida:

```
AbabaAababA
```

## Solución

Si S1S2 es un palíndromo y S2 no es más larga que S1, S2 es el reverso
de algún prefijo de S1, y el resto de S1 tras ese prefijo tiene que ser
un palíndromo. Así que la S2 más corta sale del sufijo palindrómico más
largo de S1 que empieza en la posición 1 o después: S2 no puede ser
vacía, de modo que S1 entera nunca cuenta, aunque sea un palíndromo.

Un sufijo X de la cola T = S1 sin su primera letra es un palíndromo
justo cuando X también es prefijo de reverse(T). Con la función de
prefijos sobre reverse(T) + `#` + T, su último valor es la longitud L del
sufijo más largo de ese tipo, y la respuesta es S1 seguida de las
primeras |S1| − L letras de S1 al revés. `O(|S1|)`.

Detalles a tener en cuenta:

- un palíndromo también necesita una letra: `abcba` da `abcbabcba`
  (prueba 05);
- una sola letra se duplica, porque la cola vacía cuenta como
  palíndromo (prueba 04);
- mayúsculas y minúsculas son letras distintas (pruebas 03 y 07);
- comprobar cada sufijo directamente puede costar 10⁸ pasos en largas
  series de una misma letra (prueba generada 4).

Las respuestas se compararon con probar directamente cada longitud de
prefijo en 300 palabras aleatorias de hasta 12 letras, y en las pruebas
generadas se comprobó que la respuesta es un palíndromo sin otra
adición más corta.

## Soluciones optimizadas

La solución optimizada en C++ nunca construye la cadena
reverse(T) + `#` + T de unas 2·|S1| letras. Calcula la función de
prefijos solo de reverse(S1), leyendo las letras de S1 con índices
invertidos, y después ejecuta la fase de búsqueda de Knuth–Morris–Pratt
con T como texto: la longitud emparejada tras la última letra es L. La
tabla usa `unsigned short`, dos bytes por entrada, porque una longitud
emparejada no pasa de 9999 en una palabra de hasta 10 000 letras. En
lugar de `iostream`, la palabra se lee con `scanf` en un arreglo fijo y
se imprime con `fputs`, y las letras añadidas salen una a una con
`putchar`: {1354_strings_optimized.cpp}.

La solución optimizada en Go nunca construye la cadena
reverse(T) + `#` + T de unas 2·|S1| letras. Calcula la función de
prefijos solo de reverse(S1), leyendo las letras de S1 con índices
invertidos, y después ejecuta la fase de búsqueda de Knuth–Morris–Pratt
con T como texto: la longitud emparejada tras la última letra es L. La
tabla usa `uint16`, dos bytes por entrada, porque una longitud
emparejada no pasa de 9999 en una palabra de hasta 10 000 letras, y la
respuesta se escribe con un `bufio.Writer` sin armarla como cadena:
{1354_strings_optimized.go}.

La solución optimizada en Java nunca construye la cadena reverse(T) +
`#` + T de unas 2·|S1| letras. Calcula la función de prefijos solo de
reverse(S1), leyendo las letras de S1 con índices invertidos, y después
ejecuta la fase de búsqueda de Knuth–Morris–Pratt con T como texto: la
longitud emparejada tras la última letra es L. La tabla es un `char[]`,
dos bytes por entrada, porque una longitud emparejada no pasa de 9999 en
una palabra de hasta 10 000 letras, y la respuesta se escribe con un
`BufferedWriter` sin armarla como cadena: {1354_strings_optimized.java}.

La solución optimizada en Python nunca construye la cadena reverse(T) +
`#` + T de unas 2·|S1| letras. Calcula la función de prefijos solo de
reverse(S1) y después ejecuta la fase de búsqueda de Knuth–Morris–Pratt
con T como texto: la longitud emparejada tras la última letra es L.
Trabaja con `bytes`, y la tabla es un `array("H")` de entradas de dos
bytes en lugar de una lista de objetos enteros, porque una longitud
emparejada no pasa de 9999 en una palabra de hasta 10 000 letras:
{1354_strings_optimized.py}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1354_strings_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +67.68%; base: `1354_strings.cpp`.

- `1354_strings_optimized.go`: reducción de tiempo +0.00%; reducción de
  memoria +37.66%; base: `1354_strings.go`.

- `1354_strings_optimized.java`: reducción de tiempo +26.90%; reducción
  de memoria +30.42%; base: `1354_strings.java`.

- `1354_strings_optimized.py`: reducción de tiempo +0.00%; reducción de
  memoria +57.57%; base: `1354_strings.py`.

## Notas por lenguaje

- Las cinco soluciones usan la misma función de prefijos sobre bytes o
  caracteres.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1354_strings.cpp](1354_strings.cpp) | G++ 13.2 x64 | strings | O(len(S1)) | AC | 0.015 s | 396 KB | 11285248 |
| [1354_strings.go](1354_strings.go) | Go 1.14 x64 | strings | O(len(S1)) | AC | 0.031 s | 1540 KB | 11285253 |
| [1354_strings.java](1354_strings.java) | Java 1.8 | strings | O(len(S1)) | AC | 0.171 s | 960 KB | 11285261 |
| [1354_strings.py](1354_strings.py) | Python 3.12 x64 | strings | O(len(S1)) | AC | 0.109 s | 1216 KB | 11285257 |
| [1354_strings.rs](1354_strings.rs) | Rust 1.75 x64 | strings | O(len(S1)) | AC | 0.031 s | 336 KB | 11285267 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1354_strings_optimized.cpp](1354_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(len(S1)) | AC | 0.015 s | 128 KB | 11304449 |
| [1354_strings_optimized.go](1354_strings_optimized.go) | Go 1.14 x64 | strings | O(len(S1)) | AC | 0.031 s | 960 KB | 11304450 |
| [1354_strings_optimized.java](1354_strings_optimized.java) | Java 1.8 | strings | O(len(S1)) | AC | 0.125 s | 668 KB | 11304452 |
| [1354_strings_optimized.py](1354_strings_optimized.py) \* | Python 3.12 x64 | strings | O(len(S1)) | AC | 0.109 s | 516 KB | 11304453 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
