# 1424. Microbús

[Timus 1424](https://acm.timus.ru/problem.aspx?space=1&num=1424) · dificultad 708 · greedy

Problema original de Dmitry Kovalioff, Ilya Grebnov y Nikita Rybak (idea de Sergey Sofronov), de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un microbús de M plazas (M ≤ 1000) hace un viaje de la parada 1 a la N
(N ≤ 100 000). K personas (K ≤ 50 000) quieren viajar, la persona i de
la parada S[i] a la F[i], y cada una paga P sea cual sea la distancia.
El conductor puede rechazar a cualquiera. Hay que imprimir el mayor
beneficio y los números de las personas a llevar, en cualquier orden;
vale cualquier conjunto óptimo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, M, K y P, luego K líneas S F.

## Salida

El beneficio y luego las personas a llevar.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 2 6 9
1 4
2 6
1 5
2 3
4 6
3 6
```

Salida:

```
36
1 5 6 4
```

## Solución

Todos pagan lo mismo, así que hay que llevar a tantas personas como sea
posible con como mucho M a bordo a la vez; una plaza que queda libre en
una parada puede ocuparse en esa misma parada. Se recorren las paradas
en orden. En cada parada bajan aquellos cuyo viaje termina allí, suben
todos los que esperan, y mientras haya más de M a bordo se rechaza al
que va más lejos, como si nunca se le hubiera llevado.

Rechazar al que va más lejos es seguro: entre los que van a bordo tras
una parada, cualquier plan óptimo debe dejar fuera al menos tantos como
el exceso, y cambiar un viaje corto rechazado por el largo que se
conservó nunca llena más una parada posterior, porque el viaje corto
termina antes. Un montículo de máximos por parada final encuentra al
que va más lejos, y unos contadores de viajeros por parada final
mantienen el número a bordo. `O(N + K log K)`.

Detalles a tener en cuenta:

- los viajes son semiabiertos: quien baja en una parada libera la plaza
  para quien sube allí (prueba 05);
- sin ninguna persona la respuesta es 0 y una lista vacía (prueba 02);
- varias personas pueden querer exactamente el mismo viaje (pruebas 04,
  gen3).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1424_greedy.cpp](1424_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + K log K) | AC | 0.093 s | 4752 KB |
| [1424_greedy.go](1424_greedy.go) | Go 1.14 x64 | greedy | O(N + K log K) | AC | 0.109 s | 12376 KB |
| [1424_greedy.java](1424_greedy.java) | Java 1.8 | greedy | O(N + K log K) | AC | 0.187 s | 13932 KB |
| [1424_greedy.py](1424_greedy.py) | Python 3.12 x64 | greedy | O(N + K log K) | AC | 0.218 s | 30352 KB |
| [1424_greedy.rs](1424_greedy.rs) | Rust 1.75 x64 | greedy | O(N + K log K) | AC | 0.031 s | 10376 KB |
