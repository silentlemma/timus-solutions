# 1488. Póquer ACM

[Timus 1488](https://acm.timus.ru/problem.aspx?space=1&num=1488) · dificultad 1540 · implementation

Problema original de Vladimir Yakovlev, del Campeonato de la Universidad Estatal de los Urales, 7 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

A cada jugador se le reparten tres cartas. Dima puede cambiar a
escondidas una o dos de sus cartas por las dos que guarda en la manga,
pero nunca saca una carta igual a una de las de Sasha ni se queda con
dos cartas iguales. Las manos, de mejor a peor: tres treses, escalera de
color, trío, escalera, color, pareja, carta alta. Combinaciones iguales,
o dos manos sin pareja, se comparan por rangos de mayor a menor; una
pareja compara primero la pareja y luego la carta suelta. El as es
alto, y A-2-3 y K-A-2 no son escaleras. Para cada partida se escribe
«Dima» si Dima puede ganar, «Artyom» (quien reparte y se queda un
empate) si solo puede empatar, y «Sasha» en otro caso.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Partidas separadas por líneas vacías: las tres cartas de Sasha, las
tres de Dima y las dos de la manga, escritas como 10H o QS.

## Salida

Un nombre por partida.

## Ejemplos

### Ejemplo 1

Entrada:

```
4C AC 2C
4S KD 6H
5C KH

JS 8H JC
8C 8D 10H
8H 10H

10D 8D 9D
3D 3C 3H
AH AS

2C 3D 4H
2D 3H 4S
AH AH
```

Salida:

```
Dima
Sasha
Dima
Artyom
```

## Solución

Dima tiene como mucho diez manos para elegir: la repartida, cada una de
las tres cartas cambiada por cualquiera de la manga, y las dos de la
manga junto con una de las repartidas. Antes se descartan las cartas de
la manga iguales a alguna de Sasha, y se saltan las manos con dos cartas
iguales.

Cada mano recibe una clave que se ordena igual que las manos: el número
de la combinación y luego los rangos que deshacen empates. Los rangos
van de mayor a menor; en una pareja, el rango de la pareja y luego el
de la carta suelta. Tres treses no necesitan nada más. Dima gana si
alguna clave supera a la de Sasha, empata si alguna es igual y pierde
en otro caso. `O(1)` por partida.

Detalles a tener en cuenta:

- A-2-3 y K-A-2 no son escaleras, pero Q-K-A sí (prueba 02);
- en la manga puede haber una carta de Sasha, una copia de una carta
  propia de Dima o dos cartas iguales, y ninguna puede usarse de forma
  prohibida (pruebas 01, 02, gen3);
- tres treses ganan incluso a la mejor escalera de color (pruebas 01,
  02);
- claves iguales son un empate aunque los palos difieran (prueba 02,
  gen2).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1488_implementation.cpp](1488_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) per game | AC | 0.001 s | 428 KB |
| [1488_implementation.go](1488_implementation.go) | Go 1.14 x64 | implementation | O(1) per game | AC | 0.031 s | 5896 KB |
| [1488_implementation.java](1488_implementation.java) | Java 1.8 | implementation | O(1) per game | AC | 0.156 s | 6824 KB |
| [1488_implementation.py](1488_implementation.py) | Python 3.12 x64 | implementation | O(1) per game | AC | 0.203 s | 2232 KB |
| [1488_implementation.rs](1488_implementation.rs) | Rust 1.75 x64 | implementation | O(1) per game | AC | 0.015 s | 1256 KB |
