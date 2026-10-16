# 1737. Mnemotecnia y palíndromos 3

[Timus 1737](https://acm.timus.ru/problem.aspx?space=1&num=1737) · dificultad 254 · strings

Problema original de Alexander Ipatov, del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Listar en orden alfabético todas las palabras de longitud n sobre las
letras a, b y c que no tienen ninguna subcadena palíndroma de dos o más
letras. Si ocuparían más de 100 000 letras en total, imprimir
`TOO LONG`.

## Entrada

n (1 ≤ n ≤ 20 000).

## Salida

Las palabras, una por línea, o `TOO LONG`.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
ab
ac
ba
bc
ca
cb
```

## Solución

Un palíndromo de dos o más letras tiene en su centro un palíndromo de
dos o tres letras, así que basta con que no haya dos letras vecinas
iguales ni dos letras iguales a una de distancia. Entonces tres letras
seguidas cualesquiera son a, b y c en algún orden, y cada letra repite
la de tres posiciones atrás: la palabra es uno de los seis órdenes de
a, b y c repetido. Así hay tres palabras para n = 1 y seis para todo n
mayor, y la respuesta es `TOO LONG` cuando 6n > 100 000, es decir, desde
n = 16 667. `O(n)`.

Trampas:

- para n = 1 los seis órdenes dan solo tres palabras distintas;
- el límite es sobre la longitud total, no sobre el número de palabras.

Las listas coinciden con la comprobación una por una de todas las
palabras sobre a, b y c para n hasta 9.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1737_strings.cpp](1737_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 252 KB |
| [1737_strings.go](1737_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1448 KB |
| [1737_strings.java](1737_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 3052 KB |
| [1737_strings.py](1737_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.125 s | 1132 KB |
| [1737_strings.rs](1737_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 328 KB |
