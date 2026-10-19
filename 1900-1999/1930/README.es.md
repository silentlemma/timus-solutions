# 1930. Una ruta con el mínimo de cambios de marcha

[Timus 1930](https://acm.timus.ru/problem.aspx?space=1&num=1930) · difficulty 162 · shortest_paths

Original problem from Ural Regional School Programming Contest 2012 | by Grigoriy Nazarov (prepared by Bulat Zaynullin).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada carretera se recorre en ambos sentidos. El registro a,b indica
subida de a hacia b; el sentido opuesto requiere marcha de bajada.
Hallar una ruta entre origen y destino distintos que minimice cambios
entre esas dos marchas. La primera se elige gratis. Existe una ruta.
Límites: 1,5 segundos, 64 MB.

## Entrada

Primero n,m: 2≤n≤10000, 1≤m≤100000. Siguen m líneas con extremos
distintos a,b en 1..n; a→b es subida. No hay bucles ni más de una
carretera por pareja sin orden. La última línea contiene origen y destino,
distintos y conectados. Otras componentes pueden estar desconectadas.
El valor numérico de las ciudades no determina el sentido.

## Salida

Un entero: mínimo número de cambios de marcha.

## Evaluación

Comparación exacta de un token entero.

## Ejemplos

```
3 2
1 2
3 2
1 3
```

```
1
```

```
3 3
1 2
2 3
3 1
1 3
```

```
0
```

## Solución

Crear dos estados por ciudad, ciudad y marcha actual. Un recorrido que
necesita marcha d pasa de (ciudad,g) a (vecina,d), con coste 0 si g=d
y 1 en caso contrario. Ambos estados del origen empiezan en distancia
cero, incorporando la elección inicial gratis. Sirve cualquier marcha final.

Usar BFS 0–1: una mejora de coste cero entra por delante del deque,
una de coste uno por detrás. Fijar un estado al extraerlo por primera
vez y omitir copias posteriores. Devolver al fijar un estado del destino.
La cola procesa distancias pendientes como Dijkstra: transiciones cero
conservan la distancia actual y las unitarias quedan después. Por ello,
la primera distancia fijada de cada estado es óptima.

Cada ruta real corresponde a un camino de estados con el mismo número
de cambios; cada transición de estados corresponde a una carretera
válida, quizá precedida de un cambio. Los dos estados iniciales gratis
representan ambas primeras marchas. Así, la mínima distancia expandida
es exactamente la respuesta, alcanzada por el primer destino fijado.

O(n+m) tiempo y espacio. Hay 2n estados y 4m transiciones posibles;
cada estado fijado recorre una sola vez la adyacencia de su ciudad.
Las copias se omiten y cada mejora se carga a una transición.

Menos carreteras no implica menos cambios. Separar las dos marchas
de cada ciudad: llegadas igualmente baratas en marchas distintas no
son intercambiables. No cobrar la primera marcha ni imponer subida
inicial. Interpretar cada sentido por separado: el segundo ejemplo
contiene un ciclo dirigido. No deducir alturas a partir de identificadores.
Solo se garantiza conexión entre origen y destino, no de todo el grafo.

## Notas por lenguaje

La adyacencia codifica 2·vecina+marchaNecesaria, dos entradas por carretera.
Distancias enteras con signo de 32 bits bastan. 2n sirve de infinito:
un camino simple expandido tiene menos de 2n arcos, cada uno de coste ≤1.
Java usa lectura entera con búfer, arreglos primitivos y deque circular.
Con A=2m entradas, hay como máximo 2+2A inserciones; capacidad 2A+3
deja una celda libre. Go usa dos pilas: invierte la trasera diferida
solo al vaciarse la delantera. Cada entrada diferida se transfiere una
vez, con coste total lineal. C++ y Rust usan deques estándar; Python,
deque y bytearray para estados fijados. Búferes y grafo ocupan O(n+m).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1930_shortest_paths.cpp](1930_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(n+m) | AC | 0.046 s | 1936 KB |
| [1930_shortest_paths.go](1930_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(n+m) | AC | 0.093 s | 6744 KB |
| [1930_shortest_paths.java](1930_shortest_paths.java) | Java 1.8 | shortest_paths | O(n+m) | AC | 0.140 s | 3524 KB |
| [1930_shortest_paths.py](1930_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(n+m) | AC | 0.187 s | 19520 KB |
| [1930_shortest_paths.rs](1930_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(n+m) | AC | 0.015 s | 4468 KB |
