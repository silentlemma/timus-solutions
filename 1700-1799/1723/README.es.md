# 1723. El libro de Sandro

[Timus 1723](https://acm.timus.ru/problem.aspx?space=1&num=1723) · dificultad 62 · strings

Problema original de Ivan Burmistrov (preparado por Olga Soboleva), del Concurso Regional de Programación por Equipos de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada subcadena de una palabra dada es un hechizo, y su fuerza es el
número de veces que aparece en la palabra, contando las apariciones
solapadas. Imprimir un hechizo de fuerza máxima.

## Entrada

Una palabra no vacía de a lo sumo 50 letras latinas minúsculas.

## Salida

Cualquier hechizo de fuerza máxima.

## Ejemplos

### Ejemplo 1

Entrada:

```
tebidohtebidoh
```

Salida:

```
tebidoh
```

## Solución

Cada aparición de un hechizo empieza con una aparición de su primera
letra, y apariciones distintas empiezan en lugares distintos. Así que
ningún hechizo es más fuerte que su primera letra sola, y una letra más
frecuente es un hechizo de fuerza máxima. `O(n)`.

En el ejemplo cada letra aparece dos veces, así que `t` es tan fuerte
como `tebidoh`.

Trampas:

- las apariciones pueden solaparse: `aba` aparece tres veces en
  `abababa`, pero `a` aparece cuatro;
- se acepta cualquier hechizo de fuerza máxima, así que las pruebas usan
  un comprobador.

El comprobador cuenta las apariciones de la respuesta, con solapamientos,
y las compara con las de la respuesta esperada. Una letra más frecuente
coincide con una búsqueda exhaustiva de todas las subcadenas en 300
palabras aleatorias.

## Soluciones optimizadas

La solución optimizada en C++ cuenta las letras a medida que las lee
con `getchar`, sin guardar la cadena: 84 KB en lugar de 352 KB.

La solución optimizada en Java lee las letras byte a byte desde
`System.in` en lugar de leer la palabra con `Scanner`, y escribe la
respuesta como un byte: 348 KB en lugar de 1556 KB, con el mismo tiempo.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1723_strings.cpp](1723_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 352 KB | 11303504 |
| [1723_strings.go](1723_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1068 KB | 11289348 |
| [1723_strings.java](1723_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 1556 KB | 11303505 |
| [1723_strings.py](1723_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 404 KB | 11289349 |
| [1723_strings.rs](1723_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 228 KB | 11289353 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1723_strings_optimized.cpp](1723_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 84 KB | 11303635 |
| [1723_strings_optimized.java](1723_strings_optimized.java) \* | Java 1.8 | strings | O(n) | AC | 0.140 s | 348 KB | 11303774 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
