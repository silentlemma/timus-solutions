# 1866. Pie métrico

[Timus 1866](https://acm.timus.ru/problem.aspx?space=1&num=1866) · dificultad 752 · parsing

Problema original de Alex Samsonov, del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un pie es un grupo de sílabas con una de ellas acentuada. El troqueo y
el yambo tienen pies de dos sílabas acentuados en la primera y en la
segunda; el dáctilo, el anfíbraco y el anapesto tienen pies de tres
sílabas acentuados en la primera, la segunda y la tercera. Cada verso
de un poema es una serie de pies de un mismo tipo, y el último pie
puede quedar incompleto. Las sílabas de una palabra van unidas por
guiones y las acentuadas van entre corchetes. Hay que nombrar el metro
del poema o escribir "not a poem".

## Entrada

n (2 ≤ n ≤ 100), luego n versos de como mucho 50 caracteres con al
menos cuatro sílabas cada uno, hechos de letras latinas, espacios,
guiones y corchetes.

## Salida

"trochee", "iamb", "dactyl", "amphibrach", "anapaest" o "not a poem".

## Ejemplos

### Ejemplo 1

Entrada:

```
4
My [un]-cle [high] i-[deals] ins-[pire] him
But [when] past [jo]-king [he] fell [sick]
he [real]-ly [forced] one [to] ad-[mire] him
and [ne]-ver [played] a [shrew]-der [trick]
```

Salida:

```
iamb
```

## Solución

Se parte cada verso por espacios y guiones en sílabas y se marcan las
que llevan un corchete. Un metro con pies de k sílabas acentuados en el
lugar p encaja en un verso si la sílaba i (desde 0) está acentuada
exactamente cuando i mod k = p − 1. Un último pie incompleto no cambia
nada, porque solo importa el lugar dentro del pie. La respuesta es el
primer metro que encaja en todos los versos; con al menos cuatro
sílabas por verso no hay dos metros con las mismas marcas, así que el
orden de las comprobaciones da igual. `O(L)` para L caracteres en
total.

En el ejemplo cada verso acentúa las sílabas 2, 4, 6 y 8: es un yambo.

Trampas:

- cada sílaba debe coincidir, también las átonas: una sílaba átona en
  un lugar acentuado rompe el metro;
- entre palabras puede haber varios espacios, así que hay que saltar
  los trozos vacíos;
- "not a poem" son tres palabras, que la salida debe escribir tal cual.

Las respuestas coinciden con una implementación aceptada independiente
en 300 poemas aleatorios, 120 de ellos rotos en una sílaba o en un
verso.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1866_parsing.cpp](1866_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 432 KB |
| [1866_parsing.go](1866_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.031 s | 1156 KB |
| [1866_parsing.java](1866_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.125 s | 1132 KB |
| [1866_parsing.py](1866_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.078 s | 480 KB |
| [1866_parsing.rs](1866_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.046 s | 240 KB |
