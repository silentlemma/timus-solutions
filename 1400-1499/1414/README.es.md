# 1414. Base de datos astronómica

[Timus 1414](https://acm.timus.ru/problem.aspx?space=1&num=1414) · dificultad 431 · sorting, binary_search

Problema original de Pavel Egorov, del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una base de nombres de estrellas empieza con el único nombre «sun».
Siguen hasta 10 000 operaciones, una por línea: «+name» añade un nombre
(puede añadirse de nuevo más tarde) y «?prefix» pide los nombres que
empiezan por el prefijo. Los argumentos son de 1 a 20 letras latinas
minúsculas o cifras. Para cada consulta hay que imprimir el prefijo y
luego los nombres que coinciden en orden de diccionario, sin
repeticiones, cada uno con una sangría de dos espacios, como mucho los
20 primeros.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Las operaciones.

## Salida

Las respuestas a las consultas.

## Ejemplos

### Ejemplo 1

Entrada:

```
?e
+earth
+egg
?e
+eagle
+earth
?ea
```

Salida:

```
e
e
  earth
  egg
ea
  eagle
  earth
```

## Solución

Se guardan los nombres en un conjunto ordenado. Los nombres con un
prefijo dado forman un tramo contiguo en orden de diccionario que
empieza donde se insertaría el propio prefijo, así que cada consulta
encuentra ese sitio por búsqueda binaria y avanza mientras el nombre
tenga el prefijo y se hayan impreso menos de 20. C++, Java y Rust usan
sus conjuntos de árbol; Go y Python mantienen un arreglo ordenado e
insertan en él, moviendo como mucho 10 000 referencias por inserción.
`O(Q log Q)` con conjuntos de árbol.

Detalles a tener en cuenta:

- «sun» está en la base desde el principio (prueba 02);
- los nombres añadidos varias veces no se repiten en la respuesta
  (prueba 03);
- solo se imprimen los 20 primeros nombres (prueba 04);
- los nombres tienen cifras, que van antes que las letras (prueba 07);
- el ejemplo del enunciado muestra los dos espacios de sangría como
  puntos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1414_sorting.cpp](1414_sorting.cpp) | G++ 13.2 x64 | sorting | O(Q log Q) | AC | 0.031 s | 5748 KB |
| [1414_sorting.go](1414_sorting.go) | Go 1.14 x64 | sorting | O(Q log Q) | AC | 0.031 s | 1868 KB |
| [1414_sorting.java](1414_sorting.java) | Java 1.8 | sorting | O(Q log Q) | AC | 0.156 s | 24264 KB |
| [1414_sorting.py](1414_sorting.py) | Python 3.12 x64 | sorting | O(Q log Q) | AC | 0.156 s | 19372 KB |
| [1414_sorting.rs](1414_sorting.rs) | Rust 1.75 x64 | sorting | O(Q log Q) | AC | 0.031 s | 6144 KB |
