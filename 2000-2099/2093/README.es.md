# 2093. La ruta más rápida por carreteras que la nieve frena

[Timus 2093](https://acm.timus.ru/problem.aspx?space=1&num=2093) · dificultad 1369 · dijkstra

Problema original de Denis Dublennykh, del Concurso Individual Abierto de la UrFU 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n cruces están unidos por m carreteras con tiempos normales tᵢ. La nieve
cae desde el momento 0; una carretera en la que se entra T minutos
después de su última limpieza (o del comienzo) se recorre en
min(⌈(1 + T/100) tᵢ⌉, 100500 tᵢ). Cada carretera tiene un horario de
limpiezas, durante las cuales está cerrada, y un recorrido debe
terminar antes de que empiece la limpieza siguiente. Se puede esperar en
los cruces. Hallar la llegada más temprana al cruce n saliendo del
cruce 1 en el momento 0. Los límites son 2 segundos y 64 MB.

## Entrada

n y m (hasta 10⁵), las m carreteras aᵢ bᵢ tᵢ (tᵢ ≤ 10⁶) y después
k ≤ 10⁵ limpiezas pᵢ sᵢ fᵢ (carretera e intervalo de cierre, tiempos
hasta 10⁹; las limpiezas de una carretera no se solapan).

## Salida

El momento de llegada más temprano.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
1 2 10
2 3 10
3 4 10
1
2 10 15
```

Salida:

```
38
```

## Solución

Se fija una carretera y el momento en que se llega a su extremo. Entre
dos limpiezas, salir más tarde solo significa más nieve, así que en
cada hueco abierto la mejor salida es la más temprana. Un hueco
posterior empieza tras una limpieza que comenzó cuando la salida
anterior ya podría haber terminado, así que el primer hueco cuya salida
más temprana aún termina antes de la limpieza siguiente da la llegada
más temprana; tras la última limpieza la carretera siempre se puede
usar. Esta función de llegada nunca decrece al llegar más tarde, así que
funciona el algoritmo de Dijkstra sobre los tiempos de llegada: al
extraer un cruce, cada carretera se relaja recorriendo sus limpiezas
ordenadas. Cada carretera se relaja a lo sumo dos veces, así que el
recorrido cuesta O(m + k) y las operaciones de la cola de prioridad
cuestan O((n + m) log n). Ordenar los horarios de limpieza cuesta
O(k log k), por lo que el total es O((n + m) log n + k log k).
Los tiempos se calculan en enteros con el tope de 100500 tᵢ.

Un error frecuente es omitir la ordenación: la prueba gen7 (generador
`5 7`) solo tiene dos cruces y una carretera, pero 100000 limpiezas
desordenadas, cuyo coste de ordenación no cabe en O(k log n).

En el ejemplo la primera carretera cuesta 10 minutos; la segunda se
limpia de 10 a 15, así que se entra en 15 y se sale en 25; la tercera
lleva 25 minutos de nieve y cuesta ⌈1.25 · 10⌉ = 13 minutos, con
llegada en 38.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2093_dijkstra.cpp](2093_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O((n + m) log n + k log k) | AC | 0.156 s | 7948 KB |
| [2093_dijkstra.go](2093_dijkstra.go) | Go 1.14 x64 | dijkstra | O((n + m) log n + k log k) | AC | 0.062 s | 13480 KB |
| [2093_dijkstra.java](2093_dijkstra.java) | Java 1.8 | dijkstra | O((n + m) log n + k log k) | AC | 0.187 s | 10832 KB |
| [2093_dijkstra.py](2093_dijkstra.py) | Python 3.12 x64 | dijkstra | O((n + m) log n + k log k) | AC | 1.015 s | 21440 KB |
| [2093_dijkstra.rs](2093_dijkstra.rs) | Rust 1.75 x64 | dijkstra | O((n + m) log n + k log k) | AC | 0.031 s | 15516 KB |
