# 1706. Mensaje cifrado 2

[Timus 1706](https://acm.timus.ru/problem.aspx?space=1&num=1706) · dificultad 678 · strings

Problema original de Dmitry Ivankov, del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una cadena s de longitud n y una clave k < n, para cada posición
i se toman los k caracteres que empiezan en i, volviendo al principio
de s al llegar al final, y se cuentan las subcadenas no vacías
distintas de esa ventana. Imprimir los n conteos.

## Entrada

k (1 ≤ k ≤ 1000) en la primera línea y s en la segunda: letras latinas
minúsculas, con longitud n, k < n ≤ 4000.

## Salida

Los n conteos separados por espacios.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
abaccc
```

Salida:

```
5 6 5 3 5 6
```

## Solución

Repetimos s para que cada ventana sea un tramo simple [a, a + k).
Cada subcadena distinta de una ventana se cuenta en su inicio j más a
la izquierda. Desde j, la ventana contiene las longitudes
1 … a + k − j, y una longitud ya está tomada justo cuando algún inicio
anterior j′ de la ventana, a ≤ j′ < j, comparte con j al menos esa
cantidad de caracteres. Así, el conteo de la ventana es la suma sobre
j de a + k − j menos best[j], el prefijo común más largo de j con un
inicio anterior de la ventana, sin bajar de cero.

Recorremos a de derecha a izquierda. Cuando a pasa a ser el extremo
izquierdo de una ventana, a cada best[j] solo se suma un inicio
anterior nuevo, el propio a, así que best[j] sube hasta lcp(a, j) para
j = a + 1 … a + k − 1. Estos prefijos salen del paso anterior:
lcp(a, a + d) vale lcp(a + 1, a + 1 + d) + 1 si coinciden los
caracteres en a y a + d, y 0 si no, de modo que basta un arreglo
indexado por la distancia d. Cada paso cuesta O(k), y el recorrido
empieza k posiciones más allá de la última ventana para que los
prefijos que importan ya sean exactos. Tiempo `O((n + k) · k)`,
memoria `O(n + k)`.

Trampas:

- las ventanas dan la vuelta al final de s; cuatro copias de s
  mantienen todas las comparaciones del recorrido dentro del texto;
- un autómata de sufijos por ventana también sirve, pero cuesta unos
  n · k pasos del autómata con transiciones por 26 letras;
- k = 1 da un 1 en cada posición (test 02).

Las respuestas coinciden con una implementación aceptada independiente
en cadenas aleatorias de dos, tres y todas las letras, una palabra de
Fibonacci y cadenas periódicas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1706_strings.cpp](1706_strings.cpp) | G++ 13.2 x64 | strings | O((n + k) k) | AC | 0.015 s | 272 KB |
| [1706_strings.go](1706_strings.go) | Go 1.14 x64 | strings | O((n + k) k) | AC | 0.046 s | 1292 KB |
| [1706_strings.java](1706_strings.java) | Java 1.8 | strings | O((n + k) k) | AC | 0.109 s | 972 KB |
| [1706_strings.py](1706_strings.py) | Python 3.12 x64 | strings | O((n + k) k) | AC | 1.734 s | 1224 KB |
| [1706_strings.rs](1706_strings.rs) | Rust 1.75 x64 | strings | O((n + k) k) | AC | 0.031 s | 408 KB |
