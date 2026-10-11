# 1297. Palíndromo

[Timus 1297](https://acm.timus.ru/problem.aspx?space=1&num=1297) · dificultad 82 · strings

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
- si no hay dos letras vecinas iguales, la respuesta es la primera
  letra (prueba 03);
- los empates se los lleva el palíndromo de más a la izquierda
  (pruebas 05 y 06);
- los palíndromos de longitud par necesitan sus propios centros
  (pruebas 05 y 08).

Las respuestas se compararon con revisar todas las subcadenas en 300
líneas aleatorias.

## Notas por lenguaje

- La línea se lee entera y se quitan los espacios sobrantes, como un
  `\r` final, antes de buscar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1297_strings.cpp](1297_strings.cpp) | G++ 13.2 x64 | strings | O(n^2) | AC | 0.015 s | 364 KB |
| [1297_strings.go](1297_strings.go) | Go 1.14 x64 | strings | O(n^2) | AC | 0.015 s | 1088 KB |
| [1297_strings.java](1297_strings.java) | Java 1.8 | strings | O(n^2) | AC | 0.125 s | 444 KB |
| [1297_strings.py](1297_strings.py) | Python 3.12 x64 | strings | O(n^2) | AC | 0.171 s | 452 KB |
| [1297_strings.rs](1297_strings.rs) | Rust 1.75 x64 | strings | O(n^2) | AC | 0.046 s | 244 KB |
