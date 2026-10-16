# 1769. Vieja leyenda de los Urales

[Timus 1769](https://acm.timus.ru/problem.aspx?space=1&num=1769) · dificultad 204 · strings

Problema original de Daniil Ayzenshteyn, del XIV Campeonato de los Urales de Programación Competitiva, 10 de abril de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una línea no vacía de cifras decimales, hallar el menor entero
positivo cuya notación decimal no aparece en la línea.

## Entrada

La línea, de a lo sumo 10⁵ cifras.

## Salida

Ese entero.

## Ejemplos

### Ejemplo 1

Entrada:

```
10123456789
```

Salida:

```
11
```

## Solución

Una línea de n cifras tiene a lo sumo n trozos de cada longitud,
mientras que hay 9·10⁵ números de seis cifras, así que siempre falta
algún número de seis cifras y la respuesta tiene a lo sumo seis. Cada
trozo de una a seis cifras que no empieza por cero es la notación de un
número; marcándolos todos y contando desde 1 hasta el primer número sin
marcar se obtiene la respuesta. `O(6n)`.

En el ejemplo aparecen del 1 al 9 y el 10, pero no el 11.

Trampas:

- los trozos que empiezan por 0 no son notaciones de números, aunque el
  número tras el cero sigue apareciendo una cifra después;
- una línea de ceros no contiene el 1;
- buscar en la línea cada número por turno puede ser lento en líneas
  largas con una respuesta grande.

Las respuestas coinciden con buscar en la línea 1, 2, 3 y así
sucesivamente en 90 líneas aleatorias y con una implementación
aceptada independiente en 20 líneas largas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1769_strings.cpp](1769_strings.cpp) | G++ 13.2 x64 | strings | O(6n) | AC | 0.015 s | 632 KB |
| [1769_strings.go](1769_strings.go) | Go 1.14 x64 | strings | O(6n) | AC | 0.031 s | 2740 KB |
| [1769_strings.java](1769_strings.java) | Java 1.8 | strings | O(6n) | AC | 0.140 s | 2144 KB |
| [1769_strings.py](1769_strings.py) | Python 3.12 x64 | strings | O(6n) | AC | 0.328 s | 23756 KB |
| [1769_strings.rs](1769_strings.rs) | Rust 1.75 x64 | strings | O(6n) | AC | 0.031 s | 1472 KB |
