# 1760. Trabajo infernal

[Timus 1760](https://acm.timus.ru/problem.aspx?space=1&num=1760) · dificultad 681 · math

Problema original de Alexander Ipatov, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n elementos se copian en el mismo orden en dos cuadernos, a por página
en el primero y b por página en el segundo. Contar los pares de
elementos que están en una misma página del primer cuaderno pero en
páginas distintas del segundo.

## Entrada

a, b y n (1 ≤ a, b ≤ n ≤ 25 000 000).

## Salida

El número de esos pares.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4 10
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
2 4 10
```

Salida:

```
0
```

## Solución

La respuesta son los pares en una misma página del primer cuaderno,
n div a páginas llenas de C(a, 2) pares más C(n mod a, 2), menos los
pares en una misma página de ambos. Los saltos de página de los dos
cuadernos cortan la fila en trozos, y los pares en una misma página de
ambos son la suma de C(len, 2) sobre los trozos.

Esa suma se toma página a página sobre el cuaderno de páginas más
grandes: cada una de esas páginas queda cortada por las pequeñas en un
comienzo, algunas páginas pequeñas enteras y una cola, lo que cuesta
O(1) por página grande. Los saltos de ambos cuadernos se repiten cada
L = lcm(a, b) elementos, así que cuando L ≤ n la suma de un periodo se
multiplica por n div L y se suma el resto. En cualquier caso se
recorren a lo sumo unas √n páginas grandes: si L ≤ n hay
L / max(a, b) = min(a, b) / gcd(a, b) por periodo, a lo sumo √L, y si
L > n entonces max(a, b) > √n. El trabajo es `O(√n)`.

En el primer ejemplo las páginas de 3 tienen 3 pares cada una, 9 en
total, y los saltos en 3, 4, 6, 8 y 9 cortan la fila en trozos de 3, 1,
2, 2, 1 y 1 elementos con 5 pares: 9 − 5 = 4.

Trampas:

- la respuesta llega a unos 3·10¹⁴, más de 32 bits;
- recorrer los n elementos es demasiado lento en algunos lenguajes, y
  recorrer cada página del tamaño menor también cuando es diminuto;
- lcm(a, b) puede llegar a 6·10¹⁴, así que se calcula como a / gcd · b
  en 64 bits.

Las respuestas coinciden con un recuento par a par en 300 casos
pequeños, un recuento lineal en 60 más grandes y una implementación
aceptada independiente en 100 casos hasta los límites.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1760_math.cpp](1760_math.cpp) | G++ 13.2 x64 | math | O(sqrt(n)) | AC | 0.015 s | 128 KB |
| [1760_math.go](1760_math.go) | Go 1.14 x64 | math | O(sqrt(n)) | AC | 0.031 s | 1064 KB |
| [1760_math.java](1760_math.java) | Java 1.8 | math | O(sqrt(n)) | AC | 0.140 s | 1600 KB |
| [1760_math.py](1760_math.py) | Python 3.12 x64 | math | O(sqrt(n)) | AC | 0.078 s | 528 KB |
| [1760_math.rs](1760_math.rs) | Rust 1.75 x64 | math | O(sqrt(n)) | AC | 0.031 s | 236 KB |
