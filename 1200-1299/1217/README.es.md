# 1217. Billetes de la suerte a la vez en Moscú y en San Petersburgo

[Timus 1217](https://acm.timus.ru/problem.aspx?space=1&num=1217) · dificultad 408 · combinatorics

Problema original de Leonid Volkov, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El número de un billete tiene `N` cifras, `N` par y como mucho 20, con
ceros a la izquierda permitidos. Es de la suerte en Moscú si sus dos
mitades tienen la misma suma de cifras, y en San Petersburgo si las
cifras de las posiciones impares suman lo mismo que las de las pares.
Hay que contar los billetes de la suerte en ambos sentidos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

El número de esos billetes.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
100
```

## Solución

Se reparten las posiciones en cuatro grupos según la mitad y la paridad:
`A` y `B` son las posiciones impares y pares de la primera mitad, `C` y
`D` las de la segunda, y cada letra designa también la suma de cifras de
su grupo. Las dos condiciones se escriben `A + B = C + D` y
`A + C = B + D`. Sumándolas sale `A = D` y restándolas `B = C`; y al
revés, esas dos igualdades devuelven ambas condiciones. Los grupos son
independientes, así que la respuesta es

(pares de rellenos de `A` y `D` con sumas iguales) × (pares de rellenos
de `B` y `C` con sumas iguales).

El número de formas de obtener una suma `s` con `k` cifras sale de una
pequeña tabla construida cifra a cifra, y cada factor es la suma sobre
`s` de los productos de dos de esos números. `O(N²)` con constantes
diminutas.

Detalles a tener en cuenta:

- el tamaño de los grupos depende de si `N/2` es impar; contarlos
  posición a posición evita equivocarse;
- la respuesta para `N = 20` es de unos `1.9·10¹⁷`, más de 32 bits pero
  dentro de 64.

La fórmula se comprobó por fuerza bruta con todos los billetes de seis
cifras, y cada `N` par de 2 a 20 se comparó con una solución escrita
aparte.

## Notas por lenguaje

- Todos los lenguajes construyen las tablas de sumas de cifras igual y
  usan enteros de 64 bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1217_combinatorics.cpp](1217_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N²) | AC | 0.001 s | 192 KB |
| [1217_combinatorics.go](1217_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N²) | AC | 0.031 s | 1072 KB |
| [1217_combinatorics.java](1217_combinatorics.java) | Java 1.8 | combinatorics | O(N²) | AC | 0.109 s | 1592 KB |
| [1217_combinatorics.py](1217_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N²) | AC | 0.078 s | 436 KB |
| [1217_combinatorics.rs](1217_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N²) | AC | 0.031 s | 224 KB |
