# 1158. Contar las frases de longitud M que evitan todas las palabras prohibidas

[Timus 1158](https://acm.timus.ru/problem.aspx?space=1&num=1158) · dificultad 506 · strings

Problema original de Nick Durov, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un alfabeto tiene `N ≤ 50` letras, y una frase es cualquier cadena de
exactamente `M ≤ 50` letras. Se dan `P ≤ 10` palabras prohibidas de como
mucho 10 letras; una frase está prohibida si contiene una de ellas como
subcadena. Cuenta las frases que no están prohibidas. Las letras pueden
ser cualquier carácter con código mayor que 32, incluidos los mayores que
127.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N`, `M` y `P`, luego las `N` letras en una línea y luego las `P`
palabras.

## Salida

El número de frases permitidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3 3
QWE
QQ
WEE
Q
```

Salida:

```
7
```

## Solución

Se construye el autómata de Aho–Corasick de las palabras prohibidas: un
trie con enlaces de fallo, completado para que cada estado tenga
transición con cada letra. Un estado representa el final más largo del
texto leído que es prefijo de alguna palabra; es malo si en él termina una
palabra, directamente o a través de sus enlaces de fallo. Una frase está
permitida justo cuando al leerla nunca se entra en un estado malo.

Así que se cuentan caminos: `ways[s]` es el número de comienzos
permitidos de la longitud actual que acaban en el estado `s`. Se empieza
con un comienzo vacío en la raíz y se dan `M` pasos, cada uno enviando
`ways[s]` por las `N` transiciones que no entran en un estado malo. La
respuesta es la suma sobre todos los estados. El autómata tiene como
mucho 101 estados, así que un paso son unas 5000 sumas.

Detalles a tener en cuenta:

- la cuenta llega a `50⁵⁰ ≈ 8,9·10⁸⁴`, así que hacen falta enteros
  grandes;
- una palabra que contiene otra ya es mala en la más corta, lo que
  transmiten los enlaces de fallo;
- las letras son bytes arbitrarios, quizá mayores que 127, así que la
  entrada se lee como bytes y no se decodifica como texto;
- la misma palabra puede darse dos veces.

Las respuestas se compararon con el listado de todas las frases en 200
entradas aleatorias pequeñas; las pruebas guardan las letras mayores que
127 como caracteres Latin-1 en UTF-8, y el programa de ejecución las pasa
a las soluciones como bytes sueltos.

## Notas por lenguaje

- Python, Go y Java usan sus enteros grandes; C++ y Rust suman números
  guardados en bloques de nueve cifras decimales, que es todo lo que
  necesita el recuento.
- Java lee toda la entrada como bytes y lleva cada byte a `0..255`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1158_strings.cpp](1158_strings.cpp) | G++ 13.2 x64 | strings | O(M·S·N) | AC | 0.015 s | 472 KB |
| [1158_strings.go](1158_strings.go) | Go 1.14 x64 | strings | O(M·S·N) | AC | 0.031 s | 1684 KB |
| [1158_strings.java](1158_strings.java) | Java 1.8 | strings | O(M·S·N) | AC | 0.109 s | 5476 KB |
| [1158_strings.py](1158_strings.py) | Python 3.12 x64 | strings | O(M·S·N) | AC | 0.093 s | 768 KB |
| [1158_strings.rs](1158_strings.rs) | Rust 1.75 x64 | strings | O(M·S·N) | AC | 0.031 s | 340 KB |
