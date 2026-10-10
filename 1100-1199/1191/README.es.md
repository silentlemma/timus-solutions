# 1191. ¿Puede un policía atrapar a un ladrón que cambia de tranvía?

[Timus 1191](https://acm.timus.ru/problem.aspx?space=1&num=1191) · dificultad 248 · math

Problema original de Leonid Volkov, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un ladrón lleva `L` minutos de ventaja a un policía y corren a la misma
velocidad. En cada una de `N` paradas el ladrón espera un tranvía de una
línea que pasa cada `Ki` minutos, con una fase desconocida, y lo toma
hasta la parada siguiente; el policía llega a la misma parada y toma el
siguiente tranvía de la misma línea, y detiene al ladrón si lo encuentra
todavía esperando. Todos los tranvías van a la misma velocidad. Hay que
decidir si el policía puede llegar a atrapar al ladrón antes de que
terminen los `N` viajes.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`L` y `N`, y luego `K1 … KN`, todos enteros menores que 100.

## Salida

`YES` si es posible atraparlo, si no `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
8 3
6 4 3
```

Salida:

```
NO
```

### Ejemplo 2

Entrada:

```
15 4
7 3 13 6
```

Salida:

```
YES
```

## Solución

Solo importa la distancia en tiempo entre ellos, y solo cambia en las
paradas. Si el ladrón llega a una parada con una ventaja de `g` minutos y
espera `w` minutos (`0 ≤ w < K`, según el horario), el policía llega `g`
minutos después que él. Si `w ≥ g`, el ladrón sigue allí. Si no, el
policía sale en el primer tranvía tras su llegada, un número entero de
intervalos después del tranvía del ladrón, así que la nueva ventaja es un
múltiplo de `K` de al menos `g − w`. Elegir `w = g mod K` da la menor
ventaja nueva posible, `g − g mod K`.

Una ventaja menor nunca es peor después, pues `g − g mod K` solo crece
con `g`. Así que se sigue el caso más afortunado: en cada parada la
ventaja pasa a ser `g − g mod K`, y atraparlo es posible exactamente
cuando la ventaja llega a 0 en alguna parada, lo que ocurre cuando es
menor que el intervalo de allí. `O(N)`.

Detalles a tener en cuenta:

- una ventaja igual al intervalo no permite atraparlo, simplemente se
  mantiene;
- los intervalos de 1 minuto nunca cambian la ventaja;
- aunque la ventaja sea múltiplo de un intervalo, las paradas siguientes
  todavía pueden reducirla.

Las respuestas se compararon con una solución escrita aparte en 300
persecuciones aleatorias y en todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes actualizan la ventaja con el operador de resto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1191_math.cpp](1191_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 124 KB |
| [1191_math.go](1191_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1060 KB |
| [1191_math.java](1191_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 1636 KB |
| [1191_math.py](1191_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 352 KB |
| [1191_math.rs](1191_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 212 KB |
