# 2107. Completar una regla de saltos que se repite a los k segundos

[Timus 2107](https://acm.timus.ru/problem.aspx?space=1&num=2107) · dificultad 1488 · dp, graphs

Problema original de Alexey Danilyuk, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay bailarines en las plataformas 1 … n, y cada segundo el bailarín de la
plataforma i salta a la plataforma f(i). Algunos valores de f están
fijados y los demás (dados como 0) se pueden elegir libremente. Elegirlos
para que tras k segundos cada bailarín vuelva a su plataforma inicial, o
informar de que es imposible. Se acepta cualquier compleción válida. Los
límites son 2 segundos y 150 MB.

## Entrada

n y k, 1 ≤ n ≤ 35, 1 ≤ k ≤ 10⁹, y después f(1) … f(n), 0 ≤ f(i) ≤ n.

## Salida

"No", o "Yes" y la f completada.

## Evaluación

Un comprobador verifica que la f impresa conserva los valores fijados y
devuelve a todos a su sitio tras k segundos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4
1 2 3
```

Salida:

```
Yes
1 2 3
```

### Ejemplo 2

Entrada:

```
3 4
0 0 0
```

Salida:

```
Yes
1 2 3
```

### Ejemplo 3

Entrada:

```
3 1
2 2 2
```

Salida:

```
No
```

### Ejemplo 4

Entrada:

```
2 666
2 0
```

Salida:

```
Yes
2 1
```

### Ejemplo 5

Entrada:

```
2 777
2 0
```

Salida:

```
No
```

## Solución

Todos vuelven tras k segundos exactamente cuando f es una permutación
cuyos ciclos tienen longitudes que dividen a k. Por eso dos valores
fijados con el mismo destino dan "No", y un ciclo ya cerrado por los
valores fijados debe tener una longitud que divida a k.

Las demás aristas fijadas forman caminos disjuntos; una plataforma con
valor abierto y sin arista entrante es un camino de un vértice. Completar
f es unir los caminos en ciclos: el final de cada camino apunta al
principio del siguiente de su grupo. Así que hay que repartir los caminos
en grupos cuyo número total de vértices divida a k.

Solo importan las longitudes de los caminos, así que un estado es cuántos
caminos de cada longitud quedan sin usar, codificado en base mixta. El
producto de (cantidad + 1) sobre las longitudes con suma como mucho 35
queda por debajo de mil estados. Un grupo es cualquier subestado no vacío
cuya suma divide a k. Para no contar el mismo reparto en distintos
órdenes, el grupo de un estado debe contener un camino de la mayor
longitud presente en él; un estado es resoluble si tal grupo deja un resto
resoluble. Después se reproducen las elecciones guardadas para construir
los ciclos con los caminos reales.

En el cuarto ejemplo 1 → 2 es un camino de dos vértices y 666 es par, así
que el ciclo 1 → 2 → 1 sirve; para 777 no.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2107_dp_graphs.cpp](2107_dp_graphs.cpp) | G++ 13.2 x64 | dp, graphs | O(S^2 n) with S < 10^3 states | AC | 0.015 s | 464 KB |
| [2107_dp_graphs.go](2107_dp_graphs.go) | Go 1.14 x64 | dp, graphs | O(S^2 n) with S < 10^3 states | AC | 0.031 s | 1144 KB |
| [2107_dp_graphs.java](2107_dp_graphs.java) | Java 1.8 | dp, graphs | O(S^2 n) with S < 10^3 states | AC | 0.125 s | 576 KB |
| [2107_dp_graphs.py](2107_dp_graphs.py) | Python 3.12 x64 | dp, graphs | O(S^2 n) with S < 10^3 states | AC | 0.093 s | 936 KB |
| [2107_dp_graphs.rs](2107_dp_graphs.rs) | Rust 1.75 x64 | dp, graphs | O(S^2 n) with S < 10^3 states | AC | 0.031 s | 268 KB |
