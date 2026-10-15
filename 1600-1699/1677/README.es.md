# 1677. Mono ante el teclado

[Timus 1677](https://acm.timus.ru/problem.aspx?space=1&num=1677) · dificultad 1586 · strings

Problema original de Igor Chevdar, del Ural SU Contest en el campus de verano de Petrozavodsk, agosto de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada segundo un mono teclea una de las N primeras letras, todas con la
misma probabilidad. Hay que hallar el número esperado de segundos hasta
que aparezca una palabra dada en el texto tecleado, redondeado hacia
abajo.

## Entrada

N (1 ≤ N ≤ 26) y luego la palabra: letras minúsculas entre las N
primeras, como mucho 30000.

## Salida

El tiempo esperado, redondeado hacia abajo (de todos modos es entero).

## Ejemplos

### Ejemplo 1

Entrada:

```
2
aa
```

Salida:

```
6
```

### Ejemplo 2

Entrada:

```
2
ba
```

Salida:

```
4
```

## Solución

La respuesta es la suma de N^k sobre todos los k tales que las k
primeras letras de la palabra coinciden con sus k últimas (sus bordes),
incluida la palabra entera. Para aa con N = 2 es 2 + 4 = 6; para ba,
solo 4.

Un argumento de apuestas explica por qué. Antes de cada segundo llega un
jugador nuevo con 1 moneda y apuesta todo, a la cuota justa de N a 1, a
que la siguiente letra es la primera de la palabra; si gana, apuesta
todo a la segunda letra, y así sucesivamente. El juego es justo, así que
en el momento en que aparece la palabra por primera vez las ganancias
totales menos las monedas aportadas tienen esperanza cero. En ese momento
siguen jugando exactamente los que empezaron en un borde de la palabra,
con N^k cada uno para un borde de longitud k, y cada segundo aportó una
moneda. Así que el tiempo esperado es la suma de N^k.

Los bordes salen de la función de prefijos: el borde más largo de la
palabra, el más largo de este, y así sucesivamente. La suma, escrita en
base N, solo tiene dígitos 0 y 1, así que se construye con la regla de
Horner desde el dígito más alto; tiene hasta unos 42 500 dígitos
decimales. `O(L²)` operaciones sobre las cifras del número y `O(L)` para
los bordes.

Detalles a tener en cuenta:

- la respuesta es un entero exacto enorme (prueba 05), así que hace falta
  aritmética de precisión arbitraria; los números de coma flotante no
  sirven aquí;
- con N = 1 el tiempo es simplemente la longitud de la palabra
  (prueba 03).

Las respuestas coinciden con la solución exacta de las ecuaciones de
espera para todas las palabras de longitud hasta 5 sobre a lo sumo tres
letras, y con una implementación aceptada independiente.

## Notas por lenguaje

- C++ y Rust hacen la aritmética por su cuenta en cifras de base 10⁹:
  cada paso multiplica por N y suma un dígito.
- Python quita el límite de conversión de enteros enormes a texto con
  sys.set_int_max_str_digits(0).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1677_strings.cpp](1677_strings.cpp) | G++ 13.2 x64 | strings | O(L^2) | AC | 0.218 s | 408 KB |
| [1677_strings.go](1677_strings.go) | Go 1.14 x64 | strings | O(L^2) | AC | 0.078 s | 6000 KB |
| [1677_strings.java](1677_strings.java) | Java 1.8 | strings | O(L^2) | AC | 0.953 s | 5976 KB |
| [1677_strings.py](1677_strings.py) | Python 3.12 x64 | strings | O(L^2) | AC | 0.328 s | 26416 KB |
| [1677_strings.rs](1677_strings.rs) | Rust 1.75 x64 | strings | O(L^2) | AC | 0.156 s | 776 KB |
