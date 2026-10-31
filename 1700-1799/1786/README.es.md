# 1786. La biografía de Sandro

[Timus 1786](https://acm.timus.ru/problem.aspx?space=1&num=1786) · dificultad 110 · strings

Problema original de Olga Soboleva, del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que cambiar un texto de letras latinas para que contenga la palabra
"Sandro". Sustituir una letra por otra del mismo caso cuesta 5 monedas,
y cambiar el caso de una letra también cuesta 5. Hallar el menor coste.

## Entrada

El texto, de 6 a 200 letras.

## Salida

El menor número de monedas.

## Ejemplos

### Ejemplo 1

Entrada:

```
MyNameIsAlexander
```

Salida:

```
20
```

## Solución

Se prueban todas las posiciones para las seis letras del nombre. Una
letra cuesta 5 si su caso es incorrecto y 5 más si es otra letra, así
que una letra incorrecta en ambos sentidos cuesta 10. Se suman los seis
costes en cada posición y se toma la menor suma. El recorrido tarda
`O(n)`, pero Python copia el sufijo `text[start:]` en cada posición,
por lo que esa implementación tarda `O(n^2)`. Todas las implementaciones
usan `O(n)` memoria contando la entrada; la longitud máxima es solo 200.

En el ejemplo la mejor posición es "xander": la x necesita otra letra y
mayúscula, 10, mientras que e → r y r → o cuestan 5 cada una, 20 en
total.

Trampas:

- una letra incorrecta con el caso incorrecto paga las dos tarifas;
- en el test 03, `sANDRO`, las seis letras tienen el caso incorrecto y cuestan 30;
- el nombre puede empezar en la primera letra o acabar en la última.

Las respuestas de Python coinciden con un oráculo independiente basado
en el grafo de operaciones permitidas en 2.000 textos cortos aleatorios,
592 casos dirigidos, los 8 tests guardados y 64 casos generados.

## Soluciones optimizadas

La solución optimizada en C++ lee el texto con `scanf` en un búfer de
201 bytes, suficiente para 200 letras y el cero final, en lugar de
`std::cin` y `std::string`, y como el texto solo tiene letras latinas,
distingue la caja comparando con `'Z'` y pasa una letra a minúscula
sumando `'a' − 'A'` en lugar de llamar a `isupper` y `tolower`:
{1786_strings_optimized.cpp}.

La solución optimizada en Java lee el texto carácter a carácter
directamente desde `System.in` en lugar de crear un `Scanner`, y como el
texto solo tiene letras latinas, distingue la caja comparando con `'Z'`
y pasa una letra a minúscula sumando `'a' − 'A'` en lugar de llamar a
`Character.isUpperCase` y `Character.toLowerCase`:
{1786_strings_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1786_strings_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +68.42%; base: `1786_strings.cpp`.

- `1786_strings_optimized.java`: reducción de tiempo +28.44%; reducción
  de memoria +75.13%; base: `1786_strings.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1786_strings.go](1786_strings.go).
- [1786_strings.rs](1786_strings.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1786_strings.cpp](1786_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 380 KB | 11304047 |
| [1786_strings.go](1786_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1088 KB | 11289804 |
| [1786_strings.java](1786_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 1576 KB | 11304048 |
| [1786_strings.py](1786_strings.py) | Python 3.12 x64 | strings | O(n^2) | AC | 0.109 s | 408 KB | 11304049 |
| [1786_strings.rs](1786_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 216 KB | 11289809 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1786_strings_optimized.cpp](1786_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 120 KB | 11304276 |
| [1786_strings_optimized.java](1786_strings_optimized.java) | Java 1.8 | strings | O(n) | AC | 0.078 s | 392 KB | 11304277 |
