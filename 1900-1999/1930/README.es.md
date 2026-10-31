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

## Soluciones optimizadas

La solución optimizada en C++ analiza a mano hasta 200 004 números desde
un búfer de 4 KB que se rellena con `fread` e imprime con `printf` en
lugar de usar `iostream`; el grafo y el BFS 0–1 son los mismos:
{1930_shortest_paths_optimized.cpp}.

La solución optimizada en Go analiza los números a mano desde un búfer
de 4 KB leído de la entrada estándar en lugar de llamar a `fmt.Fscan`
para cada uno de hasta 200 004 números; el grafo y el BFS 0–1 son los
mismos: {1930_shortest_paths_optimized.go}.

La solución optimizada en Java analiza los números a mano desde un
`BufferedInputStream` en lugar de `StreamTokenizer` y guarda la deque
como un búfer circular en un arreglo de `int` en lugar de un
`ArrayDeque` de `Integer` envueltos. Con `A = 2m` entradas de adyacencia
entran como mucho `2 + 2A` estados, así que una capacidad de `2A + 3`
nunca se llena y deja una celda libre:
{1930_shortest_paths_optimized.java}.

La solución optimizada en Python lee la entrada en trozos de 4 KB en
lugar de partirla toda de golpe y guarda cada lista de adyacencia en un
`array("H")` de números sin signo de 16 bits en lugar de una lista de
objetos enteros: un destino 2·ciudad+marcha no pasa de 19 999, ya que
n ≤ 10000: {1930_shortest_paths_optimized.py}.

La solución optimizada en Rust guarda las listas de adyacencia como
`Vec<u16>` en lugar de `Vec<usize>`, 2 bytes en lugar de 8 por entrada:
un destino 2·ciudad+marcha no pasa de 19 999, ya que n ≤ 10000. Los
números se analizan a mano desde un búfer de 4 KB en lugar de leer toda
la entrada en un `String`: {1930_shortest_paths_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1930_shortest_paths_optimized.cpp`: reducción de tiempo +67.39%;
  reducción de memoria +12.81%; base: `1930_shortest_paths.cpp`.

- `1930_shortest_paths_optimized.go`: reducción de tiempo +66.67%;
  reducción de memoria +20.11%; base: `1930_shortest_paths.go`.

- `1930_shortest_paths_optimized.java`: reducción de tiempo +37.60%;
  reducción de memoria -36.59%; base: `1930_shortest_paths.java`.

- `1930_shortest_paths_optimized.py`: reducción de tiempo +0.00%;
  reducción de memoria +87.93%; base: `1930_shortest_paths.py`.

- `1930_shortest_paths_optimized.rs`: reducción de tiempo +0.00%;
  reducción de memoria +69.02%; base: `1930_shortest_paths.rs`.

## Notas por lenguaje

La adyacencia codifica 2·vecina+marchaNecesaria, dos entradas por
carretera. Distancias enteras con signo de 32 bits bastan. 2n sirve de
infinito: un camino simple expandido tiene menos de 2n arcos, cada uno
de coste ≤1. Java lee con `StreamTokenizer`, guarda un arreglo de `int`
de destinos por ciudad y usa `ArrayDeque`. Go usa dos pilas: invierte la
trasera diferida solo al vaciarse la delantera. Cada entrada diferida se
transfiere una vez, con coste total lineal. C++ y Rust usan deques
estándar; Python, deque y bytearray para estados fijados. Búferes y
grafo ocupan O(n+m).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1930_shortest_paths.cpp](1930_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(n+m) | AC | 0.046 s | 1936 KB | 11291679 |
| [1930_shortest_paths.go](1930_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(n+m) | AC | 0.093 s | 6744 KB | 11291681 |
| [1930_shortest_paths.java](1930_shortest_paths.java) | Java 1.8 | shortest_paths | O(n+m) | AC | 0.125 s | 2536 KB | 11307200 |
| [1930_shortest_paths.py](1930_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(n+m) | AC | 0.187 s | 19520 KB | 11291686 |
| [1930_shortest_paths.rs](1930_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(n+m) | AC | 0.015 s | 4468 KB | 11291694 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1930_shortest_paths_optimized.cpp](1930_shortest_paths_optimized.cpp) | G++ 13.2 x64 | shortest_paths | O(n+m) | AC | 0.015 s | 1688 KB | 11307202 |
| [1930_shortest_paths_optimized.go](1930_shortest_paths_optimized.go) | Go 1.14 x64 | shortest_paths | O(n+m) | AC | 0.031 s | 5388 KB | 11307203 |
| [1930_shortest_paths_optimized.java](1930_shortest_paths_optimized.java) | Java 1.8 | shortest_paths | O(n+m) | AC | 0.078 s | 3464 KB | 11307206 |
| [1930_shortest_paths_optimized.py](1930_shortest_paths_optimized.py) | Python 3.12 x64 | shortest_paths | O(n+m) | AC | 0.187 s | 2356 KB | 11307205 |
| [1930_shortest_paths_optimized.rs](1930_shortest_paths_optimized.rs) | Rust 1.75 x64 | shortest_paths | O(n+m) | AC | 0.015 s | 1384 KB | 11307204 |
