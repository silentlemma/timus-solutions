# 1784. Tahúres

[Timus 1784](https://acm.timus.ru/problem.aspx?space=1&num=1784) · dificultad 1243 · greedy

Problema original de Alexander Ipatov, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una baraja de 52 cartas está en cuatro montones de 13. Cada montón
tiene de arriba abajo los valores 2, 3, …, A, pero los palos están
mezclados. Un movimiento toma unas cuantas cartas de un mismo palo de
la cima de un montón, sin cambiar su orden, y o bien forma con ellas un
montón nuevo, o bien las pone sobre la carta cuyo valor es uno más que
el de la carta de abajo de las tomadas. Hallar el menor número de
movimientos que deja cuatro montones, cada uno de un solo palo.

## Entrada

Cuatro líneas, los montones de arriba abajo, con 13 cartas cada una.
Una carta es un valor (2–9, T, J, Q, K, A) seguido de un palo (S, C, D,
H). Todas las cartas son distintas.

## Salida

El menor número de movimientos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2C 3C 4C 5C 6C 7C 8C 9C TC JC QC KC AC
2S 3S 4S 5S 6S 7S 8D 9D TD JD QD KD AD
2D 3D 4D 5D 6D 7D 8S 9S TS JS QS KS AS
2H 3H 4H 5H 6H 7H 8H 9H TH JH QH KH AH
```

Salida:

```
3
```

## Solución

Se recorren los valores de arriba abajo. Supongamos que cada montón ya
empieza con una serie de un solo palo desde el 2 hasta el valor r. Esa
serie debe acabar sobre la carta de valor r + 1 del mismo palo, que
está en la fila siguiente de algún montón. Así la fila r da una
aplicación de montones en montones: el montón i debe ir sobre el montón
target(i). Un montón que va a sí mismo no necesita nada. Los demás se
dividen en ciclos. En un ciclo de longitud L cada destino está tapado
por una serie que también hay que mover, así que una serie va primero a
un montón nuevo, luego se mueven una tras otra las otras L − 1, y la
serie apartada se mueve al final: L + 1 movimientos. Después cada
montón vuelve a empezar con una serie de un solo palo, ahora hasta el
valor r + 1, y la fila siguiente se trata igual. La respuesta suma los
costes de los 12 huecos entre filas. `O(1)`, la baraja tiene tamaño
fijo.

En el ejemplo solo cambia el palo entre el 7 y el 8. Las picas del
segundo montón deben ir sobre el 8S del tercero, y los diamantes del
tercero sobre el 8D del segundo: un ciclo de dos, 3 movimientos. Las
picas van a un montón nuevo, los diamantes van sobre el 8D y las picas
sobre el 8S.

Trampas:

- un ciclo cuesta uno más que su longitud, no su longitud;
- en una fila pueden aparecer varios ciclos separados, y cada uno paga
  su movimiento extra;
- para la aplicación solo importa el palo de la carta, el valor lo fija
  la fila.

Las respuestas coinciden con una implementación aceptada independiente
en 120 repartos aleatorios y con una búsqueda completa de todos los
movimientos en 225 barajas pequeñas con menos valores.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1784_greedy.cpp](1784_greedy.cpp) | G++ 13.2 x64 | greedy | O(1) | AC | 0.031 s | 380 KB |
| [1784_greedy.go](1784_greedy.go) | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 1112 KB |
| [1784_greedy.java](1784_greedy.java) | Java 1.8 | greedy | O(1) | AC | 0.140 s | 1652 KB |
| [1784_greedy.py](1784_greedy.py) | Python 3.12 x64 | greedy | O(1) | AC | 0.078 s | 512 KB |
| [1784_greedy.rs](1784_greedy.rs) | Rust 1.75 x64 | greedy | O(1) | AC | 0.031 s | 224 KB |
