# 1177. Comparar cadenas con patrones like de SQL

[Timus 1177](https://acm.timus.ru/problem.aspx?space=1&num=1177) · dificultad 1249 · strings

Problema original de Pavel Atnashev, del Tercer Concurso Individual de Programación de la Universidad Estatal de los Urales, Ekaterimburgo, 16 de febrero de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que responder hasta 1000 preguntas de la forma
`'cadena' like 'patrón'`. En un patrón, `%` coincide con cualquier
secuencia de caracteres, `_` con un carácter cualquiera, `[...]` con un
carácter de un conjunto de caracteres sueltos y rangos `c1-c2`, y
`[^...]` con un carácter fuera de ese conjunto; todo lo demás coincide
consigo mismo. Cadenas y patrones tienen hasta 100 caracteres de códigos
32–255, y una comilla dentro de ellos se escribe dos veces.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas `'cadena' like 'patrón'`.

## Salida

`YES` o `NO` para cada línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
15
'abcde' like 'a'
'abcde' like 'a%'
'abcde' like '%a'
'abcde' like 'b'
'abcde' like 'b%'
'abcde' like '%b'
'25%' like '_5[%]'
'_52' like '[_]5%'
'ab' like 'a[a-cdf]'
'ad' like 'a[a-cdf]'
'ab' like 'a[-acdf]'
'a-' like 'a[-acdf]'
'[]' like '[[]]'
'''''' like '_'''
'U' like '[^a-zA-Z0-9]'
```

Salida:

```
NO
YES
NO
NO
NO
NO
YES
YES
YES
YES
NO
YES
YES
YES
NO
```

## Solución

Cada línea se lee como bytes y se deshacen las comillas dobladas en ambas
partes. Después se recorre el patrón elemento a elemento, guardando el
conjunto de longitudes `i` tales que lo recorrido del patrón coincide
exactamente con los primeros `i` bytes de la cadena:

- un byte o `_` lleva cada `i` a `i + 1` si el byte siguiente encaja;
- un conjunto hace lo mismo con su prueba de pertenencia;
- `%` conserva todas las longitudes desde la menor del conjunto en
  adelante.

La respuesta es si la longitud completa está en el conjunto al final.
`O(n·m)` por pregunta.

La sintaxis de los conjuntos requiere cuidado. Tras `[` un `^` opcional
niega; después vienen elementos hasta el primer `]`. Un elemento `a-b` es
un rango cuando hay un tercer carácter y no es `]`; si no, `a` y `-` son
caracteres separados, así que `[-acdf]` y `[a-]` contienen un guion, y
`[[]` es un conjunto con solo `[`. Un `[` sin `]` de cierre no coincide
con nada.

Detalles a tener en cuenta:

- los caracteres por encima de 127 son bytes sueltos, así que deben
  compararse y meterse en rangos como bytes sin signo, no decodificarse
  como texto;
- un patrón vacío solo coincide con la cadena vacía, y `%` también
  coincide con ella;
- un rango con los extremos al revés, como `[c-a]`, está vacío.

Las respuestas se compararon con una solución escrita aparte en 60 000
preguntas aleatorias con comillas, corchetes, `^`, `-`, bytes altos y
conjuntos sin cerrar.

## Notas por lenguaje

- Python guarda el conjunto de longitudes como una máscara de bits en un
  entero grande, con una máscara por cada byte de la cadena; los demás
  lenguajes usan un arreglo booleano en cada paso. Java lee la entrada
  como Latin-1, para que cada byte sea el carácter con el mismo código.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1177_strings.cpp](1177_strings.cpp) | G++ 13.2 x64 | strings | O(n·m) per question | AC | 0.031 s | 372 KB |
| [1177_strings.go](1177_strings.go) | Go 1.14 x64 | strings | O(n·m) per question | AC | 0.015 s | 5424 KB |
| [1177_strings.java](1177_strings.java) | Java 1.8 | strings | O(n·m) per question | AC | 0.093 s | 5036 KB |
| [1177_strings.py](1177_strings.py) | Python 3.12 x64 | strings | O(n·m) per question | AC | 0.203 s | 1132 KB |
| [1177_strings.rs](1177_strings.rs) | Rust 1.75 x64 | strings | O(n·m) per question | AC | 0.015 s | 736 KB |
