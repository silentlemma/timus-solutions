# 1322. Espía

[Timus 1322](https://acm.timus.ru/problem.aspx?space=1&num=1322) · dificultad 179 · strings

Problema original con idea de Alexander Klepinin, preparado por Alexander Klepinin y Stanislav Vasiliev, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cifrador toma un texto de hasta 100 000 caracteres, escribe todas
sus rotaciones cíclicas, las ordena y devuelve la última columna de la
tabla ordenada junto con el número K de la fila que contiene el texto
original. Dados K y la última columna, hay que recuperar el texto. Los
caracteres son letras y el guion bajo, ordenados así: A a Z, luego `_`,
luego a a z.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

El número K en la primera línea y la última columna en la segunda.

## Salida

El texto original.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
rdarcaaaabb
```

Salida:

```
abracadabra
```

## Solución

Es la inversa de la transformada de Burrows–Wheeler. Las filas que
terminan en un carácter c se convierten en las filas que empiezan por c
al pasar c del final al principio, y esto conserva su orden. Las filas
que empiezan por c están ordenadas por lo que sigue a c, y así
exactamente están ordenadas las filas que terminan en c. Por tanto, la
j-ésima fila que termina en c es la j-ésima fila que empieza por c,
rotada una posición.

Se ordenan de forma estable las posiciones de la última columna por
carácter; el resultado se llama order. La fila order[j] termina con el
j-ésimo carácter de la columna ordenada, el mismo con el que empieza la
fila j, y la fila order[j] es la fila j desplazada una posición a la
izquierda: la rotación que empieza un carácter más tarde. Partiendo de
la fila K y siguiendo order n veces se recorren las rotaciones que
empiezan en el segundo, tercer, … carácter del texto, y el último
carácter de cada una es el que está justo antes de su inicio, así que
el texto sale en orden. El orden de caracteres dado es el orden ASCII,
así que una ordenación por conteo sobre 128 códigos hace la ordenación
estable en tiempo `O(n)`. Python usa en su lugar la ordenación estable
por comparaciones incorporada, con tiempo `O(n log n)` en el peor caso.
Todas las implementaciones usan `O(n)` de espacio adicional.

Detalles a tener en cuenta:

- en un texto periódico varias filas son iguales y K puede señalar
  cualquiera de ellas; todas llevan al mismo texto (prueba 04);
- las mayúsculas van antes del guion bajo y las minúsculas después
  (prueba 05);
- la ordenación debe ser estable, o los caracteres iguales se mezclan;
- el límite de tiempo es de 0,25 segundos, así que se deben usar entrada
  y salida con búfer.

El descifrador se comprobó cifrando 400 textos aleatorios y periódicos
de hasta 12 caracteres con una ordenación directa de sus rotaciones.

## Soluciones optimizadas

La solución optimizada en C++ empaqueta en cada elemento de `order` el
carácter con el que termina su fila: los 7 bits bajos guardan el código
del carácter, menor que 128, y los bits de arriba la fila, menor que
100 000 < 2^17, así que un elemento cabe en 32 bits. Seguir las filas
lee entonces un arreglo en lugar de dos, y cada carácter se imprime con
`putchar` en el acto en lugar de construir el texto en una cadena. La
columna se lee con `scanf` en un búfer estático de 100 001 bytes en
lugar de con `iostream` y `std::string`: {1322_strings_optimized.cpp}.

La solución optimizada en Java empaqueta en cada elemento de `order` el
carácter con el que termina su fila: los 7 bits bajos guardan el código
del carácter, menor que 128, y los bits de arriba la fila, menor que
100 000 < 2^17, así que un elemento cabe en un `int`. Seguir las filas
lee entonces un arreglo en lugar de dos, y cada carácter va directamente
a un `BufferedOutputStream` en lugar de a un arreglo `char` y un
`String`. La columna se lee byte a byte en bloques de 4 KB en un arreglo
`byte` de 100 000 elementos, en lugar de juntar las líneas en un
`StringBuilder` y copiarlas a arreglos `char`:
{1322_strings_optimized.java}.

La solución optimizada en Python sustituye el `sorted` incorporado por
una ordenación por conteo sobre los 128 códigos y guarda `order` en un
`array("I")` de elementos de 32 bits en lugar de una lista de enteros de
Python. Cada elemento guarda además el carácter con el que termina su
fila: los 7 bits bajos el código del carácter, menor que 128, y los bits
de arriba la fila, menor que 100 000 < 2^17, así que un elemento cabe en
32 bits. El texto se construye en un `bytearray` en lugar de una lista
de cadenas de un carácter. La ordenación por conteo es un bucle en
Python, más lento que `sorted`, así que la ganancia está sobre todo en
la memoria: {1322_strings_optimized.py}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1322_strings_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +43.24%; base: `1322_strings.cpp`.

- `1322_strings_optimized.java`: reducción de tiempo +0.00%; reducción
  de memoria +70.69%; base: `1322_strings.java`.

- `1322_strings_optimized.py`: reducción de tiempo -39.74%; reducción de
  memoria +84.08%; base: `1322_strings.py`.

## Notas por lenguaje

- Python ordena las posiciones con la ordenación estable incorporada;
  los demás lenguajes usan una ordenación por conteo.
- Python y Rust leen toda la entrada antes de analizarla; Java acumula
  las líneas antes de separarlas en tokens, mientras que C++ y Go leen
  tokens de una entrada con búfer.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1322_strings.cpp](1322_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 1036 KB | 11284953 |
| [1322_strings.go](1322_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.015 s | 2624 KB | 11284954 |
| [1322_strings.java](1322_strings.java) | Java 1.8 | strings | O(n) | AC | 0.093 s | 3152 KB | 11284956 |
| [1322_strings.py](1322_strings.py) | Python 3.12 x64 | strings | O(n log n) | AC | 0.078 s | 6308 KB | 11284955 |
| [1322_strings.rs](1322_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 1108 KB | 11284957 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1322_strings_optimized.cpp](1322_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.001 s | 588 KB | 11307290 |
| [1322_strings_optimized.java](1322_strings_optimized.java) \* | Java 1.8 | strings | O(n) | AC | 0.093 s | 924 KB | 11307302 |
| [1322_strings_optimized.py](1322_strings_optimized.py) \* | Python 3.12 x64 | strings | O(n) | AC | 0.109 s | 1004 KB | 11307297 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
