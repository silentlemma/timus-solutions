# 1424. Microbús

[Timus 1424](https://acm.timus.ru/problem.aspx?space=1&num=1424) · dificultad 697 · greedy

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
el exceso, y cambiar un viaje largo conservado por el corto que se
rechazó nunca llena más una parada posterior, porque el viaje corto
termina antes. Un montículo de máximos por parada final encuentra al
que va más lejos, y unos contadores de viajeros por parada final
mantienen el número a bordo. `O(N + K log K)`.

Detalles a tener en cuenta:

- los viajes son semiabiertos: quien baja en una parada libera la plaza
  para quien sube allí (prueba 05);
- sin ninguna persona la respuesta es 0 y una lista vacía (prueba 02);
- varias personas pueden querer exactamente el mismo viaje (pruebas 04,
  gen3).

## Soluciones optimizadas

`1424_sorting_greedy_optimized.cpp`. Conserva la asignación voraz por destino creciente. Guarda el último destino de cada asiento en un arreglo ordenado. upper_bound encuentra el asiento disponible que se liberó más tarde; al aceptar el viaje, memmove quita esa entrada y añade su destino al final, pues los destinos se procesan en orden. Se conserva 1424_sorting_greedy.cpp con árbol y sus propias métricas Accepted. Con M≤1000, los desplazamientos contiguos resultaron más rápidos y pequeños pese a O(M) por viaje aceptado. Peor tiempo O(N+M+KM), espacio O(N+M+K) más búferes fijos; el árbol mantiene O(N+M+K log M).

Accepted del fuente exacto #11326980: 0.015 s / 920 KB. Comparación G++ 13.2 guardada el 2026-11-20: tiempo 1/43, memoria 3/43.

Se procesan los viajes por destino creciente. Se asigna el asiento que se liberó más tarde entre los que ya están libres al subir el pasajero.

Los viajes se agrupan por parada de origen en arreglos compactos. Cada clave del montículo contiene el destino y el número del pasajero para poder descartar el viaje más lejano.

**Envíos de las versiones optimizadas en Timus**

`1424_sorting_greedy_optimized.cpp` (G++ 13.2 x64) №11326980 · `1424_sorting_greedy.cpp` (G++ 13.2 x64) №11317526 · `1424_greedy_optimized.go` (Go 1.14 x64) №11317540 · `1424_greedy_optimized.java` (Java 1.8) №11317543 · `1424_greedy_optimized.py` (Python 3.12 x64) №11317528 · `1424_greedy_optimized.rs` (Rust 1.75 x64) №11317532.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322134 · Go 1.14 x64 №11322135 · Java 1.8 №11322136 · Python 3.12 x64 №11322137 · Rust 1.75 x64 №11322139.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1424_greedy.cpp](1424_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + K log K) | AC | 0.078 s | 4772 KB | 11322134 |
| [1424_greedy.go](1424_greedy.go) | Go 1.14 x64 | greedy | O(N + K log K) | AC | 0.109 s | 12396 KB | 11322135 |
| [1424_greedy.java](1424_greedy.java) | Java 1.8 | greedy | O(N + K log K) | AC | 0.218 s | 13936 KB | 11322136 |
| [1424_greedy.py](1424_greedy.py) | Python 3.12 x64 | greedy | O(N + K log K) | AC | 0.203 s | 30052 KB | 11322137 |
| [1424_greedy.rs](1424_greedy.rs) | Rust 1.75 x64 | greedy | O(N + K log K) | AC | 0.046 s | 10368 KB | 11322139 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1424_sorting_greedy_optimized.cpp](1424_sorting_greedy_optimized.cpp) | G++ 13.2 x64 | sorting, greedy | O(N+M+KM) time; O(N+M+K) space | AC | 0.015 s | 920 KB | 11326980 |
| [1424_sorting_greedy.cpp](1424_sorting_greedy.cpp) \* | G++ 13.2 x64 | sorting, greedy | O(N + M + K log M) | AC | 0.078 s | 1032 KB | 11317526 |
| [1424_greedy_optimized.py](1424_greedy_optimized.py) | Python 3.12 x64 | greedy | O(N + K log K) | AC | 0.203 s | 3804 KB | 11317528 |
| [1424_greedy_optimized.rs](1424_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(N + K log K) | AC | 0.046 s | 1752 KB | 11317532 |
| [1424_greedy_optimized.go](1424_greedy_optimized.go) | Go 1.14 x64 | greedy | O(N + K log K) | AC | 0.031 s | 3916 KB | 11317540 |
| [1424_greedy_optimized.java](1424_greedy_optimized.java) | Java 1.8 | greedy | O(N + K log K) | AC | 0.14 s | 4604 KB | 11317543 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
