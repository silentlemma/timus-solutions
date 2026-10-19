# 2075. Beber un cóctel por capas con una pajita

[Timus 2075](https://acm.timus.ru/problem.aspx?space=1&num=2075) · dificultad 2610 · fenwick

Problema original de Mikhail Rubinchik, preparado por Egor Shchelkonogov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los licores se vierten en un vaso y forman capas por densidad: un nombre
lexicográficamente menor es más denso y queda más abajo, y un licor
vertido de nuevo se une a su capa. Quien bebe mantiene la pajita a una
altura fija H y bebe 1 mm por segundo desde esa altura, así que las
capas de encima bajan hasta la pajita. Deja de beber en cuanto el cóctel
ya no llega a H, salvo que justo en ese momento se vierta algo. Dados
los eventos con tiempo (vertidos, colocación de la pajita, una
quemadura que la saca), imprimir los intervalos de tiempo en que bebe y
el licor de cada uno. Los límites son 1 segundo y 256 MB.

## Entrada

n ≤ 10⁵ eventos en tiempos T ≤ 10⁹ distintos y crecientes: `T name h`
vierte h ≤ 10⁹ mm de un licor (de 1 a 10 letras minúsculas), `T Oleg H`
pone la pajita a la altura H ≤ 10¹⁴, por debajo de la cima actual, y
empieza a beber, `T fire` deja de beber (solo llega mientras bebe).

## Salida

Líneas `from-to name` en tiempo creciente; dos líneas vecinas del mismo
licor no deben tocarse, así que los trozos que se tocan se unen.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
1 kahlua 1
2 baileys 1
3 cointreau 1
4 Oleg 0
5 kahlua 3
6 fire
20 Oleg 0
```

Salida:

```
4-5 baileys
5-6 cointreau
20-24 kahlua
```

## Solución

El vaso es una lista de capas ordenada por nombre. Beber d segundos a la
altura H quita el material de [H; H + d) y, como todo lo de encima baja,
lo toma de abajo hacia arriba. Así que hay que hallar la capa que
contiene la altura H, beber su parte por encima de H (o menos, si d se
acaba) y repetir con la capa siguiente mientras queden tiempo y cóctel.
La altura de la pajita no cambia mientras tanto.

Primero se leen y ordenan todos los nombres, lo que da a cada licor un
lugar fijo, y un árbol de Fenwick guarda las alturas de los lugares. La
capa que contiene la altura H es el primer lugar cuya suma de prefijo
supera H, hallado con el descenso habitual por el árbol en O(log m),
junto con cuánto de esa capa queda por encima de H. Cada paso o termina
de beber o vacía el resto de una capa por encima de la pajita; una capa
que está entera por encima de la pajita desaparece, así que aparte de
O(1) pasos por evento los pasos los pagan los vertidos, y el total es
O(n log n).

Entre dos eventos se bebe durante su diferencia de tiempo. Si el cóctel
se acaba antes, se deja de beber; si se acaba justo en el
evento siguiente, se sigue bebiendo, lo que solo importa si ese evento
es un vertido (una pajita nueva o la quemadura fijan el estado de todos
modos). Tras el último evento, si aún bebe, se vacía todo lo que hay por
encima de la pajita. Los trozos de un mismo licor que se tocan en el
tiempo se unen antes de imprimirlos.

En el ejemplo la pajita en 0 toma primero baileys (4-5) y luego el
cointreau que bajó (5-6); en 20 solo queda kahlua, 4 mm, bebidos en
20-24.

## Notas por lenguaje

Las alturas llegan a 10¹⁴ y los tiempos a unos 10⁹ + 10¹⁴, así que se
usan enteros de 64 bits. La solución en Python se envía en PyPy: en
CPython queda cerca del límite.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2075_fenwick.cpp](2075_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n log n) | AC | 0.531 s | 17600 KB |
| [2075_fenwick.go](2075_fenwick.go) | Go 1.14 x64 | fenwick | O(n log n) | AC | 0.343 s | 31640 KB |
| [2075_fenwick.java](2075_fenwick.java) | Java 1.8 | fenwick | O(n log n) | AC | 0.609 s | 46824 KB |
| [2075_fenwick.py](2075_fenwick.py) | PyPy 3.10 x64 | fenwick | O(n log n) | AC | 0.843 s | 79896 KB |
| [2075_fenwick.rs](2075_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n log n) | AC | 0.187 s | 27692 KB |
