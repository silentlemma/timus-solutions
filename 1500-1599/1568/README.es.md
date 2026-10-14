# 1568. Ordenación de vagones

[Timus 1568](https://acm.timus.ru/problem.aspx?space=1&num=1568) · dificultad 1573 · constructive

Problema original de Sergey Pupyrev, del XII Campeonato de Programación de la Universidad Estatal de los Urales, 6 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tren de N ≤ 10000 vagones numerados 1 … N en algún orden se ordena
con pegados: en una bifurcación cada vagón va a la izquierda o a la
derecha, conservando su orden, y luego la parte izquierda se pega
delante de la derecha. Hay que hallar el menor número de pegados que
deja los vagones en orden 1 … N e imprimir el orden antes y después de
cada uno.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego el orden de los vagones.

## Salida

El número K de pegados y luego K + 1 líneas con los órdenes. Se acepta
cualquier secuencia mínima.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
5 1 3 2 4
```

Salida:

```
2
5 1 3 2 4
1 2 5 3 4
1 2 3 4 5
```

### Ejemplo 2

Entrada:

```
6
6 5 2 4 1 3
```

Salida:

```
3
6 5 2 4 1 3
6 4 1 5 2 3
6 1 2 3 4 5
1 2 3 4 5 6
```

## Solución

Se cortan los números 1 … N en el menor número de tramos v, v + 1, …, w
que ya están de izquierda a derecha en el tren; empieza un tramo nuevo
dondequiera que el vagón v + 1 esté antes que el vagón v. Los tramos se
numeran 0 … r − 1.

Un pegado es la inversa de una mezcla americana (riffle), y un orden
sale del ordenado con k de esas mezclas exactamente cuando tiene como
mucho 2^k tramos así (secuencias crecientes): un hecho conocido sobre
barajar cartas. Así que el menor número de pegados es K = ⌈log₂ r⌉, lo
que confirmó una búsqueda sobre todos los pegados para cada orden de
hasta 6 vagones.

Los pegados en sí son una ordenación por dígitos de los números de
tramo: el pegado b manda a la derecha los vagones cuyo número de tramo
tiene el bit b a 1. Tras los pegados de los bits 0 … b, los vagones
quedan ordenados por los b + 1 bits bajos de sus números de tramo y
conservan su orden previo en los empates, así que tras los K los tramos
quedan en orden y cada tramo ya está ordenado por dentro.
`O(N log N)`.

Detalles a tener en cuenta:

- hay varias respuestas mínimas, y la respuesta de aquí al primer
  ejemplo difiere de la del enunciado (un verificador comprueba los
  movimientos);
- un tren ya ordenado no necesita pegados y se imprime una sola vez
  (pruebas 03, 04);
- 2^13 tramos necesitan 13 pegados y un tramo más necesita 14 (pruebas
  gen3, gen4).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1568_constructive.cpp](1568_constructive.cpp) | G++ 13.2 x64 | constructive | O(N log N) | AC | 0.046 s | 208 KB |
| [1568_constructive.go](1568_constructive.go) | Go 1.14 x64 | constructive | O(N log N) | AC | 0.031 s | 3168 KB |
| [1568_constructive.java](1568_constructive.java) | Java 1.8 | constructive | O(N log N) | AC | 0.093 s | 5580 KB |
| [1568_constructive.py](1568_constructive.py) | Python 3.12 x64 | constructive | O(N log N) | AC | 0.125 s | 6612 KB |
| [1568_constructive.rs](1568_constructive.rs) | Rust 1.75 x64 | constructive | O(N log N) | AC | 0.046 s | 2124 KB |
