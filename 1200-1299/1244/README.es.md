# 1244. Qué cartas faltan en una baraja, por su peso

[Timus 1244](https://acm.timus.ru/problem.aspx?space=1&num=1244) · dificultad 254 · dp

Problema original de Alexander Petrov, del Concurso Individual de la Universidad Estatal de los Urales, 1 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una baraja completa tiene N cartas (2 ≤ N ≤ 100) de pesos conocidos de 1
a 1000 miligramos. Una baraja incompleta pesa W, menos que la completa.
Hay que imprimir los números de las cartas que faltan en orden creciente
si quedan determinadas de forma única, -1 si pueden faltar distintos
conjuntos de cartas, y 0 si no puede faltar ninguno.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

W, luego N y luego los N pesos de las cartas.

## Salida

Las cartas que faltan, -1 o 0.

## Ejemplos

### Ejemplo 1

Entrada:

```
270
4
100
110
170
200
```

Salida:

```
2 4
```

### Ejemplo 2

Entrada:

```
270
4
100
110
160
170
```

Salida:

```
-1
```

### Ejemplo 3

Entrada:

```
270
4
100
120
160
180
```

Salida:

```
0
```

## Solución

Las cartas que quedan en la baraja forman un conjunto de peso total W, y
las que faltan son el resto. Así que se cuentan los conjuntos de cartas
que pesan W, pero solo hasta 2, porque no importa más: `ways[i][s]` es el
número de conjuntos de las primeras i cartas que pesan s, con tope 2, y
`ways[i][s] = min(2, ways[i−1][s] + ways[i−1][s − w_i])`. Entonces
`ways[N][W]` vale 0, 2 (se imprime -1) o exactamente 1.

Para el conjunto único, se recorre hacia atrás desde la última carta con
s = W: la carta i falta justo cuando las primeras i − 1 cartas ya forman
s por sí solas, `ways[i−1][s] = 1`; si no, está en la baraja y s baja en
su peso. La unicidad hace que solo pueda cumplirse una de las dos cosas.
`O(N·W)` con W < 100 000.

Detalles a tener en cuenta:

- cartas iguales son cartas distintas: con dos cartas de peso 1 y W = 1
  puede faltar cualquiera, así que la respuesta es -1 (prueba 04);
- pueden faltar varias cartas, hasta todas menos una (prueba 08).

Las respuestas se compararon con la prueba de todos los subconjuntos en
1500 barajas pequeñas aleatorias.

## Notas por lenguaje

- Python guarda «al menos una forma» y «al menos dos formas» como dos
  enteros grandes usados como conjuntos de bits, un par por prefijo de la
  baraja; los demás lenguajes guardan un byte por peso.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1244_dp.cpp](1244_dp.cpp) | G++ 13.2 x64 | dp | O(N·W) | AC | 0.031 s | 9472 KB |
| [1244_dp.go](1244_dp.go) | Go 1.14 x64 | dp | O(N·W) | AC | 0.031 s | 11676 KB |
| [1244_dp.java](1244_dp.java) | Java 1.8 | dp | O(N·W) | AC | 0.109 s | 12768 KB |
| [1244_dp.py](1244_dp.py) | Python 3.12 x64 | dp | O(N·W) | AC | 0.093 s | 2848 KB |
| [1244_dp.rs](1244_dp.rs) | Rust 1.75 x64 | dp | O(N·W) | AC | 0.031 s | 9692 KB |
