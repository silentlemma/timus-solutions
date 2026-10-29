# 1297. Palíndromo

[Timus 1297](https://acm.timus.ru/problem.aspx?space=1&num=1297) · dificultad 82 · strings, greedy

Problema original de Evgeny Krokhalev, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da una línea de como mucho 1000 letras latinas. Hay que imprimir su
subcadena más larga que se lee igual en ambos sentidos; si hay varias,
la que está más a la izquierda. Mayúsculas y minúsculas son letras
distintas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La línea.

## Salida

La subcadena palíndroma más larga.

## Ejemplos

### Ejemplo 1

Entrada:

```
Kazak
```

Salida:

```
aza
```

## Solución

Todo palíndromo tiene un centro: una letra si su longitud es impar, el
hueco entre dos letras si es par. Una línea de n letras tiene 2n − 1
centros. Desde cada uno se expande hacia fuera mientras las letras de
ambos lados coincidan. La expansión llega al palíndromo más largo con
ese centro, y los más cortos empiezan más a la derecha, así que nunca
ganan.

El mejor palíndromo es el más largo y, entre iguales, el de menor
inicio. `O(n²)` en el peor caso (una línea de una sola letra), solo
unas 500 000 comparaciones para n = 1000.

El algoritmo de Manacher lo haría en `O(n)`, pero con este tamaño no
hace falta.

Detalles a tener en cuenta:

- las letras se comparan tal cual, así que `K` y `k` son distintas
  (pruebas 01, 04 y 10);
- si todas las letras son distintas, la respuesta es la primera letra
  (prueba 03); no tener vecinas iguales descarta los palíndromos de
  longitud par, pero permite los impares, como `aba` (prueba 06);
- los empates se los lleva el palíndromo de más a la izquierda
  (pruebas 05 y 06);
- los palíndromos de longitud par necesitan sus propios centros
  (pruebas 05 y 08).

Las respuestas se compararon con revisar todas las subcadenas en 300
líneas aleatorias.

## Soluciones optimizadas

La solución optimizada en C++ lee las letras una a una con `getchar`, en
lugar de leer la línea entera, en un arreglo fijo para las a lo sumo
1000 letras, hasta el primer espacio en blanco. Escribe la respuesta
directamente desde ese arreglo, sin construir una cadena: 92 KB en lugar
de 364 KB, con el mismo tiempo. La solución optimizada en Rust lee y
escribe las letras como bytes, sin una cadena UTF-8 en medio: 0.015 s en
lugar de 0.046 s y 208 KB en lugar de 244 KB. La búsqueda desde cada
centro es la misma.

**Hacer crecer el mejor palíndromo** (Python). Un palíndromo que termina
en la letra siguiente es a lo sumo 2 más largo que el mejor hallado: si
se le quitan los extremos, queda un palíndromo que termina una letra
antes. Así que para cada letra solo se comprueban los dos candidatos de
longitud best + 2 y best + 1 que terminan en ella, comparando el trozo
con su inverso, cosa que Python hace en C: 0.109 s en lugar de 0.171 s,
aunque la memoria sube de 452 KB a 464 KB.

## Notas por lenguaje

- Las soluciones sencillas leen la línea entera y quitan los espacios
  sobrantes, como un `\r` final, antes de buscar.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1297_strings.cpp](1297_strings.cpp) | G++ 13.2 x64 | strings | O(n^2) | AC | 0.015 s | 364 KB | 11284682 |
| [1297_strings.go](1297_strings.go) | Go 1.14 x64 | strings | O(n^2) | AC | 0.015 s | 1088 KB | 11284689 |
| [1297_strings.java](1297_strings.java) | Java 1.8 | strings | O(n^2) | AC | 0.125 s | 444 KB | 11284696 |
| [1297_strings.py](1297_strings.py) | Python 3.12 x64 | strings | O(n^2) | AC | 0.171 s | 452 KB | 11284694 |
| [1297_strings.rs](1297_strings.rs) | Rust 1.75 x64 | strings | O(n^2) | AC | 0.046 s | 244 KB | 11284699 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1297_greedy.py](1297_greedy.py) | Python 3.12 x64 | greedy | O(n^2) | AC | 0.109 s | 464 KB | 11303737 |
| [1297_strings_optimized.cpp](1297_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n^2) | AC | 0.015 s | 92 KB | 11303962 |
| [1297_strings_optimized.rs](1297_strings_optimized.rs) | Rust 1.75 x64 | strings | O(n^2) | AC | 0.015 s | 208 KB | 11303738 |
