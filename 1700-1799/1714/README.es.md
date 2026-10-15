# 1714. Mnemotecnia y palíndromos 2

[Timus 1714](https://acm.timus.ru/problem.aspx?space=1&num=1714) · dificultad 3123 · constructive

Problema original de Igor Chevdar, de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La complejidad de una palabra es el menor número de palíndromos en que
se puede partir. Imprimir una palabra de n letras a y b con la mayor
complejidad.

## Entrada

n (1 ≤ n ≤ 1000).

## Salida

Una palabra así. Se acepta cualquiera.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
```

Salida:

```
aababb
```

## Solución

Con dos letras los palíndromos aparecen con facilidad, así que una
palabra difícil debe evitar los largos. La palabra usada aquí empieza
con aabab, repite el bloque bbaaba y termina con una cola corta elegida
según n mod 6: nada, b, bb, bbaaababb, bbaa o bbaab. Cada bloque añade
dos palíndromos a la partición mínima. Algunas longitudes cortas
necesitan palabras propias: ab para 2, aababbaa para 8 y aababbaabab
para 11. Hasta 5 letras basta un prefijo de aabab. `O(n)`.

La complejidad de estas palabras es ⌊n/3⌋ + 1 para n ≥ 12, y una más
cuando n ≡ 2 (mod 6). Las longitudes menores dan 1, 2, 2, 2, 2, 3, 3,
4, 4, 4, 5. Una búsqueda exhaustiva sobre todas las palabras confirma
que es la mayor complejidad para todo n hasta 20. Para n mayores no se
demuestra aquí una cota que coincida: las palabras son las de una
implementación aceptada independiente, y coinciden con ella para todo
n de 1 a 1000.

Trampas:

- la regla simple del prefijo falla en n = 2: aa es un palíndromo,
  mientras que ab necesita dos;
- en n = 8 la cola larga aún no cabe, y en n = 11 al patrón le falta
  un palíndromo, así que esas longitudes usan palabras halladas por
  búsqueda;
- se acepta cualquier palabra de complejidad máxima, así que las
  pruebas usan un comprobador que calcula el mínimo número de
  palíndromos por partición con programación dinámica.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1714_constructive.cpp](1714_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.031 s | 380 KB |
| [1714_constructive.go](1714_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1112 KB |
| [1714_constructive.java](1714_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.140 s | 1660 KB |
| [1714_constructive.py](1714_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.093 s | 452 KB |
| [1714_constructive.rs](1714_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 224 KB |
