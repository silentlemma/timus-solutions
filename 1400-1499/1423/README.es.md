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

## Evaluación

El repositorio usa un comprobador semántico y acepta cualquier salida que satisfaga estas condiciones. El comprobador exige un entero; acepta-1 exactamente si la referencia dice que no hay giro. En otro caso vale cualquier X en [0,N) que mueva los últimos X bytes de S al principio y produzca T, sin exigir mínimo.

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

`1423_strings_optimized.rs`. Conserva KMP por bytes e índice de rotación derecha. Prefijos u32 y recorrido de s seguido de s sin último byte eliminan módulo por posición sin duplicar cadena. Tokens de bytes conservan caracteres33…255. O(N) tiempo/espacio, salida directa en vez de formato Rust.

Frente a `1423_strings.rs`: tiempo 0.031 s → 0.031 s; memoria 3052 KB → 1 804 KB.

`1423_strings_optimized.py`. Conserva búsqueda en bytes duplicados y giro derecho(n-offset) mod n, o -1 si falta. Lee tres tokens con archivo binario sin búfer y vacía antes de os._exit(0). Sigue almacenando O(n) bytes; E/S y salida del intérprete no cambian el orden. La búsqueda adaptativa/Two-Way de CPython 3.12 mantiene O(n): [fuente](https://raw.githubusercontent.com/python/cpython/v3.12.0/Objects/stringlib/fastsearch.h). Este Accepted usa más memoria y no mejora del 30%; entra por la regla separada de primer 30% con mejor puesto, conservando asterisco.

Frente a `1423_strings.py`: tiempo 0.109 s → 0.093 s; memoria 1372 KB → 1 592 KB.

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

Cada versión optimizada tiene Accepted y cumple un criterio de clasificación
o de mejora de recursos. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1423_strings_optimized.cpp`: reducción de tiempo -106.67%; reducción
  de memoria +40.82%; base: `1423_strings.cpp`.

- `1423_strings_optimized.go`: reducción de tiempo +0.00%; reducción de
  memoria +40.39%; base: `1423_strings.go`.

- `1423_strings_optimized.java`: reducción de tiempo +19.87%; reducción
  de memoria +39.97%; base: `1423_strings.java`.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1423_strings_optimized.py`: puesto de tiempo 11/55 y de memoria 1/55 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

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
| [1423_strings_optimized.py](1423_strings_optimized.py) \* | Python 3.12 x64 | strings | O(n) | AC | 0.093 s | 1592 KB | 11325463 |
| [1423_strings_optimized.rs](1423_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(N) time; O(N) space | AC | 0.031 s | 1804 KB | 11325527 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
