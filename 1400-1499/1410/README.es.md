# 1410. Grieta

[Timus 1410](https://acm.timus.ru/problem.aspx?space=1&num=1410) · dificultad 386 · dp

Problema original de Den Raskovalov (idea de Magaz Asanov), del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da una frase: las palabras son tramos de letras latinas y cualquier
otro carácter las separa; ninguna palabra se repite sin contar
mayúsculas. Arthur responde con la misma frase tras borrar algunas
palabras, sin cambiar el orden. Una palabra puede durar como mucho
tantos segundos como letras tiene, y dos palabras que estaban juntas en
la frase no pueden quedar ambas. ¿Cuántos segundos puede durar la
respuesta como máximo?

Hasta 10 000 palabras de hasta 100 letras, como mucho 512 KB de
entrada.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

La frase.

## Salida

La duración máxima de la respuesta, en segundos.

## Ejemplos

### Ejemplo 1

Entrada:

```
You have come a long way
```

Salida:

```
11
```

En el ejemplo la respuesta es «You come long».

## Solución

Dos palabras forman un par prohibido en la respuesta justo cuando
estaban juntas en la frase, así que hay que elegir palabras sin dos
vecinas y con la mayor longitud total. Se recorren las palabras
guardando dos números: el mejor total con la última palabra conservada
y con ella borrada. Una palabra nueva de longitud w da
kept' = dropped + w y dropped' = max(kept, dropped). Las palabras se
separan al leer, sin guardar la frase. `O(tamaño de la entrada)`.

Detalles a tener en cuenta:

- la frase puede ocupar varias líneas (prueba 02);
- cualquier carácter que no sea letra separa palabras, incluidos
  apóstrofos, dígitos y `=`, y varios separadores seguidos no dan
  palabras vacías (pruebas 04, 05, gen4);
- puede que la entrada no tenga ninguna palabra, y entonces la respuesta
  es 0 (pruebas 03 y 06);
- tomar primero la palabra más larga es un error: en «tiny Enormous
  small» ganan las dos cortas (prueba 08).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1410_dp.cpp](1410_dp.cpp) | G++ 13.2 x64 | dp | O(L) | AC | 0.015 s | 108 KB |
| [1410_dp.go](1410_dp.go) | Go 1.14 x64 | dp | O(L) | AC | 0.031 s | 3180 KB |
| [1410_dp.java](1410_dp.java) | Java 1.8 | dp | O(L) | AC | 0.109 s | 568 KB |
| [1410_dp.py](1410_dp.py) | Python 3.12 x64 | dp | O(L) | AC | 0.078 s | 2012 KB |
| [1410_dp.rs](1410_dp.rs) | Rust 1.75 x64 | dp | O(L) | AC | 0.046 s | 1240 KB |
