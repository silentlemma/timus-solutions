# 1164. ¿Qué letras quedan tras encontrar todas las palabras de una sopa de letras?

[Timus 1164](https://acm.timus.ru/problem.aspx?space=1&num=1164) · dificultad 206 · strings

Problema original de Alex Selivanov, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cuadrícula de `N×M` letras mayúsculas (`2 ≤ N, M ≤ 10`) esconde
`P ≤ 100` palabras. Cada palabra ocupa un camino de casillas vecinas por
un lado, y ninguna casilla pertenece a dos palabras ni dos veces a la
misma. Siempre existe una colocación válida. Hay que imprimir, en orden
alfabético, las letras de las casillas que no usa ninguna palabra.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`, `M` y `P`, luego las `N` filas de la cuadrícula y luego las `P`
palabras.

## Salida

Las letras sobrantes, ordenadas, en una línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3 2
EBG
GEE
EGE
BEG
GEE
```

Salida:

```
EEG
```

## Solución

No hace falta encontrar las palabras. Cualquier colocación usa cada letra
de cada palabra en exactamente una casilla, así que, sea cual sea la
colocación, las casillas sobrantes tienen las letras de la cuadrícula
menos las letras de las palabras, contadas con multiplicidad. Se cuentan
las 26 letras en la cuadrícula, se restan sus cuentas en las palabras y se
imprime cada letra tantas veces como quede.
`O(N·M + longitud total de las palabras)`.

Detalles a tener en cuenta:

- la búsqueda parece necesaria pero no lo es: la colocación puede ser
  ambigua, como en el ejemplo, pero el multiconjunto de letras sobrantes
  nunca lo es;
- si las palabras cubren toda la cuadrícula, la respuesta es una línea
  vacía.

## Notas por lenguaje

- Todos los lenguajes leen la entrada como palabras separadas por
  espacios, así que los saltos de línea no importan.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1164_strings.cpp](1164_strings.cpp) | G++ 13.2 x64 | strings | O(N·M + total word length) | AC | 0.015 s | 380 KB |
| [1164_strings.go](1164_strings.go) | Go 1.14 x64 | strings | O(N·M + total word length) | AC | 0.031 s | 1184 KB |
| [1164_strings.java](1164_strings.java) | Java 1.8 | strings | O(N·M + total word length) | AC | 0.109 s | 1640 KB |
| [1164_strings.py](1164_strings.py) | Python 3.12 x64 | strings | O(N·M + total word length) | AC | 0.078 s | 436 KB |
| [1164_strings.rs](1164_strings.rs) | Rust 1.75 x64 | strings | O(N·M + total word length) | AC | 0.015 s | 220 KB |
