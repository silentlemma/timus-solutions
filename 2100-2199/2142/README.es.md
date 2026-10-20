# 2142. Pagar maná rojo, azul y de cualquier color con tierras dobles

[Timus 2142](https://acm.timus.ru/problem.aspx?space=1&num=2142) · dificultad 125 · greedy

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay A tierras rojas, B azules y C dobles; cada una da un maná, y una
doble da rojo o azul a elegir. Un hechizo necesita X maná rojo, Y azul y
Z más de cualquier color. Decidir si las tierras bastan. Los límites son
1 segundo y 256 MB.

## Entrada

A, B, C, y luego X, Y, Z, todos entre 0 y 10⁹.

## Salida

"It is a kind of magic" si el hechizo se puede pagar, y si no "There are
no miracles in life".

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3 1
2 2 1
```

Salida:

```
It is a kind of magic
```

### Ejemplo 2

Entrada:

```
5 6 5
6 5 6
```

Salida:

```
There are no miracles in life
```

## Solución

Las tierras rojas deben pagar primero el maná rojo y las azules el azul,
porque la parte de cualquier color la puede pagar cualquier tierra. Lo
que dejan sin pagar, max(0, X − A) + max(0, Y − B), tiene que salir de
las tierras dobles. Después cada tierra restante de cualquier clase puede
pagar el maná Z de cualquier color, así que la segunda condición es
A + B + C ≥ X + Y + Z. Las dos juntas son necesarias y suficientes. Las
sumas llegan a 3 · 10⁹, más allá de los enteros de 32 bits.

En el segundo ejemplo el rojo necesita 6 − 5 = 1 tierra doble, pero en
total hay 16 tierras para 17 de maná.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2142_greedy.cpp](2142_greedy.cpp) | G++ 13.2 x64 | greedy | O(1) | AC | 0.015 s | 124 KB |
| [2142_greedy.go](2142_greedy.go) | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 1088 KB |
| [2142_greedy.java](2142_greedy.java) | Java 1.8 | greedy | O(1) | AC | 0.109 s | 1620 KB |
| [2142_greedy.py](2142_greedy.py) | Python 3.12 x64 | greedy | O(1) | AC | 0.078 s | 416 KB |
| [2142_greedy.rs](2142_greedy.rs) | Rust 1.75 x64 | greedy | O(1) | AC | 0.031 s | 228 KB |
