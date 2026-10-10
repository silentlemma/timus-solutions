# 1118. El número con la menor suma de divisores propios por unidad

[Timus 1118](https://acm.timus.ru/problem.aspx?space=1&num=1118) · dificultad 103 · number_theory

Problema original de Leonid Volkov, del USU Open Collegiate Programming Contest, octubre de 2001, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La razón de un entero positivo `N` es la suma de sus divisores propios
(los menores que `N`) dividida entre `N`. Para `1 ≤ I ≤ J ≤ 10^6`, imprime
un número de `[I, J]` con la menor razón.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`I J` en una línea.

## Salida

El número con la menor razón.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
24 28
```

Salida:

```
25
```

## Solución

El 1 no tiene divisores propios, razón 0, y gana siempre que `I = 1`. Un
primo `p` tiene razón `1/p`, así que entre los primos el mayor es el
mejor. También supera a todo compuesto `n ≤ J` del rango: un compuesto
tiene un divisor `d ≥ √n` además del 1, así que su razón es al menos
`(1 + √n)/n`, y el mayor primo no mayor que `J` supera `J/2` (postulado de
Bertrand), lo que hace `1/p` menor. Así que se baja desde `J` y se para en
el primer primo.

Solo cuando el rango no contiene ningún primo hay que comparar razones;
ese rango está dentro de un hueco entre primos, como mucho 113 números por
debajo de `10^6`. Cada suma de divisores cuesta `O(√n)` por división de
prueba, y dos razones se comparan exactamente como `σ(a)·b < σ(b)·a`,
ganando el número menor en caso de empate. En total `O(g · √J)` para el
mayor hueco `g`.

Detalles a tener en cuenta:

- con `I = 1` la respuesta es 1, no el mayor primo;
- en un rango sin primos el mejor número no tiene por qué ser el mayor ni
  un cuadrado: `[24, 28]` da 25, `[8, 10]` da 9;
- no hace falta comparar razones en coma flotante; el producto cruzado
  cabe en 64 bits.

Las respuestas se comprobaron con una criba de las sumas de divisores de
todos los números hasta `10^6` y una comparación exacta en todo el rango,
en todas las pruebas, en 200 rangos aleatorios menores que 3000 y en el
mayor hueco entre primos por debajo de un millón.

## Notas por lenguaje

- Todos los lenguajes usan la misma división de prueba.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1118_number_theory.cpp](1118_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(g · √J), g ≤ 114 | AC | 0.015 s | 128 KB |
| [1118_number_theory.go](1118_number_theory.go) | Go 1.14 x64 | number_theory | O(g · √J), g ≤ 114 | AC | 0.031 s | 1060 KB |
| [1118_number_theory.java](1118_number_theory.java) | Java 1.8 | number_theory | O(g · √J), g ≤ 114 | AC | 0.109 s | 1552 KB |
| [1118_number_theory.py](1118_number_theory.py) | Python 3.12 x64 | number_theory | O(g · √J), g ≤ 114 | AC | 0.093 s | 440 KB |
| [1118_number_theory.rs](1118_number_theory.rs) | Rust 1.75 x64 | number_theory | O(g · √J), g ≤ 114 | AC | 0.031 s | 212 KB |
