# 1179. La base en la que un texto contiene más números

[Timus 1179](https://acm.timus.ru/problem.aspx?space=1&num=1179) · dificultad 295 · strings

Problema original de Pavel Atnashev, del Tercer Concurso Individual de Programación de la Universidad Estatal de los Urales, Ekaterimburgo, 16 de febrero de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un texto de hasta 1 MB consta de dígitos, letras latinas mayúsculas,
espacios y saltos de línea; las letras son dígitos de `A = 10` a `Z = 35`.
En base `K`, un número es una racha máxima de caracteres que son dígitos
de la base `K`. Hay que hallar la base `K` de 2 a 36 en la que el texto
tiene más números, la menor en caso de empate, y esa cantidad.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El texto.

## Salida

`K` y el número de números.

## Ejemplos

### Ejemplo 1

Entrada:

```
01234B56789
AZA
```

Salida:

```
11 4
```

## Solución

Cada carácter recibe un valor: su valor de dígito, o 36 para un espacio o
un salto de línea, que es demasiado grande para ser dígito en cualquier
base. También se pone un separador así delante del texto. En base `K`,
empieza un número en cada carácter cuyo valor es menor que `K` mientras el
valor anterior es al menos `K`. Así que un par vecino de valores
`(left, right)` con `right < left` empieza un número en cada base de
`right + 1` a `left` (y desde 2 como mínimo).

Se cuenta cuántas veces aparece cada uno de los 37 × 37 pares, se reparte
cada cuenta sobre su rango de bases con un arreglo de diferencias y se
elige la mejor base. `O(L + 37²)` para un texto de longitud `L`.

Detalles a tener en cuenta:

- el primer carácter también empieza un número, de lo que se encarga el
  separador puesto delante;
- un texto vacío, o sin dígitos, da `2 0`;
- en base 36 toda letra, incluida la `Z`, es un dígito.

Las respuestas se compararon con una solución escrita aparte, que sigue
cada base carácter a carácter, en 200 textos aleatorios y en todas las
pruebas.

## Notas por lenguaje

- Python evita un bucle sobre un megabyte: convierte el texto en valores
  con un solo `translate` y cuenta cada par de dos bytes con
  `bytes.count`. Un par de dos bytes distintos no puede solaparse con otra
  copia de sí mismo, así que esta cuenta es exacta. Los demás lenguajes cuentan los pares en
  una pasada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1179_strings.cpp](1179_strings.cpp) | G++ 13.2 x64 | strings | O(L + 37²) | AC | 0.031 s | 116 KB |
| [1179_strings.go](1179_strings.go) | Go 1.14 x64 | strings | O(L + 37²) | AC | 0.015 s | 3160 KB |
| [1179_strings.java](1179_strings.java) | Java 1.8 | strings | O(L + 37²) | AC | 0.125 s | 588 KB |
| [1179_strings.py](1179_strings.py) | Python 3.12 x64 | strings | O(L + 37²) | AC | 0.640 s | 3100 KB |
| [1179_strings.rs](1179_strings.rs) | Rust 1.75 x64 | strings | O(L + 37²) | AC | 0.015 s | 2124 KB |
