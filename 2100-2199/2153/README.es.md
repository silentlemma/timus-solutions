# 2153. El mayor grupo de papeles distintos y qué recluta ayudaría

[Timus 2153](https://acm.timus.ru/problem.aspx?space=1&num=2153) · dificultad 934 · dp, bitmask

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de los n miembros del gremio tiene un conjunto no vacío de las
cuatro cualificaciones guerrero, mago, clérigo y pícaro. Un grupo da a
miembros distintos papeles distintos de sus cualificaciones. Hallar el
mayor grupo y, si tiene menos de cuatro miembros, enumerar las
cualificaciones para las que contratar a una persona solo con esa
cualificación haría mayor el mayor grupo. Los límites son 0.5 segundos y
256 MB.

## Entrada

n, 1 ≤ n ≤ 15, y luego las cualificaciones de cada miembro como una
subsecuencia de "WMCR".

## Salida

El mayor tamaño y, si es menor que 4, una línea "Looking for" con las
cualificaciones en el orden warrior, mage, cleric, rogue.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
W
```

Salida:

```
1
Looking for mage cleric rogue
```

### Ejemplo 2

Entrada:

```
2
M
CR
```

Salida:

```
2
Looking for warrior cleric rogue
```

### Ejemplo 3

Entrada:

```
4
WMCR
WMCR
WMCR
WMCR
```

Salida:

```
4
```

### Ejemplo 4

Entrada:

```
1
WMCR
```

Salida:

```
1
Looking for warrior mage cleric rogue
```

## Solución

Solo hay 16 conjuntos de papeles. Una DP sobre los miembros guarda qué
conjuntos de papeles pueden cubrir personas distintas: un miembro se
queda fuera o toma un papel libre del conjunto. Recorrer los conjuntos
en orden decreciente dentro del paso de un miembro le impide tomar dos
papeles. El mayor grupo es el mayor conjunto alcanzable.

Un recluta solo con la cualificación r agranda el grupo exactamente
cuando algún conjunto máximo no usa r: ese conjunto más el recluta es
mayor, y si todo conjunto máximo usara r, un grupo mayor contendría un
conjunto alcanzable del tamaño máximo anterior sin r. Así que el anuncio
enumera los papeles fuera de la intersección de todos los conjuntos
alcanzables máximos. El trabajo es O(16 · 4 · n).

En el segundo ejemplo los grupos mayores son {mago, clérigo} y
{mago, pícaro}; su intersección es {mago}, así que se buscan guerreros,
clérigos y pícaros.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2153_dp_bitmask.cpp](2153_dp_bitmask.cpp) | G++ 13.2 x64 | dp, bitmask | O(64 n) | AC | 0.015 s | 448 KB |
| [2153_dp_bitmask.go](2153_dp_bitmask.go) | Go 1.14 x64 | dp, bitmask | O(64 n) | AC | 0.031 s | 1168 KB |
| [2153_dp_bitmask.java](2153_dp_bitmask.java) | Java 1.8 | dp, bitmask | O(64 n) | AC | 0.078 s | 392 KB |
| [2153_dp_bitmask.py](2153_dp_bitmask.py) | Python 3.12 x64 | dp, bitmask | O(64 n) | AC | 0.109 s | 640 KB |
| [2153_dp_bitmask.rs](2153_dp_bitmask.rs) | Rust 1.75 x64 | dp, bitmask | O(64 n) | AC | 0.046 s | 244 KB |
