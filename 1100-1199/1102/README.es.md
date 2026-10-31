# 1102. Partir una línea en las palabras de un diálogo extraño

[Timus 1102](https://acm.timus.ru/problem.aspx?space=1&num=1102) · dificultad 176 · strings

Problema original de Katya Ovechkina, del Tetrahedron Team Contest, mayo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un diálogo es cualquier secuencia de las palabras `out`, `output`,
`puton`, `in`, `input` y `one`, escrita sin espacios. Para cada una de
`N` líneas (`N ≤ 1000`, letras minúsculas, `≤ 4 · 10^6` letras en total)
imprime `YES` si es un diálogo y `NO` si no.

Límite de tiempo: 1 segundo. Límite de memoria: 16 MB.

## Entrada

`N` (`1 ≤ N ≤ 1000`) y luego `N` líneas no vacías de letras latinas
minúsculas.

## Salida

`YES` o `NO` para cada línea.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
puton
inonputin
oneputonininputoutoutput
oneininputwooutoutput
outpu
utput
```

Salida:

```
YES
NO
YES
NO
NO
NO
```

## Solución

Leídas hacia delante, las palabras se solapan mal: `out` empieza
`output`, `in` empieza `input`, y `output` + `one` se lee como `out` +
`puton` + `e`. Leídas hacia atrás se convierten en `tuo`, `tuptuo`,
`notup`, `ni`, `tupni` y `eno`, y ninguna es el principio de otra. Así
que en cada punto termina como mucho una palabra, y cortar la línea de
forma voraz desde el final, palabra a palabra, o bien consume toda la
línea o bien demuestra que no hay partición. `O(L)` para `L` letras.

Detalles a tener en cuenta:

- un voraz hacia delante que toma siempre la palabra más larga falla:
  `outputon` es `out` + `puton`, pero tomar primero `output` deja `on`;
- las líneas son largas y el límite de memoria es de solo 16 MB, así que
  hay que evitar copias de toda la entrada.

Las respuestas se comprobaron con una programación dinámica hacia
delante sobre los prefijos, en todos los diálogos de hasta tres palabras,
en casi diálogos y en líneas aleatorias estropeadas.

## Soluciones optimizadas

La solución optimizada en C++ reconoce los diálogos con un autómata
finito en lugar de cortar palabras desde el final. Las seis palabras,
24 letras en total, forman un trie de como mucho 25 nodos, así que un
conjunto de nodos del trie cabe en una máscara de 32 bits. Un estado es
el conjunto de nodos alcanzados por las palabras que se están leyendo,
donde la raíz significa además que el prefijo leído se parte en palabras
enteras; los pocos conjuntos así alcanzables desde la raíz se hallan una
vez al principio y reciben una tabla de transiciones. Después cada letra
cuesta una consulta a la tabla, la línea nunca se guarda y la respuesta
es `YES` si la raíz está en el conjunto al final de la línea. En lugar
de leer con `cin` una línea de hasta cuatro millones de letras en un
`string`, la entrada se lee en bloques de 4 KB: {1102_parsing.cpp}.

La solución optimizada en Go reconoce los diálogos con un autómata
finito en lugar de cortar palabras desde el final. Las seis palabras,
24 letras en total, forman un trie de como mucho 25 nodos, así que un
conjunto de nodos del trie cabe en una máscara de 32 bits. Un estado es
el conjunto de nodos alcanzados por las palabras que se están leyendo,
donde la raíz significa además que el prefijo leído se parte en palabras
enteras; los pocos conjuntos así alcanzables desde la raíz se hallan una
vez al principio y reciben una tabla de transiciones. Después cada
letra, tomada directamente del lector con búfer, cuesta una consulta a
la tabla, la línea no se guarda como cadena y la respuesta es `YES` si
la raíz está en el conjunto al final de la línea: {1102_parsing.go}.

La solución optimizada en Java con programación dinámica lee la entrada
byte a byte de un flujo con búfer y avanza por la línea: `good[i]` dice
si las primeras `i` letras se parten en palabras, y es cierto cuando una
de las seis palabras termina en la letra `i` y `good` es cierto justo
antes de esa palabra. Una palabra tiene como mucho seis letras, así que
solo se guardan en un anillo las siete últimas letras y valores, y la
línea nunca se guarda, mientras que la solución simple en Java lee cada
línea en un arreglo de cuatro millones de caracteres: {1102_dp.java}.

La solución optimizada en Java con autómata reconoce los diálogos con un
autómata finito en lugar de cortar palabras desde el final. Las seis
palabras, 24 letras en total, forman un trie de como mucho 25 nodos, así
que un conjunto de nodos del trie cabe en una máscara de 32 bits. Un
estado es el conjunto de nodos alcanzados por las palabras que se están
leyendo, donde la raíz significa además que el prefijo leído se parte en
palabras enteras; los pocos conjuntos así alcanzables desde la raíz se
hallan una vez al principio y reciben una tabla de transiciones. Después
cada byte, leído en bloques de 4 KB, cuesta una consulta a la tabla, y
la respuesta es `YES` si la raíz está en el conjunto al final de la
línea. La línea nunca se guarda, mientras que la solución simple en Java
lee cada línea en un arreglo de cuatro millones de caracteres:
{1102_parsing.java}.

La solución optimizada en Rust reconoce los diálogos con un autómata
finito en lugar de cortar palabras desde el final. Las seis palabras,
24 letras en total, forman un trie de como mucho 25 nodos, así que un
conjunto de nodos del trie cabe en una máscara de 32 bits. Un estado es
el conjunto de nodos alcanzados por las palabras que se están leyendo,
donde la raíz significa además que el prefijo leído se parte en palabras
enteras; los pocos conjuntos así alcanzables desde la raíz se hallan una
vez al principio y reciben una tabla de transiciones. Después cada letra
cuesta una consulta a la tabla, hecha directamente sobre los bloques del
búfer de entrada, y la respuesta es `YES` si la raíz está en el conjunto
al final de la línea. Ninguna línea se copia a un vector propio:
{1102_parsing.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1102_parsing.cpp`: reducción de tiempo +80.13%; reducción de memoria
  +97.50%; base: `1102_strings.cpp`.

- `1102_parsing.go`: reducción de tiempo +41.03%; reducción de memoria
  +90.39%; base: `1102_strings.go`.

- `1102_dp.java`: reducción de tiempo -68.40%; reducción de memoria
  +94.84%; base: `1102_strings.java`.

- `1102_parsing.java`: reducción de tiempo +50.00%; reducción de memoria
  +90.40%; base: `1102_strings.java`.

- `1102_parsing.rs`: reducción de tiempo -106.67%; reducción de memoria
  +94.23%; base: `1102_strings.rs`.

## Notas por lenguaje

- Python compara la línea invertida con la expresión regular
  `(?:tuo|tuptuo|notup|ni|tupni|eno)*+`; el `*+` posesivo no guarda
  estados a los que volver, lo que es seguro porque la partición es
  única.
- Java lee cada línea carácter a carácter en un único arreglo `char`
  dimensionado para los cuatro millones de letras de toda la entrada,
  8 MB: `readLine` haría además copias temporales de una línea larga, y
  no caben en 16 MB.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1102_strings.cpp](1102_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.156 s | 5768 KB | 11279162 |
| [1102_strings.go](1102_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.078 s | 11448 KB | 11279163 |
| [1102_strings.java](1102_strings.java) | Java 1.8 | strings | O(L) | AC | 0.250 s | 8372 KB | 11307280 |
| [1102_strings.py](1102_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.140 s | 8328 KB | 11279164 |
| [1102_strings.rs](1102_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 7760 KB | 11279166 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1102_parsing.cpp](1102_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.031 s | 144 KB | 11307270 |
| [1102_parsing.go](1102_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.046 s | 1100 KB | 11307275 |
| [1102_dp.java](1102_dp.java) \* | Java 1.8 | dp | O(L) | AC | 0.421 s | 432 KB | 11307279 |
| [1102_parsing.java](1102_parsing.java) \* | Java 1.8 | parsing | O(L) | AC | 0.125 s | 804 KB | 11307272 |
| [1102_parsing.rs](1102_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.031 s | 448 KB | 11307277 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
