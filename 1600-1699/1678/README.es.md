# 1678. Póquer espacial 3

[Timus 1678](https://acm.timus.ru/problem.aspx?space=1&num=1678) · dificultad 5108 · combinatorics

Problema original de Alex Samsonov, del Ural SU Contest en el campus de verano de Petrozavodsk, agosto de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N jugadores reciben M cartas propias cada uno y se reparten K cartas
comunes en la mesa; la mano de un jugador son sus cartas propias más las
comunes. Las cartas solo tienen valor (13 valores, de 2 a A) y cada
carta de la baraja infinita toma cada valor con probabilidad 1/13. Una
combinación (v1, …, vL) pide v1 cartas de un valor, v2 de otro, etc.,
con L valores distintos; una mano la contiene si tiene al menos esas
cartas. Las C combinaciones vienen de la más barata a la más valiosa y
gana la ronda quien tenga la combinación más valiosa de la mesa; si
varios jugadores la comparten, hay empate.

Conociendo las cartas propias del primer jugador y las comunes ya
mostradas, hallar la probabilidad de que ese jugador gane en solitario.

## Entrada

N, M y K (2 ≤ N, M ≤ 10; 1 ≤ K ≤ 5); las M cartas propias del primer
jugador; las cartas comunes mostradas, como mucho K (la línea puede
estar vacía); C (1 ≤ C ≤ 100) y las combinaciones de la más barata a la
más valiosa, cada una como L v1 … vL, con todos los vi positivos y de
suma a lo sumo M + K.

## Salida

La probabilidad, con un error de a lo sumo 10⁻⁵.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 5 2
23456

1
1 2
```

Salida:

```
0.0883526857
```

### Ejemplo 2

Entrada:

```
2 5 2
23456
78
2
7 1 1 1 1 1 1 1
1 4
```

Salida:

```
0.8407915043
```

## Solución

Solo importa cuántas cartas hay de cada valor. Una mano contiene
(v1, …, vL) exactamente cuando, con ambas listas en orden decreciente,
la i-ésima mayor cantidad es al menos el i-ésimo mayor vi: la mayor
exigencia siempre puede tomar el valor más frecuente. Así, la mejor
combinación de una mano depende solo de sus cantidades ordenadas, que
una caché recuerda.

Se enumeran las cartas comunes ocultas como cantidades sobre los 13
valores; h cartas ocultas dan como mucho C(h + 12, 12) ≤ 6188 patrones,
cada uno con probabilidad multinomial h! / (Π xᵢ! · 13ʰ). Para cada
patrón se toma la mejor combinación c del primer jugador; sin ninguna
combinación no se puede ganar. Fijadas las cartas comunes, las cartas
propias de los rivales son independientes, así que el patrón suma su
probabilidad por q^(N − 1), donde q es la probabilidad de que la mejor
combinación de un rival sea más barata que c (no tener ninguna cuenta
como lo más barato).

Esa probabilidad depende solo de las cantidades comunes ordenadas, así
que hay como mucho p(K) ≤ 7 tablas distintas. Para construir una, se
agrupan los valores por su cantidad común: los g valores de un grupo
con cantidad común v son intercambiables, así que el grupo recibe una
partición de su parte s de las M cartas del rival en como mucho g
partes, colocada de g! / ((g − partes)! · Π mult!) maneras (mult cuenta
las partes iguales), con peso 1 / Π x!. El estado tras cada grupo es la
lista ordenada de cantidades del rival y el número de cartas usadas; al
final, cada estado completo por M! / 13ᴹ va a su mejor combinación, y
las sumas prefijas dan la probabilidad de «más barata que c» para cada c.

`O(C(K + 12, 12) · 13 + p(K) · S)`, donde S es el trabajo de una tabla,
unos pocos miles de formas de como mucho M + K cartas; todo tarda muy
por debajo de un segundo.

Trampas:

- la tercera línea puede estar vacía, así que la entrada se lee por líneas;
- un empate no es una victoria: el rival debe ser estrictamente más barato;
- una combinación pide al menos vi cartas, así que «KQKQKQ» contiene (2, 3).

Las respuestas coinciden con una enumeración directa de todos los
repartos en tamaños diminutos y con una implementación aceptada
independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1678_combinatorics.cpp](1678_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(C(K + 12, 12) · 13 + p(K) · S) | AC | 0.015 s | 624 KB |
| [1678_combinatorics.go](1678_combinatorics.go) | Go 1.14 x64 | combinatorics | O(C(K + 12, 12) · 13 + p(K) · S) | AC | 0.031 s | 5856 KB |
| [1678_combinatorics.java](1678_combinatorics.java) | Java 1.8 | combinatorics | O(C(K + 12, 12) · 13 + p(K) · S) | AC | 0.250 s | 7596 KB |
| [1678_combinatorics.py](1678_combinatorics.py) | Python 3.12 x64 | combinatorics | O(C(K + 12, 12) · 13 + p(K) · S) | AC | 0.171 s | 1260 KB |
| [1678_combinatorics.rs](1678_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(C(K + 12, 12) · 13 + p(K) · S) | AC | 0.046 s | 636 KB |
