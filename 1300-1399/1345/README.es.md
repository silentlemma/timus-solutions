# 1345. HTML

[Timus 1345](https://acm.timus.ru/problem.aspx?space=1&num=1345) · dificultad 1389 · parsing

Problema original de Pavel Egorov, del USU Championship 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado un programa correcto en Pascal de hasta 100 000 caracteres, hay
que envolver cada comentario, palabra clave, cadena y número en
`<span class=comment>`, `<span class=keyword>`, `<span class=string>`
o `<span class=number>` y `</span>`, dejando todo lo demás como está.
Lo que está dentro de un comentario pertenece al comentario, y lo que
está dentro de una cadena, a la cadena.

- Una cadena es un texto entre dos apóstrofos sin apóstrofos dentro, o
  `#` seguido de una serie no vacía de cifras, lo más larga posible.
- Un número empieza y acaba en cifra y solo tiene cifras y como mucho un
  punto; siempre es la serie más larga posible.
- Un identificador empieza por una letra o `_` y sigue con letras,
  cifras y `_`, también la serie más larga posible.
- Un comentario es `{` hasta la siguiente `}`, ambas incluidas, o `//`
  hasta el final de la línea, sin el salto de línea. Un comentario
  dentro de otro es parte del exterior.
- Las palabras clave son 35 identificadores como `begin`, `end` e
  `implementation`, en cualquier mayúscula o minúscula.

El texto puede tener bytes mayores que 127, y su última línea puede no
tener salto de línea.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El programa.

## Salida

El programa con las etiquetas.

## Ejemplos

### Ejemplo 1

Entrada:

```
Begin
  writeln('Hello world!');
end.
```

Salida:

```
<span class=keyword>Begin</span>
  writeln(<span class=string>'Hello world!'</span>);
<span class=keyword>end</span>.
```

## Solución

Se lee el texto de izquierda a derecha y el primer carácter decide qué
empieza ahí: `{` o `//` empiezan un comentario, `'` o `#` con una cifra
una cadena, una cifra un número, y una letra o `_` un identificador.
Cada parte se lee entera y se envuelve si corresponde; lo demás se copia.
Como lo que empieza antes se queda con todo hasta su propio final, una
`{` dentro de una cadena o un `'` dentro de un comentario no
necesitan ningún cuidado. Un identificador recibe la etiqueta de palabra
clave cuando su forma en minúsculas está en la lista, y leer los
identificadores enteros evita tomar las cifras de `a1` por un número.
`O(L)` para L caracteres.

Detalles a tener en cuenta:

- `1..10` son dos números y un rango, y `1.5.3` es el número `1.5`, un
  punto y el número `3`: un punto solo cuenta con cifras detrás
  (prueba 04);
- `'it''s'` son dos cadenas, `'it'` y `'s'`, y `#13#10` también son dos
  (prueba 05);
- un comentario `{` acaba en la primera `}`, aunque dentro haya otra
  `{` (prueba 03);
- el texto se trata como bytes, así que las letras por encima de 127
  pasan sin cambios (prueba 06), y un salto de línea final que falta
  sigue faltando (pruebas 01 y 08);
- los saltos de línea de Windows se leen como saltos normales, así que
  un comentario `//` no se lleva el retorno de carro.

## Notas por lenguaje

- Todas las soluciones trabajan con bytes; Python los lee como latin-1,
  que convierte cada byte en un carácter y vuelta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1345_parsing.cpp](1345_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 556 KB |
| [1345_parsing.go](1345_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.031 s | 1136 KB |
| [1345_parsing.java](1345_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.093 s | 1140 KB |
| [1345_parsing.py](1345_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.078 s | 828 KB |
| [1345_parsing.rs](1345_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.062 s | 504 KB |
