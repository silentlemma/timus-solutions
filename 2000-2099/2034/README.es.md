# 2034. El mayor cuello de botella entre rutas mínimas

[Timus 2034](https://acm.timus.ru/problem.aspx?space=1&num=2034) · dificultad 283 · bfs, dp

Problema original de Oleg Merkurev, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo simple no dirigido y conexo tiene aristas de longitud uno y
tres vértices distintos `s,f,r`. Solo puede elegirse un camino mínimo de
`s` a `f`. Su puntuación es la menor distancia desde `r` a cualquier
vértice del camino, incluidos ambos extremos. Maximiza esa puntuación
entre todos los caminos mínimos. Las distancias desde `r` usan todo el
grafo; un rodeo más largo no es admisible.

Límites: `3 ≤ n ≤ 100000`, `2 ≤ m ≤ 100000`, sin bucles ni aristas repetidas,
grafo conexo; 1 segundo, 64 MB.

## Entrada

Primero `n m`, luego `m` parejas de extremos en `1..n`.
La última línea es `s f r`, todos diferentes.

## Salida

Un entero: la máxima puntuación entre rutas mínimas. Cero es válido si todas
pasan por `r`. Los extremos `s` y `f` también pueden ser el vértice más cercano.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
7 7
1 2
2 4
2 5
3 4
4 6
5 6
6 7
1 7 3
```

```
2
```

## Solución

Un BFS desde `s` obtiene `ds` y el orden de visita; otro desde `r` obtiene `dr`.
Usa la transición `u→v` solo si `ds[v]=ds[u]+1`. Estas aristas forman un grafo
acíclico ordenado por capas BFS. Sea `best[v]` el mayor mínimo de `dr` entre
los caminos mínimos de `s` a `v`. Inicializa `best[s]=dr[s]` y los demás `-1`.
Recorre el orden del primer BFS y actualiza cada transición válida con
`best[v]=max(best[v],min(best[u],dr[v]))`. La respuesta es `best[f]`.

### Corrección

Todo prefijo de una ruta mínima es mínimo: reemplazar uno más largo
acortaría la ruta completa. Por ello cada arista aumenta `ds`
exactamente uno. A la inversa, un camino `s-f` de tales aristas tiene
longitud `ds[f]` y es mínimo. La base incluye el inicio. Toda ruta
mínima a `v` acaba en algún `u` de la capa anterior; su puntuación es el
mínimo de la del prefijo y `dr[v]`. Este mínimo es monótono respecto al
prefijo: basta conservar el mejor en cada `u`. El máximo sobre todos los
predecesores produce exactamente `best[v]`. El orden BFS los procesa
primero, demostrando el resultado por inducción.

También pueden procesarse vértices fuera de todas las rutas mínimas `s-f`.
Si su contribución alcanza `f` por capas crecientes, la ruta completa sigue
teniendo longitud `ds[f]` y es válida; si no, no puede afectar la respuesta.

En el ejemplo, `1-2-4-6-7` tiene distancia mínima uno desde el vértice 3,
alcanzada en 4. La ruta `1-2-5-6-7` tiene mínimo dos en 2 o 6.
El máximo de las dos puntuaciones es dos.

Dos BFS y un recorrido de aristas cuestan `O(n+m)`. Adyacencia, distancias,
orden y programación dinámica ocupan `O(n+m)` memoria.

Trampas:

- Toma primero el mínimo por vértices de cada ruta y después el máximo
  por rutas.
- Avanza exactamente una capa BFS por transición.
- Usa distancias desde `r` en todo el grafo e incluye `s` y `f`.
- Cero es válido si `r` es inevitable en las rutas mínimas.
- Un rodeo seguro pero más largo queda excluido.

## Notas por lenguaje

Los recorridos son iterativos: una cadena de 100000 vértices no requiere
recursión. Java usa arreglos primitivos de adyacencia y cola; Go,
entrada por bytes. Python lee las aristas por líneas a un arreglo
compacto antes de la terna final y construye adyacencia por iterador.
Rust conserva el texto y analiza por iterador. Todos usan `O(n+m)`
espacio; distancias y puntuaciones caben en enteros de 32 bits con
signo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2034_bfs_dp.cpp](2034_bfs_dp.cpp) | G++ 13.2 x64 | bfs, dp | O(n+m) | AC | 0.078 s | 6892 KB |
| [2034_bfs_dp.go](2034_bfs_dp.go) | Go 1.14 x64 | bfs, dp | O(n+m) | AC | 0.109 s | 11080 KB |
| [2034_bfs_dp.java](2034_bfs_dp.java) | Java 1.8 | bfs, dp | O(n+m) | AC | 0.125 s | 8304 KB |
| [2034_bfs_dp.py](2034_bfs_dp.py) | Python 3.12 x64 | bfs, dp | O(n+m) | AC | 0.515 s | 28236 KB |
| [2034_bfs_dp.rs](2034_bfs_dp.rs) | Rust 1.75 x64 | bfs, dp | O(n+m) | AC | 0.078 s | 13112 KB |
