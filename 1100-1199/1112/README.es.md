# 1112. Conservar el mayor número de segmentos sin puntos interiores comunes

[Timus 1112](https://acm.timus.ru/problem.aspx?space=1&num=1112) · dificultad 165 · greedy

Problema original de la Olimpiada Nacional Búlgara de Informática, segundo día.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` segmentos en una recta (`1 ≤ N ≤ 99`), el segmento `i` va de
`A_i` a `B_i` con enteros `−999 ≤ A_i < B_i ≤ 999`. Quita los menos
segmentos posibles para que ningún par de los que quedan comparta un punto
interior; los extremos pueden tocarse. Imprime los segmentos que quedan.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas `A_i B_i`.

## Salida

El número `P` de segmentos conservados y luego `P` líneas `A B` en orden
creciente de los extremos izquierdos. Se acepta cualquier respuesta
óptima.

## Evaluación

Se acepta cualquier respuesta óptima. El comprobador calcula el mayor
número posible de segmentos con una programación dinámica cuadrática y
verifica que la salida conserva esa cantidad, los toma de la entrada, los
lista por su extremo izquierdo y no tiene dos que se solapen.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
3 6
1 3
2 5
```

Salida:

```
2
1 3
3 6
```

## Solución

Es el problema de selección de actividades. Se ordenan los segmentos por
su extremo derecho y se toma cada uno que empiece no antes del extremo
derecho del último tomado. El segmento que termina primero siempre forma
parte de alguna respuesta óptima: en cualquier conjunto óptimo, el
segmento con el extremo derecho más a la izquierda puede cambiarse por él
sin crear un solape. Repetir el argumento con el resto demuestra la
elección voraz. Los segmentos conservados son disjuntos, así que su orden
por extremo derecho es también su orden por extremo izquierdo.
`O(N log N)`.

Detalles a tener en cuenta:

- los segmentos que se tocan (uno termina donde empieza el siguiente) no
  comparten puntos interiores y pueden quedarse ambos;
- ordenar por extremo izquierdo o por longitud y elegir de forma voraz da
  respuestas erróneas: un segmento largo que empieza primero puede tapar
  varios cortos;
- los segmentos pueden repetirse; cada copia es un segmento aparte, pero
  como mucho una puede quedarse.

Las respuestas se comprobaron con el comprobador en todas las pruebas y en
150 conjuntos aleatorios, con cadenas de segmentos que se tocan,
segmentos repetidos y anidados.

## Notas por lenguaje

- Todos los lenguajes hacen la misma ordenación y un recorrido.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1112_greedy.cpp](1112_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 192 KB |
| [1112_greedy.go](1112_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.015 s | 1156 KB |
| [1112_greedy.java](1112_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.156 s | 3944 KB |
| [1112_greedy.py](1112_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 460 KB |
| [1112_greedy.rs](1112_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 232 KB |
