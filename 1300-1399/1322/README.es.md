# 1322. Espía

[Timus 1322](https://acm.timus.ru/problem.aspx?space=1&num=1322) · dificultad 184 · strings

Problema original con idea de Alexander Klepinin, preparado por Alexander Klepinin y Stanislav Vasiliev, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cifrador toma un texto de hasta 100 000 caracteres, escribe todas
sus rotaciones cíclicas, las ordena y devuelve la última columna de la
tabla ordenada junto con el número K de la fila que contiene el texto
original. Dados K y la última columna, hay que recuperar el texto. Los
caracteres son letras y el guion bajo, ordenados así: A a Z, luego `_`,
luego a a z.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

El número K en la primera línea y la última columna en la segunda.

## Salida

El texto original.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
rdarcaaaabb
```

Salida:

```
abracadabra
```

## Solución

Es la inversa de la transformada de Burrows–Wheeler. Las filas que
terminan en un carácter c se convierten en las filas que empiezan por c
al pasar c del final al principio, y esto conserva su orden. Las filas
que empiezan por c están ordenadas por lo que sigue a c, y así
exactamente están ordenadas las filas que terminan en c. Por tanto, la
j-ésima fila que termina en c es la j-ésima fila que empieza por c,
rotada una posición.

Se ordenan de forma estable las posiciones de la última columna por
carácter; el resultado se llama order. La fila order[j] termina con el
j-ésimo carácter de la columna ordenada, el mismo con el que empieza la
fila j, y la fila order[j] es la fila j desplazada una posición a la
izquierda: la rotación que empieza un carácter más tarde. Partiendo de
la fila K y siguiendo order n veces se recorren las rotaciones que
empiezan en el segundo, tercer, … carácter del texto, y el último
carácter de cada una es el que está justo antes de su inicio, así que
el texto sale en orden. El orden de caracteres dado es el orden ASCII,
así que una ordenación por conteo sobre 128 códigos hace la ordenación
estable. `O(n)`.

Detalles a tener en cuenta:

- en un texto periódico varias filas son iguales y K puede señalar
  cualquiera de ellas; todas llevan al mismo texto (prueba 04);
- las mayúsculas van antes del guion bajo y las minúsculas después
  (prueba 05);
- la ordenación debe ser estable, o los caracteres iguales se mezclan;
- el límite de tiempo es de 0,25 segundos, así que la entrada se lee de
  una vez.

El descifrador se comprobó cifrando 400 textos aleatorios y periódicos
de hasta 12 caracteres con una ordenación directa de sus rotaciones.

## Notas por lenguaje

- Python ordena las posiciones con la ordenación estable incorporada;
  los demás lenguajes usan una ordenación por conteo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1322_strings.cpp](1322_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 1036 KB |
| [1322_strings.go](1322_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.015 s | 2624 KB |
| [1322_strings.java](1322_strings.java) | Java 1.8 | strings | O(n) | AC | 0.093 s | 3152 KB |
| [1322_strings.py](1322_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 6308 KB |
| [1322_strings.rs](1322_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 1108 KB |
