# 1744. La compañía del capitán

[Timus 1744](https://acm.timus.ru/problem.aspx?space=1&num=1744) · dificultad 2042 · constructive

Problema original de Artyom Ripatti, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada día tres de n soldados hacen la guardia nocturna, y dos soldados
no pueden hacer guardia juntos más de tres veces. Hacer un turno para
el mayor número de días posible.

## Entrada

Un n impar (3 ≤ n ≤ 99).

## Salida

El mayor número de días k y los tres soldados de cada día. Se acepta
cualquier turno de k días.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
3
1 2 3
2 3 1
3 1 2
```

### Ejemplo 2

Entrada:

```
5
```

Salida:

```
10
1 2 3
1 2 4
1 2 5
1 3 4
1 3 5
1 4 5
2 3 4
2 3 5
2 4 5
3 4 5
```

## Solución

Cada día junta tres pares de soldados, y cada uno de los n(n − 1)/2
pares puede coincidir tres veces, así que hay a lo sumo n(n − 1)/2
días. Esa cantidad se alcanza: se numeran los soldados 0 … n − 1 y se
toman los tríos i, i + d, i + 2d módulo n para todo i y todo d de 1 a
(n − 1)/2.

Un par de soldados cuyos números difieren en δ coincide dos veces como
vecinos en un trío, en los tríos del d con δ = ±d que empiezan en
cualquiera de los dos, y una vez como extremos de un trío, para el d
con δ = ±2d. Como n es impar, cada δ corresponde exactamente a un d del
primer tipo y, como se puede dividir entre 2 módulo n, exactamente a
uno del segundo, así que cada par coincide exactamente tres veces. Los
tres soldados de un trío son distintos porque d y 2d no son múltiplos
de n. `O(n²)`.

Para n = 3 esto da el primer ejemplo: d = 1 y las tres rotaciones de
1, 2, 3.

Trampas:

- los mismos tres soldados pueden hacer guardia varios días;
- el orden de los soldados dentro de un día no importa.

El comprobador verifica el número de días, los soldados y las veces que
coincide cada par; el turno se comprobó para todo n impar de 3 a 99.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1744_constructive.cpp](1744_constructive.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.015 s | 380 KB |
| [1744_constructive.go](1744_constructive.go) | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1228 KB |
| [1744_constructive.java](1744_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.125 s | 2028 KB |
| [1744_constructive.py](1744_constructive.py) | Python 3.12 x64 | constructive | O(n²) | AC | 0.078 s | 836 KB |
| [1744_constructive.rs](1744_constructive.rs) | Rust 1.75 x64 | constructive | O(n²) | AC | 0.015 s | 320 KB |
