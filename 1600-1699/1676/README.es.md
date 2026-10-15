# 1676. Mortal Kombat

[Timus 1676](https://acm.timus.ru/problem.aspx?space=1&num=1676) · dificultad 1707 · matching

Problema original de Magaz Asanov (preparado por Alexander Ipatov), del Ural SU Contest en el campus de verano de Petrozavodsk, agosto de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de N monstruos debe luchar con un luchador distinto de los M de
la Tierra, y los luchadores deben ganar todas las peleas; una matriz de
ceros y unos dice qué luchador vence a qué monstruo. Para cada par
(monstruo i, luchador j) hay que imprimir 1 si elegir ese par como
primera pelea hace imposible una asignación ganadora completa, y 0 si no.

## Entrada

N y M (1 ≤ N ≤ 300, N ≤ M ≤ 1500) y luego N filas de M dígitos.

## Salida

La matriz N × M de respuestas.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
1111
1000
1111
1111
```

Salida:

```
1000
0111
1000
1000
```

### Ejemplo 2

Entrada:

```
4 5
10000
10000
10000
10000
```

Salida:

```
11111
11111
11111
11111
```

## Solución

Un par sirve exactamente cuando pertenece a algún emparejamiento de todos
los monstruos con luchadores que los vencen. El algoritmo de Kuhn halla
uno; si falla para algún monstruo, todos los pares son imposibles.

Si no, el monstruo i conserva su luchador m(i), y puede tomar un
luchador j que lo vence de dos formas más:

- j está libre, e i simplemente cambia;
- j pertenece al monstruo k, que toma otro luchador que lo vence: el que
  i deja (cerrando un ciclo), uno libre o el de un tercer monstruo, que
  entonces debe moverse del mismo modo.

Con una flecha k → k₂ cuando k puede tomar el luchador de k₂, esto
significa: k alcanza a i, o k alcanza un monstruo al que vence algún
luchador libre (incluido el propio k). La alcanzabilidad entre los N
monstruos sale de una búsqueda desde cada uno (cierre transitivo con
conjuntos de bits en Python), así que el total es `O(N² · M)`.

Detalles a tener en cuenta:

- un luchador que no vence a nadie da una columna de unos (prueba 05); un
  monstruo al que nadie vence hace que toda la respuesta sea unos (prueba 04);
- sin asignación completa la respuesta es toda unos, incluso en pares
  donde el luchador gana (ejemplo 2);
- las filas son dígitos sin espacios.

Las respuestas coinciden con una búsqueda de todas las asignaciones
completas en 600 entradas pequeñas aleatorias y con una implementación
aceptada independiente en las grandes.

## Notas por lenguaje

- Python guarda cada fila como un entero grande y hace la búsqueda de
  Kuhn con los luchadores no visitados como conjunto de bits, así que el
  siguiente candidato sale directamente de adj[u] & unseen.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1676_matching.cpp](1676_matching.cpp) | G++ 13.2 x64 | matching | O(N^2 M) | AC | 0.078 s | 2528 KB |
| [1676_matching.go](1676_matching.go) | Go 1.14 x64 | matching | O(N^2 M) | AC | 0.078 s | 7576 KB |
| [1676_matching.java](1676_matching.java) | Java 1.8 | matching | O(N^2 M) | AC | 0.406 s | 10656 KB |
| [1676_matching.py](1676_matching.py) | Python 3.12 x64 | matching | O(N^2 M) | AC | 0.296 s | 3976 KB |
| [1676_matching.rs](1676_matching.rs) | Rust 1.75 x64 | matching | O(N^2 M) | AC | 0.046 s | 4120 KB |
