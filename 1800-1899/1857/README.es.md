# 1857. Alicia y el Bandersnatch

[Timus 1857](https://acm.timus.ru/problem.aspx?space=1&num=1857) · dificultad 1351 · combinatorics

Problema original de Pavel Klimov, del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La clave del cifrado de Alicia es una sucesión x₁, …, xₙ de números de
0 a a − 1, donde a es el tamaño del alfabeto; la clave se aplica una y
otra vez a las letras del mensaje. Las claves que solo difieren en un
desplazamiento cíclico cuentan como una, y no se usan las claves que
repiten un bloque más corto (con periodo menor que n). Contar las
claves distintas.

## Entrada

a y n (1 ≤ a ≤ 26, 1 ≤ n ≤ 10 000).

## Salida

El número exacto de claves.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4
```

Salida:

```
18
```

### Ejemplo 2

Entrada:

```
10 2
```

Salida:

```
45
```

## Solución

Las claves son los collares de longitud n sobre a letras con periodo
exactamente n, es decir, las palabras de Lyndon. Toda palabra de
longitud n repite un bloque primitivo cuya longitud d divide a n, así
que aⁿ = Σ para d | n de d·L(d), donde L(d) cuenta las palabras de
Lyndon de longitud d (cada una da d rotaciones distintas). La inversión
de Möbius lo convierte en n·L(n) = Σ para d | n de μ(d)·a^(n/d), donde
solo cuentan los d libres de cuadrados, con signo (−1) elevado al número
de sus factores primos.

Un número hasta 10 000 tiene como mucho cinco factores primos
distintos, así que hay como mucho 32 términos, pero a^(n/d) tiene hasta
14 150 cifras. Python, Go y Java usan sus enteros grandes; las
soluciones en C++ y Rust guardan los números en base 10⁹ y solo
necesitan multiplicar por a, sumar, restar y dividir entre n: los
términos positivos y los negativos se suman por separado y se restan
una vez. En C++ y Rust cada término se construye multiplicando por a
paso a paso: menos de 3n multiplicaciones de números de hasta 1600
cifras en base 10⁹, en tiempo O(n^2).

En el primer ejemplo, de las 81 claves de longitud 4 hay 9 con periodo
2 o 1, y las 72 restantes se agrupan en clases de rotación de 4: 18.

Trampas:

- con una sola letra toda clave de longitud mayor que 1 se repite a sí
  misma: la respuesta es 0, y 1 para n = 1;
- la respuesta es exacta y larga; Python 3.12 necesita levantar el
  límite por defecto para imprimir enteros largos.

Las respuestas coinciden con un conteo de todas las claves para a y n
pequeños y con una implementación aceptada independiente en longitudes
de hasta 10 000.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1857_combinatorics.cpp](1857_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n^2) | AC | 0.031 s | 228 KB |
| [1857_combinatorics.go](1857_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n^2) | AC | 0.031 s | 1464 KB |
| [1857_combinatorics.java](1857_combinatorics.java) | Java 1.8 | combinatorics | O(n^2) | AC | 0.140 s | 3932 KB |
| [1857_combinatorics.py](1857_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n^2) | AC | 0.093 s | 840 KB |
| [1857_combinatorics.rs](1857_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n^2) | AC | 0.062 s | 260 KB |
