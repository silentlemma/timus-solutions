# 1230. Un programa en un lenguaje de juguete que se imprime a sí mismo

[Timus 1230](https://acm.timus.ru/problem.aspx?space=1&num=1230) · dificultad 793 · strings

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que imprimir un programa en PIBAS, un pequeño lenguaje definido en el
enunciado, que imprima exactamente su propio texto. Un programa PIBAS es
una línea de sentencias separadas por `;`. Una sentencia o asigna una
expresión de texto a una variable nombrada por una letra mayúscula,
`V=expresión`, o la imprime, `?expresión`. Una expresión une con `+`
variables, constantes entre comillas simples o dobles (que no pueden
contener su propia comilla) y subcadenas `$(V,inicio,longitud)`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

No hay entrada.

## Salida

El programa PIBAS.

## Evaluación

Se acepta cualquier programa que sea PIBAS válido e imprima exactamente
su propio texto; el verificador de referencia lo ejecuta con un pequeño
intérprete de la gramática.

## Ejemplos

No hay entrada, y cualquier programa correcto es una respuesta válida,
así que el enunciado no da ninguna salida de ejemplo.

## Solución

La idea habitual de un quine: guardar la mayor parte del programa en una
cadena `A` e imprimirla dos veces, una entre comillas como el valor que
se asigna y otra como código. La dificultad son las comillas. `A` va
entre comillas simples, así que no puede contener una comilla simple, y
sin embargo el código que lleva tiene que imprimir ambas clases de
comilla. Por eso el programa primero las guarda en variables, `C="'"` y
`B='"'`, y el código que imprime solo se refiere a `C` y `B`:

```text
C="'";B='"';A=';?"C="+B+C+B+";B="+C+B+C+";A="+C+A+C+A';?"C="+B+C+B+";B="+C+B+C+";A="+C+A+C+A
```

La última sentencia imprime `C="'";B='"';A=` con las comillas sacadas de
las variables, luego `'`, el texto de `A`, `'` otra vez y el texto de `A`
una vez más, que es el programa entero. Cada solución imprime esta línea,
construida a partir de su comienzo y del texto de `A`. `O(1)`.

Detalles a tener en cuenta:

- una constante no puede contener su propia comilla, así que ninguna de
  las dos comillas se puede escribir directamente dentro de `A`;
- `?` imprime sin salto de línea, así que el programa debe imprimirse sin
  nada añadido entre sus partes.

El verificador ejecuta el programa impreso y compara lo que imprime con
su texto.

## Notas por lenguaje

- C++ y Rust usan cadenas en bruto y Go acentos graves para las dos
  piezas; Python usa una cadena con triples comillas para el comienzo, y
  Java escapa las comillas dobles.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1230_strings.cpp](1230_strings.cpp) | G++ 13.2 x64 | strings | O(1) | AC | 0.015 s | 80 KB |
| [1230_strings.go](1230_strings.go) | Go 1.14 x64 | strings | O(1) | AC | 0.001 s | 992 KB |
| [1230_strings.java](1230_strings.java) | Java 1.8 | strings | O(1) | AC | 0.031 s | 188 KB |
| [1230_strings.py](1230_strings.py) | Python 3.12 x64 | strings | O(1) | AC | 0.046 s | 284 KB |
| [1230_strings.rs](1230_strings.rs) | Rust 1.75 x64 | strings | O(1) | AC | 0.001 s | 176 KB |
