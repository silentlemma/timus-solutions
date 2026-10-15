# 1730. HombreOsoCerdo

[Timus 1730](https://acm.timus.ru/problem.aspx?space=1&num=1730) · dificultad 1147 · constructive

Problema original de Fedor Fominykh (preparado por Ivan Burmistrov), del Concurso Regional Escolar de Programación de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cruzar dos criaturas da una criatura que tiene, de cada animal, la
media de las dos proporciones. Dados los animales de una criatura y sus
proporciones, escribir una genealogía que la produzca: una lista de
líneas, cada una un animal o el cruce de dos líneas anteriores, que
termina con la criatura, y donde cada línea salvo la última participa
en algún cruce. Imprimir `No solution` si no la hay.

## Entrada

El nombre de la criatura: de uno a diez nombres de animales distintos
unidos por guiones, de 200 caracteres como mucho. Luego la proporción
de cada animal como fracción a/b (1 ≤ a ≤ b ≤ 1500); las proporciones
suman 1.

## Salida

El número de líneas n (1 ≤ n ≤ 10 000) y las líneas, o `No solution`.
Se acepta cualquier genealogía válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
man-bear-pig
1/2 1/4 1/4
```

Salida:

```
7
man
pig
1 2
bear
man
4 5
3 6
```

### Ejemplo 2

Entrada:

```
man
1/1
```

Salida:

```
1
man
```

### Ejemplo 3

Entrada:

```
man-bear-pig
1/3 1/3 1/3
```

Salida:

```
No solution
```

## Solución

En un cruce cada proporción es la media de dos proporciones, así que
por inducción toda proporción de cualquier genealogía tiene una
potencia de dos como denominador. Si alguna proporción reducida no la
tiene, no hay solución.

Si no, sea L el mayor denominador reducido, a lo sumo 1024. Se reparte
a cada animal su parte de L hojas iguales, en orden, y se construye
sobre las hojas un árbol binario equilibrado: cada nodo interno cruza
sus dos mitades, así que cada hoja aporta exactamente 1/L de la
criatura. Un subárbol cuyas hojas son todas un mismo animal es ese
animal, así que queda en una sola línea. Salen a lo sumo
2L − 1 ≤ 2047 líneas. `O(L)`.

En el primer ejemplo L = 4 y las hojas son man, man, bear, pig. La
mitad izquierda es man puro y la derecha cruza bear con pig, así que la
genealogía es man, bear, pig, 2 3, 1 4.

Trampas:

- las proporciones llegan sin reducir, como 750/1500, y hay que
  reducirlas antes de mirar el denominador;
- un animal puro es una genealogía de una línea, sin ningún cruce;
- el mismo animal puede aparecer en varias líneas.

El comprobador reproduce la genealogía con fracciones exactas y
verifica las proporciones, las referencias a líneas y que se use cada
antepasado. Las genealogías lo pasan en 200 casos aleatorios, con
`No solution` exactamente donde lo da una implementación aceptada
independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1730_constructive.cpp](1730_constructive.cpp) | G++ 13.2 x64 | constructive | O(L) | AC | 0.015 s | 428 KB |
| [1730_constructive.go](1730_constructive.go) | Go 1.14 x64 | constructive | O(L) | AC | 0.031 s | 1176 KB |
| [1730_constructive.java](1730_constructive.java) | Java 1.8 | constructive | O(L) | AC | 0.125 s | 1704 KB |
| [1730_constructive.py](1730_constructive.py) | Python 3.12 x64 | constructive | O(L) | AC | 0.093 s | 504 KB |
| [1730_constructive.rs](1730_constructive.rs) | Rust 1.75 x64 | constructive | O(L) | AC | 0.015 s | 244 KB |
