# 2135. Menos segmentos con productos dentro de un rango

[Timus 2135](https://acm.timus.ru/problem.aspx?space=1&num=2135) · dificultad 991 · dp, two_pointers

Problema original de Anna Khanova, del concurso «Más vale tarde que nunca».

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Partir una sucesión de n enteros positivos en el menor número de
segmentos consecutivos de modo que el producto de cada segmento esté en
[l, r], o indicar que es imposible. Los límites son 2 segundos y 256 MB.

## Entrada

n, l y r, 1 ≤ n ≤ 50 000, 1 ≤ l ≤ r ≤ 10¹⁸, y luego los números, cada
uno de 1 a 10⁹.

## Salida

El menor número de segmentos, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 8 20
2 4 8 16 1 3 5
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
7 10 20
2 4 8 16 1 3 5
```

Salida:

```
-1
```

## Solución

Sea best(i) el menor número de segmentos que cubren los i primeros
números. El último segmento de una partición de los i primeros empieza
en algún j, y su producto crece al mover j a la izquierda, porque todos
los números son al menos 1. Así que los inicios con producto a lo sumo r
forman un sufijo de posiciones desde U, y los inicios con producto al
menos l forman un prefijo de posiciones antes de L; los inicios
permitidos son el intervalo [U, L).

Ambos extremos solo se mueven a la derecha al crecer i, así que dos
punteros los mantienen, cada uno con el producto de su ventana: cuando
el siguiente número llevaría un producto más allá de su cota, primero se
dividen números por la izquierda, lo que mantiene cada producto dentro
de 64 bits. Un número mayor que r reinicia la ventana superior, y uno al
menos l reinicia la inferior. Los valores best(j) con j en [U, L) entran
y salen de una cola doble monótona, que da su mínimo en O(1), así que
best(i) = 1 + ese mínimo. Todo el recorrido es O(n).

En el primer ejemplo 2 · 4 | 8 | 16 · 1 | 3 · 5 usa cuatro segmentos con
productos 8, 8, 16 y 15.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2135_dp_two_pointers.cpp](2135_dp_two_pointers.cpp) | G++ 13.2 x64 | dp, two_pointers | O(n) | AC | 0.015 s | 836 KB |
| [2135_dp_two_pointers.go](2135_dp_two_pointers.go) | Go 1.14 x64 | dp, two_pointers | O(n) | AC | 0.046 s | 3016 KB |
| [2135_dp_two_pointers.java](2135_dp_two_pointers.java) | Java 1.8 | dp, two_pointers | O(n) | AC | 0.093 s | 1344 KB |
| [2135_dp_two_pointers.py](2135_dp_two_pointers.py) | Python 3.12 x64 | dp, two_pointers | O(n) | AC | 0.156 s | 5472 KB |
| [2135_dp_two_pointers.rs](2135_dp_two_pointers.rs) | Rust 1.75 x64 | dp, two_pointers | O(n) | AC | 0.031 s | 1940 KB |
