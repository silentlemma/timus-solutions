# 2011. Al Menos Seis Ordenaciones Distintas

[Timus 2011](https://acm.timus.ru/problem.aspx?space=1&num=2011) · dificultad 103 · combinatorics

Problema original de Alexey Kungurtsev, del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dispones de `n` símbolos de tres tipos posibles. Ordena todos para
formar una palabra de longitud `n`; los símbolos iguales son
indistinguibles. Decide si existen al menos seis palabras diferentes.
Cada símbolo disponible debe usarse exactamente una vez.

## Entrada

La primera línea contiene `n`, `1 ≤ n ≤ 100`. La segunda contiene `n`
enteros entre 1 y 3 que indican los tipos. Tiempo límite 0,5 segundos y
memoria 64 MB.

## Salida

Escribe `Yes` si existen al menos seis palabras, y `No` en caso
contrario. Se distinguen mayúsculas y minúsculas. La respuesta única se
compara por tokens.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
6
1 2 2 3 3 3
```

```
Yes
```

Las multiplicidades son 1, 2 y 3. Hay `6!/(1!·2!·3!)=60` palabras
distintas, de modo que la respuesta es `Yes`.

## Solución

Las piezas de un mismo tipo son iguales, así que k piezas con c₁, c₂, c₃
de cada tipo forman k!/(c₁!·c₂!·c₃!) palabras distintas. Se leen las
piezas una a una y se mantiene esta cuenta para las leídas: cuando llega
la k-ésima pieza y su tipo aparece ahora c veces, la cuenta se
multiplica por k y se divide exactamente entre c. En cuanto la cuenta
llega a 6, la respuesta es `Yes`: las piezas restantes, añadidas en un
orden fijo, mantienen distintas las palabras. Si nunca llega a 6, la
respuesta es `No`. `O(n)`.

Antes de cada paso la cuenta es a lo sumo 5, así que 5 · 100 cabe en
cualquier tipo entero; se multiplica antes de dividir.

Detalles a tener en cuenta:

- exactamente seis palabras ya es `Yes`;
- no hay que calcular los factoriales completos: se desbordan.

## Soluciones optimizadas

La solución optimizada en C++ cuenta los valores al leerlos con `scanf`
en lugar de `iostream` y un vector, e imprime la respuesta en cuanto la
conoce: 116 KB en lugar de 380 KB, con el mismo tiempo.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2011_combinatorics.cpp](2011_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.031 s | 380 KB | 11292493 |
| [2011_combinatorics.go](2011_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.046 s | 1112 KB | 11292495 |
| [2011_combinatorics.java](2011_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.125 s | 1668 KB | 11303363 |
| [2011_combinatorics.py](2011_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.109 s | 516 KB | 11292497 |
| [2011_combinatorics.rs](2011_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.062 s | 232 KB | 11292499 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2011_combinatorics_optimized.cpp](2011_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.015 s | 116 KB | 11303791 |
