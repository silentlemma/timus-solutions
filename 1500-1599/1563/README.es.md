# 1563. Bayan

[Timus 1563](https://acm.timus.ru/problem.aspx?space=1&num=1563) · dificultad 54 · hashing

Problema original de Vladimir Yakovlev, del XII Campeonato de Programación de la Universidad Estatal de los Urales, 6 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Angela recorre en orden N tiendas (N ≤ 1000) y dice «Bayan» en cada
tienda cuyo nombre ya había visto. Hay que contar cuántas veces lo dice
Angela. Un nombre es una cadena de 1 a 30 letras latinas y espacios, y no
hay dos nombres que difieran solo en mayúsculas y minúsculas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego un nombre de tienda por línea.

## Salida

El número de tiendas repetidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
12
ESPRIT
Nice Connection
Camelot
Adilisik
Lady and Gentleman City
MEXX
Camelot
Sultanna Frantsuzova
Camaieu
MEXX
Axara
Camelot
```

Salida:

```
3
```

## Solución

Cada tienda posterior a la primera con su nombre es una repetición, así
que la respuesta es N menos el número de nombres distintos, contados con
un conjunto hash. Un nombre es la línea entera, espacios incluidos, así
que las líneas se leen completas y solo se quita el fin de línea.
Tiempo esperado `O(N)`.

Detalles a tener en cuenta:

- los nombres tienen espacios, así que leerlos palabra a palabra los
  parte (pruebas 03, gen3);
- un espacio de más o de menos da otro nombre (prueba 03);
- un nombre puede ser prefijo de otro (prueba 05).

## Soluciones optimizadas

La solución optimizada en C++ guarda el mismo conjunto de nombres. Lee
cada línea carácter a carácter en un búfer de 30 caracteres en lugar de
`getline` y reserva el conjunto para `N` nombres de antemano: 300 KB en
lugar de 512 KB, con el mismo tiempo.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1563_hashing.cpp](1563_hashing.cpp) | G++ 13.2 x64 | hashing | O(N) | AC | 0.015 s | 512 KB | 11287691 |
| [1563_hashing.go](1563_hashing.go) | Go 1.14 x64 | hashing | O(N) | AC | 0.031 s | 1144 KB | 11287693 |
| [1563_hashing.java](1563_hashing.java) | Java 1.8 | hashing | O(N) | AC | 0.078 s | 660 KB | 11287696 |
| [1563_hashing.py](1563_hashing.py) | Python 3.12 x64 | hashing | O(N) | AC | 0.078 s | 516 KB | 11287695 |
| [1563_hashing.rs](1563_hashing.rs) | Rust 1.75 x64 | hashing | O(N) | AC | 0.046 s | 476 KB | 11287697 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1563_hashing_optimized.cpp](1563_hashing_optimized.cpp) | G++ 13.2 x64 | hashing | O(N) | AC | 0.015 s | 300 KB | 11303620 |
