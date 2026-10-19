# 2080. Las tarjetas en orden de su próximo uso

[Timus 2080](https://acm.timus.ru/problem.aspx?space=1&num=2080) · dificultad 746 · fenwick

Problema original de Eugene Kurpilyansky, preparado por Mikhail Vyatskov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n tarjetas forman una pila y se usarán k veces en un orden conocido:
cada vez la tarjeta a usar debe estar arriba, y tras usarla se puede
devolver a cualquier profundidad. Dar el orden inicial de la pila y, para
cada uso, cuántas tarjetas quedan encima de la tarjeta al devolverla. Se
acepta cualquier respuesta válida. Los límites son 2 segundos y 256 MB.

## Entrada

n y k, 1 ≤ n, k ≤ 10⁵, y después los k números de tarjeta en el orden
de uso.

## Salida

La pila inicial de arriba abajo y después k líneas con el número de
tarjetas encima de cada tarjeta usada tras devolverla.

## Evaluación

Un comprobador reproduce los usos: cada tarjeta debe estar arriba cuando
se necesita, y cada profundidad de devolución debe ser a lo sumo n − 1.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5
3 1 2 2 1
```

Salida:

```
3 1 2
2
1
0
1
0
```

## Solución

Se mantiene la pila ordenada por el momento del próximo uso, con las
tarjetas que no se vuelven a usar al fondo. Así la de arriba siempre es
la siguiente que se usa. Al principio es el orden de primer uso, seguido
de las tarjetas sin usar. Tras el uso en el momento i, el próximo uso de
la tarjeta es en el momento j (o nunca), y debe quedar justo debajo de
las tarjetas cuyo próximo uso llega antes de j. Cada una de ellas se usa
en algún momento entre i y j, y cada tarjeta usada ahí tiene su próximo
uso antes de j, así que su número es la cantidad de tarjetas distintas
entre los usos i + 1 … j − 1 (o hasta k si la tarjeta no se vuelve a
usar).

Los valores distintos en tramos se cuentan fuera de línea con un árbol
de Fenwick sobre los momentos. Un momento t > i es el primer uso de su
tarjeta después de i exactamente cuando el uso anterior de esa tarjeta
es a lo sumo i. Así que las consultas van en i creciente, y el momento t
se añade al árbol en cuanto i llega al uso anterior de su tarjeta (los
momentos que son primeros usos en absoluto se añaden al principio). La
respuesta para i es el número de momentos añadidos en (i, j). El recorrido
de Fenwick cuesta O((n + k) log k); las cotas de abajo incluyen el orden inicial.

En el ejemplo la tarjeta 1 se usa en los momentos 2 y 5, y entre ellos
solo se usa la tarjeta 2, así que tras el momento 2 vuelve bajo una
tarjeta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2080_fenwick.cpp](2080_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n log n + k log k) | AC | 0.125 s | 2312 KB |
| [2080_fenwick.go](2080_fenwick.go) | Go 1.14 x64 | fenwick | O(n log² n + k log k) | AC | 0.078 s | 5636 KB |
| [2080_fenwick.java](2080_fenwick.java) | Java 1.8 | fenwick | O((n + k) log k) | AC | 0.156 s | 8412 KB |
| [2080_fenwick.py](2080_fenwick.py) | Python 3.12 x64 | fenwick | O((n + k) log k) | AC | 0.718 s | 30084 KB |
| [2080_fenwick.rs](2080_fenwick.rs) | Rust 1.75 x64 | fenwick | O((n + k) log k) | AC | 0.046 s | 9992 KB |
