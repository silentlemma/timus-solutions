# 1027. Comprobar paréntesis y comentarios en un lenguaje de juguete

[Timus 1027](https://acm.timus.ru/problem.aspx?space=1&num=1027) · dificultad 637 · parsing

Problema original de Leonid Volkov y Alexey Lysenko, de la Segunda Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 7 de octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un texto de como mucho 10 000 caracteres es un programa correcto si se
divide en texto normal, comentarios y expresiones aritméticas así:

- un **comentario** empieza con `(*` y acaba en el siguiente `*)`; puede
  contener cualquier cosa y aparecer en cualquier sitio, también dentro de
  una expresión; debe cerrarse;
- una **expresión aritmética** empieza con `(` (no seguido de `*`) y acaba
  con su `)` correspondiente; entre ellos solo se permiten los caracteres
  `=+-*/0123456789`, paréntesis y saltos de línea (sin espacios), y los
  paréntesis deben estar equilibrados;
- el **texto normal** restante puede contener cualquier carácter salvo `(` y
  `)`.

Imprime `YES` si el texto es un programa correcto y `NO` en otro caso.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

El texto: letras latinas, dígitos, paréntesis, signos aritméticos, espacios
y saltos de línea.

## Salida

`YES` o `NO`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
Program text (1+2) more words (* a comment ) with a bracket *) end
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
just a) bracket
```

Salida:

```
NO
```

## Solución

Una pasada de izquierda a derecha con un solo contador `depth`: el nivel de
anidamiento de la expresión aritmética en que estamos (0 en texto normal).

- En `(*` empieza un comentario, estemos donde estemos: se busca el primer
  `*)` **después** del par de apertura y se salta tras él; si no lo hay, la
  respuesta es `NO`. Los comentarios no cambian `depth`.
- `(` abre un paréntesis: `depth + 1`.
- `)` cierra uno: si `depth` es 0, el paréntesis está en texto normal: `NO`;
  si no, `depth - 1`.
- Cualquier otro carácter vale en texto normal; dentro de una expresión
  (`depth > 0`) debe ser uno de `=+-*/0123456789` o un salto de línea.

Al final `depth` debe ser 0. `O(longitud)`.

Detalles a tener en cuenta:

- `(*)` **no** es un comentario cerrado: la búsqueda de `*)` empieza
  después de `(*`;
- los comentarios no se anidan: en `(* (*) *)` el comentario termina en el
  primer `*)` y el último `)` sobra;
- `(*` siempre abre un comentario, así que una expresión no puede empezar
  con `*` justo tras su paréntesis; pero `((*c*)*1)` es correcto: el
  comentario está entre `(` y `*`;
- un espacio dentro de una expresión hace incorrecto el programa; un salto
  de línea no;
- en Windows los saltos de línea pueden ser `\r\n`: trata `\r` como `\n`.

## Notas por lenguaje

La misma pasada en todos los lenguajes; el texto se lee como bytes crudos o
como una cadena entera.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1027_parsing.cpp](1027_parsing.cpp) | G++ 13.2 x64 | parsing | O(length) | AC | 0.015 s | 160 KB |
| [1027_parsing.go](1027_parsing.go) | Go 1.14 x64 | parsing | O(length) | AC | 0.031 s | 1080 KB |
| [1027_parsing.java](1027_parsing.java) | Java 1.8 | parsing | O(length) | AC | 0.093 s | 452 KB |
| [1027_parsing.py](1027_parsing.py) | Python 3.12 x64 | parsing | O(length) | AC | 0.093 s | 408 KB |
| [1027_parsing.rs](1027_parsing.rs) | Rust 1.75 x64 | parsing | O(length) | AC | 0.015 s | 232 KB |
