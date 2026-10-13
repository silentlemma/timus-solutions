# 1423. Fábula de una cadena

[Timus 1423](https://acm.timus.ru/problem.aspx?space=1&num=1423) · dificultad 171 · strings

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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1423_strings.cpp](1423_strings.cpp) | G++ 13.2 x64 | strings | O(N) | AC | 0.015 s | 1940 KB |
| [1423_strings.go](1423_strings.go) | Go 1.14 x64 | strings | O(N) | AC | 0.031 s | 4268 KB |
| [1423_strings.java](1423_strings.java) | Java 1.8 | strings | O(N) | AC | 0.125 s | 3492 KB |
| [1423_strings.py](1423_strings.py) | Python 3.12 x64 | strings | O(N) | AC | 0.109 s | 1372 KB |
| [1423_strings.rs](1423_strings.rs) | Rust 1.75 x64 | strings | O(N) | AC | 0.031 s | 3052 KB |
