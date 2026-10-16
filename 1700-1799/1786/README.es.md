# 1786. La biografía de Sandro

[Timus 1786](https://acm.timus.ru/problem.aspx?space=1&num=1786) · dificultad 110 · strings

Problema original de Olga Soboleva, del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que cambiar un texto de letras latinas para que contenga la palabra
"Sandro". Sustituir una letra por otra del mismo caso cuesta 5 monedas,
y cambiar el caso de una letra también cuesta 5. Hallar el menor coste.

## Entrada

El texto, de 6 a 200 letras.

## Salida

El menor número de monedas.

## Ejemplos

### Ejemplo 1

Entrada:

```
MyNameIsAlexander
```

Salida:

```
20
```

## Solución

Se prueban todas las posiciones para las seis letras del nombre. Una
letra cuesta 5 si su caso es incorrecto y 5 más si es otra letra, así
que una letra incorrecta en ambos sentidos cuesta 10. Se suman los seis
costes en cada posición y se toma la menor suma. El recorrido tarda
`O(n)`, pero Python copia el sufijo `text[start:]` en cada posición,
por lo que esa implementación tarda `O(n^2)`. Todas las implementaciones
usan `O(n)` memoria contando la entrada; la longitud máxima es solo 200.

En el ejemplo la mejor posición es "xander": la x necesita otra letra y
mayúscula, 10, mientras que e → r y r → o cuestan 5 cada una, 20 en
total.

Trampas:

- una letra incorrecta con el caso incorrecto paga las dos tarifas;
- en el test 03, `sANDRO`, las seis letras tienen el caso incorrecto y cuestan 30;
- el nombre puede empezar en la primera letra o acabar en la última.

Las respuestas de Python coinciden con un oráculo independiente basado
en el grafo de operaciones permitidas en 2.000 textos cortos aleatorios,
592 casos dirigidos, los 8 tests guardados y 64 casos generados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1786_strings.cpp](1786_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 384 KB |
| [1786_strings.go](1786_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1088 KB |
| [1786_strings.java](1786_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 1616 KB |
| [1786_strings.py](1786_strings.py) | Python 3.12 x64 | strings | O(n^2) | AC | 0.078 s | 428 KB |
| [1786_strings.rs](1786_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 216 KB |
