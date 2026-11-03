# 1109. El menor número de aristas que tocan todos los vértices de un grafo bipartito

[Timus 1109](https://acm.timus.ru/problem.aspx?space=1&num=1109) · dificultad 249 · matching

Problema original de la Olimpiada Nacional Búlgara de Informática, primer día.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo bipartito tiene `M` vértices a la izquierda y `N` a la derecha
(`M, N ≤ 1000`) y `K` aristas, cada una entre un vértice izquierdo y uno
derecho; todo vértice tiene al menos una arista. Halla el menor número de
aristas tal que todo vértice sea extremo de al menos una arista elegida.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`M N K` y luego `K` líneas `a b`: una arista entre el vértice izquierdo
`a` y el vértice derecho `b`. Las aristas pueden repetirse.

## Salida

El menor número de aristas.

## Evaluación

Se compara un entero. El candidato Python real coincidió con una
enumeración independiente de matchings por subconjuntos en los 46312 grafos
sin aislados con ambas partes hasta cuatro. En 327 grafos hasta 3×3 también
se enumeraron coberturas por aristas directamente, sin asumir la fórmula.
Los seis programas reales pasaron cada uno 82 formas extra y 12 entradas
del repositorio en Docker, con su propio Accepted de fuente exacta.

Incluyen cadena alternante de hasta 1000 vértices por lado, millón de aristas
distintas, bloques deficientes de Hall, duplicados y límites 63/64/65 bits.
Python también comprobó 16 cortes de entero/pareja entre bloques y último
token sin separador. Las 46312 ejecuciones son Python, no cada fuente nativa.
Cuatro pruebas CPython alcanzaron localmente 0,194 segundos CPU y 17240 KB
RSS, dentro de 0,5 s/64 MB; RSS local no es memoria reportada por el juez.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2 4
1 1
2 1
3 1
3 2
```

Salida:

```
3
```

## Solución

Los delegados son vértices bipartitos y las llamadas permitidas,
aristas. No hay vértices aislados. Un matching máximo de tamaño `q` cubre
`2q` vértices; añade una arista incidente por cada restante. Dos vértices
libres no pueden ser adyacentes, pues aumentarían el matching. Se construye
así una cobertura por aristas de tamaño `M+N−q`.

Para la cota inferior, una cobertura con `c` componentes tiene al menos
`M+N−c` aristas. Una arista de cada componente forma un matching de tamaño
`c`, así que `c≤q`. Toda cobertura tiene al menos `M+N−q`: es el óptimo.
La garantía de no tener aislados es esencial.

La base didáctica C++ usa DFS de Kuhn. Inicia cualquier matching voraz y
busca una ruta aumentante desde cada vértice izquierdo inicialmente libre,
marcando derechos por número de búsqueda. El matching inicial es máximo
en el subconjunto de izquierdos que cubre. Añadir un izquierdo libre sube
el óptimo a lo sumo uno, y una nueva ruta debe empezar en él. Si aparece,
se invierte y aumenta uno; si no, el óptimo queda igual. La inducción prueba
la solución final. Esta versión corta está comprobada en C++, sin afirmar
que puertos no probados pasen. Tiempo `O(M(V+K))`, espacio `O(V+K)`, `V=M+N`.

Las cinco fuentes anteriores con capas BFS/DFS se conservan. La ausencia
de ruta aumentante prueba máximo por diferencia simétrica. No toda ruta
elegida es la más corta: filas `[1,2,3]`, `[2,3]`, `[1]` permiten que Python
elija cinco aristas aunque exista una de tres. Para esas implementaciones
se usa la cota segura `O(L(V+K))`, con cursores de aristas y hasta
`L=min(M,N)` fases exitosas, sin asumir la cota estricta de Hopcroft–Karp
basada en rutas mínimas. Espacio `O(V+K)`.

## Soluciones optimizadas

El nuevo algoritmo guarda una máscara de vecinos por izquierdo,
orientando la parte menor como `L=min(M,N)`, y `R=max(M,N)` la otra.
Por cada nueva raíz izquierda, BFS busca una ruta alternante. Primero
interseca vecinos con los derechos libres; un acierto termina. Si no,
todos están emparejados: visita cada derecho no visto una vez, guarda
su padre izquierdo y encola su único compañero izquierdo. Caben hasta `L`
entradas. Invierte padres y matching anterior hasta la raíz libre. Sin
extremo libre no existe ruta aumentante; la inducción incremental prueba máximo.

Aristas duplicadas solo ponen el mismo bit. Los bits sobrantes del último
word no existen en las máscaras adyacentes y no producen vértices falsos.
Con `B=ceil(R/w)`, una cota conservadora es `O(K+L²B+LR)` operaciones de
words y `O(LB+V)` words más buffers acotados. Words nativos de 64 bits;
Python usa bloques de enteros grandes. Sin vecino libre hay hasta `L`
derechos emparejados que extraer, acotando también el trabajo de enteros Python.

Python construye filas byte mutables y convierte cada una una vez a entero,
sin copiar una máscara ancha por arista. Sus bloques de 65536 bytes conservan
enteros incompletos y medias parejas; lectores nativos usan 4096 bytes.
Se imprime un entero. El algoritmo difiere de DFS y de capas: nombre propio.

Las cinco se admiten por memoria: C++ 280 KB frente a la NUEVA base C++
de 496 KB, 43,5% menos; Go 1292/2512, 48,6%; Java 680/1264, 46,2%; Python
3868/8516, 54,6%; Rust 356/1820, 80,4%. C++ 0,031→0,015 s es un tick,
sin prueba fiable de aceleración. Python registra 0,140 frente a 0,093 s,
50,5% más tiempo; Java/Go/Rust también suben un tick. Son mejoras de memoria
con el compromiso temporal explícito.

## Notas por lenguaje

El nuevo DFS C++ es la base sencilla preferida; el C++ de capas queda
como otro algoritmo Accepted. Otros lenguajes retienen sus bases. Se compara
cada rápido con su base ACTUAL, incluido el nuevo C++. Python usa CPython3.12.
Instantánea del 2 de noviembre de 2026: C++ rápido 1/1 frente a 74 entradas
filtradas de otros autores; Java 3/1 frente a seis y Python 11/12 frente a
25 llevan asterisco. Go/Rust tienen muestras vacías, solo cobertura formal.
Meta C++:15% superior o primeros diez en ambas métricas; otras familias,
primero en ambas. Las mejoras admitidas bajo la meta mantienen asterisco.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1109_dfs_matching.cpp](1109_dfs_matching.cpp) | G++ 13.2 x64 | dfs, matching | O(M(V+K)) | AC | 0.031 s | 496 KB | 11308433 |
| [1109_matching.go](1109_matching.go) | Go 1.14 x64 | matching | O(L(V+K)) | AC | 0.015 s | 2512 KB | 11279198 |
| [1109_matching.java](1109_matching.java) | Java 1.8 | matching | O(L(V+K)) | AC | 0.125 s | 1264 KB | 11279200 |
| [1109_matching.py](1109_matching.py) | Python 3.12 x64 | matching | O(L(V+K)) | AC | 0.093 s | 8516 KB | 11279199 |
| [1109_matching.rs](1109_matching.rs) | Rust 1.75 x64 | matching | O(L(V+K)) | AC | 0.015 s | 1820 KB | 11279201 |
| [1109_matching.cpp](1109_matching.cpp) | G++ 13.2 x64 | matching | O(L(V+K)) | AC | 0.062 s | 468 KB | 11279197 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1109_bfs_bitmask_matching.cpp](1109_bfs_bitmask_matching.cpp) | G++ 13.2 x64 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.015 s | 280 KB | 11308425 |
| [1109_bfs_bitmask_matching.go](1109_bfs_bitmask_matching.go) | Go 1.14 x64 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.031 s | 1292 KB | 11308428 |
| [1109_bfs_bitmask_matching.java](1109_bfs_bitmask_matching.java) \* | Java 1.8 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.140 s | 680 KB | 11308426 |
| [1109_bfs_bitmask_matching.py](1109_bfs_bitmask_matching.py) \* | Python 3.12 x64 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.140 s | 3868 KB | 11308424 |
| [1109_bfs_bitmask_matching.rs](1109_bfs_bitmask_matching.rs) | Rust 1.75 x64 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.031 s | 356 KB | 11308431 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
